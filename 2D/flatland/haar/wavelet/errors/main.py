from kernel_haar_phi import *
from mpmath import *
import sys
from wavedecs import *
def K_Error(K,n):
	f1 = lambda s, t: 1/ (2*pow(((s - t) * (s - t) + 1), 1.5))
	# f = lambda s, t: f1(s, t) * pow(n, 0.5) * pow(n, 0.5)
	print K,"fasdfasdfsdf"
	K_error = matrix(n, n)
	for i in range(0, n):
		for j in range(0, n):
			f_error = lambda s, t: (f1(s, t) - K[i, j] * pow(n, 0.5) * pow(n, 0.5))*(f1(s, t) - K[i, j] * pow(n, 0.5) * pow(n, 0.5))
			K_error[i, j] = quad(f_error, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)])

	return K_error
def B_Error(B_proj,n):
	b = lambda s:12.0/13.0*s+6.0/13.0
	print n
	B_error=zeros(n,1)
	for i in range(n):
		print i,"afdjahdf"
		b_error=lambda s:(b(s)-B_proj[i])*(b(s)-B_proj[i])
		B_error[i]=quad(b_error,[i / float(n), (i + 1) / float(n)])

		print i,"afdjahdf"
	return B_error
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

	B_error=B_Error(B_proj,n)
	K_thres=idwt2(K_dwt_thres)
	K_thres_error=K_Error(K_thres,n)
	print "\n\n\nB_error" + "=", B_error
	fo.write("\n\n\nB_error" + "=" + str(B_error))
	print "K_thres=", K_thres
	fo.write("\n\n\nK_thres" + "=" + str(K_thres))
	print "\n\n\nK_thres_error" + "=", K_thres_error
	fo.write("\n\n\nK_thres_error" + "=" + str(K_thres_error))	
	print "\n\n\nB_error"+"=", B_error
	fo.write("\n\n\nB_error"+"="+str(B_error))
	return B_proj,B_error,K_thres,K_thres_error
if __name__ == "__main__":
	top_n=10
	thres_converge=0.001
	main_fn(4,thres_converge,top_n)
	# print thres(project_kernel_haar_phi(4),12)
	# print matrix(5,5)
