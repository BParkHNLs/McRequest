'''
Script to produce the csv files for the sample requests
'''

from request_points_Apr22 import request_points as points_B
from request_points_Apr22_Bc import request_points as points_Bc

doScore = True  # should be false for the csv file for the request
doBc = True
version = '13042022'

if doScore:
  fout_name = 'request_{v}_score.csv'.format(v=version) if not doBc else 'request_{v}_Bc_score.csv'.format(v=version)
  fout = open(fout_name, 'w')
  fout.write('dataset,fragment,events,generator,time per event,size per event,match efficiency,filter efficiency,score\n')
else:
  fout_name = 'request_{v}.csv'.format(v=version) if not doBc else 'request_{v}_Bc.csv'.format(v=version)
  fout = open(fout_name, 'w')
  fout.write('dataset,fragment,events,generator,time per event,size per event,match efficiency,filter efficiency\n')

if not doBc:
  all_points = [(m,ctau,eff,time,size,nevts,'B') for m,ctau,eff,time,size,nevts in points_B]
else:
  all_points = [(m,ctau,eff,time,size,nevts,'Bc') for m,ctau,eff,time,size,nevts in points_Bc]

for m,ctau,eff,time,size,nevts,spc in all_points:
  # name for fragment
  if ctau!=0.01:
    frag_name = '{}ToHNLMuX_HNLToMuPi_SoftQCD_b_mHNL{:.1f}_ctau{:.1f}mm'.format(spc,m,ctau)
  else:
    frag_name = '{}ToHNLMuX_HNLToMuPi_SoftQCD_b_mHNL{:.1f}_ctau{:.2f}mm'.format(spc,m,ctau)
 
  # name for dataset
  # see https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=%2FBuToKPsi2S_Toee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen%2FRunIIAutumn18MiniAOD-PUPoissonAve20_BParking_102X_upgrade2018_realistic_v15-v1%2FMINIAODSIM
  # and https://cms-pdmv.gitbook.io/project/mccontact/rules-for-dataset-names
  ds_name = '{}ToHNLMuX_HNLToMuPi_SoftQCD_b_mHNL{}_ctau{}mm'.format(spc,str(m).replace('.', 'p'),str(ctau).replace('.','p'))
  ds = ds_name + '_TuneCP5_13TeV-pythia8-evtgen'
  if not doBc:
    path = 'genFragments/Generator/Pythia/BToHNLMuX_HNLToMuPi/' 
  else:
    path = 'genFragments/Hadronizer/13TeV/BcToHNLMuX_HNLToMuPi/'
  fragment = path + frag_name + '_TuneCP5_13TeV_pythia8-evtgen' + '_cfi.py' 
  events = nevts
  generator = 'pythia8-evtgen'
  timeperevent = '{:.2e}'.format(time*eff)   # NOTE: time         (for us)          is the time it takes to generate an event that passes the filter (after filter)
                                             #       timeperevent (for McM request) is the time it takes to generate an event before the requirement on the filter
  filterefficiency = '{:.2e}'.format(eff)
  sizeperevent = '{:.2e}'.format(size)


  if not doScore:
    fout.write('{dataset},{fragment},{events},{generator},{timeperevent},{sizeperevent},{matchefficiency},{filterefficiency}\n'.format(
                dataset=ds, fragment=fragment, events=events, generator=generator, matchefficiency=1.0,
                timeperevent=timeperevent, filterefficiency=filterefficiency, sizeperevent=sizeperevent))
  else:
    fout.write('{dataset},{fragment},{events},{generator},{timeperevent},{sizeperevent},{matchefficiency},{filterefficiency},{score}\n'.format(
                dataset=ds, fragment=fragment, events=events, generator=generator, matchefficiency=1.0,
                timeperevent=timeperevent, filterefficiency=filterefficiency, sizeperevent=sizeperevent,score=(8*3600/(time*eff))*eff))
  
fout.close() 
