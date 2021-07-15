from python.common  import Point,Config,getCtauEff

## TODO:
## add number of events to csv file
## follow-up exact points: e.g. mass=2 GeV for Bc, are they needed? 

m_ctau_eff_time_s = [

## BC
##(2.0,  10000.0, 1.87e-02, 29.72, 591.7),
##(2.0,   1000.0, 1.01e-01, 32.98, 598.9),
##(2.0,    100.0, 1.88e-01, 45.55, 602.2),
##(2.0,     10.0, 1.92e-01, 45.09, 601.6),

# Bc
(3.0,   1000.0, 8.52e-02, 46.54, 608.5,   2000000),   
(3.0,    100.0, 1.53e-01, 45.83, 609.0,   840336),  
(3.0,     10.0, 1.54e-01, 42.63, 609.0,   452489),  
(3.0,      1.0, 1.54e-01, 46.37, 609.0,   473934),  
(4.5,    100.0, 3.40e-02, 39.28, 630.1,   621118),  
(4.5,     10.0, 3.49e-02, 30.68, 630.1,   315457),  
(4.5,      1.0, 3.47e-02, 31.01, 630.6,   386847),  
(4.5,      0.1, 3.47e-02, 29.74, 631.5,   684932),  
(5.5,     10.0, 1.22e-03, 80.61, 681.0,   814332),  
(5.5,      1.0, 1.22e-03, 82.08, 681.7,   883392),  
(5.5,      0.1, 1.23e-03, 80.95, 681.6,   1152074), 
(5.5,     0.01, 1.19e-03, 77.47, 687.0,   1162791), 

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
  







