import pywt
from mpmath import *
import copy
import math
root3=pow(3,0.5)
root2=pow(2,0.5)
root8=root2*2
def dwt_inside(E):
	# print E
	length=len(E)
	E_dwt=[0]*length
	for i in range(length/4):
		# print i,"i"
		E_dwt[2*i]=(2*E[4*i]+2*E[4*i+2])/root8
		E_dwt[2*i+1]=(-root3*E[4*i]+E[4*i+1]+root3*E[4*i+2]+E[4*i+3])/root8
	for i in range(length/4):
		E_dwt[2*i+length/2]=(-2*E[4*i+1]+2*E[4*i+3])/root8
		E_dwt[2*i+1+length/2]=(E[4*i]+root3*E[4*i+1]-E[4*i+2]+root3*E[4*i+3])/root8


	# print E_dwt
	return matrix(E_dwt)
def dwt(E):
	length=len(E)
	E_dwt=copy.deepcopy(E)
	E_dwt=dwt_inside(E)
	if length>4:
		for i in range(2,int(math.log(length,2))):
			E_dwt[0:length-pow(2,i)]=dwt_inside(E_dwt[0:length-pow(2,i)])
	return E_dwt

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
def idwt_inside(E):
	# print E
	# print type(E)
	# print type(E)

	length=len(E)
	E_idwt=[0]*length
	# print type(E[2*0])
	for i in range(length/4):
		# print i ,"i"
		# print E[2*i],E[2*i+1],E[length/2+2*i],E[length/2+2*i+1]
		E_idwt[4*i]=E[2*i]/root2-E[2*i+1]*root3/root8+E[length/2+2*i]*0+E[length/2+2*i+1]/root8
		E_idwt[4*i+1]=E[2*i]*0+E[2*i+1]/root8-E[length/2+2*i]/root2+E[length/2+2*i+1]*root3/root8
		E_idwt[4*i+2]=E[2*i]/root2+E[2*i+1]*root3/root8+E[length/2+2*i]*0-E[length/2+2*i+1]/root8
		E_idwt[4*i+3]=E[2*i]*0+E[2*i+1]/root8+E[length/2+2*i]/root2+E[length/2+2*i+1]*root3/root8

	# print E_idwt
	return matrix(E_idwt)
def idwt(E):
	length=len(E)
	E_idwt=copy.deepcopy(E)
	# E_dwt=dwt_inside(E)
	# if length>4:
	# 	for i in range(2,int(math.log(length,2))):
	# 		E_dwt[0:length-pow(2,i)]=dwt_inside(E_dwt[0:length-pow(2,i)])
	for i in range(2,int(math.log(length,2))+1):
		E_idwt[0:pow(2,i)]=idwt_inside(E_idwt[0:pow(2,i)])


	return E_idwt
if __name__=="__main__":
# 	K=matrix([
# [1,0,1,0],[0,0,0,0],[1,0,1,0],[0,0,0,0]
# 		])
	E=matrix([[1,1,1,1,1,1,1,0]])
	# E=matrix([ 0.288461538460848,0.0333086693845357, 0.403846153845187,0.0333086693845357, 0.519230769229526,0.0333086693845357, 0.634615384613866, 0.0333086693845357])
	print E,"\n"
	print dwt_inside(E),"\n"
	print idwt_inside(dwt_inside(E)),"\n"
	# print E[0]

