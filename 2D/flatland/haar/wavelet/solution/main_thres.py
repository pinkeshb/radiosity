from kernel_haar_phi import *
from mpmath import *
import sys
from wavedecs import *

def thres(K_dwt, top_n):
    L = []
    K = []
    n = K_dwt.cols
    K_dwt_thres = matrix(n, n)
    K = K_dwt.tolist()
    print n
    for i in range(n):
        L.extend(K[i][:])
    for i in range(len(L)):
        L[i] = abs(L[i])
    L.sort()
    L.reverse()
    print L
    # print top_n
    thresh = L[top_n - 1]
    print thresh
    start = L.index(thresh)
    alowed = top_n - start
    print start
    for i in range(0, n):
        for j in range(0, n):
            if abs(K_dwt[i, j]) > thresh:
                K_dwt_thres[i, j] = K_dwt[i, j]
            elif abs(K_dwt[i, j]) == thresh and alowed > 0:
                alowed = alowed - 1
                K_dwt_thres[i, j] = K_dwt[i, j]
            else:
                K_dwt_thres[i, j] = 0
    return K_dwt_thres
def main_fn(n,thres_converge,top_n):
    fname=str(n)+'haar_wavelet'+".txt"
    fo = open(fname, "w")


    K=project_kernel_haar_phi(n)
    K_dwt=dwt2(K)
    K_dwt_thres = thres(K_dwt, top_n)
    E1 = matrix([[0] * n]).transpose()
    E1[3 * n / 4:n] = ones(n / 4, 1) / pow(n, 0.5)
    E2 = matrix([[0] * n])
    E1_dwt=dwt(E1)
    E2_dwt=dwt(E2)
    B1_dwt = zeros(n, 1)
    B2_dwt = zeros(n, 1)
    B1_pre_dwt = zeros(n, 1)
    B2_pre_dwt = zeros(n, 1)


    print "K=", K
    print "E1=", E1
    print "E2=", E2
    print "K_dwt=", K_dwt
    print "K_dwt_thres=", K_dwt_thres
    print "E1_dwt=", E1_dwt
    print "E2_dwt=", E2_dwt
    fo.write("n="+str(n)+"\n")
    fo.write("K="+str(K)+"\n")
    fo.write("E1="+str(E1)+"\n")
    fo.write("E2="+str(E2)+"\n")
    fo.write("K_dwt="+str(K_dwt)+"\n")
    fo.write("K_dwt_thres="+str(K_dwt_thres)+"\n")
    fo.write("E1_dwt="+str(E1_dwt)+"\n")
    fo.write("E2_dwt="+str(E2_dwt)+"\n")
    fo.write("interation begines\n\n")
    B1_dwt_pre = B1_dwt + 1
    B2_dwt_pre = B2_dwt + 1
    iter = 0
    converged=False

    print "B1_dwt" + str(iter) + "=", B1_dwt
    fo.write("B1_dwt" + str(iter) + "=" + str(B1_dwt) + "\n")
    print "B2_dwt" + str(iter) + "=", B2_dwt
    fo.write("B2_dwt" + str(iter) + "=" + str(B2_dwt) + "\n")

    while (not converged):
            # solve
            iter += 1
            B1_dwt_pre = B1_dwt
            B2_dwt_pre = B2_dwt
            B1_dwt = E1_dwt + K_dwt_thres  * B2_dwt_pre
            B2_dwt = E2_dwt  + K_dwt_thres  * B1_dwt_pre
            print "B1_dwt  " + str(iter) + "=", B1_dwt
            fo.write("B1_dwt  " + str(iter) + "=" + str(B1_dwt) + "\n\n")
            print "B2_dwt  " + str(iter) + "=", B2_dwt
            fo.write("B2_dwt  " + str(iter) + "=" + str(B2_dwt) + "\n\n")
            # if int(input("Please enter an integer: "))!=1:
            #  converged=True

            change_energy = 0
            for i in range(n):
               change_energy = change_energy + \
                   (B1_dwt[i] - B1_dwt_pre[i]) * (B1_dwt[i] - B1_dwt_pre[i]) + \
                   (B2_dwt[i] - B2_dwt_pre[i]) * (B2_dwt[i] - B2_dwt_pre[i])
            print change_energy
            if change_energy < thres_converge:
                converged = True

    print "final"
    print "\n\n\nB1_dwt_final"+"=", B1_dwt
    fo.write("\n\n\nB1_dwt_final"+"="+str(B1_dwt))
    print "\n\n\nB2_dwt_final"+"=", B2_dwt
    fo.write("\n\n\nB2_dwt_final"+"="+str(B2_dwt))
    B1=idwt(B1_dwt)
    B2=idwt(B2_dwt)
    print "\n\n\nB1_final"+"=", B1
    fo.write("\n\n\nB1_final"+"="+str(B1))
    print "\n\n\nB2_final"+"=", B2
    fo.write("\n\n\nB2_final"+"="+str(B2))
    B1_proj=B1*pow(n,0.5)
    B2_proj=B2*pow(n,0.5)
    print "\n\n\nB1_proj"+"=", B1_proj
    fo.write("\n\n\nB1_proj"+"="+str(B1_proj))
    print "\n\n\nB2_proj"+"=", B2_proj
    fo.write("\n\n\nB2_proj"+"="+str(B2_proj))
    return B1_proj, B2_proj

if __name__ == "__main__":
    top_n = 16
    thres_converge = 0.001
    main_fn(4, thres_converge, top_n)



