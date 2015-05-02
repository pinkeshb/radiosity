from kernel_haar_phi import *
from mpmath import *
import sys
from wavedecs import *

def thres(K_dwt,top_n):
	L=[]
	K=[]
	n=K_dwt.cols
	K_dwt_thres=matrix(n,n)
	K=K_dwt.tolist()
	print n
	for i in range(n):
		L.extend(K[i][:])
	for i in range(len(L)):
		L[i]=abs(L[i])
	L.sort()
	L.reverse()
	print L
	# print top_n
	thresh=L[top_n-1]
	print thresh
	start=L.index(thresh)
	alowed=top_n-start
	print start 
	for i in range(0,n):
		for j in range(0,n):
			if abs(K_dwt[i,j])>thresh:
				K_dwt_thres[i,j]=K_dwt[i,j]
			elif abs(K_dwt[i,j])==thresh and alowed>0:
				alowed=alowed-1
				K_dwt_thres[i,j]=K_dwt[i,j]
			else:
				K_dwt_thres[i,j]=0
	return K_dwt_thres
def main_fn(n,thres_converge,top_n):
	fname=str(n)+'haar_wavelet'+".txt"
	fo = open(fname, "w")


	K=project_kernel_haar_phi(n)
	K_dwt=dwt2(K)
	K_dwt_thres=thres(K_dwt,top_n)
	E=matrix([[1.0/pow(n,0.5)]*n])
	E_dwt=dwt(E)
	B_dwt=zeros(n,1)
	B_pre=ones(n,1)

	print "K=", K
	print "E=", E
	print "K_dwt=", K_dwt
	print "K_dwt_thres=", K_dwt_thres
	print "E_dwt=", E_dwt
	fo.write("n="+str(n)+"\n")
	fo.write("K="+str(K)+"\n")
	fo.write("E="+str(E)+"\n")
	fo.write("K_dwt="+str(K_dwt)+"\n")
	fo.write("K_dwt_thres="+str(K_dwt_thres)+"\n")
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
	    B_dwt = E_dwt + K_dwt_thres * B_pre

		
	    print "B_dwt" + str(iter) + "=", B_dwt
	    fo.write("B_dwt" + str(iter) + "=" + str(B_dwt) + "\n")

	    change_energy=0
	    for i in range(n):
	    	change_energy=change_energy+(B_dwt[i]-B_pre[i])*(B_dwt[i]-B_pre[i])
	    if change_energy<thres_converge:
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
	top_n=10
	thres_converge=0.001
	main_fn(4,thres_converge,top_n)
	# print thres(project_kernel_haar_phi(4),12)
	# print matrix(5,5)
