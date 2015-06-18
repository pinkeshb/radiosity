# from kernel_haar_phi import *
from mpmath import *
from wavedecs import *
from save_read import *
def all_it():
    n=64
    dist=0.0625
    fname = str(n) + 'qlmw_K_mat_dist_'+str(dist) + ".txt"
    fo = open(fname, "r")
    n=fo.readline()
    n=int(n)
    K = matrix(n*3,n*3)
    for i in range(n*3):
        line=fo.readline()
        # print line
        line = line.split()
        # print line[0]
        print i
        for j in range(n*3):

            K[i,j]=float(line[j])

    # K1=dwt2_inside(K)
    # K1=K1[0:128*2,0:128*2]
    # n=K1.cols/2
    # saveit(n,K1,"qlmw_K_mat_dist_"+str(dist))
    # K2=dwt2_inside(K)
    # K2=K2[0:64*2,0:64*2]
    # n=K2.cols/2
    # saveit(n,K2,"qlmw_K_mat_dist_"+str(dist))

    K3=dwt2_inside(K)
    K3=K3[0:32*3,0:32*3]
    n=K3.cols/3
    saveit(n,K3,"qlmw_K_mat_dist_"+str(dist))
    K4=dwt2_inside(K3)
    K4=K4[0:16*3,0:16*3]
    n=K4.cols/3
    saveit(n,K4,"qlmw_K_mat_dist_"+str(dist))
    K5=dwt2_inside(K4)
    K5=K5[0:8*3,0:8*3]
    n=K5.cols/3
    saveit(n,K5,"qlmw_K_mat_dist_"+str(dist))
    K6=dwt2_inside(K5)
    K6=K6[0:4*3,0:4*3]
    n=K6.cols/3
    saveit(n,K6,"qlmw_K_mat_dist_"+str(dist))
    # K3=dwt2_inside(K2[0:64,0:64])
    # K4=dwt2_inside(K3[0:32,0:32])
    # K5=dwt2_inside(K4[0:16,0:16])
    # K6=dwt2_inside(K5[0:16,0:16])
    # print "K",K6
    # print "K_original",K_original
    n=4
    K_original=project_kernel_m3_phi(n,dist)

    num_k=0
    for i in range(3*n):
        for j in range(3*n):
            num_k=num_k+abs(K6[i,j]-K_original[i,j])
    print num_k
def all_it1():
    n=8
    dist=1
    K = project_kernel_m3_phi(n,dist)

    # K1=dwt2_inside(K)
    # K1=K1[0:128*2,0:128*2]
    # n=K1.cols/2
    # saveit(n,K1,"qlmw_K_mat_dist_"+str(dist))
    # K2=dwt2_inside(K)
    # K2=K2[0:64*2,0:64*2]
    # n=K2.cols/2
    # saveit(n,K2,"qlmw_K_mat_dist_"+str(dist))


    K6=dwt2_inside(K)
    K6=K6[0:4*3,0:4*3]
    n=K6.cols/3
    saveit(n,K6,"qlmw_K_mat_dist_"+str(dist))
    # K3=dwt2_inside(K2[0:64,0:64])
    # K4=dwt2_inside(K3[0:32,0:32])
    # K5=dwt2_inside(K4[0:16,0:16])
    # K6=dwt2_inside(K5[0:16,0:16])
    # print "K",K6
    # print "K_original",K_original
    n=4
    K_original=project_kernel_m3_phi(n,dist)

    num_k=0
    for i in range(3*n):
        for j in range(3*n):
            num_k=num_k+abs(K6[i,j]-K_original[i,j])
    print num_k
all_it()