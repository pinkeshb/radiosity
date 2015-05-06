from main import *

thres=0.001
n_min,n_max=2,7

fname = 'haar_scale_all_error' + ".txt"
fo = open(fname, "w")

for n_log in range(n_min,n_max):
	n=pow(2,n_log)

	B_proj,B_error,K,K_error=main_fn(n,thres)
	num_k=0
	for i in range(n):
		for j in range(n):
			num_k=num_k+K_error[i,j]


	num_b =0
	for i in range(n):
		num_b=num_b+B_error[i]


	print "n = ", n, "\n"
	fo.write("n = "+str(n) + "\n")

	print "error_k = ", num_k, "\n"
	fo.write("error_k = "+str(num_k) + "\n")

	print "error_b = ", num_b, "\n"
	fo.write("error_b = "+str(num_b) + "\n")

	print "\n\n\n"
