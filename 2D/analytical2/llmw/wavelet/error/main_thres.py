from kernel_m2_phi import *
from mpmath import *
import sys
from wavedecs import *
def K_Error(K,n):
    f1 = lambda s, t: s*s*s*s - t*t*t
    K_error =matrix(n,n)

    a=1.0/n
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
    return K_error
def thres_it(K_dwt,top_n):
    print "K_dwt",K_dwt
    L=[]
    K=[]
    n=K_dwt.cols/2
    K_dwt_thres=matrix(n*2,n*2)
    K=K_dwt.tolist()
    print "n",n
    for i in range(n*2):
        L.extend(K[i][:])
    for i in range(len(L)):
        L[i]=abs(L[i])
    L.sort()
    L.reverse()
    print "L",L
    # print top_n
    thresh=L[top_n-1]
    print "thresh",thresh
    start=L.index(thresh)
    alowed=top_n-start
    print "start", start 
    for i in range(0,n*2):
        for j in range(0,n*2):
            if abs(K_dwt[i,j])>thresh:
                K_dwt_thres[i,j]=K_dwt[i,j]
            elif abs(K_dwt[i,j])==thresh and alowed>0:
                alowed=alowed-1
                K_dwt_thres[i,j]=K_dwt[i,j]
            else:
                K_dwt_thres[i,j]=0
    print "K_dwt_thres",K_dwt_thres
    return K_dwt_thres
def B_Error(B,n):
    b = lambda s:8.0/9.0*s*s*s*s+32.0/45.0
    print n
    B_error=zeros(n,1)
    a=1.0/n
    for i in range(n):
        print i,"afdjahdf"
        b_error=lambda s:(b(s)-B[2*i]*dia_trans(s, a, i  / float(n), phi_1_m2)-B[2*i+1]*dia_trans(s, a, i  / float(n), phi_2_m2))*\
                        (b(s)-B[2*i]*dia_trans(s, a, i/ float(n), phi_1_m2)-B[2*i+1]*dia_trans(s, a, i/ float(n), phi_2_m2))
        B_error[i]=quad(b_error,[i / float(n), (i + 1) / float(n)],method='gauss-legendre')
        print B_error[i]

        print i,"afdjahdf"
    return B_error
def main_fn(n, thres_converge,top_n):
    fname=str(n)+'haar_sscale'+".txt"
    fo = open(fname, "w")

    K=project_kernel_m2_phi(n)
    K_dwt=dwt2(K)
    K_dwt_thres=thres_it(K_dwt,top_n)
    K_thres=idwt2(K_dwt_thres)

    E=matrix([[1.0/pow(n,0.5)]*n*2]).transpose()
    for i in range(n*2):
        if i%2==1:
            E[i]=0
    E_dwt=dwt(E)
    B=zeros(2*n,1)
    B_dwt=zeros(2*n,1)
    B_pre=B+0.1

    print "K=", K
    print "K_dwt=", K_dwt
    # for i in range(n*2):
    #   for j in range(n*2):
    #       if abs(K_dwt[i,j])<0.05:
    # #             K_dwt[i,j]=0
    # print "K_dwt="
    # print  K_dwt
    print "E=", E
    print "E_dwt=", E_dwt
    fo.write("n="+str(n)+"\n")
    fo.write("K="+str(K)+"\n")
    fo.write("K_dwt="+str(K_dwt)+"\n")
    fo.write("E="+str(E)+"\n")

    iter = 0
    converged = False

    print "B_dwt  " + str(iter) + "=", B_dwt
    fo.write("B_dwt  " + str(iter) + "=" + str(B_dwt) + "\n\n")


    while(not converged):
        iter+=1
        B_pre=B_dwt
        B_dwt=E_dwt+K_dwt*B_pre

        # if int(input("Please enter an integer: "))==1:
        #   check=True
        # else:
        #   check=False
        # print "B_pre"+str(iter)+"=", B_pre
        print "B_dwt"+str(iter)+"=", B_dwt
        fo.write("B_dwt  " + str(iter) + "=" + str(B_dwt) + "\n\n")
        # print "error"
        # print diag(B_dwt)*B_dwt-diag(B_pre)*B_pre
        # print "error"
        change_energy = 0
        for i in range(2*n):
          change_energy = change_energy + \
              (B_dwt[i] - B_pre[i]) * (B_dwt[i] - B_pre[i])
        if change_energy < thres_converge:
          converged = True
    print "final solution"
    print "\n\n\nB"+str(iter)+"=", B_dwt
    fo.write("\n\n\nB"+str(iter)+"="+str(B_dwt))
    B=idwt(B_dwt)
    print "\n\n\nB"+str(iter)+"=", B
    fo.write("\n\n\nB"+str(iter)+"="+str(B))
    K_error=K_Error(K_thres,n)
    B_error=B_Error(B,n)
    fo.write("\n\n\nB_error"+str(iter)+"="+str(B_error))
    return B,B_error,K,K_error
if __name__ == "__main__":
    thres = 0.001
    print main_fn(4, thres,64)
