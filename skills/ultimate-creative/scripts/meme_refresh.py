#!/usr/bin/env python3
"""按需刷新发现池；元数据只形成线索，永不自动升级语境卡。不创建定时任务。"""
import argparse
from datetime import datetime, timezone, timedelta
import json
from pathlib import Path
import collect_bilibili
from meme_engine import title_matches

def write_json(path,value):
    temp=path.with_name(path.name+'.tmp')
    temp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    temp.replace(path)

def run_query(query,days,out):
    # 每次 collect 创建唯一目录；返回值只包含此次文件，不捕获全局 stdout。
    before=set(out.iterdir())
    collect_bilibili.collect(query,1,days,out)
    candidates=[p for p in out.iterdir() if p not in before and (p/'manifest.json').exists()]
    matching=[p for p in candidates if json.loads((p/'manifest.json').read_text())['query']==query]
    if len(matching)!=1:raise RuntimeError('本次查询目录识别失败；请用 --import-run 载入已保存的目录。')
    return matching[0]

def aggregate(paths,library,days=7):
    manifests=[];works={}
    now=datetime.now(timezone.utc);cutoff=now-timedelta(days=days)
    for path in paths:
        m=json.loads((path/'manifest.json').read_text());manifests.append({**m,'run_directory':str(path)})
        if m['status']=='failed':continue
        d=json.loads((path/'samples.json').read_text())
        for w in d['items']:
            item=works.setdefault(w['work_id'],{**w,'queries':[],'matched_family_ids':[]})
            if m['query'] not in item['queries']:item['queries'].append(m['query'])
    for w in works.values():
        w['window_status_at_collection']=w['window_status']
        pub=datetime.fromisoformat(w['published_at']) if w.get('published_at') else None
        w['window_status']='unknown_date' if pub is None else 'future_date' if pub>now+timedelta(minutes=5) else 'recent' if pub>=cutoff else 'older'
        for c in library['cards']:
            if title_matches(c,w['title']):
                w['matched_family_ids'].append(c['family_id'])
        w['qualification']='phrase_match_only' if w['matched_family_ids'] else 'discovery_or_irrelevant_title'
        w['semantic_reviewed']=False
    return {'observed_at':now.isoformat(),'window_days':days,'cutoff':cutoff.isoformat(),'runs':manifests,'works':list(works.values()),
        'raw_unique_works':len(works),'raw_recent_works':sum(w['window_status']=='recent' for w in works.values()),
        'recent_phrase_match_unique_works':sum(w['window_status']=='recent' and bool(w['matched_family_ids']) for w in works.values()),
        'content_level':'title_and_metadata_only','auto_promotions':0,'scheduler_enabled':False}

def save_state(out,snapshot):
    state_path=out/'refresh-state.json'
    state=json.loads(state_path.read_text()) if state_path.exists() else {'schema_version':1,'last_success':None}
    failures=[m for m in snapshot['runs'] if m['status']=='failed']
    attempt={'at':snapshot['observed_at'],'queries':len(snapshot['runs']),'failed_queries':len(failures),
        'status':'failed' if len(failures)==len(snapshot['runs']) else 'partial' if failures else 'success',
        'raw_unique_works':snapshot['raw_unique_works'],'recent_phrase_match_unique_works':snapshot['recent_phrase_match_unique_works']}
    archive=out/('snapshot-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'.json')
    write_json(archive,snapshot);attempt['snapshot']=str(archive)
    state['last_attempt']=attempt
    # 部分成功保存本次快照，但不替换全量成功指针；失败不声称零新增。
    if not failures:
        state['last_success']=attempt
        write_json(out/'latest-success.json',snapshot)
    write_json(state_path,state)
    return state

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--keyword',action='append',default=[])
    p.add_argument('--import-run',type=Path,action='append',default=[])
    p.add_argument('--days',type=int,default=7)
    p.add_argument('--output',type=Path,required=True,help='本任务交付目录内的绝对路径')
    p.add_argument('--library',type=Path,default=Path(__file__).resolve().parents[1]/'references/meme-library.json')
    args=p.parse_args()
    if not args.output.is_absolute():p.error('--output 必须是绝对路径。')
    if not args.keyword and not args.import_run:p.error('需要 --keyword 或 --import-run。')
    if not 1<=args.days<=365 or len(args.keyword)>12 or len(set(args.keyword))!=len(args.keyword):
        p.error('days需1—365，关键词至多12个，不能重复。')
    if any(not q.strip() or len(q)>200 for q in args.keyword):p.error('关键词需1—200字符。')
    args.output.mkdir(parents=True,exist_ok=True)
    run_out=args.output/'runs';run_out.mkdir(exist_ok=True)
    paths=[x.resolve() for x in args.import_run]
    # 同一查询依赖返回目录，顺序执行；网络请求本身有15秒上限。
    for query in args.keyword:paths.append(run_query(query,args.days,run_out))
    snapshot=aggregate(paths,json.loads(args.library.read_text()),args.days)
    state=save_state(args.output,snapshot)
    print(json.dumps({'state':state,'context_cards_changed':False,'auto_promotions':0},ensure_ascii=False,indent=2))
    return 0 if state['last_attempt']['status']=='success' else 1

if __name__=='__main__':raise SystemExit(main())
