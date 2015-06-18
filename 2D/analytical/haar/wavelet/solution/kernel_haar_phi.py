from mpmath import *
def project_kernel_haar_phi(n):
	# kernel
	f1 = lambda s, t: s*s+t*s
	# basis
	amplitude=pow(n,0.5)
	f2 = lambda s: amplitude
	f3 = lambda s: amplitude
	# integrand
	# f = lambda s,t: f1(s,t)*f2(s)*f3(t)
	f = lambda s,t: f1(s,t)*f3(t)*f2(s)

	K=matrix(n,n)
	for i in range(0,n):
		for j in range(0,n):
			K[i,j]=quad(f,[i/float(n),(i+1)/float(n)],[j/float(n),(j+1)/float(n)])
			print [i/float(n),(i+1)/float(n)],[j/float(n),(j+1)/float(n)]
			# K[i,j]=i*j

	return K

