from kernel_haar_phi import *
from wavedecs import *

def project_kernel_wavelet(n):
	K=project_kernel_haar_phi(n)
	K_dwt=dwt2(K)
	return K_dwt
