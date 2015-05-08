from kernel_m3_phi import *
from mpmath import *
import sys
from wavedecs import *
def B_Error(B,n):
    b = lambda s:8.0/9.0*s*s*s*s+32.0/45.0
    print n
    B_error=zeros(n,1)
    a=1.0/n
    for i in range(n):
        print i,"afdjahdf"
        b_error=lambda s:(b(s)-B[3*i]*dia_trans(s, a, i  / float(n), phi_0_m3)-B[3*i+1]*dia_trans(s, a, i  / float(n), phi_1_m3)-B[3*i+2]*dia_trans(s, a, i  / float(n), phi_2_m3) )*\
                        (b(s)-B[3*i]*dia_trans(s, a, i  / float(n), phi_0_m3)-B[3*i+1]*dia_trans(s, a, i  / float(n), phi_1_m3)-B[3*i+2]*dia_trans(s, a, i  / float(n), phi_2_m3))
        B_error[i]=quad(b_error,[i / float(n), (i + 1) / float(n)])
        print B_error[i]

        print i,"afdjahdf"
    return B_error
def K_Error(K,n):
    f1 = lambda s, t: s*s*s*s - t*t*t
    K_error =matrix(n,n)

    a=1.0/n
    for i in range(0, n):
        for j in range(0, n):
            f_error = lambda s, t: (f1(s, t) - K[3*i, 3*j] * dia_trans(s, a, (i) / float(n),
                                              phi_0_m3) * dia_trans(t, a, (j) / float(n), phi_0_m3)
                                                - K[3*i, 3*j+1] * dia_trans(s, a, (i) / float(n),
                                              phi_0_m3) * dia_trans(t, a, (j) / float(n), phi_1_m3)
                                                - K[3*i, 3*j+2] * dia_trans(s, a, (i) / float(n),
                                              phi_0_m3) * dia_trans(t, a, (j) / float(n), phi_2_m3)
                                                - K[3*i+1, 3*j+0] * dia_trans(s, a, (i) / float(n),
                                              phi_1_m3) * dia_trans(t, a, (j) / float(n), phi_0_m3)
                                                - K[3*i+1, 3*j+1] * dia_trans(s, a, (i) / float(n),
                                              phi_1_m3) * dia_trans(t, a, (j) / float(n), phi_1_m3)
                                                - K[3*i+1, 3*j+2] * dia_trans(s, a, (i) / float(n),
                                              phi_1_m3) * dia_trans(t, a, (j) / float(n), phi_2_m3)
                                                - K[3*i+2, 3*j] * dia_trans(s, a, (i) / float(n),
                                              phi_2_m3) * dia_trans(t, a, (j) / float(n), phi_0_m3)
                                                - K[3*i+2, 3*j+1] * dia_trans(s, a, (i) / float(n),
                                              phi_2_m3) * dia_trans(t, a, (j) / float(n), phi_1_m3)
                                                - K[3*i+2, 3*j+2] * dia_trans(s, a, (i) / float(n),
                                              phi_2_m3) * dia_trans(t, a, (j) / float(n), phi_2_m3))*\
                                    (f1(s, t) - K[3*i, 3*j] * dia_trans(s, a, (i) / float(n),
                                              phi_0_m3) * dia_trans(t, a, (j) / float(n), phi_0_m3)
                                                - K[3*i, 3*j+1] * dia_trans(s, a, (i) / float(n),
                                              phi_0_m3) * dia_trans(t, a, (j) / float(n), phi_1_m3)
                                                - K[3*i, 3*j+2] * dia_trans(s, a, (i) / float(n),
                                              phi_0_m3) * dia_trans(t, a, (j) / float(n), phi_2_m3)
                                                - K[3*i+1, 3*j+0] * dia_trans(s, a, (i) / float(n),
                                              phi_1_m3) * dia_trans(t, a, (j) / float(n), phi_0_m3)
                                                - K[3*i+1, 3*j+1] * dia_trans(s, a, (i) / float(n),
                                              phi_1_m3) * dia_trans(t, a, (j) / float(n), phi_1_m3)
                                                - K[3*i+1, 3*j+2] * dia_trans(s, a, (i) / float(n),
                                              phi_1_m3) * dia_trans(t, a, (j) / float(n), phi_2_m3)
                                                - K[3*i+2, 3*j] * dia_trans(s, a, (i) / float(n),
                                              phi_2_m3) * dia_trans(t, a, (j) / float(n), phi_0_m3)
                                                - K[3*i+2, 3*j+1] * dia_trans(s, a, (i) / float(n),
                                              phi_2_m3) * dia_trans(t, a, (j) / float(n), phi_1_m3)
                                                - K[3*i+2, 3*j+2] * dia_trans(s, a, (i) / float(n),
                                              phi_2_m3) * dia_trans(t, a, (j) / float(n), phi_2_m3))

            K_error[i, j] = quad(f_error, [i / float(n), (i + 1) / float(n)],
                           [j / float(n), (j + 1) / float(n)])
            print [i / float(n), (i + 1) / float(n)]
            print [j / float(n), (j + 1) / float(n)]
    print "K_error",K_error
    return K_error
def thres_it(K_dwt,top_n):
    print "K_dwt",K_dwt
    L=[]
    K=[]
    n=K_dwt.cols/3
    K_dwt_thres=matrix(n*3,n*3)
    K=K_dwt.tolist()
    print "n",n
    for i in range(n*3):
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
    for i in range(0,n*3):
        for j in range(0,n*3):
            if abs(K_dwt[i,j])>thresh:
                K_dwt_thres[i,j]=K_dwt[i,j]
            elif abs(K_dwt[i,j])==thresh and alowed>0:
                alowed=alowed-1
                K_dwt_thres[i,j]=K_dwt[i,j]
            else:
                K_dwt_thres[i,j]=0
    print "K_dwt_thres",K_dwt_thres
    return K_dwt_thres
def main_fn(n, thres_converge,top_n):
    fname=str(n)+'haar_scale'+".txt"
    fo = open(fname, "w")
    # K=ones(3*n,3*n)
    K=project_kernel_m3_phi(n)
 
    K_dwt=dwt2(K)
    K_dwt_thres=thres_it(K_dwt,top_n)
    K_thres=idwt2(K_dwt_thres)
    E=matrix([[1.0/pow(n,0.5)]*n*3])
    for i in range(n*3):
        if i%3!=0:
            E[i]=0
    E_dwt=dwt(E).transpose()
    B=zeros(3*n,1)
    B_dwt=zeros(3*n,1)
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
        B_dwt=E_dwt+K_dwt_thres*B_pre

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
        for i in range(3*n):
          change_energy = change_energy + \
              (B_dwt[i] - B_pre[i]) * (B_dwt[i] - B_pre[i])
        if change_energy < thres_converge:
          converged = True
    print "final solution"
    print "\n\n\nB"+str(iter)+"=", B_dwt
    fo.write("\n\n\nB"+str(iter)+"="+str(B_dwt))
    B=idwt(B_dwt.transpose())
    print "\n\n\nB"+str(iter)+"=", B
    fo.write("\n\n\nB"+str(iter)+"="+str(B))
    K_error=K_Error(K_thres,n)
    B_error=B_Error(B,n)
    return B,B_error,K,K_error
if __name__ == "__main__":
    thres = 0.001
    print main_fn(4, thres,4*4*9)
