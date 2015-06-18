import pywt
from mpmath import *
import copy
import math
from read_save import *

root8 = pow(8, 0.5)
root2 = pow(2, 0.5)


def dwt(E):
    length = len(E)
    E_dwt = copy.deepcopy(E)
    E_dwt = dwt_inside(E)
    if length > 2:
        for i in range(1, int(math.log(length, 2))):
            # print i,"before inside"
            E_dwt[
                0:length / pow(2, i)] = dwt_inside(E_dwt[0:length / pow(2, i)])
    return E_dwt


def dwt_inside(E):
    # print "inside",E,"inside"
    length = len(E)
    E_dwt = [0] * length
    for i in range(length / 2):

        E_dwt[i] = (E[2 * i] + E[2 * i + 1]) / root2
    for i in range(length / 2):
        E_dwt[i + length / 2] = (E[2 * i] - E[2 * i + 1]) / root2

    return matrix(E_dwt)


def dwt2(K):
    K_dwt = copy.deepcopy(K)
    K_dwt_i = copy.deepcopy(K)
    for i in range(K.cols):
        K_dwt_i[:, i] = dwt(K[:, i])
    for i in range(K.rows):
        K_dwt[i, :] = dwt(K_dwt_i[i, :]).transpose()
    return K_dwt
def dwt2_inside(K):
    K_dwt = copy.deepcopy(K)
    K_dwt_i = copy.deepcopy(K)
    for i in range(K.cols):
        K_dwt_i[:, i] = dwt_inside(K[:, i])
    for i in range(K.rows):
        K_dwt[i, :] = dwt_inside(K_dwt_i[i, :]).transpose()
    return K_dwt


def idwt2(K):
    K_dwt = copy.deepcopy(K)
    K_dwt_i = copy.deepcopy(K)
    for i in range(K.rows):
        # print i
        K_dwt_i[i, :] = idwt(K[i, :].transpose()).transpose()
    for i in range(K.cols):
        K_dwt[:, i] = idwt(K_dwt_i[:, i])

    return K_dwt
def idwt2_inside(K):
    K_dwt = copy.deepcopy(K)
    K_dwt_i = copy.deepcopy(K)
    for i in range(K.rows):
        # print i
        K_dwt_i[i, :] = idwt_inside(K[i, :].transpose()).transpose()
    for i in range(K.cols):
        K_dwt[:, i] = idwt_inside(K_dwt_i[:, i])

    return K_dwt

def idwt_inside(E):

    length = len(E)
    E_idwt = [0] * length

    for i in range(length / 2):

        E_idwt[2 * i] = (E[i] + E[length / 2 + i]) / root2
        E_idwt[2 * i + 1] = (E[i] - E[length / 2 + i]) / root2
        # if E_idwt[2 * i + 1] < 0.000000000001:
        #     E_idwt[2 * i + 1] = 0

    return matrix(E_idwt)


def idwt(E):
    length = len(E)
    E_idwt = copy.deepcopy(E)

    for i in range(1, int(math.log(length, 2)) + 1):
        E_idwt[0:pow(2, i)] = idwt_inside(E_idwt[0:pow(2, i)])
        # print i,E_idwt[0:pow(2,i)], i

    return E_idwt
def dwt4(K,n):
    # K_dwt = copy.deepcopy(K)
    K_dwt_i_1 = copy.deepcopy(K)
    K_dwt_i_2 = copy.deepcopy(K)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                K_dwt_i_1[:][i][j][k]=dwt(matrix(K[:][ i][j][k])).transpose().tolist()[0]
        # K_dwt_i[:, i] = dwt(K[:, i])
    for i in range(n):
        for j in range(n):
            for k in range(n):
                K_dwt_i_2[i][:][j][k]=dwt(matrix(K_dwt_i_1[i][ :][j][k])).transpose().tolist()[0]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                K_dwt_i_1[i][j][:][k]=dwt(matrix(K_dwt_i_2[i][ j][:][k])).transpose().tolist()[0]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                K_dwt_i_2[i][j][k][:]=dwt(matrix(K_dwt_i_1[i][ j][k][:])).transpose().tolist()[0]
    return K_dwt_i_2
def idwt4(K,n):
    # K_dwt = copy.deepcopy(K)
    K_dwt_i_1 = copy.deepcopy(K)
    K_dwt_i_2 = copy.deepcopy(K)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                K_dwt_i_1[:][i][j][k]=idwt(matrix(K[:][ i][j][k])).transpose().tolist()[0]
        # K_dwt_i[:, i] = dwt(K[:, i])
    for i in range(n):
        for j in range(n):
            for k in range(n):
                K_dwt_i_2[i][:][j][k]=idwt(matrix(K_dwt_i_1[i][ :][j][k])).transpose().tolist()[0]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                K_dwt_i_1[i][j][:][k]=idwt(matrix(K_dwt_i_2[i][ j][:][k])).transpose().tolist()[0]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                K_dwt_i_2[i][j][k][:]=idwt(matrix(K_dwt_i_1[i][ j][k][:])).transpose().tolist()[0]
    return K_dwt_i_2
if __name__ == "__main__":
    n=2
    dist=0.25
    # K_1=readit(n,dist)
    K_1= readit(n,0.25)
    print K_1

    print K_1
    K=idwt4(dwt4(K_1,n),n)
    print K
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if abs(K[i][j][k][l]-K_1[i][j][k][l]) > 0.0001:
                        print "diff"
    # K = matrix(
    #     [
    #         [1, 1, 1, 1],
    #         [1, 0, 1, 1],
    #         [1, 1, 0, 1],
    #         [1, 1, 1, 0]
    #     ])
    # n=2
    # e = matrix([[1, 1, 1, 1, 1, 1, 1, 0]])
    # K=[[[[0.4154199472473506, 0.093736162923114735], [0.093736162923114721, 0.029311837464653323]], [[0.093736162923114777, 0.4154199472473506], [0.029311837464653327, 0.093736162923114721]]], [[[0.093736162923115013, 0.029311837464653292], [0.4154199472473506, 0.093736162923114735]], [[0.029311837464653295, 0.093736162923115013], [0.093736162923114777, 0.4154199472473506]]]]
    # dist=0.25
    # K=readit(4,dist)
    # K_rec=idwt4(dwt4(K,n),n)
    # print K_rec
    # print matrix([[1, 1, 1, 1, 1, 1, 1, 0]]).tolist()
    # print e
    # print dwt(e)
    # print idwt(dwt(e))
