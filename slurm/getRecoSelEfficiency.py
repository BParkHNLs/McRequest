'''
Script to retrieve for each mass-ctau point:
- reconstruction + pre-selection efficiency, after running the analysis
'''
import sys
import os
import subprocess
import glob
import ROOT

from python.common import Point

#import ROOT


def getOptions():

  # convention: no capital letters

  from argparse import ArgumentParser

  parser = ArgumentParser(description='Production helper for B-initiated HNL signals', add_help=True)

  parser.add_argument('--pl', type=str, dest='ver', help='production label, e.g. V00_v00', default='V00_v00')
  parser.add_argument('--points', type=str, dest='pointFile', help='name of file contaning information on scan to be run', default='points.py')
  parser.add_argument('--user', type=str, dest='user', help='', default='mratti')
  parser.add_argument('--nanotag', type=str, dest='nanotag', help='', default='looseselection')

  return parser.parse_args()

if __name__ == "__main__":

  opt = getOptions()
  ROOT.gROOT.SetBatch(True)
  ROOT.TH1.SetDefaultSumw2()

  ps = __import__(opt.pointFile.split('.py')[0])
  points = ps.points

  for p in points:

    print('\n===> Processing new point')
    #p.stamp_simpli()
    print 'mass{m}_ctau{ctau}'.format(m=p.mass,ctau=p.ctau,)
 
    # nano merged file
    nanofile = '/pnfs/psi.ch/cms/trivcat/store/user/{u}/BHNLsGen/{pl}/mass{m}_ctau{ctau}/nanoFiles/merged/bparknano_{nt}.root'.format(
        pl=opt.ver,m=p.mass,ctau=p.ctau,
        u=opt.user,nt=opt.nanotag)
    print nanofile
    f = ROOT.TFile.Open(nanofile,'READ')


    try:
      tree = f.Get('Events')
      print type(tree)
      h =    ROOT.TH1F('h', 'h', 1, 0., 1500.)
      htot = ROOT.TH1F('htot', 'htot', 1, 0., 1500.)
      tree.Draw('BToMuMuPi_sv_lxy>>h', 'BToMuMuPi_isMatched==1', 'goff')
      truns = f.Get("Runs")
      truns.Draw('genEventCount>>h_ngen')
      h_ngen = truns.GetHistogram()
      #print h_ngen.GetEntries(), h_ngen.GetMean()
      htot.SetBinContent(1,h_ngen.GetEntries() * h_ngen.GetMean() )
      htot.Scale(0.5) # electron vs muon channel
      #htot.SetBinError(1,sqrt(htot.GetBinContent(1)))
      #print htot.GetBinContent(1),h.GetBinContent(1)

      peff = ROOT.TEfficiency(h,htot)
      print 'pass={} tot={}'.format(h.Integral(),htot.Integral())
      print 'eff={:.4f} + {:.4f} - {:.4f}'.format(peff.GetEfficiency(1),peff.GetEfficiencyErrorUp(1), peff.GetEfficiencyErrorLow(1))

    except:
      print 'no eff could be calculated'
      pass
    
    #eff = float(num)/float(den)
    #print('{:.2f} {:.2f} {:.2f}%'.format(num,den,eff*100)) 
