from mpmath import *
from kernel_haar_phi import *
from wavedecs import *
def K_error(n):
	K_p=project_kernel_haar_phi(n)
	print K_p
	K_dwt=dwt2(K_p)
	print K_dwt
	thres=float(raw_input())
	print "thres" ,thres
	for i in range(n):
		for j in range(n):
			# print abs(K_dwt[i,j]) 
			if abs(K_dwt[i,j])<thres:

				K_dwt[i,j]=0
	print "K_dwt_thres",K_dwt
	K=idwt2(K_dwt)

	print K
	f1 = lambda s, t: s-t
	f=lambda s,t: f1(s,t)*f1(s,t)
	den=quad(f,[0,1],[0,1])



	num=0
	K_error=matrix(n,n)
	for i in range(n):
		for j in range(n):
			f_error=lambda s,t: f1(s,t)-K[i,j]*pow(n,0.5)*pow(n,0.5)
			f=lambda s,t: f_error(s,t)*f_error(s,t)
			K_error[i,j]=quad(f,[i/float(n),(i+1)/float(n)],[j/float(n),(j+1)/float(n)])
			num=num+K_error[i,j]
	# print K_error
	# print K
	return K_dwt,K*pow(n,0.5)*pow(n,0.5),K_error,num,den,thres

if __name__=="__main__":
	n=4
	

	K_dwt,K,K_error,num,den,thres=K_error(n)
	fname=str(n)+'haar_scale_error_thres_'+str(thres)+".txt"
	fo = open(fname, "w")
	print "num=",num
	fo.write("num="+str(num)+"\n")
	fo.write("thres="+str(thres)+"\n")
	print "den=",den
	fo.write("den="+str(den)+"\n")
	print "K_error",K_error
	fo.write("K_error"+str(K_error)+"\n")
	print "K",K
	fo.write("K"+str(K)+"\n")
	print "K_dwt",K_dwt
	fo.write("K_dwt"+str(K_dwt)+"\n")
	print "relative_error=",num/den
	fo.write("relative_error"+str(num/den)+"\n")
	print "relative_error_%=",num/den*100,"  %"
	fo.write("relative_error_%"+str(num/den*100)+" % "+"\n")
