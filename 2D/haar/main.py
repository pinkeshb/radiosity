from kernel_haar_phi import *
from mpmath import *
import time
import datetime
import sys


n=4
ts=time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
fname=str(n)+'haar_scale'+".txt"
fo = open(fname, "w")


K=project_kernel_haar_phi(n)
E=matrix([[1.0/pow(n,0.5)]*n]).transpose()
B=zeros(n,1)
G=zeros(n,1)


print "K="
print  K
print "E=", E
fo.write("n="+str(n)+"\n")
fo.write("K="+str(K)+"\n")
fo.write("E="+str(E)+"\n")



iter = 200
while(iter>=0):
	print "B=", B
	fo.write("B="+str(B)+"\n")
	G=K*B
	B=E+G

	# if int(input("Please enter an integer: "))==1:
	# 	check=True
	# else:
	# 	check=False
	iter-=1
print "B=", B*pow(n,0.5)
fo.write("B="+str(B*pow(n,0.5)))
