from mpmath import *
import numpy


def quadit(f,(a1,b1),(a2,b2),(a3,b3),(a4,b4),deg=5):

    x,w=([-0.90617985, -0.53846931,  0.        ,  0.53846931,  0.90617985],[ 0.23692689,  0.47862867,  0.56888889,  0.47862867,  0.23692689])
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

def project_kernel_haar_phi(n,dist):
    # # kernel
    # dist=1
    # f1 = lambda s, t: dist*dist/ (2*pow(((s - t) * (s - t) + dist*dist), 1.5))
    # f = lambda s, t: f1(s, t) * pow(n, 0.5) * pow(n, 0.5)
    def fun(x1,y1,x2,y2):
        # return x1*y1*x2*y2
        den = 3.14159265359*((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+dist*dist)*((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+dist*dist)/float(dist*dist)
        # print n*n/den
        # print n
        return n*n/den
    K = [[[[1 for x in range(n)] for x in range(n)] for x in range(n)] for x in range(n)] 
    for i1 in range(0, n):
        print i1
        for j1 in range(0, n):
            for i2 in range(0, n):
                for j2 in range(0, n):
                    # pass
                    # print i1
                    # K[i1][j1][i2][j2] =
                    K[i1][j1][i2][j2] = quadit(
                        fun,    [i1 / float(n), (i1 + 1) / float(n)],
                                [j1 / float(n), (j1 + 1) / float(n)],
                                [i2 / float(n), (i2 + 1) / float(n)],
                                [j2 / float(n), (j2 + 1) / float(n)])
                    # print       [i1 / float(n), (i1 + 1) / float(n)],\
                                # [j1 / float(n), (j1 + 1) / float(n)],\
                                # [i2 / float(n), (i2 + 1) / float(n)],\
                                # [j2 / float(n), (j2 + 1) / float(n)]
                    # if i1==i2 and j1==j2:
                        # print K[i1][j1][i2][j2]
    return K

# print project_kernel_haar_phi(4)
# print ([[1]*n]*n)
