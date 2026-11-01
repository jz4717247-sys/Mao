#!/usr/bin/env python3
"""Read-only DOCX corpus extraction. Standard library only; no network or rendering.

IDs are hashes of relative paths. P numbers are nonempty OOXML paragraphs in body
order, including table cells. They are extraction locators, never page numbers.
"""
import argparse
import collections
import csv
import hashlib
import json
from pathlib import Path
import re
import zipfile
import xml.etree.ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    source, out = args.source.resolve(), args.output.resolve()
    if not source.is_dir():
        ap.error('Source directory does not exist or is not a directory.')
    documents = sorted(source.rglob('*.docx'))
    if not documents:
        ap.error('Source contains no DOCX files; existing output was not changed.')
    if source == out or source in out.parents:
        ap.error('Output must be outside the source corpus.')
    out.mkdir(parents=True, exist_ok=True)
    (out/'texts').mkdir(exist_ok=True)
    manifest, seen = [], {}
    ledger = source/'整理清单.csv'
    rows = []
    if ledger.exists():
        with ledger.open(encoding='utf-8-sig') as f:
            rows = list(csv.DictReader(f))
    by_name = collections.defaultdict(list)
    for row in rows:
        names = {Path(row.get(k,'')).name for k in ['最终Word路径','destination','本轮修订Word路径'] if row.get(k)}
        for name in names:
            by_name[name].append(row)
    for path in documents:
        rel = path.relative_to(source).as_posix()
        sid = 'S'+hashlib.sha256(rel.encode()).hexdigest()[:10]
        item = dict(id=sid, category=path.relative_to(source).parts[0], relative_path=rel,
                    source_path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())
        try:
            with zipfile.ZipFile(path) as z:
                root = ET.fromstring(z.read('word/document.xml'))
                body = root.find(W+'body')
                paras = []
                for p in body.iter(W+'p'):
                    text = ''.join((n.text or '') if n.tag==W+'t' else ('\t' if n.tag==W+'tab' else '\n')
                                   for n in p.iter() if n.tag in {W+'t',W+'tab',W+'br'})
                    text = text.strip()
                    if text:
                        paras.append(text)
                joined = '\n'.join(paras)
                digest = hashlib.sha256(joined.encode()).hexdigest()
                item.update(paragraphs=len(paras), chars=len(joined), text_sha256=digest,
                            duplicate_of=seen.get(digest), table_count=len(list(body.iter(W+'tbl'))),
                            image_count=len(list(body.iter(W+'drawing'))), extraction='ok')
                seen.setdefault(digest,sid)
                (out/'texts'/f'{sid}.txt').write_text('\n'.join(f'P{i:04d} {t}' for i,t in enumerate(paras,1)),encoding='utf-8')
                item['text_file']=f'texts/{sid}.txt'
                item['quality_flags']=[flag for flag,pat in {
                    'requires_verification':r'待声画复核|未完成声画|待核实|未逐镜|未重新.*(?:观看|核验)|未复听',
                    'incomplete_or_unknown':r'待补全|无法确认|未识别|听不清|待补充',
                    'machine_failure_text':r'Traceback|Selected model is at capacity|TLS handshake|HTTP 50[0234]',
                    'unreadable_symbols':r'�{2,}',
                }.items() if re.search(pat,joined)]
                if len(joined)<1000: item['quality_flags'].append('short_text')
        except Exception as exc:
            item.update(extraction='error',error=f'{type(exc).__name__}: {exc}')
        hits = by_name.get(path.name,[])
        item['ledger_matches']=len(hits)
        item['ledger_notes']=[{k:r.get(k,'') for k in ['剧名','剧目ID','实际解析范围','题材标签','完整分析状态','分析证据边界','正文质量状态','质量问题','本轮全项验收状态']} for r in hits]
        manifest.append(item)
    (out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    summary=dict(files=len(manifest), ledger_rows=len(rows), categories=dict(collections.Counter(x['category'] for x in manifest)),
                 extracted=sum(x['extraction']=='ok' for x in manifest), errors=[x['id'] for x in manifest if x['extraction']!='ok'],
                 duplicate_texts=sum(bool(x.get('duplicate_of')) for x in manifest),
                 total_chars=sum(x.get('chars',0) for x in manifest),
                 flag_counts=dict(collections.Counter(flag for x in manifest for flag in x.get('quality_flags',[]))))
    (out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    with (out/'inventory.csv').open('w',encoding='utf-8-sig',newline='') as f:
        fields=['id','category','relative_path','sha256','paragraphs','chars','duplicate_of','extraction','quality_flags']
        writer=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(manifest)
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
