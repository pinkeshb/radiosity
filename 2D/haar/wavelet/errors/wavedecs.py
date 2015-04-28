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
		# print i
	return matrix(Result)

def dwt2(K):
	K_dwt=copy.deepcopy(K)
	K_dwt_i=copy.deepcopy(K)
	for i in range(K.cols):
		K_dwt_i[:,i]=dwt(K[:,i])
	for i in range(K.rows):
		K_dwt[i,:]=dwt(K_dwt_i[i,:]).transpose()
	return K_dwt
def idwt2(K):
	K_dwt=copy.deepcopy(K)
	K_dwt_i=copy.deepcopy(K)
	for i in range(K.rows):
		print i
		K_dwt_i[i,:]=idwt(K[i,:].transpose()).transpose()
	for i in range(K.cols):
		K_dwt[:,i]=idwt(K_dwt_i[:,i])

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
	K=matrix(
		[
		[1,1,1,1],
		[1,0,1,1],
		[1,1,0,1],
		[1,1,1,0]
		])
	# print K
	# print dwt2(K)
	# print matrix([[1,1,1,1]])
	# print K[0,:]
	print idwt2(dwt2(K))
	# print idwt(matrix([[1,1,1,1]]).transpose())