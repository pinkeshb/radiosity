def phi_haar(x):
	if 0<=x<1:
		return 1.0
	else:
		return 0.0
def dia_trans(x,a,s,f):
	return f((x-s)/float(a))/pow(a,0.5)