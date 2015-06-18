from mpmath import *
def relit(dist): 
    f1 = lambda s, t: dist*dist/ (2*pow(((s - t) * (s - t) + dist*dist), 1.5))
    f=lambda s,t:f1(s,t)*f1(s,t)
    return quad(f,[0,1],[0,1])
fname = "rel"+ ".txt"
fo = open(fname, "w")
for dist in [1 , 0.5, 0.25, 0.125, 0.0625]:
    fo.write("dist="+str(dist)+"L2="+str(relit(dist))+"\n")