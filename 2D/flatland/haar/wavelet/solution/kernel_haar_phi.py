from mpmath import *
def project_kernel_haar_phi(n,dist):
	# kernel
	# dist=0.125
	f1 = lambda s, t:	dist*dist/ (2*pow(((s - t) * (s - t) + dist*dist), 1.5))
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
			K[i,j]=quad(f,[i/float(n),(i+1)/float(n)],[j/float(n),(j+1)/float(n)],method='gauss-legendre')
			print [i/float(n),(i+1)/float(n)],[j/float(n),(j+1)/float(n)]
			# K[i,j]=i*j

	return K
# print project_kernel_haar_phi(8)

