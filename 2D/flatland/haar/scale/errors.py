from mpmath import *
from kernel_haar_phi import *
def K_error(n):
	K=project_kernel_haar_phi(n)
	f1 = lambda s, t: 1/pow(((s-t)*(s-t)+1),1.5)
	f=lambda s,t: f1(s,t)*f1(s,t)
	den=quad(f1,[0,1],[0,1])


	num=0
	K_error=matrix(n,n)
	for i in range(n):
		for j in range(n):
			f_error=lambda s,t: f1(s,t)-K[i,j]*pow(n,0.5)*pow(n,0.5)
			f=lambda s,t: f_error(s,t)*f_error(s,t)
			K_error[i,j]=quad(f,[i/float(n),(i+1)/float(n)],[j/float(n),(j+1)/float(n)])
			num=num+K_error[i,j]
	return K_error,num,den
if __name__=="__main__":
	n=16
	
	fname=str(n)+'haar_scale_error'+".txt"
	fo = open(fname, "w")
	K_error,num,den=K_error(n)
	print "num=",num
	fo.write("num="+str(num)+"\n")
	print "den=",den
	fo.write("den="+str(den)+"\n")
	print "K_error",K_error
	fo.write("K_error"+str(K_error)+"\n")
	print "relative_error=",num/den
	fo.write("relative_error"+str(num/den)+"\n")
	print "relative_error_%=",num/den*100,"  %"
	fo.write("relative_error_%"+str(num/den*100)+" % "+"\n")
