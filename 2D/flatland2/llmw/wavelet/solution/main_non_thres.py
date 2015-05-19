from kernel_m2_phi import *
from mpmath import *
import sys
from wavedecs import *

def main_fn(n, thres_converge):
    fname=str(n)+'haar_scale'+".txt"
    fo = open(fname, "w")

    K=project_kernel_m2_phi(n)
    K_dwt=dwt2(K)

    E1=matrix([[1.0/pow(n,0.5)]*n*2]).transpose()
    for i in range(n*2):
        if i%2==1 or i<3*n/2:
            E1[i]=0
    E2=matrix([[0]*n*2]).transpose()
    E1_dwt=dwt(E1)
    E2_dwt=dwt(E2)
    B1_dwt = zeros(2*n, 1)
    B2_dwt = zeros(2*n, 1)
    B1_pre = zeros(2*n, 1)
    B2_pre = zeros(2*n, 1)

    
    print "K=", K
    print "E1=", E1
    print "E2=", E2    
    print "K_dwt=", K_dwt
    print "E1_dwt=", E1_dwt
    print "E2_dwt=", E2_dwt
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

    print "B1_dwt  " + str(iter) + "=", B1_dwt
    fo.write("B1_dwt  " + str(iter) + "=" + str(B1_dwt) + "\n\n")
    print "B2_dwt  " + str(iter) + "=", B2_dwt
    fo.write("B2_dwt  " + str(iter) + "=" + str(B2_dwt) + "\n\n")
    # while(not (diag(B1)*B1-diag(B1_pre)*B1_pre == zeros(n,1) or
    # diag(B2)*B2-diag(B2_pre)*B2_pre == zeros(n,1))):
    while (not converged):
        # solve
        iter += 1
        B1_pre = B1_dwt
        B2_pre = B2_dwt
        B1_dwt = E1_dwt + K_dwt * B2_pre
        B2_dwt = E2_dwt + K_dwt * B1_pre

        print "B1_dwt  " + str(iter) + "=", B1_dwt
        fo.write("B1_dwt  " + str(iter) + "=" + str(B1_dwt) + "\n\n")
        print "B2_dwt  " + str(iter) + "=", B2_dwt
        fo.write("B2_dwt  " + str(iter) + "=" + str(B2_dwt) + "\n\n")
        # if int(input("Please enter an integer: "))==1:
        #   check=True
        # else:
        #   check=False
        # print diag(B1)*B1-diag(B1_pre)*B1_pre
        # print diag(B2)*B2-diag(B2_pre)*B2_pre
        print "B1_pre",B1_pre
        print "B2_pre",B2_pre
        print B1_dwt
        print B2_dwt
        change_energy = 0
        for i in range(2*n):
            change_energy = change_energy + \
                (B1_dwt[i] - B1_pre[i]) * (B1_dwt[i] - B1_pre[i]) + \
                (B2_dwt[i] - B2_pre[i]) * (B2_dwt[i] - B2_pre[i])
        if change_energy < thres_converge:
            converged = True
        print change_energy
    print "final"
    print "\n\n\nB1_dwt  " + str(iter) + "=", B1_dwt
    fo.write("\n\n\nB1_dwt  " + str(iter) + "=" + str(B1_dwt))
    print "\n\n\nB2_dwt  " + str(iter) + "=", B2_dwt
    fo.write("\n\n\nB2_dwt  " + str(iter) + "=" + str(B2_dwt))
    B1=idwt(B1_dwt)
    B2=idwt(B2_dwt)
    print "\n\n\nB1  " + str(iter) + "=", B1
    fo.write("\n\n\nB1  " + str(iter) + "=" + str(B1))
    print "\n\n\nB2  " + str(iter) + "=", B2
    fo.write("\n\n\nB2  " + str(iter) + "=" + str(B2))
 
    return B1,B2
if __name__ == "__main__":
    thres = 0.001
    print main_fn(4, thres)
