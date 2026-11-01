#!/usr/bin/env python3
"""Search the bundled local evidence library; no network, writes or popularity scoring."""
import argparse
import json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--kind', choices=['cards', 'catalog', 'evidence'], default='cards')
    ap.add_argument('--query', default='', help='Whitespace-separated terms; all terms must match.')
    ap.add_argument('--route', choices=['douyin', 'realistic', 'animation'])
    ap.add_argument('--source-id')
    ap.add_argument('--limit', type=int, default=5)
    ap.add_argument('--full', action='store_true', help='Include all available evidence and boundary fields.')
    args = ap.parse_args()
    if not 1 <= args.limit <= 100:
        ap.error('--limit must be between 1 and 100')
    refs = Path(__file__).resolve().parent.parent/'references'
    filenames = {'cards': 'tag-cards.json', 'catalog': 'corpus-catalog.json', 'evidence': 'evidence.json'}
    data = json.loads((refs/filenames[args.kind]).read_text(encoding='utf-8'))
    records = data if args.kind=='catalog' else data[args.kind]
    routes = {'抖音超创':'douyin', '红果 AI 仿真人':'realistic', '红果 AI 漫剧':'animation'}
    terms = args.query.casefold().split()
    result = []
    for record in records:
        route = record.get('route', routes.get(record.get('category')))
        if args.route and route != args.route:
            continue
        if args.source_id and record.get('source_id') != args.source_id:
            continue
        haystack = json.dumps(record, ensure_ascii=False).casefold()
        if all(term in haystack for term in terms):
            result.append(record)
    selected = result[:args.limit]
    if not args.full and args.kind=='cards':
        selected = [{k:x.get(k) for k in ['id','route','source_id','work_title','tags']}
                    for x in selected]
    print(json.dumps({'matches':len(result), 'shown':len(selected),
                      'match_method':'literal_all_terms_not_semantic_ranking',
                      'boundary':'创作来源检索；没有真实爆款概率。用 --full 查看证据层级和限制。',
                      'results':selected}, ensure_ascii=False, indent=2))


if __name__=='__main__':
    main()
