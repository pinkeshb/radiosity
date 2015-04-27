from kernel_m2_phi import *
from mpmath import *
import time
import datetime
import sys
from wavedecs import *


n=4


ts=time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
fname=str(n)+'haar_sscale'+".txt"
fo = open(fname, "w")


K=project_kernel_m2_phi(n)
K_dwt=dwt2(K)

E=matrix([[1.0/pow(n,0.5)]*n*2]).transpose()
for i in range(n*2):
	if i%2==1:
		E[i]=0
E_dwt=dwt(E)
B=zeros(2*n,1)
B_dwt=zeros(2*n,1)
G=zeros(2*n,1)


print "K="
print  K
print "K_dwt="
print  K_dwt
for i in range(n*2):
	for j in range(n*2):
		if abs(K_dwt[i,j])<0.05:
			K_dwt[i,j]=0
print "K_dwt="
print  K_dwt
print "E=", E
print len(E)
print len(E_dwt)
print "E_dwt=", E_dwt,"fin"
fo.write("n="+str(n)+"\n")
fo.write("K="+str(K)+"\n")
fo.write("E="+str(E)+"\n")
B_pre=B+0.1
B_pre

iter = 1
while(not diag(B_dwt)*B_dwt-diag(B_pre)*B_pre == zeros(2*n,1)):
	print "B_dwt"+str(iter)+"=", B_dwt
	fo.write("B"+str(iter)+"="+str(B)+"\n")
	B_pre=B_dwt
	B_dwt=E_dwt+K_dwt*B_pre

	# if int(input("Please enter an integer: "))==1:
	# 	check=True
	# else:
	# 	check=False
	print "B_pre"+str(iter)+"=", B_pre
	print "B_dwt"+str(iter)+"=", B_dwt
	print "error"
	print diag(B_dwt)*B_dwt-diag(B_pre)*B_pre
	print "error"
	iter+=1
print "final solution"
print "\n\n\nB"+str(iter)+"=", B_dwt
fo.write("\n\n\nB"+str(iter)+"="+str(B_dwt))
print "\n\n\nB"+str(iter)+"=", idwt(B_dwt)
fo.write("\n\n\nB"+str(iter)+"="+str(idwt(B_dwt)))

