import math
from matplotlib import pyplot
from mpmath import *

root3=1.732050808
def phi_1_m2(x):
	if 0<=x<1:
		return 1.0
	else:
		return 0.0
def phi_2_m2(x):
	# print x
	if 0<=x<1:
		# print "in range"

		return (2*float(x)-1)*root3
	else:
		return 0.0
def dia_trans(x,a,s,f):
	# print x
	if f == phi_2_m2:
		# return f((x-s)/float(a))
		# print "hi"
		return f((x-s)/float(a))/pow(a,0.5)
	return f((x-s)/float(a))/pow(a,0.5)
# print dia_trans(0.49,0.25,0.25,phi_2_m2)
# print pow(1.732050808,math.log(2,2))
def psi_1_m2(x):
	if 0<=x<0.5:
		return -root3*(4*x-1)
	elif 0.5<=x<1:
		return root3*(4*x-3)
	else:
		return 0
def psi_2_m2(x):
	if 0<=x<0.5:
		return (6*x-1)
	elif 0.5<=x<1:
		return (6*x-5)
	else:
		return 0
if __name__=="__main__":
	m=linspace(0,1,250)

	f=lambda s: dia_trans(s,1,0,phi_1_m2)*dia_trans(s,1,0,phi_2_m2)
	print quad(f,[0,1])
	y=[f(z) for z in m]

	pyplot.plot(m,y)
	pyplot.show()

	# print y