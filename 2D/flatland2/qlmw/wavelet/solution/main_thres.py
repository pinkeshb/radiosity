from kernel_m3_phi import *
from mpmath import *
import sys
from wavedecs import *
from save_read import *
def thres_it(K_dwt,top_n):
    # print "K_dwt",K_dwt
    L=[]
    K=[]
    n=K_dwt.cols/3
    K_dwt_thres=matrix(n*3,n*3)
    K=K_dwt.tolist()
    # print "n",n
    for i in range(n*3):
        L.extend(K[i][:])
    for i in range(len(L)):
        L[i]=abs(L[i])
    L.sort()
    L.reverse()
    # print "L",L
    # print top_n
    thresh=L[top_n-1]
    # print "thresh",thresh
    start=L.index(thresh)
    alowed=top_n-start
    # print "start", start 
    for i in range(0,n*3):
        for j in range(0,n*3):
            if abs(K_dwt[i,j])>thresh:
                K_dwt_thres[i,j]=K_dwt[i,j]
            elif abs(K_dwt[i,j])==thresh and alowed>0:
                alowed=alowed-1
                K_dwt_thres[i,j]=K_dwt[i,j]
            else:
                K_dwt_thres[i,j]=0
    # print "K_dwt_thres",K_dwt_thres
    return K_dwt_thres
def main_fn(n, thres_converge,top_n):
    fname=str(n)+'haar_scale'+".txt"
    fo = open(fname, "w")
    print   "inside main"
    K=readit(n,"qlmw_K_mat")
    # K=project_kernel_m3_phi(n)
    # fkname = str(n) + 'qlmw_K_mat_dist_'+str(dist) + ".txt"
    # fk = open(fkname, "r")
    # # fo.write(str(n) + "\n")
    # n=fk.readline()
    # print n
    # n=int(n)
    # print n
    # K = matrix(n*3,n*3)
    # for i in range(n*3):
    #     line=fk.readline()
    #     line = line.split()
    #     for j in range(n*3):
    #         K[i,j]=float(line[j])
            # print float(line[j])
    #     # fo.write("\n")
    # print K
    # fk.close()
    K_dwt=dwt2(K)

    K_dwt_thres=thres_it(K_dwt,top_n)
    E1=matrix([[1.0/pow(n,0.5)]*n*3]).transpose()
    for i in range(n*3):
        if i%3!=0 or i>=3*n/4:
            E1[i]=0
    E2=matrix([[0]*n*3]).transpose()
    E1_dwt=dwt(E1)
    E2_dwt=dwt(E2)
    B1_dwt = zeros(3*n, 1)
    B2_dwt = zeros(3*n, 1)
    B1_pre = zeros(3*n, 1)
    B2_pre = zeros(3*n, 1)

    
    # print "K=", K
    # print "E1=", E1
    # print "E2=", E2    
    # print "K_dwt=", K_dwt
    # print "E1_dwt=", E1_dwt
    # print "E2_dwt=", E2_dwt
    fo.write("n=" + str(n) + "\n")
    fo.write("K=" + str(K) + "\n")
    fo.write("E1=" + str(E1) + "\n")
    fo.write("E2=" + str(E2) + "\n")
    fo.write("K_dwt=" + str(K_dwt) + "\n")
    fo.write("E1_dwt=" + str(E1_dwt) + "\n")
    fo.write("E2_dwt=" + str(E2_dwt) + "\n")
    fo.write("interation begines\n\n")
    B1_pre = B1_dwt + 1
    B2_pre = B2_dwt + 1

    iter = 0
    converged = False

    # print "B1_dwt  " + str(iter) + "=", B1_dwt
    fo.write("B1_dwt  " + str(iter) + "=" + str(B1_dwt) + "\n\n")
    # print "B2_dwt  " + str(iter) + "=", B2_dwt
    fo.write("B2_dwt  " + str(iter) + "=" + str(B2_dwt) + "\n\n")
    # while(not (diag(B1)*B1-diag(B1_pre)*B1_pre == zeros(n,1) or
    # diag(B2)*B2-diag(B2_pre)*B2_pre == zeros(n,1))):
    while (not converged):
        # solve
        iter += 1
        B1_pre = B1_dwt
        B2_pre = B2_dwt
        B1_dwt = E1_dwt + K_dwt_thres * B2_pre
        B2_dwt = E2_dwt + K_dwt_thres * B1_pre

        # print "B1_dwt  " + str(iter) + "=", B1_dwt
        fo.write("B1_dwt  " + str(iter) + "=" + str(B1_dwt) + "\n\n")
        # print "B2_dwt  " + str(iter) + "=", B2_dwt
        fo.write("B2_dwt  " + str(iter) + "=" + str(B2_dwt) + "\n\n")
        # if int(input("Please enter an integer: "))==1:
        #   check=True
        # else:
        #   check=False
        # print diag(B1)*B1-diag(B1_pre)*B1_pre
        # print diag(B2)*B2-diag(B2_pre)*B2_pre
        # print "B1_pre",B1_pre
        # print "B2_pre",B2_pre
        # print B1_dwt
        # print B2_dwt
        change_energy = 0
        for i in range(3*n):
            change_energy = change_energy + \
                (B1_dwt[i] - B1_pre[i]) * (B1_dwt[i] - B1_pre[i]) + \
                (B2_dwt[i] - B2_pre[i]) * (B2_dwt[i] - B2_pre[i])
        if change_energy < thres_converge:
            converged = True
        # print change_energy
    # print "final"
    # print "\n\n\nB1_dwt  " + str(iter) + "=", B1_dwt
    fo.write("\n\n\nB1_dwt  " + str(iter) + "=" + str(B1_dwt))
    # print "\n\n\nB2_dwt  " + str(iter) + "=", B2_dwt
    fo.write("\n\n\nB2_dwt  " + str(iter) + "=" + str(B2_dwt))
    B1=idwt(B1_dwt)
    B2=idwt(B2_dwt)
    # print "\n\n\nB1  " + str(iter) + "=", B1
    fo.write("\n\n\nB1  " + str(iter) + "=" + str(B1))
    # print "\n\n\nB2  " + str(iter) + "=", B2
    fo.write("\n\n\nB2  " + str(iter) + "=" + str(B2))
 
    return B1,B2
if __name__ == "__main__":
    thres = 0.001
    n=64
    print main_fn(n, thres,9*n*n)
