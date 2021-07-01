from pilot_V33_stats_Lxy1300_tkPt500MeV_lepPt400MeV_points import m_ctau_eff_time_s as points_B  
from pilot_V33_stats_Lxy1300_tkPt500MeV_lepPt400MeV_Bc_points import m_ctau_eff_time_s as points_Bc


fout = open('request_newtune.csv', 'w')
#fout.write('dataset,fragment,events,generator,time per event,filter efficiency,score\n')
fout.write('dataset,fragment,events,generator,time per event,filter efficiency,size per event\n')

all_points = [(m,ctau,eff,time,size,'B') for m,ctau,eff,time,size in points_B] + [(m,ctau,eff,time,size,'Bc') for m,ctau,eff,time,size in points_Bc]

for m,ctau,eff,time,size,spc in all_points:

  # name for fragment
  if ctau!=0.01:
    name = '{}ToNMuX_NToEMuPi_SoftQCD_b_mN{:.1f}_ctau{:.1f}mm'.format(spc,m,ctau)
  else:
    name = '{}ToNMuX_NToEMuPi_SoftQCD_b_mN{:.1f}_ctau{:.2f}mm'.format(spc,m,ctau)
 
  # name for dataset
  ds_name = '{}ToNMuX_NToEMuPi_SoftQCD_b_mN{}_ctau{}mm'.format(spc,str(m).replace('.', 'p'),str(ctau).replace('.','p'))

  ds = ds_name + '_TuneCP5_13TeV-pythia8-evtgen'
  path = 'genFragments/Generator/Pythia/BHNL/'
  fragment = path + name + '_TuneCP5_13TeV_pythia8-evtgen' + '_cfi.py' 
  events = 100000
  generator = 'pythia8-evtgen'
  timeperevent = '{:.2e}'.format(time*eff)
  #timeperevent = '{:.2e}'.format(time)
  filterefficiency = '{:.2e}'.format(eff)
  sizeperevent = '{:.2e}'.format(size)

  fout.write('{dataset},{fragment},{events},{generator},{timeperevent},{filterefficiency},{sizeperevent}\n'.format(
                dataset=ds, fragment=fragment, events=events, generator=generator,
                timeperevent=timeperevent, filterefficiency=filterefficiency, sizeperevent=sizeperevent))
  #fout.write('{dataset},{fragment},{events},{generator},{timeperevent},{filterefficiency},{score}\n'.format(
  #              dataset=ds, fragment=fragment, events=events, generator=generator,
  #              timeperevent=timeperevent, filterefficiency=filterefficiency, score=(8*3600/(time*eff))*eff))
  
fout.close() 
