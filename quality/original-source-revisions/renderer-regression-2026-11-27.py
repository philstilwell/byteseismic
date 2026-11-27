#!/usr/bin/env python3
"""Read-only regression checks for the November27 source-structure additions.
Run from the repository root. No builds or page writes are performed.
"""
import copy,json,pathlib,sys,subprocess,types
sys.path.insert(0,'scripts')
import revise_source_conversations as r
import revise_site_native_profiles as s
import revise_empiricists_from_original as e
counts={'conversation':0,'siteNative':0,'empiricists':0,'legacyAnnotationParity':0}
prior=types.ModuleType('prior_renderer');prior.__file__=str(pathlib.Path('scripts/revise_source_conversations.py').resolve())
exec(compile(subprocess.check_output(['git','show','bcec2e1e0daf626081e21f76cd652dfb352f5aa8:scripts/revise_source_conversations.py'],text=True),prior.__file__,'exec'),prior.__dict__)
for cf in sorted(r.DATA.glob('*-edits.json')):
 c=json.loads(cf.read_text())
 if 'pageFile' in c:
  h=pathlib.Path(c['pageFile']).read_text();rendered=r.render(c)
  if cf.stem in ('philosopher-club-membership-edits','philosophers-or-philosophy-edits'):
   assert h==subprocess.check_output(['git','show','bcec2e1e0daf626081e21f76cd652dfb352f5aa8:'+c['pageFile']],text=True)
   assert prior.render(c)==rendered
   assert h.splitlines()[1:]==rendered.splitlines()[1:]
   assert 'cycle 7 batch 100' in h.splitlines()[0]
   r.verify(c,rendered);prior.verify(c,rendered);counts['legacyAnnotationParity']+=1
  else:r.verify(c,h);assert rendered==h;counts['conversation']+=1
 elif cf.name.endswith('-site-native-edits.json'):
  if 'pagePath' not in c:c['pagePath']='/philosophers/'+cf.name.replace('-site-native-edits.json','')+'/'
  h=pathlib.Path(c['pagePath'].strip('/')+'/index.html').read_text();s.verify(c,h);assert s.render(c)==h;counts['siteNative']+=1
 elif cf.name=='empiricists-edits.json':
  h=pathlib.Path('philosophers/empiricists/index.html').read_text();e.verify(h);assert e.render()==h;counts['empiricists']+=1
for slug,field,child in [('what-is-bayes-theorem','headingWithinFirstResponseColumn','groupSha256'),('hypostatic-illogic','trailingResponseSiblingRanges','sha256'),('induction-cold-reading','sourceVideoLinks','sourceUrl')]:
 c=json.loads((r.DATA/f'{slug}-edits.json').read_text());mapping=c[field];x=mapping[next(iter(mapping))];x=x[0] if isinstance(x,list) else x;x[child]='intentionally-invalid'
 try:r.render(c)
 except AssertionError:pass
 else:raise AssertionError(field+' accepted invalid source identity')
print(json.dumps(counts,sort_keys=True))
