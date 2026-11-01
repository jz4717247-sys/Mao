#!/usr/bin/env python3
"""角色融梗检索、校验与使用账本。标准库实现；检索结果仍需剧作者作情境判断。"""
import argparse
from collections import Counter
from datetime import date, datetime, timezone
import json
from pathlib import Path
import re

DEFAULT_LIBRARY = Path(__file__).resolve().parents[1] / 'references' / 'meme-library.json'
SENSITIVE = {'救命指令', '创伤告白', '死亡哀悼', '高潮选择'}

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def emit(value):
    print(json.dumps(value, ensure_ascii=False, indent=2))

def normalize(s):
    return re.sub(r'[\s，。！!？?、/／…·:：;；（）()]', '', s).casefold()

def title_matches(card,title):
    """保守字面匹配；不判断语义。短词避免把商品／系统包当作保证语。"""
    if card['expression']=='包的':
        return bool(re.search(r'(?:^|[\s：:！!？?，,。\u300a\u300c\u201c])包的(?:$|[\s！!？?，,。\u300b\u300d\u201d])',title) or '包赢的' in title)
    terms=[card['expression']]+card.get('variants',[])
    if card['expression']=='从夯到拉':terms=['从夯到拉','夯爆了','拉完了']
    return any(len(t)>=2 and '×' not in t and t.casefold() in title.casefold() for t in terms)

def audit(db):
    errors = []
    sources = {s['id']: s for s in db.get('sources', [])}
    cards = db.get('cards', [])
    ids, families, terms = set(), set(), {}
    for c in cards:
        for key in ('id', 'family_id', 'expression', 'readiness', 'kind', 'intents', 'voices',
                    'relationships', 'trigger', 'avoid', 'plain_alternative', 'evidence', 'freshness'):
            if not c.get(key):
                errors.append(f"{c.get('id')}: missing {key}")
        if c['id'] in ids or c['family_id'] in families:
            errors.append(f"duplicate id/family: {c['id']}")
        ids.add(c['id']); families.add(c['family_id'])
        for phrase in [c['expression']] + c.get('variants', []):
            term = normalize(phrase)
            if term in terms and terms[term] != c['family_id']:
                errors.append(f"variant overlap: {phrase}")
            terms[term] = c['family_id']
        for e in c['evidence']:
            if e['source_id'] not in sources:
                errors.append(f"missing source: {e['source_id']}")
        if c['readiness'] == 'text_ready':
            if not c.get('meaning') or not any(e['level'] in ('text_context', 'documented_definition') for e in c['evidence']):
                errors.append(f"ready without contextual evidence: {c['id']}")
            if c.get('requires_original_audio'):
                errors.append(f"audio-dependent card marked ready: {c['id']}")
            try:
                date.fromisoformat(c['documented_at'])
                date.fromisoformat(c['freshness']['last_context_documented_at'])
            except (ValueError,TypeError,KeyError):
                errors.append(f"ready without real context date: {c['id']}")
        if c['freshness'].get('heat_growth') is not None and not c['freshness'].get('growth_evidence'):
            errors.append(f"growth without evidence: {c['id']}")
        if c.get('origin_verified') and not c.get('origin_evidence'):
            errors.append(f"origin without evidence: {c['id']}")
    return {'ok': not errors, 'errors': errors, 'cards': len(cards),
            'readiness': dict(Counter(c['readiness'] for c in cards)),
            'kinds': dict(Counter(c['kind'] for c in cards)), 'sources': len(sources),
            'sources_cited': len({e['source_id'] for c in cards for e in c['evidence']})}

def query(db, args, ledger=None):
    if args.setting != '现代' or args.language != 'zh':
        return {'decision': 'use_plain_dialogue', 'reason': '本库为现代中文表达；当前时代或语言不适配。先写人物自己的幽默。', 'cards': []}
    if args.scene in SENSITIVE:
        return {'decision': 'use_plain_dialogue', 'reason': '此场核心信息、承诺或情绪需要完整落地；默认不插网络梗。', 'cards': []}
    used = (ledger or {}).get('uses', [])
    results = []
    today = date.fromisoformat(args.as_of)
    for c in db['cards']:
        if c['readiness'] != 'text_ready':
            continue
        if args.intent and args.intent not in c['intents']:
            continue
        if args.voice and args.voice not in c['voices']:
            continue
        if args.relationship and args.relationship not in c['relationships']:
            continue
        if args.text and args.text not in json.dumps(c, ensure_ascii=False):
            continue
        if args.story_year and int(c['documented_at'][:4]) > args.story_year:
            continue
        # 最新语境证据日期与本次查看日期分开。标题再传播不能更新此字段。
        context_date = date.fromisoformat(c['freshness']['last_context_documented_at'])
        age = (today - context_date).days
        if age < 0 or (args.fresh_days is not None and age > args.fresh_days):
            continue
        family_uses = [u for u in used if u['family_id'] == c['family_id']]
        if any(u['episode'] == args.episode for u in family_uses):
            continue
        if any(u['character'] == args.character and 0 <= args.episode-u['episode'] <= args.cooldown for u in family_uses):
            continue
        if len({u['character'] for u in family_uses}) >= 2 and args.character not in {u['character'] for u in family_uses}:
            continue
        score = (3 if args.intent else 0)+(2 if args.voice else 0)+(2 if args.relationship else 0)
        if args.prefer_since and c['documented_at'] >= args.prefer_since:
            score += 1
        results.append({'score': score, 'context_age_days': age,
                        'freshness_note': '文本语义可用；不等于今日热门或已证明增长。', **c})
    results.sort(key=lambda c: (-c['score'], -int(c['documented_at'].replace('-', '')), c['id']))
    budget = sum(u['episode'] == args.episode for u in used)
    if budget >= args.budget:
        return {'decision': 'use_plain_dialogue', 'reason': '本集网络梗试写预算已用完；不靠换词族绕过。', 'cards': []}
    return {'decision': 'review_candidates' if results else 'use_plain_dialogue',
            'reason': '候选必须结合动作、关系与普通替代句审阅；也可以全部不用。' if results else '当前条件下无适用卡，不用旧卡冒充近期卡。',
            'library_verified_at': db['verified_at'], 'cards': results[:args.limit]}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--library', type=Path, default=DEFAULT_LIBRARY)
    sub = p.add_subparsers(dest='command', required=True)
    sub.add_parser('audit')
    sub.add_parser('stats')
    merge = sub.add_parser('merge-context', help='合并已经逐条研读的语境补丁；不是元数据自动入库。')
    merge.add_argument('--patch', type=Path, required=True)
    merge.add_argument('--output', type=Path, required=True)
    q = sub.add_parser('query')
    q.add_argument('--intent'); q.add_argument('--voice'); q.add_argument('--relationship')
    q.add_argument('--text'); q.add_argument('--language', choices=['zh','en'], default='zh')
    q.add_argument('--setting', choices=['现代','历史','架空古代'], default='现代')
    q.add_argument('--story-year', type=int); q.add_argument('--scene', default='日常喜剧')
    q.add_argument('--fresh-days', type=int); q.add_argument('--prefer-since', default='2025-01-01')
    q.add_argument('--as-of', default=date.today().isoformat())
    q.add_argument('--limit', type=int, default=5); q.add_argument('--episode', type=int, default=1)
    q.add_argument('--character', default='未指定'); q.add_argument('--cooldown', type=int, default=3)
    q.add_argument('--budget', type=int, default=1); q.add_argument('--ledger', type=Path)
    record = sub.add_parser('record', help='剧作者选择并审阅后记一次使用；不会修改剧本。')
    record.add_argument('--card', required=True); record.add_argument('--character', required=True)
    record.add_argument('--episode', type=int, required=True); record.add_argument('--ledger', type=Path, required=True)
    record.add_argument('--line', required=True); record.add_argument('--purpose', required=True)
    args = p.parse_args(); db = read(args.library)
    if args.command in ('audit','stats'):
        result = audit(db); emit(result); return 0 if result['ok'] else 1
    if args.command == 'merge-context':
        patch=read(args.patch)
        if patch.get('review_method')!='manual_context_read' or not patch.get('review_note') or not patch.get('reviewed_at'):
            p.error('补丁需要 manual_context_read、reviewed_at 和具体 review_note；搜索元数据不能自动入库。')
        for key in ('sources','cards'):
            existing={item['id']:item for item in db[key]}
            for item in patch.get(key,[]):
                # 覆盖时传完整记录；同一 id 沿用词族，不允许借更新重复计数。
                if key=='cards' and item['id'] in existing and item['family_id']!=existing[item['id']]['family_id']:
                    p.error('更新现有卡必须保留 family_id。')
                existing[item['id']]=item
            db[key]=list(existing.values())
        result=audit(db)
        if not result['ok']:
            emit(result); return 1
        db['verified_at']=patch['reviewed_at'];db['last_context_review']=patch['review_note']
        args.output.parent.mkdir(parents=True,exist_ok=True)
        tmp=args.output.with_name(args.output.name+'.tmp')
        tmp.write_text(json.dumps(db,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');tmp.replace(args.output)
        emit({'merged':True,'output':str(args.output),'audit':result});return 0
    if args.command == 'query':
        if args.limit < 1 or args.episode < 1 or args.cooldown < 0 or args.budget < 0 or (args.fresh_days is not None and args.fresh_days < 0):
            p.error('limit/episode需正数，其余数值不能为负。')
        emit(query(db,args,read(args.ledger) if args.ledger and args.ledger.exists() else None)); return 0
    card = next((c for c in db['cards'] if c['id'] == args.card), None)
    if not card or card['readiness'] != 'text_ready':
        p.error('卡不存在或语境待核，不能记为已选用。')
    if args.episode < 1: p.error('episode需正数。')
    ledger = read(args.ledger) if args.ledger.exists() else {'schema_version':1,'uses':[]}
    if any(u['family_id'] == card['family_id'] and u['episode'] == args.episode for u in ledger['uses']):
        p.error('本集已有该词族，变体不另算一个新梗。')
    ledger['uses'].append({'card_id':card['id'],'family_id':card['family_id'],
        'character':args.character,'episode':args.episode,'line':args.line,'purpose':args.purpose,
        'recorded_at':datetime.now(timezone.utc).isoformat()})
    args.ledger.parent.mkdir(parents=True,exist_ok=True)
    temp = args.ledger.with_name(args.ledger.name+'.tmp')
    temp.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    temp.replace(args.ledger); emit({'recorded':True,'card_id':card['id'],'ledger':str(args.ledger)}); return 0

if __name__ == '__main__':
    raise SystemExit(main())
