from mpmath import *

def smrt_error(n,dist):
    K_f = matrix(n, n)
    K_fp = matrix(n, n)
    K_p= matrix(n, n)
    # =1
    f1 = lambda s, t: (s+0.1)*(t+0.1)/ (2*pow(((s+0.1)*(s+0.1) +(t+0.1)*(t+0.1)), 1.5))
    f_f = lambda s, t: f1(s, t) *f1(s, t)
    f_fp = lambda s, t: 2*f1(s, t)*n
    f_p = lambda s, t: n*n
    for i in range(0, n):
        print i/float(n)
        for j in range(0, n):

            # f_error = lambda s, t: (f1(s, t) - K[i, j] * pow(n, 0.5) * pow(n, 0.5)) *\
            #     (f1(s, t) - K[i, j] * pow(n, 0.5) * pow(n, 0.5))
            K_f[i, j] = quad(
                f_f, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            K_fp[i, j] = quad(
                f_fp, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            K_p[i, j] = quad(
                f_p, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
    return K_f,K_fp,K_p
if __name__=="__main__":
    pass