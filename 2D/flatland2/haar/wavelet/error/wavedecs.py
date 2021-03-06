import pywt
from mpmath import *
import copy

def dwt(E):
	# print E
	E_dwt=pywt.wavedec(E,'db1')
	# print E_dwt
	Result=[]
	for i in range(int(pow(len(E),0.5))+1):
		Result.extend(E_dwt[i])
		print i
	return matrix(Result)

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