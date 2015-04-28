from kernel_haar_wavelet import *
from mpmath import *
import time
import datetime
import sys
from wavedecs import *


n=4


ts=time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
fname=str(n)+'haar_wavelet'+".txt"
fo = open(fname, "w")


K=project_kernel_wavelet(n)
E=dwt(matrix([[1.0/pow(n,0.5)]*n]).transpose())
B=zeros(n,1)
G=zeros(n,1)


print "K="
print  K
print "E=", E
fo.write("n="+str(n)+"\n")
fo.write("K="+str(K)+"\n")
fo.write("E="+str(E)+"\n")
B_pre=B+1


iter = 1
while(not diag(B)*B-diag(B_pre)*B_pre == zeros(n,1)):
	print "B"+str(iter)+"=", B
	fo.write("B"+str(iter)+"="+str(B)+"\n")
	B_pre=B
	B=E+K*B_pre

	# if int(input("Please enter an integer: "))==1:
	# 	check=True
	# else:
	# 	check=False
	iter+=1
print "\n\n\nB"+str(iter)+"=", B
fo.write("\n\n\nB"+str(iter)+"="+str(B))

print "\n\n\nB_phi"+str(iter)+"=", idwt(B)*pow(n,0.5)
fo.write("\n\n\nB_phi"+str(iter)+"="+str(idwt(B)*pow(n,0.5)))
