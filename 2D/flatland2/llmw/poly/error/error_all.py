from kernel_m2_phi import *


thres=0.001
n_min,n_max=2,5

fname = 'haar_scale_all_error' + ".txt"
fo = open(fname, "w")

for n_log in range(n_min,n_max):
    n=pow(2,n_log)

    K,K_error=project_kernel_m2_phi(n)
    num_k=0
    for i in range(n):
        for j in range(n):
            num_k=num_k+K_error[i,j]



    print "n = ", n, "\n"
    fo.write("n = "+str(n) + "\n")

    print "error_k = ", num_k, "\n"
    fo.write("error_k = "+str(num_k) + "\n")


    print "\n\n\n"
