from mpmath import *
import numpy
from m2_phi import *

def quadit(f,(a1,b1),(a2,b2),(a3,b3),(a4,b4),deg=5):

    x,w=numpy.polynomial.legendre.leggauss(deg)
    bma1=(b1-a1)/2.0
    bpa1=(b1+a1)/2.0
    bma2=(b2-a2)/2.0
    bpa2=(b2+a2)/2.0
    bma3=(b3-a3)/2.0
    bpa3=(b3+a3)/2.0
    bma4=(b4-a4)/2.0
    bpa4=(b4+a4)/2.0

    # points=[) for i in range(len(x))]
    sum=0
    for i in range(len(x)):
        for j in range(len(x)):
            for k in range(len(x)):
                for l in range(len(x)):
                    sum=sum+w[i]*w[j]*w[k]*w[l]*f(  bma1*x[i]+bpa1,
                                                    bma2*x[j]+bpa2,
                                                    bma3*x[k]+bpa3,
                                                    bma4*x[l]+bpa4)
    return sum*bma1*bma2*bma3*bma4

def project_kernel_m2_phi(n):
    # # kernel
    # dist=1
    # f1 = lambda s, t: dist*dist/ (2*pow(((s - t) * (s - t) + dist*dist), 1.5))
    # f = lambda s, t: f1(s, t) * pow(n, 0.5) * pow(n, 0.5)
    def fun(x1,y1,x2,y2):
        # return x1*y1*x2*y2
        # den = 3.14159265359*((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+dist*dist)*((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+dist*dist)/float(dist*dist)
        den=1
        num=x1*y1*x2*y2
        # print n*n/den
        # print n
        return num/den
    K = [[[[1 for x in range(2*n)] for x in range(2*n)] for x in range(2*n)] for x in range(2*n)] 
    a=1.0/n
    fl=[phi_1_m2, phi_2_m2 ]
    print fl[0]
    for i1 in range(0, 2*n):
        print i1
        for j1 in range(0, 2*n):
            for i2 in range(0, 2*n):
                for j2 in range(0, 2*n):
                    f=lambda x1,y1,x2,y2:   fun(x1,y1,x2,y2)*\
                                            dia_trans(x1,a,(i1/2) / float(n),fl[i1%2])*\
                                            dia_trans(y1,a,(j1/2) / float(n),fl[j1%2])*\
                                            dia_trans(x2,a,(i2/2) / float(n),fl[i2%2])*\
                                            dia_trans(y2,a,(j2/2) / float(n),fl[j2%2])
                    K[i1][j1][i2][j2] = quadit(
                        f,    [(i1/2) / float(n), ((i1/2) + 1) / float(n)],
                                [(j1/2) / float(n), ((j1/2) + 1) / float(n)],
                                [(i2/2) / float(n), ((i2/2) + 1) / float(n)],
                                [(j2/2) / float(n), ((j2/2) + 1) / float(n)])
                    print  K[i1][j1][i2][j2],[(i1/2) / float(n), ((i1/2) + 1) / float(n)],     [(j1/2) / float(n), ((j1/2) + 1) / float(n)],[(i2/2) / float(n), ((i2/2) + 1) / float(n)],[(j2/2) / float(n), ((j2/2) + 1) / float(n)],\
                    "sg"
                    # ,fl[i1%2],fl[j1%2],fl[i2%2],fl[j2%2]
                    # if f[i1%2]=="phi_1_m2":
                    #     print "phi_1_m2"
    return K

# print project_kernel_m2_phi(4,1)
# print ([[1]*n]*n)