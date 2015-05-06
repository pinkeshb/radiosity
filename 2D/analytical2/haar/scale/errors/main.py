from kernel_haar_phi import *
from mpmath import *
import sys


def main_fn(n,thres):
    fname = str(n) + 'haar_scale' + ".txt"
    fo = open(fname, "w")

    # b = lambda s:12.0/13.0*s+6.0/13.0
    b = lambda s:8.0/9.0*s*s*s*s+32.0/45.0
    K,K_error = project_kernel_haar_phi(n)
    E = matrix([[1.0 / pow(n, 0.5)] * n]).transpose()
    B = zeros(n, 1)
    G = zeros(n, 1)
    B_error=zeros(n,1)
    B_pre=ones(n,1)

    print "K=", K
    print "E=", E
    fo.write("n=" + str(n) + "\n")
    fo.write("K=" + str(K) + "\n")
    fo.write("E=" + str(E) + "\n\n")
    fo.write("interation begines\n\n")

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
    print "\n\n\nB_proj" + "=", B_proj
    fo.write("\n\n\nnB_proj" + "=" + str(B_proj))
    for i in range(n):
        b_error=lambda s:(b(s)-B_proj[i])*(b(s)-B_proj[i])
        B_error[i]=quad(b_error,[i / float(n), (i + 1) / float(n)])
    print "\n\n\nB_error" + "=", B_error
    fo.write("\n\n\nB_error" + "=" + str(B_error))
    print "\n\n\nK_error" + "=", K_error
    fo.write("\n\n\nK_error" + "=" + str(K_error))
    return B_proj,B_error,K,K_error

if __name__ == "__main__":
	thres=0.001
	print main_fn(8,thres)
