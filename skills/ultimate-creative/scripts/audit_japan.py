#!/usr/bin/env python3
"""Check research completeness and citation links; this does not verify narrative truth."""
import argparse
import collections
import json
from pathlib import Path
from urllib.parse import urlparse


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--data-dir', type=Path, default=Path(__file__).resolve().parents[1] / 'references')
    a = ap.parse_args()
    errors = []
    warnings = []
    try:
        library = json.loads((a.data_dir / 'japan-works.json').read_text())
        atlas = json.loads((a.data_dir / 'japan-operations.json').read_text())
    except (OSError, ValueError) as exc:
        print(json.dumps({'passed': False, 'errors': [str(exc)]}, ensure_ascii=False))
        raise SystemExit(1)
    works = library.get('works', [])
    by_id = {w.get('id'): w for w in works}
    if len(by_id) != len(works):
        errors.append('duplicate work IDs')
    if len({w.get('family_id') for w in works}) != len(works):
        warnings.append('some selected works share a family; report works and families separately')

    def fail(wid, message):
        errors.append(f'{wid}: {message}')

    def walk(value):
        if isinstance(value, dict):
            for k, v in value.items():
                if k == 'source_ids':
                    yield v
                else:
                    yield from walk(v)
        elif isinstance(value, list):
            for v in value:
                yield from walk(v)

    all_sources = {}
    for w in works:
        wid = w.get('id')
        for field in ('family_id', 'title_zh', 'title_original', 'year', 'medium', 'selection_signal', 'sources', 'reading_boundary', 'premise', 'characters', 'world', 'structure', 'transfer', 'confidence'):
            if not w.get(field):
                fail(wid, f'missing {field}')
        if not isinstance(w.get('year'), int) or not 2016 <= w['year'] <= 2025:
            fail(wid, 'year outside declared selection window')
        sources = w.get('sources', [])
        source_ids = {s.get('id') for s in sources}
        if len(source_ids) != len(sources):
            fail(wid, 'duplicate source IDs')
        if len({s.get('url') for s in sources}) < 2:
            fail(wid, 'fewer than two distinct source URLs')
        if not any(s.get('source_type') in ('official_story', 'official_character', 'official_episode', 'platform_editorial') for s in sources):
            fail(wid, 'no classified official narrative source')
        for s in sources:
            if s.get('id') in all_sources:
                fail(wid, 'source ID reused by another work')
            all_sources[s.get('id')] = s
            if urlparse(s.get('url', '')).scheme not in ('http', 'https'):
                fail(wid, 'non-web source URL')
            for f in ('title', 'publisher', 'accessed_at', 'scope', 'supported_claims', 'source_type'):
                if not s.get(f):
                    fail(wid, f'source {s.get("id")} missing {f}')
        for ids in walk(w):
            if not isinstance(ids, list) or not ids or not set(ids) <= source_ids:
                fail(wid, f'dangling or empty source_ids: {ids}')
        boundary = w.get('reading_boundary', {})
        if not boundary.get('covered_scope') or not boundary.get('limitations') or not boundary.get('not_reviewed') or not isinstance(boundary.get('ending_verified'), bool):
            fail(wid, 'reading boundary incomplete')
        if boundary.get('material_type') != 'official_public_text':
            fail(wid, 'undeclared material type')
        if len(w.get('characters', [])) < 2:
            fail(wid, 'fewer than two character analyses')
        for c in w.get('characters', []):
            for f in ('name', 'desire', 'contradiction', 'strategy', 'relation_pressure', 'source_ids', 'evidence_status'):
                if not c.get(f):
                    fail(wid, f'character missing {f}')
        rules = w.get('world', {}).get('rules', [])
        if len(rules) < 2:
            fail(wid, 'fewer than two bounded world rules')
        for rule in rules:
            if not all(rule.get(f) for f in ('rule', 'cost_or_limit', 'source_ids')) or rule.get('status') not in ('verified', 'inference'):
                fail(wid, 'world rule missing evidence/status/limit')
        if len(w.get('structure', {}).get('escalation', [])) < 3 or w.get('structure', {}).get('analysis_status') != 'bounded_analysis':
            fail(wid, 'structure lacks three bounded stages')
        for f in ('scope', 'entry', 'engine', 'reveal_design', 'payoff_or_boundary', 'source_ids'):
            if not w.get('structure', {}).get(f):
                fail(wid, f'structure missing {f}')
        transfer = w.get('transfer', {})
        if len(transfer.get('abstract_operations', [])) < 3 or not all(transfer.get(f) for f in ('douyin', 'realistic', 'animation', 'do_not_copy', 'original_seed')):
            fail(wid, 'transfer incomplete')
        if not all(transfer.get('original_seed', {}).get(f) for f in ('concept', 'protagonist_goal', 'rule_limit', 'opening_action', 'repeat_engine')):
            fail(wid, 'original seed is only a premise')
        if w.get('confidence') not in ('high', 'medium', 'limited'):
            fail(wid, 'unknown confidence')
    ops = atlas.get('operations', [])
    if len({op.get('id') for op in ops}) != len(ops):
        errors.append('duplicate operation IDs')
    for op in ops:
        oid = op.get('id')
        evidence = op.get('evidence', [])
        valid = [by_id.get(e.get('work_id')) for e in evidence]
        if any(w is None for w in valid):
            errors.append(f'{oid}: unknown supporting work')
        families = {w['family_id'] for w in valid if w}
        if len(families) < 3:
            errors.append(f'{oid}: fewer than three independent analogical families')
        for e in evidence:
            w = by_id.get(e.get('work_id'))
            if not w:
                continue
            if not e.get('source_ids') or not set(e['source_ids']) <= {s['id'] for s in w['sources']} or not e.get('observation') or not e.get('transfer'):
                errors.append(f'{oid}: invalid evidence attribution')
        for field in ('name', 'dimension', 'intensity', 'principle', 'routes', 'failure_modes', 'original_example'):
            if not op.get(field):
                errors.append(f'{oid}: missing {field}')
        if not all(op.get('routes', {}).get(route) for route in ('douyin', 'realistic', 'animation')):
            errors.append(f'{oid}: route adaptation absent')
    counts = dict(collections.Counter(w.get('medium') for w in works))
    expected = library.get('counts', {}).get('by_medium')
    if expected != counts or library.get('counts', {}).get('works') != len(works):
        errors.append('declared counts disagree with actual records')
    report = {'passed': not errors, 'works': len(works), 'families': len({w.get('family_id') for w in works}), 'by_medium': counts, 'source_occurrences': len(all_sources), 'unique_urls': len({s['url'] for s in all_sources.values()}), 'operations': len(ops), 'errors': errors, 'warnings': warnings, 'scope_of_check': 'schema, declared coverage, IDs, evidence linkage and reading-boundary presence; narrative truth requires a separate source review'}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
