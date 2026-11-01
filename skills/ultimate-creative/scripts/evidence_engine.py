#!/usr/bin/env python3
"""Read-only support counts, historical cohorts and reproducible creative card seeds."""
import argparse,collections,itertools,json,random,statistics
from pathlib import Path

def load(path):
    return json.loads(path.read_text())

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--data-dir',type=Path,default=Path(__file__).resolve().parents[1]/'references')
    sub=ap.add_subparsers(dest='command',required=True)
    sub.add_parser('coverage')
    def route(p):p.add_argument('--route',choices=['all','douyin','realistic','animation'],default='all')
    p=sub.add_parser('search');p.add_argument('--query',default='');p.add_argument('--source-id');p.add_argument('--limit',type=int,default=5);p.add_argument('--full',action='store_true');route(p)
    p=sub.add_parser('support');p.add_argument('--tags',nargs='+',required=True);p.add_argument('--limit',type=int,default=5);route(p)
    p=sub.add_parser('mechanism');p.add_argument('code');p.add_argument('--limit',type=int,default=5);route(p)
    p=sub.add_parser('market');p.add_argument('--tags',nargs='+',required=True);p.add_argument('--board',choices=['ai','comic'],required=True);p.add_argument('--date');p.add_argument('--min-cohort',type=int,default=20);p.add_argument('--min-arm',type=int,default=5)
    p=sub.add_parser('draw');p.add_argument('--lock',action='append',default=[]);p.add_argument('--count',type=int,default=5);p.add_argument('--seed',type=int,required=True);route(p)
    a=ap.parse_args();data=load(a.data_dir/'full-dossiers.json');stats=load(a.data_dir/'corpus-statistics.json');taxonomy=load(a.data_dir/'tag-taxonomy.json')['tags'];ds=data['dossiers']
    byid={d['source_id']:d for d in ds};bytag={t['id']:t for t in taxonomy}
    narrow_terms={};resolution=[]
    def resolve(terms):
        narrow_terms.clear();resolution.clear()
        found=[];unknown=[]
        for s in terms:
            matched=[t['id'] for t in taxonomy if s in [t['id'],t['name'],*t['patterns']]]
            if len(matched)==1:
                tid=matched[0];found.append(tid);narrow=s not in [tid,bytag[tid]['name']]
                if narrow:narrow_terms.setdefault(tid,[]).append(s)
                resolution.append(dict(input=s,parent_tag_id=tid,parent_tag_name=bytag[tid]['name'],scope='literal term within coded raw tags' if narrow else 'controlled parent category'))
            else:unknown.append(s)
        return list(dict.fromkeys(found)),unknown
    def filtered():return [d for d in ds if a.route=='all' or d['route']==a.route]
    def match(d,tids):
        return set(tids)<={t['id'] for t in d['canonical_tags']} and all(any(term in raw['tag'] for raw in d['tags']) for tid in tids for term in narrow_terms.get(tid,[]))
    def card(d):return dict(source_id=d['source_id'],family_id=d['family_id'],title=d['title'],route=d['route'],story=d['story'],tags=d['canonical_tags'],limits=d['limits'])
    def support(rows,tids,unknown,limit):
        hits=[d for d in rows if match(d,tids)] if tids else []
        partial=[]
        for combo in [(t,) for t in tids]+list(itertools.combinations(tids,2)):
            subset=[d for d in rows if match(d,combo)]
            partial.append(dict(tags=[bytag[t]['name'] for t in combo],documents=len(subset),families=len({d['family_id'] for d in subset}),source_ids=[d['source_id'] for d in subset]))
        return dict(requested_tags=[bytag[t]['name'] for t in tids],unmapped_constraints=unknown,documents=None if unknown else len(hits),families=None if unknown else len({d['family_id'] for d in hits}),mapped_subset_documents=len(hits),mapped_subset_families=len({d['family_id'] for d in hits}),corpus_denominator=dict(documents=len(rows),families=len({d['family_id'] for d in rows})),source_ids=[d['source_id'] for d in hits],examples=[card(d) for d in hits[:limit]],partial_support=partial,interpretation='Conjunction of coded parent tags plus any literal narrow-alias constraints in a single dossier, then deduplicated by story family. Unmapped constraints make full-combination support unknown. Partial support is not evidence for the full combination. Zero coded support does not prove absence or low potential.')
    if a.command=='coverage':
        result={k:stats[k] for k in ['complete','snapshot_date','counts','raw_tag_phrases','quote_occurrences','methodology']}
    elif a.command=='search':
        rows=filtered();terms=a.query.lower().split()
        rows=[d for d in rows if (not a.source_id or d['source_id']==a.source_id) and all(s in json.dumps({k:d[k] for k in ['title','story','tags','transfer','mechanisms']},ensure_ascii=False).lower() for s in terms)]
        result=dict(matches=len(rows),results=[d if a.full else card(d) for d in rows[:max(0,a.limit)]],ordering='source ID; not a popularity ranking')
    elif a.command=='support':
        tids,unknown=resolve(a.tags);result=support(filtered(),tids,unknown,max(0,a.limit));result['tag_resolution']=resolution
    elif a.command=='mechanism':
        record=next((r for r in stats['mechanisms'] if r['code']==a.code),None)
        if not record:ap.error('mechanism must be M01..M20')
        rows=[d for d in filtered() if any(m['code']==a.code for m in d['mechanisms'])]
        result=dict(code=a.code,name=record['name'],support=record['support'][a.route],examples=[dict(source_id=d['source_id'],title=d['title'],evidence=[e for e in d['mechanisms'] if e['code']==a.code],limits=d['limits']) for d in rows[:max(0,a.limit)]],interpretation=stats['methodology'])
    elif a.command=='market':
        tids,unknown=resolve(a.tags)
        if unknown or not tids:
            result=dict(status='insufficient_tag_definition',unmapped_constraints=unknown,comparisons=[])
        else:
            groups=collections.defaultdict(list)
            for s in data['snapshots']:
                if s['board']==a.board and (not a.date or s['date']==a.date):groups[s['date']].append(s)
            comparisons=[]
            for dt,rows in sorted(groups.items()):
                fam=collections.defaultdict(list)
                for s in rows:fam[s['family_id']].append(s)
                yes=[];no=[];family_rows=[]
                for fid,ss in fam.items():
                    # Require a positive conjunction in one same-day source. Missing coding is not a true negative.
                    positive=any(match(byid[s['source_id']],tids) for s in ss)
                    rank=statistics.median(s['rank'] for s in ss)
                    (yes if positive else no).append(rank)
                    family_rows.append(dict(family_id=fid,source_ids=[s['source_id'] for s in ss],coded_positive=positive,rank_median=rank))
                eligible=len(fam)>=max(1,a.min_cohort) and len(yes)>=max(1,a.min_arm) and len(no)>=max(1,a.min_arm)
                comparisons.append(dict(date=dt,platform='红果',board=a.board,families=len(fam),coded_positive=len(yes),not_coded_positive=len(no),eligible_for_descriptive_comparison=eligible,positive_rank_median=statistics.median(yes) if eligible else None,other_rank_median=statistics.median(no) if eligible else None,rank_difference_positive_minus_other=(statistics.median(yes)-statistics.median(no)) if eligible else None,family_rows=family_rows))
            result=dict(tags=[bytag[t]['name'] for t in tids],tag_resolution=resolution,comparisons=comparisons,thresholds=dict(cohort=a.min_cohort,each_arm=a.min_arm),interpretation='Historical local ledger only. Lower rank is better. Thresholds are disclosure rules, not statistical significance. Other group means not coded positive, not verified absence. Sample is selected, incomplete and non-random; repeated families across dates are not independent replications. No causal effect, current trend or hit probability is established.')
    else:
        if not 1<=a.count<=20:ap.error('--count must be 1..20')
        tids,unknown=resolve(a.lock);rows=filtered();rng=random.Random(a.seed)
        fam=collections.defaultdict(list)
        for d in rows:fam[d['family_id']].append(d)
        candidates=[];used=set()
        # A slot policy for varied seeds; the author must still create and test causality.
        slots=[{'身份','外形','处境'},{'世界','世界触发'},{'关系'},{'任务'},{'机制','情绪承诺'}]
        for _ in range(300):
            chosen=list(tids);origins=[]
            for slot in slots:
                if any(bytag[t]['dimension'] in slot for t in chosen):continue
                if len(chosen)+len(unknown)>=max(5,len(a.lock)+2):break
                eligible={f:[(d,t) for d in dd for t in d['canonical_tags'] if t['dimension'] in slot and t['id'] not in chosen] for f,dd in fam.items()}
                eligible={f:v for f,v in eligible.items() if v}
                if not eligible:continue
                f=rng.choice(sorted(eligible));d,t=rng.choice(eligible[f]);chosen.append(t['id']);origins.append(dict(tag=t['name'],source_id=d['source_id'],family_id=f))
            key=tuple(sorted(chosen))
            if key in used:continue
            used.add(key);ev=support(rows,chosen,unknown,0)
            candidates.append(dict(candidate_id=f'C{len(candidates)+1:02}',locked=a.lock,combined_tags=list(dict.fromkeys(a.lock+[bytag[t]['name'] for t in chosen if t not in tids])),drawn_sources=origins,exact_combination_support=dict(documents=ev['documents'],families=ev['families'],mapped_subset_families=ev['mapped_subset_families']),status='creative seed; not a finished direction or market recommendation',required_next_step='Write protagonist goal, causal strategy, relationship conflict, cost, first scene and three different episode payoffs; repair incompatibilities without dropping user locks.'))
            if len(candidates)==a.count:break
        result=dict(seed=a.seed,sampling='Uniform story family, then a qualifying coded tag within the selected slot; not popularity weighting.',route=a.route,unmapped_user_locks=unknown,requested_count=a.count,returned_count=len(candidates),pool_exhausted=len(candidates)<a.count,candidates=candidates)
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
