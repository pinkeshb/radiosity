import pywt
from mpmath import *
import copy
import math
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


def idwt2(K):
    K_dwt = copy.deepcopy(K)
    K_dwt_i = copy.deepcopy(K)
    for i in range(K.rows):
        # print i
        K_dwt_i[i, :] = idwt(K[i, :].transpose()).transpose()
    for i in range(K.cols):
        K_dwt[:, i] = idwt(K_dwt_i[:, i])

    return K_dwt


def idwt_inside(E):

    length = len(E)
    E_idwt = [0] * length

    for i in range(length / 2):

        E_idwt[2 * i] = (E[i] + E[length / 2 + i]) / root2
        E_idwt[2 * i + 1] = (E[i] - E[length / 2 + i]) / root2
        if abs(E_idwt[2 * i + 1]) < 0.000000000001:
            E_idwt[2 * i + 1] = 0

    return matrix(E_idwt)


def idwt(E):
    length = len(E)
    E_idwt = copy.deepcopy(E)

    for i in range(1, int(math.log(length, 2)) + 1):
        E_idwt[0:pow(2, i)] = idwt_inside(E_idwt[0:pow(2, i)])
        # print i,E_idwt[0:pow(2,i)], i

    return E_idwt
if __name__ == "__main__":
    K = matrix(
        [
            [1, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0]
        ])

    # e = matrix([[1, 1, 1, 1, 1, 1, 1, 0]])
    # print e
    # print dwt(e)
    # print idwt(dwt(e))
    print dwt2(K)
    print idwt2(dwt2(K))
