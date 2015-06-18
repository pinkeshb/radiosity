from mpmath import *
from m2_phi import *

def smrt_error(n,dist):
    a_2_mat=matrix(n,n)
    b_2_mat=matrix(n,n)
    c_2_mat=matrix(n,n)
    d_2_mat=matrix(n,n)
    e_2_mat=matrix(n,n)
    ab2_mat=matrix(n,n)
    cd2_mat=matrix(n,n)
    ac2_mat=matrix(n,n)
    ad2_mat=matrix(n,n)
    bc2_mat=matrix(n,n)
    bd2_mat=matrix(n,n)
    ae2_mat=matrix(n,n)
    be2_mat=matrix(n,n)
    ce2_mat=matrix(n,n)
    de2_mat=matrix(n,n)
    # # =1
    # a=f
    # b=00
    # c=01
    # d=10
    # e=11
    f1 = lambda s, t: (s+0.1)*(t+0.1)/ (2*pow(((s+0.1)*(s+0.1) +(t+0.1)*(t+0.1)), 1.5))

    a_changd=1.0/n
    for i in range(0, n):
        print i/float(n)*100,"percent done"
        for j in range(0, n):
            a   = lambda s,t:   f1(s, t)
            b   = lambda s,t:   dia_trans(s, a_changd, i / float(n),phi_1_m2) * dia_trans(t, a_changd, j / float(n), phi_1_m2)
            c   = lambda s,t:   dia_trans(s, a_changd, i / float(n),phi_1_m2) * dia_trans(t, a_changd, j / float(n), phi_2_m2)
            d   = lambda s,t:   dia_trans(s, a_changd, i / float(n),phi_2_m2) * dia_trans(t, a_changd, j / float(n), phi_1_m2)
            e   = lambda s,t:   dia_trans(s, a_changd, i / float(n),phi_2_m2) * dia_trans(t, a_changd, j / float(n), phi_2_m2)
            a_2 = lambda s, t:  a(s,t)*a(s,t)
            b_2 = lambda s, t:  b(s,t)*b(s,t)
            c_2 = lambda s, t:  c(s,t)*c(s,t)
            d_2 = lambda s, t:  d(s,t)*d(s,t)
            e_2 = lambda s, t:  e(s,t)*e(s,t)
            ab2 = lambda s, t:  a(s,t)*b(s,t)*2
            cd2 = lambda s, t:  c(s,t)*d(s,t)*2
            ac2 = lambda s, t:  a(s,t)*c(s,t)*2
            ad2 = lambda s, t:  a(s,t)*d(s,t)*2
            bc2 = lambda s, t:  b(s,t)*c(s,t)*2
            bd2 = lambda s, t:  b(s,t)*d(s,t)*2
            ae2 = lambda s, t:  a(s,t)*e(s,t)*2
            be2 = lambda s, t:  b(s,t)*e(s,t)*2
            ce2 = lambda s, t:  c(s,t)*e(s,t)*2
            de2 = lambda s, t:  d(s,t)*e(s,t)*2
            # f_error = lambda s, t: (f1(s, t) - K[i, j] * pow(n, 0.5) * pow(n, 0.5)) *\
            #     (f1(s, t) - K[i, j] * pow(n, 0.5) * pow(n, 0.5))
            a_2_mat[i, j] = quad(a_2, [i / float(n), (i + 1) / float(n)],
                           [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            b_2_mat[i, j] = quad(
                b_2, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            c_2_mat[i, j] = quad(
                c_2, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            d_2_mat[i, j] = quad(
                d_2, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            e_2_mat[i, j] = quad(
                e_2, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            ab2_mat[i, j] = quad(
                ab2, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            cd2_mat[i, j] = quad(
                cd2, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            ac2_mat[i, j] = quad(
                ac2, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            ad2_mat[i, j] = quad(
                ad2, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            bc2_mat[i, j] = quad(
                bc2, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            bd2_mat[i, j] = quad(
                bd2, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            ae2_mat[i, j] = quad(
                ae2, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            be2_mat[i, j] = quad(
                be2, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            ce2_mat[i, j] = quad(
                ce2, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
            de2_mat[i, j] = quad(
                de2, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)],method='gauss-legendre')
    return a_2_mat,b_2_mat,c_2_mat,d_2_mat,e_2_mat,ab2_mat,cd2_mat,ac2_mat,ad2_mat,bc2_mat,bd2_mat,ae2_mat,be2_mat,ce2_mat,de2_mat
if __name__=="__main__":
    print smrt_error(4,1)