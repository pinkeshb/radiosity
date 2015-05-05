from kernel_m2_phi import *
from mpmath import *
import sys

def main_fn(n, thres):
    fname=str(n)+'haar_scale'+".txt"
    fo = open(fname, "w")

    K=project_kernel_m2_phi(n)
    E1=matrix([[1.0/pow(n,0.5)]*n*2]).transpose()
    for i in range(n*2):
        if i%2==1 or i<3*n/2:
            E1[i]=0
    E2=matrix([[0]*n*2]).transpose()
    B1 = zeros(2*n, 1)
    B2 = zeros(2*n, 1)
    B1_pre = zeros(2*n, 1)
    B2_pre = zeros(2*n, 1)

    
    print "K=", K
    print "E1=", E1
    print "E2=", E2
    fo.write("n=" + str(n) + "\n")
    fo.write("K=" + str(K) + "\n")
    fo.write("E1=" + str(E1) + "\n")
    fo.write("E2=" + str(E2) + "\n")
    fo.write("interation begines\n\n")
    B1_pre = B1 + 1
    B2_pre = B2 + 1

    iter = 0
    converged = False

    print "B1  " + str(iter) + "=", B1
    fo.write("B1  " + str(iter) + "=" + str(B1) + "\n\n")
    print "B2  " + str(iter) + "=", B2
    fo.write("B2  " + str(iter) + "=" + str(B2) + "\n\n")
    # while(not (diag(B1)*B1-diag(B1_pre)*B1_pre == zeros(n,1) or
    # diag(B2)*B2-diag(B2_pre)*B2_pre == zeros(n,1))):
    while (not converged):
        # solve
        iter += 1
        B1_pre = B1
        B2_pre = B2
        B1 = E1 + K * B2_pre
        B2 = E2 + K * B1_pre

        print "B1  " + str(iter) + "=", B1
        fo.write("B1  " + str(iter) + "=" + str(B1) + "\n\n")
        print "B2  " + str(iter) + "=", B2
        fo.write("B2  " + str(iter) + "=" + str(B2) + "\n\n")
        # if int(input("Please enter an integer: "))==1:
        #   check=True
        # else:
        #   check=False
        # print diag(B1)*B1-diag(B1_pre)*B1_pre
        # print diag(B2)*B2-diag(B2_pre)*B2_pre
        print "B1_pre",B1_pre
        print "B2_pre",B2_pre
        print B1
        print B2
        change_energy = 0
        for i in range(2*n):
            change_energy = change_energy + \
                (B1[i] - B1_pre[i]) * (B1[i] - B1_pre[i]) + \
                (B2[i] - B2_pre[i]) * (B2[i] - B2_pre[i])
        if change_energy < thres:
            converged = True
        print change_energy
    print "final"
    print "\n\n\nB1  " + str(iter) + "=", B1 * pow(n, 0.5)
    fo.write("\n\n\nB1  " + str(iter) + "=" + str(B1 * pow(n, 0.5)))
    print "\n\n\nB2  " + str(iter) + "=", B2 * pow(n, 0.5)
    fo.write("\n\n\nB2  " + str(iter) + "=" + str(B2 * pow(n, 0.5)))
 
    return B1,B2
if __name__ == "__main__":
    thres = 0.001
    print main_fn(4, thres)
