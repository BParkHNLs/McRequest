'''
Script to produce the csv files for the sample requests
'''


#from pilot_V33_stats_Lxy1300_tkPt500MeV_lepPt400MeV_points import m_ctau_eff_time_s as points_B  
#from pilot_V33_stats_Lxy1300_tkPt500MeV_lepPt400MeV_Bc_points import m_ctau_eff_time_s as points_Bc
from for_request_points    import m_ctau_eff_time_s as points_B  
from for_request_points_Bc import m_ctau_eff_time_s as points_Bc

doScore = False  # should be false for the csv file for the request
version = '19072021' #12072021

if doScore:
  fout = open('request_{v}_score.csv'.format(v=version), 'w')
  #fout.write('dataset,fragment,events,generator,time per event,filter efficiency,size per event,score\n')
  fout.write('dataset,fragment,events,generator,time per event,size per event,match efficiency,filter efficiency,score\n')
else:
  fout = open('request_{v}.csv'.format(v=version), 'w')
  #fout.write('dataset,fragment,events,generator,time per event,filter efficiency,size per event\n')
  fout.write('dataset,fragment,events,generator,time per event,size per event,match efficiency,filter efficiency\n')

all_points = [(m,ctau,eff,time,size,nevts,'B') for m,ctau,eff,time,size,nevts in points_B] + [(m,ctau,eff,time,size,nevts,'Bc') for m,ctau,eff,time,size,nevts in points_Bc]

for m,ctau,eff,time,size,nevts,spc in all_points:
  # name for fragment
  if ctau!=0.01:
    frag_name = '{}ToNMuX_NToEMuPi_SoftQCD_b_mN{:.1f}_ctau{:.1f}mm'.format(spc,m,ctau)
  else:
    frag_name = '{}ToNMuX_NToEMuPi_SoftQCD_b_mN{:.1f}_ctau{:.2f}mm'.format(spc,m,ctau)
 
  # name for dataset
  # see https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=%2FBuToKPsi2S_Toee_Mufilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen%2FRunIIAutumn18MiniAOD-PUPoissonAve20_BParking_102X_upgrade2018_realistic_v15-v1%2FMINIAODSIM
  # and https://cms-pdmv.gitbook.io/project/mccontact/rules-for-dataset-names
  ds_name = '{}ToNMuX_NToEMuPi_SoftQCD_b_mN{}_ctau{}mm'.format(spc,str(m).replace('.', 'p'),str(ctau).replace('.','p'))

  ds = ds_name + '_TuneCP5_13TeV-pythia8-evtgen'
  path = 'genFragments/Generator/Pythia/BHNL/'
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
