from kernel_haar_phi import *
from mpmath import *
import sys
from wavedecs import *


def main_fn(n,thres_converge):
	fname=str(n)+'haar_wavelet'+".txt"
	fo = open(fname, "w")


	K=project_kernel_haar_phi(n)
	K_dwt=dwt2(K)
	E=matrix([[1.0/pow(n,0.5)]*n])
	E_dwt=dwt(E).transpose())
	B_dwt=zeros(n,1)
	B_pre=ones(n,1)

	print "K=", K
	print "E=", E
	print "K_dwt=", K_dwt
	print "E_dwt=", E_dwt
	fo.write("n="+str(n)+"\n")
	fo.write("K="+str(K)+"\n")
	fo.write("E="+str(E)+"\n")
	fo.write("K_dwt="+str(K_dwt)+"\n")
	fo.write("E_dwt="+str(E_dwt)+"\n")
	fo.write("interation begines\n\n")

	iter = 0
	converged=False

	print "B_dwt" + str(iter) + "=", B_dwt
	fo.write("B_dwt" + str(iter) + "=" + str(B_dwt) + "\n")
	while(not converged):
	    # solve
	    iter += 1
	    B_pre = B_dwt
	    B_dwt = E_dwt + K_dwt * B_pre

		
	    print "B_dwt" + str(iter) + "=", B_dwt
	    fo.write("B_dwt" + str(iter) + "=" + str(B_dwt) + "\n")

	    change_energy=0
	    for i in range(n):
	    	change_energy=change_energy+(B_dwt[i]-B_pre[i])*(B_dwt[i]-B_pre[i])
	    if change_energy<thres:
	    	converged=True

	print "\n\n\nB_dwt_final"+"=", B_dwt
	fo.write("\n\n\nB_dwt_final"+"="+str(B_dwt))
	B=idwt(B_dwt)
	print "\n\n\nB_final"+"=", B
	fo.write("\n\n\nB_final"+"="+str(B))
	B_proj=B*pow(n,0.5)
	print "\n\n\nB_proj"+"=", B_proj
	fo.write("\n\n\nB_proj"+"="+str(B_proj))


if __name__ == "__main__":
	thres=0.001
	main_fn(4)