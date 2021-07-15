from python.common  import Point,Config,getCtauEff

## TODO:
## add number of events to csv file
## follow-up exact points: e.g. mass=2 GeV for Bc, are they needed? 

m_ctau_eff_time_s = [

## loosened , but excluded
###(1.0,  10000.0, 1.13e-03, 90.00, 720.6),
## (1.0,  10000.0, 1.79e-04, 927.77, 662.8), excluded
###(1.5,  10000.0, 1.19e-03, 73.04, 600.5),
##(1.5,  10000.0, 1.24e-04, 602.20, 703.8), excluded
###(2.0,  10000.0, 1.14e-03, 78.44, 737.3),
##(2.0,  10000.0, 4.77e-05, 1843.10, 789.1), excluded
##(2.0,   1000.0, 4.07e-04, 262.53, 697.9), too tight, was loosened
##(4.5,    100.0, 4.36e-04, 261.42, 666.5), too tight, was loosened
##(4.5,     10.0, 5.00e-04, 236.37, 668.2), too tight, was loosened
##(4.5,      1.0, 5.22e-04, 227.18, 667.3), too tight, was loosened   
##(4.5,      0.1, 5.39e-04, 213.30, 683.8), too tight, was loosened  

# normal B
(1.0,   1000.0, 1.59e-03, 97.77, 662.9,   13888889),  
(1.0,    100.0, 5.17e-03, 51.15, 663.2,   3125000),  
(1.0,     10.0, 5.85e-03, 51.72, 674.1,   704225),   
(1.5,   1000.0, 1.03e-03, 112.96, 667.2,  6756757),  
(1.5,    100.0, 3.35e-03, 46.28, 679.0,   1288660),  
(1.5,     10.0, 3.72e-03, 46.97, 680.9,   486381),   
(2.0,   1000.0, 8.95e-04, 93.73, 604.5,   11375769), 
(2.0,    100.0, 1.57e-03, 75.14, 686.9,   1329787),  
(2.0,     10.0, 1.78e-03, 65.18, 695.9,   359195),   
(3.0,   1000.0, 2.40e-03, 54.38, 643.2,   2380952),  
(3.0,    100.0, 5.58e-03, 56.78, 652.9,   836120),   
(3.0,     10.0, 5.87e-03, 60.08, 657.7,   378788),   
(3.0,      1.0, 5.87e-03, 55.43, 657.4,   337838),   
(4.5,    100.0, 6.10e-04, 182.14, 613.9,  806442),   
(4.5,     10.0, 8.00e-04, 105.12, 605.6,  409585),   
(4.5,      1.0, 8.35e-04, 101.50, 600.3,  333763),   
(4.5,      0.1, 8.62e-04, 98.62, 602.1,   419783),   


]

points = []
for m,ctau,eff,time,size,nevts in m_ctau_eff_time_s:
  p   = Point(mass=m,ctau=ctau,vv=None,ismaj=True)
  cfg = Config(nevtseff=5000,muoneff=eff,displeff=1.0,timeevt=time,timejob=12,contingency=3)
  p.setConfig(cfg)
  points.append(p)

  # 

  #print('mass={:.1f} vv={:.1e} before={:.1e}, after={:.1e}'.format(p.mass,p.vv,displEff[m][vv],getCtauEff(p.ctau*4.,1000.))) # 4 is the assumed beta*gamma factor...
  #cfg.stamp()
  







