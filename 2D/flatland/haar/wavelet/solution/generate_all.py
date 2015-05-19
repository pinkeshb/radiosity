# from kernel_haar_phi import *
from mpmath import *
from wavedecs import *
from save_read import *
n=256
fname = str(n) + 'haar_scale_K_mat_dist_0.25' + ".txt"
fo = open(fname, "r")
n=fo.readline()
n=int(n)
K = matrix(n,n)
for i in range(n):
    line=fo.readline()
    # print line
    line = line.split()
    # print line[0]
    print i
    for j in range(n):

        K[i,j]=float(line[j])

K1=dwt2_inside(K)
K1=K1[0:128,0:128]
n=K1.cols
saveit(n,K1,"haar_scale_K_mat_dist_0.25")
K2=dwt2_inside(K1)
K2=K2[0:64,0:64]
n=K2.cols
saveit(n,K2,"haar_scale_K_mat_dist_0.25")
K3=dwt2_inside(K2)
K3=K3[0:32,0:32]
n=K3.cols
saveit(n,K3,"haar_scale_K_mat_dist_0.25")
K4=dwt2_inside(K3)
K4=K4[0:16,0:16]
n=K4.cols
saveit(n,K4,"haar_scale_K_mat_dist_0.25")
K5=dwt2_inside(K4)
K5=K5[0:8,0:8]
n=K5.cols
saveit(n,K5,"haar_scale_K_mat_dist_0.25")
K6=dwt2_inside(K5)
K6=K6[0:4,0:4]
n=K6.cols
saveit(n,K6,"haar_scale_K_mat_dist_0.25")
# K3=dwt2_inside(K2[0:64,0:64])
# K4=dwt2_inside(K3[0:32,0:32])
# K5=dwt2_inside(K4[0:16,0:16])
# K6=dwt2_inside(K5[0:16,0:16])
# print "K",K6
# print "K_original",K_original
# n=4
# num_k=0
# for i in range(n):
#     for j in range(n):
#         num_k=num_k+abs(K6[i,j]-K_original[i,j])
# print num_k