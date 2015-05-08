import pywt
from mpmath import *
import copy
import math
from matplotlib import pyplot

A=matrix([
[1/sqrt(2),0,0,1/sqrt(2),0,0],
[-sqrt(3)/sqrt(8),1/sqrt(8),0,sqrt(3)/sqrt(8),1/sqrt(8),0],
[0,-sqrt(5)*sqrt(3)/(4*sqrt(2)),1/(4*sqrt(2)),0,sqrt(5)*sqrt(3)/(4*sqrt(2)),1/(4*sqrt(2))],
[1/(3*sqrt(2)),1/sqrt(6),-sqrt(5)/3/sqrt(2),-1/(3*sqrt(2)),+1/sqrt(6),sqrt(5)/3/sqrt(2)],
[0,1/(4*sqrt(2)),sqrt(3)*sqrt(5)/(4*sqrt(2)),0,-1/(4*sqrt(2)),sqrt(3)*sqrt(5)/(4*sqrt(2))],
[-sqrt(5)/6/sqrt(2),-sqrt(5)/2/sqrt(6),-2/(3*sqrt(2)),sqrt(5)/6/sqrt(2),-sqrt(5)/2/sqrt(6),2/(3*sqrt(2))]])

def dwt_inside(E):
    # print E
    length=len(E)
    E_dwt=[0]*length
    for i in range(length/6):
        # print i,"i"
        E_dwt[3*i]=    A[0,0]*E[6*i+0]+\
                    A[0,1]*E[6*i+1]+\
                    A[0,2]*E[6*i+2]+\
                    A[0,3]*E[6*i+3]+\
                    A[0,4]*E[6*i+4]+\
                    A[0,5]*E[6*i+5]
        E_dwt[3*i+1]=    A[1,0]*E[6*i+0]+\
                        A[1,1]*E[6*i+1]+\
                        A[1,2]*E[6*i+2]+\
                        A[1,3]*E[6*i+3]+\
                        A[1,4]*E[6*i+4]+\
                        A[1,5]*E[6*i+5]
        E_dwt[3*i+2]=    A[2,0]*E[6*i+0]+\
                           A[2,1]*E[6*i+1]+\
                        A[2,2]*E[6*i+2]+\
                        A[2,3]*E[6*i+3]+\
                        A[2,4]*E[6*i+4]+\
                        A[2,5]*E[6*i+5]
    for i in range(length/6):
        E_dwt[3*i+length/2]=        A[3,0]*E[6*i+0]+\
                                    A[3,1]*E[6*i+1]+\
                                    A[3,2]*E[6*i+2]+\
                                    A[3,3]*E[6*i+3]+\
                                    A[3,4]*E[6*i+4]+\
                                    A[3,5]*E[6*i+5]
        E_dwt[3*i+1+length/2]=       A[4,0]*E[6*i+0]+\
                                    A[4,1]*E[6*i+1]+\
                                    A[4,2]*E[6*i+2]+\
                                    A[4,3]*E[6*i+3]+\
                                    A[4,4]*E[6*i+4]+\
                                    A[4,5]*E[6*i+5]
        E_dwt[3*i+2+length/2]=       A[5,0]*E[6*i+0]+\
                                    A[5,1]*E[6*i+1]+\
                                    A[5,2]*E[6*i+2]+\
                                    A[5,3]*E[6*i+3]+\
                                    A[5,4]*E[6*i+4]+\
                                    A[5,5]*E[6*i+5]

    # print E_dwt
    return matrix(E_dwt)
def dwt(E):
    length=len(E)
    E_dwt=copy.deepcopy(E)
    for i in range(0,1+int(math.log(length/6,2))):
        # print i
        # print dwt_inside(E_dwt[0:length/pow(2,i)])
        # print E_dwt[0:length/pow(2,i)]
        E_dwt[0:length/pow(2,i)]=dwt_inside(E_dwt[0:length/pow(2,i)]).transpose()
    return E_dwt

def dwt2(K):
    K_dwt=copy.deepcopy(K)
    K_dwt_i=copy.deepcopy(K)
    for i in range(K.cols):
        K_dwt_i[:,i]=dwt(K[:,i].transpose()).transpose()
    for i in range(K.rows):
        K_dwt[i,:]=dwt(K_dwt_i[i,:])
    return K_dwt

def idwt_inside(E):
    # print E
    # print type(E)
    # print type(E)

    length=len(E)
    E_idwt=[0]*length
    # print type(E[2*0])
    for i in range(length/6):
        # print i ,"i"
        # print E[2*i],E[2*i+1],E[length/2+2*i],E[length/2+2*i+1]
        E_idwt[6*i+0]=         A[0,0]*E[3*i+0]+\
                            A[1,0]*E[3*i+1]+\
                            A[2,0]*E[3*i+2]+\
                            A[3,0]*E[length/2+3*i+0]+\
                            A[4,0]*E[length/2+3*i+1]+\
                            A[5,0]*E[length/2+3*i+2]
        E_idwt[6*i+1]=        A[0,1]*E[3*i+0]+\
                            A[1,1]*E[3*i+1]+\
                            A[2,1]*E[3*i+2]+\
                            A[3,1]*E[length/2+3*i+0]+\
                            A[4,1]*E[length/2+3*i+1]+\
                            A[5,1]*E[length/2+3*i+2]
        E_idwt[6*i+2]=        A[0,2]*E[3*i+0]+\
                            A[1,2]*E[3*i+1]+\
                            A[2,2]*E[3*i+2]+\
                            A[3,2]*E[length/2+3*i+0]+\
                            A[4,2]*E[length/2+3*i+1]+\
                            A[5,2]*E[length/2+3*i+2]
        E_idwt[6*i+3]=        A[0,3]*E[3*i+0]+\
                            A[1,3]*E[3*i+1]+\
                            A[2,3]*E[3*i+2]+\
                            A[3,3]*E[length/2+3*i+0]+\
                            A[4,3]*E[length/2+3*i+1]+\
                            A[5,3]*E[length/2+3*i+2]

        E_idwt[6*i+4]=        A[0,4]*E[3*i+0]+\
                            A[1,4]*E[3*i+1]+\
                            A[2,4]*E[3*i+2]+\
                            A[3,4]*E[length/2+3*i+0]+\
                            A[4,4]*E[length/2+3*i+1]+\
                            A[5,4]*E[length/2+3*i+2]

        E_idwt[6*i+5]=        A[0,5]*E[3*i+0]+\
                            A[1,5]*E[3*i+1]+\
                            A[2,5]*E[3*i+2]+\
                            A[3,5]*E[length/2+3*i+0]+\
                            A[4,5]*E[length/2+3*i+1]+\
                            A[5,5]*E[length/2+3*i+2]

    # print E_idwt
    return matrix(E_idwt)
def idwt(E):
    length=len(E)
    E_idwt=copy.deepcopy(E)
    # E_dwt=dwt_inside(E)
    # if length>4:
    #     for i in range(2,int(math.log(length,2))):
    #         E_dwt[0:length-pow(2,i)]=dwt_inside(E_dwt[0:length-pow(2,i)])
    for i in range(0,int(math.log(length/6,2))+1):
        E_idwt[0:pow(2,i)*6]=idwt_inside(E_idwt[0:pow(2,i)*6]).transpose()
    return E_idwt

def idwt2(K):
    K_dwt=copy.deepcopy(K)
    K_dwt_i=copy.deepcopy(K)
    for i in range(K.rows):
        print i
        print K[i,:]
        print idwt(K[i,:])
        K_dwt_i[i,:]=idwt(K[i,:])
    for i in range(K.cols):
    	print "hello"
    	print K_dwt_i[:,i]
    	print idwt(K_dwt_i[:,i].transpose())
    	print K_dwt[:,i]
        K_dwt[:,i]=idwt(K_dwt_i[:,i].transpose()).transpose()

    return copy.deepcopy(K_dwt)
if __name__=="__main__":

    K=matrix([
    [1,0,1,0,1,0],    [0,0,0,0,1,0],[1,0,1,0,1,0],[0,0,0,0,1,0],[0,0,0,0,1,0],[0,0,0,0,1,0]
        ])
    # E=matrix([[1,1,1,1,1,1,1,1,1,1,1,0]])
    # # E=matrix([ 0.288461538460848,0.0333086693845357, 0.403846153845187,0.0333086693845357, 0.519230769229526,0.0333086693845357, 0.634615384613866, 0.0333086693845357])
    # print E,"\n"
    K_sadas= idwt2(dwt2(K))
    for i in range(6):
    	for j in range(6):
    		if abs(K_sadas[i,j])<0.000000000001:
    			K_sadas[i,j]=0
    print K_sadas
    # print dwt(E),"\n"
    # print idwt_inside(dwt_inside(E)),"\n"
    # print E[0]