from mpmath import *
from phipsi import *
from matplotlib import pyplot
def project_kernel_CAS(n):
	# kernel
	f1 = lambda s, t: s-t
	# basis
	# amplitude=pow(n,0.5)
	# f2 = lambda s: amplitude
	# f3 = lambda s: amplitude
	# integrand
	# f = lambda s,t: f1(s,t)*f2(s)*f3(t)
	# f = lambda s,t: f1(s,t)*f3(t)*f2(s)
	# m=linspace(0,1,250)
	K=matrix(n*3,n*3)
	for i in range(0,n*3):
		for j in range(0,n*3):
			if i%3==0 and j%3==0:
				mi=i%3-1
				mj=j%3-1
				print mi,mj
				f=lambda s,t: f1(s,t)*dia_trans(s,0.25,(i/3)/float(n),phi_CAS,mi)*dia_trans(t,0.25,(j/3)/float(n),phi_CAS,mj)
			if i%3==0 and j%3==1:
				mi=i%3-1
				mj=j%3-1
				print mi,mj
				f=lambda s,t: f1(s,t)*dia_trans(s,0.25,(i/3)/float(n),phi_CAS,mi)*dia_trans(t,0.25,(j/3)/float(n),phi_CAS,mj)
			if i%3==0 and j%3==2:
				mi=i%3-1
				mj=j%3-1
				print mi,mj
				f=lambda s,t: f1(s,t)*dia_trans(s,0.25,(i/3)/float(n),phi_CAS,mi)*dia_trans(t,0.25,(j/3)/float(n),phi_CAS,mj)
			if i%3==1 and j%3==0:
				mi=i%3-1
				mj=j%3-1
				print mi,mj
				f=lambda s,t: f1(s,t)*dia_trans(s,0.25,(i/3)/float(n),phi_CAS,mi)*dia_trans(t,0.25,(j/3)/float(n),phi_CAS,mj)
			if i%3==1 and j%3==1:
				mi=i%3-1
				mj=j%3-1
				print mi,mj
				f=lambda s,t: f1(s,t)*dia_trans(s,0.25,(i/3)/float(n),phi_CAS,mi)*dia_trans(t,0.25,(j/3)/float(n),phi_CAS,mj)
			if i%3==1 and j%3==2:
				mi=i%3-1
				mj=j%3-1
				print mi,mj
				f=lambda s,t: f1(s,t)*dia_trans(s,0.25,(i/3)/float(n),phi_CAS,mi)*dia_trans(t,0.25,(j/3)/float(n),phi_CAS,mj)
			if i%3==2 and j%3==0:
				mi=i%3-1
				mj=j%3-1
				print mi,mj
				f=lambda s,t: f1(s,t)*dia_trans(s,0.25,(i/3)/float(n),phi_CAS,mi)*dia_trans(t,0.25,(j/3)/float(n),phi_CAS,mj)
			if i%3==2 and j%3==1:
				mi=i%3-1
				mj=j%3-1
				print mi,mj
				f=lambda s,t: f1(s,t)*dia_trans(s,0.25,(i/3)/float(n),phi_CAS,mi)*dia_trans(t,0.25,(j/3)/float(n),phi_CAS,mj)
			if i%3==2 and j%3==2:
				mi=i%3-1
				mj=j%3-1
				print mi,mj
				f=lambda s,t: f1(s,t)*dia_trans(s,0.25,(i/3)/float(n),phi_CAS,mi)*dia_trans(t,0.25,(j/3)/float(n),phi_CAS,mj)
				# y=[dia_trans(z,0.25,(i/3)/float(n),phi_1_m3) for z in m]
				# pyplot.plot(m,y)
				# # print y ,"y"
				# pyplot.show()

			# print f
			K[i,j]=quad(f,[(i/3)/float(n),((i/3)+1)/float(n)],[(j/3)/float(n),((j/3)+1)/float(n)])
			print [(i/3)/float(n),((i/3)+1)/float(n)],[(j/3)/float(n),((j/3)+1)/float(n)]
			# K[i,j]=i*j

	return K

print project_kernel_CAS(4)
# m=linspace(0,1,250)
# i=0
# j=1
# f1 = lambda s, t: s-t
# f=lambda s,t: f1(s,t)*dia_trans(s,0.25,(i/3)/float(n),phi_1_m3)*dia_trans(t,0.25,(j/3)/float(n),phi_2_m3)
# n=4
# print [(i/3)/float(n),((i/3)+1)/float(n)],[(j/3)/float(n),((j/3)+1)/float(n)]
# print quad(f,[(i/3)/float(n),((i/3)+1)/float(n)],[(j/3)/float(n),((j/3)+1)/float(n)])
# y=[dia_trans(z,0.25,(i/3)/float(n),phi_1_m3) for z in m]
# pyplot.plot(m,y)
# # print y ,"y"
# pyplot.show()