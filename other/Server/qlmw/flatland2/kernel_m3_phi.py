from mpmath import *
from m3_phi import *
from matplotlib import pyplot
def project_kernel_m3_phi(n):
	# kernel
	f1 = lambda s, t: (s+0.1)*(t+0.1)/ (2*pow(((s+0.1)*(s+0.1) +(t+0.1)*(t+0.1)), 1.5))
	# basis
	# amplitude=pow(n,0.5)
	# f2 = lambda s: amplitude
	# f3 = lambda s: amplitude
	# integrand
	# f = lambda s,t: f1(s,t)*f2(s)*f3(t)
	# f = lambda s,t: f1(s,t)*f3(t)*f2(s)
	m=linspace(0,1,250)
	K=matrix(n*3,n*3)
	a=1.0/n
	for i in range(0,n*3):
		for j in range(0,n*3):
			if i%3==0 and j%3==0:
				print 00
				f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_0_m3)*dia_trans(t,a,(j/3)/float(n),phi_0_m3)
			if i%3==0 and j%3==1:
				print 01
				f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_0_m3)*dia_trans(t,a,(j/3)/float(n),phi_1_m3)
			if i%3==0 and j%3==2:
				print 02
				f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_0_m3)*dia_trans(t,a,(j/3)/float(n),phi_2_m3)
			if i%3==1 and j%3==0:
				print 10
				f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_1_m3)*dia_trans(t,a,(j/3)/float(n),phi_0_m3)
			if i%3==1 and j%3==1:
				print 11
				f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_1_m3)*dia_trans(t,a,(j/3)/float(n),phi_1_m3)
			if i%3==1 and j%3==2:
				print 12
				f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_1_m3)*dia_trans(t,a,(j/3)/float(n),phi_2_m3)
			if i%3==2 and j%3==0:
				print 20
				f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_2_m3)*dia_trans(t,a,(j/3)/float(n),phi_0_m3)
			if i%3==2 and j%3==1:
				print 21
				f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_2_m3)*dia_trans(t,a,(j/3)/float(n),phi_1_m3)
			if i%3==2 and j%3==2:
				print 22
				f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/3)/float(n),phi_2_m3)*dia_trans(t,a,(j/3)/float(n),phi_2_m3)
				# y=[dia_trans(z,a,(i/3)/float(n),phi_1_m3) for z in m]
				# pyplot.plot(m,y)
				# # print y ,"y"
				# pyplot.show()

			# print f
			K[i,j]=quad(f,[(i/3)/float(n),((i/3)+1)/float(n)],[(j/3)/float(n),((j/3)+1)/float(n)],method='gauss-legendre')
			print [(i/3)/float(n),((i/3)+1)/float(n)],[(j/3)/float(n),((j/3)+1)/float(n)]
			print K[i,j]
			# if abs(K[i,j])<=0.0000000001:
			# 	K[i,j]=0
			# K[i,j]=i*j

	return K
if __name__=="__main__":
	dist=0.5
	print project_kernel_m3_phi(4,dist)
# m=linspace(0,1,250)
# i=0
# j=1
# f1 = lambda s, t: s-t
# f=lambda s,t: f1(s,t)*dia_trans(s,a,(i/2)/float(n),phi_1_m2)*dia_trans(t,a,(j/2)/float(n),phi_2_m2)
# n=4
# print [(i/2)/float(n),((i/2)+1)/float(n)],[(j/2)/float(n),((j/2)+1)/float(n)]
# print quad(f,[(i/2)/float(n),((i/2)+1)/float(n)],[(j/2)/float(n),((j/2)+1)/float(n)])
# y=[dia_trans(z,a,(i/2)/float(n),phi_1_m2) for z in m]
# pyplot.plot(m,y)
# # print y ,"y"
# pyplot.show()