from mpmath import *
from m2_phi import *
from matplotlib import pyplot


def project_kernel_m2_phi(n):
    # kernel
    dist=0.25
    f1 = lambda s, t: dist*dist/ (2*pow(((s - t) * (s - t) + dist*dist), 1.5))
    # basis
    # amplitude=pow(n,0.5)
    # f2 = lambda s: amplitude
    # f3 = lambda s: amplitude
    # integrand
    # f = lambda s,t: f1(s,t)*f2(s)*f3(t)
    # f = lambda s,t: f1(s,t)*f3(t)*f2(s)
    # m = linspace(0, 1, 250)
    K = matrix(n * 2, n * 2)
    a=1.0/n
    for i in range(0, n * 2):
        for j in range(0, n * 2):
            if i % 2 == 0 and j % 2 == 0:
                print 11
                f = lambda s, t: f1(s, t) * dia_trans(s, a, (i / 2) / float(n),
                                          phi_1_m2) * dia_trans(t, a, (j / 2) / float(n), phi_1_m2)
            if i % 2 == 0 and j % 2 == 1:
                print 12
                f = lambda s, t: f1(s, t) * dia_trans(s, a, (i / 2) / float(n),
                                          phi_1_m2) * dia_trans(t, a, (j / 2) / float(n), phi_2_m2)
            if i % 2 == 1 and j % 2 == 0:
                print 21
                f = lambda s, t: f1(s, t) * dia_trans(s, a, (i / 2) / float(n),
                                          phi_2_m2) * dia_trans(t, a, (j / 2) / float(n), phi_1_m2)
            if i % 2 == 1 and j % 2 == 1:
                print 22
                f = lambda s, t: f1(s, t) * dia_trans(s, a, (i / 2) / float(n),
                                          phi_2_m2) * dia_trans(t, a, (j / 2) / float(n), phi_2_m2)
                # y=[dia_trans(z,a,(i/2)/float(n),phi_1_m2) for z in m]
                # pyplot.plot(m,y)
                # print y ,"y"
                # pyplot.show()

            # print f
            K[i, j] = quad(f, [(i / 2) / float(n), ((i / 2) + 1) / float(n)],
                           [(j / 2) / float(n), ((j / 2) + 1) / float(n)],method='gauss-legendre')
            print[(i / 2) / float(n), ((i / 2) + 1) / float(n)
         ], [(j / 2) / float(n), ((j / 2) + 1) / float(n)]
            # K[i,j]=i*j

    K_error =matrix(n,n)
    for i in range(0, n):
        for j in range(0, n):
            f_error = lambda s, t: (f1(s, t) - K[2*i, 2*j] * dia_trans(s, a, (2*i / 2) / float(n),
                                              phi_1_m2) * dia_trans(t, a, (2*j / 2) / float(n), phi_1_m2)
                                                - K[2*i, 2*j+1] * dia_trans(s, a, (2*i / 2) / float(n),
                                              phi_1_m2) * dia_trans(t, a, ((2*j+1) / 2) / float(n), phi_2_m2)
                                                - K[2*i+1, 2*j] * dia_trans(s, a, ((2*i+1) / 2) / float(n),
                                              phi_2_m2) * dia_trans(t, a, (2*j / 2) / float(n), phi_1_m2)
                                                - K[2*i+1, 2*j+1] * dia_trans(s, a, ((2*i+1) / 2) / float(n),
                                              phi_2_m2) * dia_trans(t, a, ((2*j+1) / 2) / float(n), phi_2_m2))*\
                                    (f1(s, t) - K[2*i, 2*j] * dia_trans(s, a, (2*i / 2) / float(n),
                                              phi_1_m2) * dia_trans(t, a, (2*j / 2) / float(n), phi_1_m2)
                                                - K[2*i, 2*j+1] * dia_trans(s, a, (2*i / 2) / float(n),
                                              phi_1_m2) * dia_trans(t, a, ((2*j+1) / 2) / float(n), phi_2_m2)
                                                - K[2*i+1, 2*j] * dia_trans(s, a, ((2*i+1) / 2) / float(n),
                                              phi_2_m2) * dia_trans(t, a, (2*j / 2) / float(n), phi_1_m2)
                                                - K[2*i+1, 2*j+1] * dia_trans(s, a, ((2*i+1) / 2) / float(n),
                                              phi_2_m2) * dia_trans(t, a, ((2*j+1) / 2) / float(n), phi_2_m2))


            K_error[i, j] = quad(f_error, [i / float(n), (i + 1) / float(n)],
                           [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            print [i / float(n), (i + 1) / float(n)]
            print [j / float(n), (j + 1) / float(n)]

    return K,K_error
# print project_kernel_m2_phi(4)
# m=linspace(0,1,250)
# i=0
# j=1
# f1 = lambda s, t: s-t
# f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/2)/float(n),phi_1_m2)*dia_trans(t,a,(j/2)/float(n),phi_2_m2)
# n=4
# print [(i/2)/float(n),((i/2)+1)/float(n)],[(j/2)/float(n),((j/2)+1)/float(n)]
# print quad(f,[(i/2)/float(n),((i/2)+1)/float(n)],[(j/2)/float(n),((j/2)+1)/float(n)])
# y=[dia_trans(z,a,(i/2)/float(n),phi_1_m2) for z in m]
# pyplot.plot(m,y)
# print y ,"y"
# pyplot.show()
if __name__ == "__main__":
    K,K_error= project_kernel_m2_phi(4)
    print "k",K
    print "K_error",K_error