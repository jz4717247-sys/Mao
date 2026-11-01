#!/usr/bin/env python3
"""Read Japanese public-text research and assemble traceable, unfinished creative operations."""
import argparse
import collections
import itertools
import hashlib
import json
import random
from pathlib import Path


def read(path):
    raw = path.read_bytes()
    return json.loads(raw.decode('utf-8')), hashlib.sha256(raw).hexdigest()


def brief(work):
    return {k: work[k] for k in ('id', 'family_id', 'title_zh', 'title_original', 'year', 'medium', 'premise', 'reading_boundary', 'confidence')}


def operation_result(op, by_id):
    result = dict(op)
    works = [by_id[e['work_id']] for e in op['evidence']]
    result['support'] = {'coded_works': len({w['id'] for w in works}), 'independent_families': len({w['family_id'] for w in works}), 'work_ids': sorted({w['id'] for w in works})}
    result['interpretation'] = 'Named analogical cases in public-text research, not exhaustive coding, exact tag conjunction, current popularity, or a success probability.'
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', type=Path, default=Path(__file__).resolve().parents[1] / 'references')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('coverage')
    p = sub.add_parser('search')
    p.add_argument('--query', default='')
    p.add_argument('--medium', choices=['all', 'anime_series', 'live_drama', 'film'], default='all')
    p.add_argument('--limit', type=int, default=5)
    p.add_argument('--full', action='store_true')
    p = sub.add_parser('work')
    p.add_argument('id')
    p = sub.add_parser('operation')
    p.add_argument('id', nargs='?')
    p = sub.add_parser('combine')
    p.add_argument('--route', choices=['douyin', 'realistic', 'animation'], default='douyin')
    p.add_argument('--intensity', choices=['grounded', 'uncanny', 'radical'], default='uncanny')
    p.add_argument('--lock', action='append', default=[])
    p.add_argument('--avoid', action='append', default=[])
    p.add_argument('--seed', type=int, required=True)
    p.add_argument('--count', type=int, default=5)
    args = parser.parse_args()
    try:
        library, library_hash = read(args.data_dir / 'japan-works.json')
        atlas, atlas_hash = read(args.data_dir / 'japan-operations.json')
    except (OSError, ValueError) as error:
        parser.error(f'research data unavailable: {error}')
    works = library['works']
    by_id = {w['id']: w for w in works}
    operations = atlas['operations']
    if args.command == 'coverage':
        urls = {s['url'] for w in works for s in w['sources']}
        result = {'snapshot_date': library['collected_at'], 'scope': library['scope'], 'works': len(works), 'families': len({w['family_id'] for w in works}), 'by_medium': dict(collections.Counter(w['medium'] for w in works)), 'unique_source_urls': len(urls), 'source_occurrences': sum(len(w['sources']) for w in works), 'selection_signals': dict(collections.Counter(w['selection_signal']['kind'] for w in works)), 'confidence': dict(collections.Counter(w['confidence'] for w in works)), 'ending_explicitly_verified': sum(w['reading_boundary']['ending_verified'] for w in works), 'operations': len(operations), 'boundary': library['boundary']}
    elif args.command == 'search':
        terms = args.query.casefold().split()
        hits = [w for w in works if (args.medium == 'all' or w['medium'] == args.medium) and all(term in json.dumps({k: w[k] for k in ('title_zh', 'title_original', 'premise', 'characters', 'world', 'structure', 'transfer')}, ensure_ascii=False).casefold() for term in terms)]
        result = {'matches': len(hits), 'results': [w if args.full else brief(w) for w in hits[:max(0, args.limit)]], 'ordering': 'work ID, not popularity; literal retrieval may miss synonyms'}
    elif args.command == 'work':
        if args.id not in by_id:
            parser.error('unknown work ID')
        result = by_id[args.id]
    elif args.command == 'operation':
        chosen = [op for op in operations if not args.id or op['id'] == args.id]
        if not chosen:
            parser.error('unknown operation ID')
        result = {'operations': [operation_result(op, by_id) for op in chosen]}
    else:
        if not 1 <= args.count <= 10:
            parser.error('--count must be 1..10')
        available = [op for op in operations if args.intensity in op['intensity'] and op['routes'].get(args.route) and not any(term.casefold() in json.dumps(op, ensure_ascii=False).casefold() for term in args.avoid)]
        pairs = [(a, b) for a, b in itertools.combinations(available, 2) if a['dimension'] != b['dimension'] and any(by_id[x['work_id']]['family_id'] != by_id[y['work_id']]['family_id'] for x in a['evidence'] for y in b['evidence'])]
        rng = random.Random(args.seed)
        rng.shuffle(pairs)
        cards = []
        for a, b in pairs[:args.count]:
            compatible_sources = [(x, y) for x in a['evidence'] for y in b['evidence'] if by_id[x['work_id']]['family_id'] != by_id[y['work_id']]['family_id']]
            first, second = rng.choice(compatible_sources)
            cards.append({'candidate_id': f'C{len(cards)+1:02}', 'locked': list(args.lock), 'avoided': list(args.avoid), 'operations': [{k: op[k] for k in ('id', 'name', 'dimension', 'principle')} | {'route_adaptation': op['routes'][args.route]} for op in (a, b)], 'analogy_sources': [{'work_id': e['work_id'], 'title': by_id[e['work_id']]['title_zh'], 'family_id': by_id[e['work_id']]['family_id'], 'source_ids': e['source_ids'], 'observation': e['observation'], 'boundary': by_id[e['work_id']]['reading_boundary']} for e in (first, second)], 'combination_evidence': 'Unvalidated original combination; component analogies do not prove the combination or popularity.', 'required_author_work': ['保留所有锁定条件；avoid作用于方法候选，作者还须检查成品是否含被排除元素。', '给出被改变的常识、异常触发、能力边界和实际损失。', '为主角及对手分别写可冲突的欲望、策略和选择。', '写可见首场、三次不同兑现、持续后果与回收；不能把本卡当成剧本。', '与参考作品对照目标、规则、关系、揭示和高潮选择，改出自己的因果。'], 'status': 'operation seed, not finished story'})
        result = {'seed': args.seed, 'route': args.route, 'intensity': args.intensity, 'sampling': 'uniform distinct operation pairs; two analogy sources from different families; no popularity weighting', 'requested_count': args.count, 'returned_count': len(cards), 'pool_exhausted': len(cards) < args.count, 'locked': list(args.lock), 'avoid': list(args.avoid), 'lock_scope': 'Preserved verbatim as author constraints; not interpreted, checked for feasibility, or claimed as source-supported.', 'candidates': cards}
    if args.command in ('coverage', 'combine'):
        result['data_snapshot'] = {
            'library_version': library.get('version'),
            'atlas_version': atlas.get('version'),
            'japan_works_sha256': library_hash,
            'japan_operations_sha256': atlas_hash,
            'replay_scope': 'Same seed, arguments and identical data files; changing the data can change cards.'
        }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
