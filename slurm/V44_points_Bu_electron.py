from python.common  import Point,Config,getCtauEff

m_ctau_eff_time_s = [
(1.00,    10.00, 2.77e-03, 34.70),
(1.50,    10.00, 2.51e-03, 28.35),
(2.00,    10.00, 2.31e-03, 28.06),
(3.00,    10.00, 7.31e-03, 10.17),
(4.50,     0.10, 1.04e-02, 6.88),
(1.00,  1000.00, 5.07e-04, 148.62),
(1.00,   100.00, 2.17e-03, 34.52),
(1.50,  1000.00, 5.31e-04, 151.16),
(1.50,   100.00, 2.08e-03, 37.98),
(2.00,  1000.00, 5.15e-04, 161.29),
(2.00,   100.00, 1.99e-03, 39.10),
(3.00,  1000.00, 2.50e-03, 35.36),
(3.00,   100.00, 6.88e-03, 11.55),
(3.00,     1.00, 7.27e-03, 11.23),
(4.50,   100.00, 1.02e-02, 8.57),
(4.50,    10.00, 1.06e-02, 8.58),
(4.50,     1.00, 1.04e-02, 7.25),
(1.02,    10.00, 2.77e-03, 29.71),
(1.04,    10.00, 2.74e-03, 27.73),
(1.06,    10.00, 2.73e-03, 28.19),
(1.08,    10.00, 2.64e-03, 29.15),
(1.10,    10.00, 2.62e-03, 34.80),
(1.12,    10.00, 2.61e-03, 32.68),
(1.14,    10.00, 2.57e-03, 29.61),
(1.16,    10.00, 2.59e-03, 32.24),
(1.18,    10.00, 2.59e-03, 32.70),
(1.20,    10.00, 2.62e-03, 27.50),
(1.22,    10.00, 2.63e-03, 26.89),
(1.24,    10.00, 2.59e-03, 32.76),
(1.26,    10.00, 2.59e-03, 29.51),
(1.28,    10.00, 2.56e-03, 29.48),
(1.30,    10.00, 2.56e-03, 28.68),
(1.32,    10.00, 2.62e-03, 28.18),
(1.34,    10.00, 2.59e-03, 26.41),
(1.36,    10.00, 2.52e-03, 29.83),
(1.38,    10.00, 2.54e-03, 33.04),
(1.40,    10.00, 2.61e-03, 32.46),
(1.42,    10.00, 2.55e-03, 28.40),
(1.44,    10.00, 2.49e-03, 27.98),
(1.46,    10.00, 2.54e-03, 27.77),
(1.48,    10.00, 2.54e-03, 29.86),
(1.53,    10.00, 2.54e-03, 30.90),
(1.56,    10.00, 2.56e-03, 27.56),
(1.59,    10.00, 2.49e-03, 31.15),
(1.62,    10.00, 2.44e-03, 30.20),
(1.65,    10.00, 2.37e-03, 28.07),
(1.68,    10.00, 2.38e-03, 30.95),
(1.71,    10.00, 2.42e-03, 31.42),
(1.74,    10.00, 2.36e-03, 31.97),
(1.77,    10.00, 2.38e-03, 34.62),
(1.80,    10.00, 2.38e-03, 32.57),
(1.83,    10.00, 2.31e-03, 33.54),
(1.86,    10.00, 2.33e-03, 30.89),
(1.89,    10.00, 2.34e-03, 32.14),
(1.92,    10.00, 2.31e-03, 34.24),
(1.95,    10.00, 2.32e-03, 32.88),
(1.98,    10.00, 2.33e-03, 31.32),
(2.05,    10.00, 2.32e-03, 30.35),
(2.10,    10.00, 2.38e-03, 30.43),
(2.15,    10.00, 2.36e-03, 32.08),
(2.20,    10.00, 2.34e-03, 35.25),
(2.25,    10.00, 2.40e-03, 37.09),
(2.30,    10.00, 2.47e-03, 31.71),
(2.35,    10.00, 2.55e-03, 26.41),
(2.40,    10.00, 2.59e-03, 29.61),
(2.45,    10.00, 2.67e-03, 29.24),
(2.50,    10.00, 2.76e-03, 29.61),
(2.55,    10.00, 2.96e-03, 25.51),
(2.60,    10.00, 3.08e-03, 23.74),
(2.65,    10.00, 3.31e-03, 21.55),
(2.70,    10.00, 3.56e-03, 18.33),
(2.75,    10.00, 3.88e-03, 18.66),
(2.80,    10.00, 4.18e-03, 17.83),
(2.85,    10.00, 4.78e-03, 15.86),
(2.90,    10.00, 5.54e-03, 13.41),
(2.95,    10.00, 6.46e-03, 11.92),
(3.05,     1.00, 8.47e-03, 9.91),
(3.10,     1.00, 9.65e-03, 7.15),
(3.15,     1.00, 1.05e-02, 6.46),
(3.20,     1.00, 1.07e-02, 5.85),
(3.25,     1.00, 1.10e-02, 5.81),
(3.30,     1.00, 1.12e-02, 5.94),
(3.35,     1.00, 1.12e-02, 7.13),
(3.40,     1.00, 1.12e-02, 6.43),
(3.45,     1.00, 1.10e-02, 7.06),
(3.50,     1.00, 1.09e-02, 6.52),
(3.55,     1.00, 1.09e-02, 7.36),
(3.60,     1.00, 1.09e-02, 8.40),
(3.65,     1.00, 1.09e-02, 7.61),
(3.70,     1.00, 1.07e-02, 6.59),
(3.75,     1.00, 1.05e-02, 6.94),
(3.80,     1.00, 1.07e-02, 7.20),
(3.85,     1.00, 1.09e-02, 7.35),
(3.90,     1.00, 1.07e-02, 6.26),
(3.95,     1.00, 1.07e-02, 7.88),
(4.00,     0.10, 1.06e-02, 7.76),
(4.10,     0.10, 1.08e-02, 6.35),
(4.20,     0.10, 1.09e-02, 6.36),
(4.30,     0.10, 1.07e-02, 6.45),
(4.40,     0.10, 1.08e-02, 6.16),
(4.60,     0.10, 1.05e-02, 6.34),
(4.70,     0.10, 1.06e-02, 6.02),
(3.05,    10.00, 8.57e-03, 7.36),
(3.10,    10.00, 9.56e-03, 6.38),
(3.15,    10.00, 1.03e-02, 6.96),
(3.20,    10.00, 1.07e-02, 6.10),
(3.25,    10.00, 1.11e-02, 5.36),
(3.30,    10.00, 1.11e-02, 5.63),
(3.35,    10.00, 1.10e-02, 5.62),
(3.40,    10.00, 1.12e-02, 6.12),
(3.45,    10.00, 1.11e-02, 7.66),
(3.50,    10.00, 1.08e-02, 8.33),
(3.55,    10.00, 1.10e-02, 6.99),
(3.60,    10.00, 1.09e-02, 5.74),
(3.65,    10.00, 1.09e-02, 6.29),
(3.70,    10.00, 1.07e-02, 6.94),
(3.75,    10.00, 1.05e-02, 6.89),
(3.80,    10.00, 1.07e-02, 6.75),
(3.85,    10.00, 1.09e-02, 4.84),
(3.90,    10.00, 1.08e-02, 5.03),
(3.95,    10.00, 1.07e-02, 6.05),
]

points = []
for m,ctau,eff,time in m_ctau_eff_time_s:
  p   = Point(mass=m,ctau=ctau,vv=None,ismaj=True)
  cfg = Config(nevtseff=5000,muoneff=eff,displeff=1.0,timeevt=time,timejob=1,contingency=3)
  p.setConfig(cfg)
  points.append(p)



