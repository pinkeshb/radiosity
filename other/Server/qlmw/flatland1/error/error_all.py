from kernel_m3_phi import *


thres=0.001
n_min,n_max=3,4

fname = 'm3_poly_all_error' + ".txt"
fo = open(fname, "w")

for n_log in range(n_min,n_max):
    n=pow(2,n_log)

    K,K_error=project_kernel_m3_phi(n)
    num_k=0
    for i in range(n):
        for j in range(n):
            num_k=num_k+K_error[i,j]



    print "n = ", n, "\n"
    fo.write("n = "+str(n) + "\n")

    print "error_k = ", num_k, "\n"
    fo.write("error_k = "+str(num_k) + "\n")
    print K
    print K_error
    errorit=0
    for i in range(n):
        for j in range(n):
	    errorit=errorit+K_error[i,j]
    print errorit
    print "\n\n\n"
