#!/usr/bin/env python3
"""Read-only integrity audit. Optional source-root also verifies DOCX hashes and quotes."""
import argparse,collections,hashlib,itertools,json,re,sys,zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

def load(path):return json.loads(path.read_text(encoding='utf-8'))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--data-dir',type=Path,default=Path(__file__).resolve().parents[1]/'references')
    ap.add_argument('--source-root',type=Path)
    args=ap.parse_args();r=args.data_dir
    data=load(r/'full-dossiers.json');stats=load(r/'corpus-statistics.json');cards=load(r/'tag-cards.json')['cards'];coverage=load(r/'reading-coverage.json');catalog=load(r/'corpus-catalog.json');taxonomy=load(r/'tag-taxonomy.json')['tags']
    ds=data['dossiers'];errors=[];byid={d['source_id']:d for d in ds};cat={d['source_id']:d for d in catalog};families={d['family_id']:d for d in data['families']}
    def check(ok,msg):
        if not ok:errors.append(msg)
    check(len(byid)==len(ds),'duplicate dossier source_id')
    check(set(byid)==set(cat),'dossier/catalog coverage mismatch')
    check(len(cards)==len(ds) and {d['source_id'] for d in cards}==set(byid),'card coverage mismatch')
    check(len({d['id'] for d in cards})==len(cards),'duplicate card ID')
    check(len(coverage['records'])==len(ds) and {d['source_id'] for d in coverage['records']}==set(byid),'reading coverage mismatch')
    check(stats['complete'] and coverage['complete'],'not marked complete')
    members=[s for f in families.values() for s in f['sources']]
    check(len(members)==len(set(members)) and set(members)==set(byid),'family partition mismatch')
    for d in ds:
        sid=d['source_id'];check(d['family_id'] in families and sid in families[d['family_id']]['sources'],sid+': wrong family')
        check(d['sha256']==cat[sid]['sha256'],sid+': catalog hash mismatch')
        expected=[]
        for t in taxonomy:
            indices=[i for i,x in enumerate(d['tags']) if any(re.search(p,x['tag']) for p in t['patterns']) and not re.search(r'未知|不确定|未证实|无此',x['tag'])]
            if indices:expected.append(dict(id=t['id'],name=t['name'],dimension=t['dimension'],raw_tag_indices=indices))
        check(d['canonical_tags']==expected,sid+': canonical tag mapping mismatch')
    for route,counts in stats['counts'].items():
        rows=[d for d in ds if route=='all' or d['route']==route]
        check(counts==dict(documents=len(rows),families=len({d['family_id'] for d in rows})),route+': count mismatch')
        for m in stats['mechanisms']:
            hits=[d for d in rows if any(x['code']==m['code'] for x in d['mechanisms'])];s=m['support'][route]
            check(s['documents']==len(hits) and s['families']==len({d['family_id'] for d in hits}) and set(s['source_ids'])=={d['source_id'] for d in hits},route+': '+m['code']+' support mismatch')
    for t in stats['tags']:
        hits=[d for d in ds if any(x['id']==t['id'] for x in d['canonical_tags'])]
        check(t['documents']==len(hits) and t['families']==len({d['family_id'] for d in hits}) and set(t['source_ids'])=={d['source_id'] for d in hits},t['id']+': support mismatch')
    pairs=collections.defaultdict(set)
    for d in ds:
        for pair in itertools.combinations(sorted(t['id'] for t in d['canonical_tags']),2):pairs[pair].add(d['source_id'])
    check(set(pairs)=={tuple(p['tags']) for p in stats['tag_pairs']},'tag pair coverage mismatch')
    for p in stats['tag_pairs']:
        ids=pairs[tuple(p['tags'])]
        check(set(p['source_ids'])==ids and p['documents']==len(ids) and p['families']==len({byid[s]['family_id'] for s in ids}),'pair '+str(p['tags'])+': mismatch')
    quotes=sum(len(d[k]) for d in ds for k in ['tags','mechanisms','script_checks','limits'])
    check(quotes==stats['quote_occurrences'],'quote occurrence count mismatch')
    patterns=load(r/'direction-patterns.json') if (r/'direction-patterns.json').exists() else {'patterns':[],'unique_named_families':0}
    anchors=collections.defaultdict(list);pattern_families=set()
    for pattern in patterns['patterns']:
        fs=set()
        for c in pattern['cases']:
            check(c['source_id'] in byid,pattern['id']+': unknown case')
            if c['source_id'] in byid:
                check(c['family_id']==byid[c['source_id']]['family_id'],pattern['id']+': stale family')
                fs.add(c['family_id']);pattern_families.add(c['family_id'])
            anchors[c['source_id']].extend(c['anchors'])
        check(len(fs)==pattern['named_family_support'],pattern['id']+': named support mismatch')
    check(len(pattern_families)==patterns['unique_named_families'],'pattern union mismatch')
    source_count=0;source_quotes=0;pattern_quotes=0
    if args.source_root:
        source=args.source_root.resolve();W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        for d in ds:
            sid=d['source_id'];p=(source/d['source_file']).resolve()
            if source not in p.parents:errors.append(sid+': source path outside root');continue
            if not p.is_file():errors.append(sid+': source missing');continue
            payload=p.read_bytes();check(hashlib.sha256(payload).hexdigest()==d['sha256'],sid+': source hash changed')
            try:
                with zipfile.ZipFile(p) as z:body=ET.fromstring(z.read('word/document.xml')).find(W+'body')
                ps=[]
                for para in body.iter(W+'p'):
                    s=''.join((n.text or '') if n.tag==W+'t' else ('\t' if n.tag==W+'tab' else '\n') for n in para.iter() if n.tag in {W+'t',W+'tab',W+'br'}).strip()
                    if s:ps.append(s)
                read=set()
                for a,b in d['read_ranges']:
                    check(1<=a<=b<=len(ps),sid+': invalid read range');read.update(range(a,b+1))
                for key in ['tags','mechanisms','script_checks','limits']:
                    for e in d[key]:
                        source_quotes+=1;q=e['p'];check(1<=q<=len(ps) and bool(e['quote']) and e['quote'] in ps[q-1],f'{sid} {key} P{q}: quote mismatch');check(q in read,f'{sid} P{q}: outside reported reading')
                for e in anchors.get(sid,[]):
                    q=e['p'];pattern_quotes+=1
                    check(1<=q<=len(ps) and bool(e['quote']) and e['quote'] in ps[q-1],f'{sid} pattern P{q}: quote mismatch')
                source_count+=1
            except (OSError,zipfile.BadZipFile,ET.ParseError,KeyError) as exc:errors.append(sid+': '+str(exc))
    print(json.dumps(dict(status='pass' if not errors else 'fail',dossiers=len(ds),families=len(families),quote_occurrences=quotes,source_documents_verified=source_count,source_quote_occurrences_verified=source_quotes,pattern_quote_occurrences_verified=pattern_quotes,errors=errors,boundary='Integrity and exact source alignment, not semantic correctness, original-video fidelity or market validation.'),ensure_ascii=False,indent=2))
    return 1 if errors else 0

if __name__=='__main__':sys.exit(main())
