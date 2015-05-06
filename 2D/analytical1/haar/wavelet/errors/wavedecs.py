import pywt
from mpmath import *
import copy
import math
root8=pow(8,0.5)
root2=pow(2,0.5)
# def dwt(E):
# 	# print E
# 	E_dwt=pywt.wavedec(E,'db1')
# 	# print E_dwt
# 	Result=[]
# 	# print E_dwt
# 	# print 

# 	for i in range((int(ceil(pow(len(E),0.5)))+1)):
# 		Result.extend(E_dwt[i])
# 		# print E_dwt[i]
# 		# print i
# 	return matrix(Result)
def dwt(E):
	length=len(E)
	E_dwt=copy.deepcopy(E)
	E_dwt=dwt_inside(E)
	if length>2:
		for i in range(1,int(math.log(length,2))):
			print i,"before inside"
			E_dwt[0:length/pow(2,i)]=dwt_inside(E_dwt[0:length/pow(2,i)])
	return E_dwt
def dwt_inside(E):
	print "inside",E,"inside"
	length=len(E)
	E_dwt=[0]*length
	for i in range(length/2):
		# print i,"i"
		E_dwt[i]=(E[2*i]+E[2*i+1])/root2
	for i in range(length/2):
		E_dwt[i+length/2]=(E[2*i]-E[2*i+1])/root2

	return matrix(E_dwt)

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

# def idwt(E):
# 	# print E
# 	E_rep=E.tolist()[0:2]
# 	for i in range(1,int(pow(len(E),0.5))):
# 		E_rep.append(E[pow(2,i):pow(2,i+1)])
# 	E_idwt=pywt.waverec(E_rep,'db1')
# 	# print E_idwt
# 	return matrix(E_idwt)
def idwt_inside(E):
	# print E
	# print type(E)
	# print type(E)

	length=len(E)
	E_idwt=[0]*length
	# print type(E[2*0])
	for i in range(length/2):
		# print i ,"i"
		# print E[2*i],E[2*i+1],E[length/2+2*i],E[length/2+2*i+1]
		E_idwt[2*i]=(E[i]+E[length/2+i])/root2
		E_idwt[2*i+1]=(E[i]-E[length/2+i])/root2
		if E_idwt[2*i+1]<0.000000000001:
			E_idwt[2*i+1]=0
		# m,n=E[i],E[length/2+i]
		# print m-n
		# print m,n


	# print E_idwt
	return matrix(E_idwt)
def idwt(E):
	length=len(E)
	E_idwt=copy.deepcopy(E)
	# E_dwt=dwt_inside(E)
	# if length>4:
	# 	for i in range(2,int(math.log(length,2))):
	# 		E_dwt[0:length-pow(2,i)]=dwt_inside(E_dwt[0:length-pow(2,i)])
	for i in range(1,int(math.log(length,2))+1):
		E_idwt[0:pow(2,i)]=idwt_inside(E_idwt[0:pow(2,i)])
		print i,E_idwt[0:pow(2,i)], i


	return E_idwt
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
	e=matrix([[1,1,1,1,1,1,1,0]])
	print e
	print dwt(e)
	print idwt(dwt(e))
	# print dwt_inside(e)
	# print idwt_inside(dwt_inside(e))
	# print K[0,:]
	# print idwt2(dwt2(K))
	# print idwt(matrix([[1,1,1,1]]).transpose())