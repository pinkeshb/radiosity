from mpmath import *
from m2_phi import *
from matplotlib import pyplot
# m=linspace(0,1,250)
# # # i=0
# # # j=1
# # # # f1 = lambda s, t: s-t
# # # # f=lambda s,t: f1(s,t)*dia_trans(s,0.25,(i/2)/float(n),phi_1_m2)*dia_trans(t,0.25,(j/2)/float(n),phi_2_m2)
# # # # n=4
# # # print [(i/2)/float(n),((i/2)+1)/float(n)],[(j/2)/float(n),((j/2)+1)/float(n)]
# # # print quad(f,[(i/2)/float(n),((i/2)+1)/float(n)],[(j/2)/float(n),((j/2)+1)/float(n)])
# # y=[dia_trans(z,0.25,(6/2)/float(4),phi_2_m2) for z in m]
# # pyplot.plot(m,y)
# # print y ,"y"
# # n=4
# # i=0
# # pyplot.show()
# f=lambda s: dia_trans(s,0.25,0,phi_2_m2)*dia_trans(s,0.25,0,phi_2_m2)
# # print [(i/2)/float(n),((i/2)+1)/float(n)],[(j/2)/float(n),((j/2)+1)/float(n)]
# # print quad(f,[0,0.25])
# print f(0.0)
# # y=[f for z in m]
# pyplot.plot(m,y)
# print y ,"y"