from kernel_haar_phi import *
from mpmath import *
import sys


def main_fn(n,thres):
    fname = str(n) + 'haar_scale' + ".txt"
    fo = open(fname, "w")

    K = project_kernel_haar_phi(n)
    E = matrix([[1.0 / pow(n, 0.5)] * n]).transpose()
    B = zeros(n, 1)
    G = zeros(n, 1)

    print "K=", K
    print "E=", E
    fo.write("n=" + str(n) + "\n")
    fo.write("K=" + str(K) + "\n")
    fo.write("E=" + str(E) + "\n\n")
    fo.write("interation begines\n\n")

    B_pre = B + 1
    iter = 0
    converged=False

    print "B" + str(iter) + "=", B
    fo.write("B" + str(iter) + "=" + str(B) + "\n")

    while(not converged):
        # solve
        iter += 1
        B_pre = B
        B = E + K * B_pre

   	
        print "B" + str(iter) + "=", B
        fo.write("B" + str(iter) + "=" + str(B) + "\n")

        change_energy=0
        for i in range(n):
        	change_energy=change_energy+(B[i]-B_pre[i])*(B[i]-B_pre[i])
        if change_energy<thres:
        	converged=True
    B_proj=B * pow(n, 0.5)
    print "\n\n\nB" + str(iter) + "=", B_proj
    fo.write("\n\n\nB" + str(iter) + "=" + str(B_proj))
    return B,K

if __name__ == "__main__":
	thres=0.001
	print main_fn(4,thres)
