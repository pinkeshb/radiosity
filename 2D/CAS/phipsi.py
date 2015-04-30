import math
from matplotlib import pyplot
from mpmath import *
def phi_CAS(x,m):
	if 0<=x<1:
		return cos(2*math.pi*m*x)+sin(2*math.pi*m*x)
	else:
		return 0.0
# def phi_2_m2(x):
# 	# print x
# 	if 0<=x<1:
# 		# print "in range"

# 		return (2*float(x)-1)*1.732050808
# 	else:
# 		return 0.0
def dia_trans(x,a,s,f,m):
	# print x
	# if f == phi_2_m2:
	# 	# return f((x-s)/float(a))
	# 	# print "hi"
	# 	return f((x-s)/float(a))/pow(a,0.5)
	return f((x-s)/float(a),m)/pow(a,0.5)

# print dia_trans(0.49,0.25,0.25,phi_2_m2)
# print pow(1.732050808,math.log(2,2))
if __name__=="__main__":
	x=linspace(0,1,250)
	m=-1
	f=lambda s: dia_trans(s,0.25,0,phi_CAS,m)
	print quad(f,[0,0.25])
	y=[f(z) for z in x]

	pyplot.plot(x,y)
	pyplot.show()