from mpmath import *
f1 = lambda s, t: (s+0.1)*(t+0.1)/ (2*pow(((s+0.1)*(s+0.1) +(t+0.1)*(t+0.1)), 1.5))
f_f = lambda s, t: f1(s, t) *f1(s, t)
print quad(f_f,[0,1],[0,1])

