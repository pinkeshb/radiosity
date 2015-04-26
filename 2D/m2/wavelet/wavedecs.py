import pywt
from mpmath import *
import copy
root3=1.732050808
def dwt(E):
	# print E
	length=len(E)
	E_dwt=[0]*length
	for i in range(length/4):
		print i,"i"
		E_dwt[2*i]=2*E[4*i]+2*E[4*i+2]
		E_dwt[2*i+1]=-root3*E[4*i]+E[4*i+1]+root3*E[4*i+2]+E[4*i+3]
	for i in range(length/4):
		E_dwt[2*i+length/4]=-2*E[4*i]+2*E[4*i+2]
		E_dwt[2*i+1]=E[4*i]+root3*E[4*i+1]-E[4*i+2]+root3*E[4*i+3]

	# print E_dwt
	return matrix(E_dwt)

def dwt2(K):
	K_dwt=copy.deepcopy(K)
	K_dwt_i=copy.deepcopy(K)
	for i in range(K.cols):
		K_dwt_i[:,i]=dwt(K[:,i])
	for i in range(K.rows):
		K_dwt[i,:]=dwt(K_dwt_i[i,:]).transpose()
	return K_dwt

def idwt(E):
	# print E
	E_rep=E.tolist()[0:2]
	for i in range(1,int(pow(len(E),0.5))):
		E_rep.append(E[pow(2,i):pow(2,i+1)])
	E_idwt=pywt.waverec(E_rep,'db1')
	# print E_idwt
	return matrix(E_idwt)
if __name__=="__main__":
	K=matrix([
[1,0,1,0],[0,0,0,0],[1,0,1,0],[0,0,0,0]
		])
	# print E
	print dwt2(K)
	# print E[0]

