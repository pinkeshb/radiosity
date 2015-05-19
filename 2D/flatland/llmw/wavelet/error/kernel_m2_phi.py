from mpmath import *
from m2_phi import *
from matplotlib import pyplot
from wavedecs import *
def thres_it(K_dwt,top_n):
    print "K_dwt\n\n",K_dwt
    L=[]
    K=[]
    n=K_dwt.cols/2
    K_dwt_thres=matrix(n*2,n*2)
    K=K_dwt.tolist()
    print "n\n\n",n
    for i in range(n*2):
        L.extend(K[i][:])
    for i in range(len(L)):
        L[i]=abs(L[i])
    L.sort()
    L.reverse()
    print "L\n\n",L
    # print top_n
    thresh=L[top_n-1]
    print "thresh\n\n",thresh
    start=L.index(thresh)
    alowed=top_n-start
    print "start\n\n", start 
    for i in range(0,n*2):
        for j in range(0,n*2):
            if abs(K_dwt[i,j])>thresh:
                K_dwt_thres[i,j]=K_dwt[i,j]
            elif abs(K_dwt[i,j])==thresh and alowed>0:
                alowed=alowed-1
                K_dwt_thres[i,j]=K_dwt[i,j]
            else:
                K_dwt_thres[i,j]=0
    print "K_dwt_thres\n\n",K_dwt_thres
    return K_dwt_thres
def project_kernel_m2_phi(n,top_n,dist):
    # kernel
    # dist=1
    f1 = lambda s, t: dist*dist/ (2*pow(((s - t) * (s - t) + dist*dist), 1.5))
    # f1 = lambda s, t:1
    # basis
    # amplitude=pow(n,0.5)
    # f2 = lambda s: amplitude
    # f3 = lambda s: amplitude
    # integrand
    # f = lambda s,t: f1(s,t)*f2(s)*f3(t)
    # f = lambda s,t: f1(s,t)*f3(t)*f2(s)
    m=linspace(0,1,250)
    K=matrix(n*2,n*2)
    a=1.0/n
    for i in range(0,n*2):
        for j in range(0,n*2):
            if i%2==0 and j%2==0:
                print 11
                f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/2)/float(n),phi_1_m2)*dia_trans(t,a,(j/2)/float(n),phi_1_m2)
            if i%2==0 and j%2==1:
                print 12
                f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/2)/float(n),phi_1_m2)*dia_trans(t,a,(j/2)/float(n),phi_2_m2)
            if i%2==1 and j%2==0:
                print 21
                f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/2)/float(n),phi_2_m2)*dia_trans(t,a,(j/2)/float(n),phi_1_m2)
            if i%2==1 and j%2==1:
                print 22
                f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/2)/float(n),phi_2_m2)*dia_trans(t,a,(j/2)/float(n),phi_2_m2)
                # y=[dia_trans(z,a,(i/2)/float(n),phi_1_m2) for z in m]
                # pyplot.plot(m,y)
                # # print y ,"y"
                # pyplot.show()

            # print f
            K[i,j]=quad(f,[(i/2)/float(n),((i/2)+1)/float(n)],[(j/2)/float(n),((j/2)+1)/float(n)],method='gauss-legendre')
            print [(i/2)/float(n),((i/2)+1)/float(n)],[(j/2)/float(n),((j/2)+1)/float(n)]
            # K[i,j]=i*j
    K_dwt=dwt2(K)

    K_dwt_thres=thres_it(K_dwt,top_n)
    K_thres=idwt2(K_dwt_thres)
    K_thres_error =matrix(n,n)
    for i in range(0, n):
        for j in range(0, n):
            f_error = lambda s, t: (f1(s, t) - K_thres[2*i, 2*j] * dia_trans(s, a, (2*i / 2) / float(n),
                                              phi_1_m2) * dia_trans(t, a, (2*j / 2) / float(n), phi_1_m2)
                                                - K_thres[2*i, 2*j+1] * dia_trans(s, a, (2*i / 2) / float(n),
                                              phi_1_m2) * dia_trans(t, a, ((2*j+1) / 2) / float(n), phi_2_m2)
                                                - K_thres[2*i+1, 2*j] * dia_trans(s, a, ((2*i+1) / 2) / float(n),
                                              phi_2_m2) * dia_trans(t, a, (2*j / 2) / float(n), phi_1_m2)
                                                - K_thres[2*i+1, 2*j+1] * dia_trans(s, a, ((2*i+1) / 2) / float(n),
                                              phi_2_m2) * dia_trans(t, a, ((2*j+1) / 2) / float(n), phi_2_m2))*\
                                    (f1(s, t) - K_thres[2*i, 2*j] * dia_trans(s, a, (2*i / 2) / float(n),
                                              phi_1_m2) * dia_trans(t, a, (2*j / 2) / float(n), phi_1_m2)
                                                - K_thres[2*i, 2*j+1] * dia_trans(s, a, (2*i / 2) / float(n),
                                              phi_1_m2) * dia_trans(t, a, ((2*j+1) / 2) / float(n), phi_2_m2)
                                                - K_thres[2*i+1, 2*j] * dia_trans(s, a, ((2*i+1) / 2) / float(n),
                                              phi_2_m2) * dia_trans(t, a, (2*j / 2) / float(n), phi_1_m2)
                                                - K_thres[2*i+1, 2*j+1] * dia_trans(s, a, ((2*i+1) / 2) / float(n),
                                              phi_2_m2) * dia_trans(t, a, ((2*j+1) / 2) / float(n), phi_2_m2))


            K_thres_error[i, j] = quad(f_error, [i / float(n), (i + 1) / float(n)],
                           [j / float(n), (j + 1) / float(n)],method='gauss-legendre')


    return K,K_dwt,K_dwt_thres,K_thres,K_thres_error
if __name__=="__main__":
    n=4
    K,K_dwt,K_dwt_thres,K_thres,K_thres_error= project_kernel_m2_phi(n,n*n*4)
    print "1\n\n",K
    print "2\n\n",K_dwt
    print "3\n\n",K_dwt_thres
    print "4\n\n",K_thres
    print "5\n\n",K_thres_error
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
    # # print y ,"y"
    # pyplot.show("\n\n",)