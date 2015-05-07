from kernel_m2_phi import *
from mpmath import *
import sys
from wavedecs import *
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
def main_fn(n, thres_converge,top_n):
    fname=str(n)+'haar_sscale'+".txt"
    fo = open(fname, "w")

    K=project_kernel_m2_phi(n)
 
    K_dwt=dwt2(K)
    K_dwt_thres=thres_it(K_dwt,top_n)
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
    return B
if __name__ == "__main__":
    thres = 0.001
    print main_fn(4, thres,4)
