from kernel_haar_wavelet import *
from mpmath import *
import time
import datetime
import sys
from wavedecs import *


n=16
iter_thres=0.01

ts=time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


# f1 = lambda s: 12.0/13.0*s+6.0/13.0
f1 = lambda s:8.0/9.0*s*s*s*s+32.0/45.0
f=lambda s: f1(s)*f1(s)
den=quad(f,[0,1])
K=project_kernel_wavelet(n)
E=dwt(matrix([[1.0/pow(n,0.5)]*n]).transpose())
B=zeros(n,1)
G=zeros(n,1)
print "K",K
thres=float(raw_input())
print "thres" ,thres
fname=str(n)+'haar_wavelet_error_iter_thres_'+str(iter_thres)+"_K_thres_"+str(thres)+".txt"
fo=open(fname, "w")
for i in range(n):
	for j in range(n):
		# print abs(K_dwt[i,j]) 
		if abs(K[i,j])<thres:

			K[i,j]=0

print "K_thres="
print  K
print "E=", E
fo.write("n="+str(n)+"\n")
fo.write("K="+str(K)+"\n")
fo.write("E="+str(E)+"\n")
B_pre=B+1
error=0
for i in range(n):
	error=error+(B[i]-B_pre[i])*(B[i]-B_pre[i])

iter = 1
while(error>iter_thres):
	print "B"+str(iter)+"=", B
	fo.write("B"+str(iter)+"="+str(B)+"\n")
	B_pre=B
	B=E+K*B_pre

	# if int(input("Please enter an integer: "))==1:
	# 	check=True
	# else:
	# 	check=False
	error=0
	for i in range(n):
		error=error+(B[i]-B_pre[i])*(B[i]-B_pre[i])
	iter+=1
print "\n\n\nB"+str(iter)+"=", B
fo.write("\n\n\nB"+str(iter)+"="+str(B))
B=idwt(B)
print "\n\n\nB_phi"+str(iter)+"=", B
fo.write("\n\n\nB_phi"+str(iter)+"="+str(B*pow(n,0.5)))
B_error=zeros(n,1)
num =0
for m in range(n):
	b_error=lambda s: f1(s)-B[m]*pow(n,0.5)
	b=lambda s: b_error(s)*b_error(s)
	B_error[m]=quad(b,[m/float(n),(m+1)/float(n)])
	num=num+B_error[m]
print "thres",thres
fo.write("thres="+str(thres)+"\n")



print "num=",num
fo.write("num="+str(num)+"\n")
fo.write("thres="+str(thres)+"\n")
print "den=",den
fo.write("den="+str(den)+"\n")
# print "K_error",K_error
# fo.write("K_error"+str(K_error)+"\n")
# print "K",K
# fo.write("K"+str(K)+"\n")
# print "K_dwt",K_dwt
# fo.write("K_dwt"+str(K_dwt)+"\n")
print "relative_error=",num/den
fo.write("relative_error"+str(num/den)+"\n")
print "relative_error_%=",num/den*100,"  %"
fo.write("relative_error_%"+str(num/den*100)+" % "+"\n")
