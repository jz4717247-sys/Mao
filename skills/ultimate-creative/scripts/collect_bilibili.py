"""一次性采集B站搜索元数据并按发布时间分层；不下载视频、不创建定时任务。"""
from pathlib import Path
from datetime import datetime, timedelta, timezone
import argparse
import hashlib
import html
import http.cookiejar
import json
import re
import urllib.parse
import urllib.request
import urllib.error
import uuid

def collect(keyword, page, days, out):
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days)
    run_dir = out / (now.strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:6])
    run_dir.mkdir(parents=True)
    url = 'https://api.bilibili.com/x/web-interface/search/all/v2?' + urllib.parse.urlencode({'keyword':keyword,'page':page})
    manifest = {'schema_version':1,'platform':'bilibili','query':keyword,'page':page,'observed_at':now.isoformat(),'cutoff':cutoff.isoformat(),'window_days':days,'source_url':url,'scope':'一次搜索返回的一页视频，非全平台样本','content_level':'title_and_public_metadata_only','audio_transcribed':False,'video_downloaded':False,'scheduled':False}
    try:
        jar = http.cookiejar.CookieJar()  # 只在内存中，绝不导出浏览器凭证。
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)','Referer':'https://www.bilibili.com/'}
        with opener.open(urllib.request.Request('https://www.bilibili.com/',headers=headers),timeout=15) as response:
            response.read(256)
        with opener.open(urllib.request.Request(url,headers=headers),timeout=15) as response:
            payload = json.load(response)
        if payload.get('code') != 0:
            raise ValueError('platform_error_code=' + str(payload.get('code')))
        groups = payload.get('data',{}).get('result',[])
        raw_items = next((g.get('data',[]) for g in groups if g.get('result_type')=='video'),[])
        items,seen = [],set()
        for rank,item in enumerate(raw_items,1):
            bvid = item.get('bvid')
            if not bvid or bvid in seen:
                continue
            seen.add(bvid)
            pub = item.get('pubdate')
            published = datetime.fromtimestamp(pub,timezone.utc) if isinstance(pub,(int,float)) and pub>0 else None
            status = ('unknown_date' if published is None else 'future_date' if published>now+timedelta(minutes=5) else 'recent' if published>=cutoff else 'older')
            title = html.unescape(re.sub(r'<[^>]+>','',item.get('title','')))
            items.append({'platform':'bilibili','work_id':bvid,'url':'https://www.bilibili.com/video/'+bvid+'/','rank_in_query':rank,'title':title,'author':item.get('author'),'published_at':published.isoformat() if published else None,'window_status':status,'duration_display':item.get('duration'),'play_snapshot':item.get('play'),'danmaku_snapshot':item.get('video_review'),'observed_at':now.isoformat(),'text_source':'search_title','origin_confirmed':False,'meme_phrase':None,'original_context':None,'heat_growth':None,'canonical_family_id':None,'discovery_status':'work_lead_not_verified_meme'})
        recent = [x for x in items if x['window_status']=='recent']
        samples = {'manifest':manifest,'items':items,'recent_items':recent}
        samples_path = run_dir/'samples.json'
        samples_path.write_text(json.dumps(samples,ensure_ascii=False,indent=2)+'\n')
        manifest.update({'status':'success_with_recent_leads' if recent else 'success_zero_recent_leads','total_video_items':len(items),'recent_video_items':len(recent),'older_video_items':sum(x['window_status']=='older' for x in items),'unknown_or_future_video_items':sum(x['window_status'] in ['unknown_date','future_date'] for x in items),'samples_sha256':hashlib.sha256(samples_path.read_bytes()).hexdigest()})
        lines = ['# B站一次获取结果','',f'查询：{keyword}；窗口：近{days}天；共{len(items)}条视频线索，其中{len(recent)}条时间落在窗口内。','',
                 '这里只取得标题、作者、日期和公开元数据，尚未取得原声语境。视频标题不能自动算作一个梗，也不能据总播放量判断当前增长。','',
                 '| 作品 | 作者 | 发布时间 UTC | 播放快照 |','|---|---|---|---|']
        for item in recent:
            title = item['title'].replace('|','／').replace('[','［').replace(']','］')
            lines.append(f"| [{title}]({item['url']}) | {item['author']} | {item['published_at']} | {item['play_snapshot']} |")
        if not recent:
            lines.append('| 本页没有窗口内作品，不能以旧条目补数 | | | |')
        (run_dir/'获取结果.md').write_text('\n'.join(lines)+'\n')
        exit_code = 0
    except (urllib.error.URLError, TimeoutError, ValueError, OSError, KeyError, OverflowError, TypeError):
        # 只记故障类别，避免打印错误页、网络凭证或完整响应头。
        import sys
        manifest.update({'status':'failed','failure_type':sys.exc_info()[0].__name__,'total_video_items':None,'recent_video_items':None})
        exit_code = 1
    (run_dir/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':manifest['status'],'video_items':manifest.get('total_video_items'),'recent_items':manifest.get('recent_video_items'),'run_directory':str(run_dir)},ensure_ascii=False))
    return exit_code

if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--keyword',default='热梗')
    parser.add_argument('--page',type=int,default=1)
    parser.add_argument('--days',type=int,default=7)
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'runs')
    args = parser.parse_args()
    if not args.keyword.strip() or len(args.keyword)>200 or args.page<1 or not 1<=args.days<=365:
        parser.error('keyword需1—200字符，page需正数，days需1—365。')
    raise SystemExit(collect(args.keyword,args.page,args.days,args.output.resolve()))
