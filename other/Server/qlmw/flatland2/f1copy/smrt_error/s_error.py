from mpmath import *
from m3_phi import *

def smrt_error(n,dist):
    a_2_mat=matrix(n,n)
    b_2_mat=matrix(n,n)
    c_2_mat=matrix(n,n)
    d_2_mat=matrix(n,n)
    e_2_mat=matrix(n,n)
    f_2_mat=matrix(n,n)
    g_2_mat=matrix(n,n)
    h_2_mat=matrix(n,n)
    i_2_mat=matrix(n,n)
    j_2_mat=matrix(n,n)

    ab2_mat=matrix(n,n)
    ac2_mat=matrix(n,n)
    ad2_mat=matrix(n,n)
    ae2_mat=matrix(n,n)
    af2_mat=matrix(n,n)
    ag2_mat=matrix(n,n)
    ah2_mat=matrix(n,n)
    ai2_mat=matrix(n,n)
    aj2_mat=matrix(n,n)

    bc2_mat=matrix(n,n)
    bd2_mat=matrix(n,n)
    be2_mat=matrix(n,n)
    bf2_mat=matrix(n,n)
    bg2_mat=matrix(n,n)
    bh2_mat=matrix(n,n)
    bi2_mat=matrix(n,n)
    bj2_mat=matrix(n,n)

    cd2_mat=matrix(n,n)
    ce2_mat=matrix(n,n)
    cf2_mat=matrix(n,n)
    cg2_mat=matrix(n,n)
    ch2_mat=matrix(n,n)
    ci2_mat=matrix(n,n)
    cj2_mat=matrix(n,n)

    de2_mat=matrix(n,n)
    df2_mat=matrix(n,n)
    dg2_mat=matrix(n,n)
    dh2_mat=matrix(n,n)
    di2_mat=matrix(n,n)
    dj2_mat=matrix(n,n)

    ef2_mat=matrix(n,n)
    eg2_mat=matrix(n,n)
    eh2_mat=matrix(n,n)
    ei2_mat=matrix(n,n)
    ej2_mat=matrix(n,n)

    fg2_mat=matrix(n,n)
    fh2_mat=matrix(n,n)
    fi2_mat=matrix(n,n)
    fj2_mat=matrix(n,n)

    gh2_mat=matrix(n,n)
    gi2_mat=matrix(n,n)
    gj2_mat=matrix(n,n)

    hi2_mat=matrix(n,n)
    hj2_mat=matrix(n,n)

    ij2_mat=matrix(n,n)

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
            b   = lambda s,t:   dia_trans(s, a_changd, i / float(n),phi_0_m3) * dia_trans(t, a_changd, j / float(n), phi_0_m3)
            c   = lambda s,t:   dia_trans(s, a_changd, i / float(n),phi_0_m3) * dia_trans(t, a_changd, j / float(n), phi_1_m3)
            d   = lambda s,t:   dia_trans(s, a_changd, i / float(n),phi_0_m3) * dia_trans(t, a_changd, j / float(n), phi_2_m3)
            e   = lambda s,t:   dia_trans(s, a_changd, i / float(n),phi_1_m3) * dia_trans(t, a_changd, j / float(n), phi_0_m3)
            f   = lambda s,t:   dia_trans(s, a_changd, i / float(n),phi_1_m3) * dia_trans(t, a_changd, j / float(n), phi_1_m3)
            g   = lambda s,t:   dia_trans(s, a_changd, i / float(n),phi_1_m3) * dia_trans(t, a_changd, j / float(n), phi_2_m3)
            h   = lambda s,t:   dia_trans(s, a_changd, i / float(n),phi_2_m3) * dia_trans(t, a_changd, j / float(n), phi_0_m3)
            I   = lambda s,t:   dia_trans(s, a_changd, i / float(n),phi_2_m3) * dia_trans(t, a_changd, j / float(n), phi_1_m3)
            J   = lambda s,t:   dia_trans(s, a_changd, i / float(n),phi_2_m3) * dia_trans(t, a_changd, j / float(n), phi_2_m3)



            a_2 =   lambda s,t: a(s,t)*a(s,t)
            b_2 =   lambda s,t: b(s,t)*b(s,t)
            c_2 =   lambda s,t: c(s,t)*c(s,t)
            d_2 =   lambda s,t: d(s,t)*d(s,t)
            e_2 =   lambda s,t: e(s,t)*e(s,t)
            f_2 =   lambda s,t: f(s,t)*f(s,t)
            g_2 =   lambda s,t: g(s,t)*g(s,t)
            h_2 =   lambda s,t: h(s,t)*h(s,t)
            i_2 =   lambda s,t: I(s,t)*I(s,t)
            j_2 =   lambda s,t: J(s,t)*J(s,t)
            
              
            ab2 =   lambda s,t: a(s,t)*b(s,t)*2
            ac2 =   lambda s,t: a(s,t)*c(s,t)*2
            ad2 =   lambda s,t: a(s,t)*d(s,t)*2
            ae2 =   lambda s,t: a(s,t)*e(s,t)*2
            af2 =   lambda s,t: a(s,t)*f(s,t)*2
            ag2 =   lambda s,t: a(s,t)*g(s,t)*2
            ah2 =   lambda s,t: a(s,t)*h(s,t)*2
            ai2 =   lambda s,t: a(s,t)*I(s,t)*2
            aj2 =   lambda s,t: a(s,t)*J(s,t)*2
            
              
            bc2 =   lambda s,t: b(s,t)*c(s,t)*2
            bd2 =   lambda s,t: b(s,t)*d(s,t)*2
            be2 =   lambda s,t: b(s,t)*e(s,t)*2
            bf2 =   lambda s,t: b(s,t)*f(s,t)*2
            bg2 =   lambda s,t: b(s,t)*g(s,t)*2
            bh2 =   lambda s,t: b(s,t)*h(s,t)*2
            bi2 =   lambda s,t: b(s,t)*I(s,t)*2
            bj2 =   lambda s,t: b(s,t)*J(s,t)*2
            
              
            cd2 =   lambda s,t: c(s,t)*d(s,t)*2
            ce2 =   lambda s,t: c(s,t)*e(s,t)*2
            cf2 =   lambda s,t: c(s,t)*f(s,t)*2
            cg2 =   lambda s,t: c(s,t)*g(s,t)*2
            ch2 =   lambda s,t: c(s,t)*h(s,t)*2
            ci2 =   lambda s,t: c(s,t)*I(s,t)*2
            cj2 =   lambda s,t: c(s,t)*J(s,t)*2
            
              
            de2 =   lambda s,t: d(s,t)*e(s,t)*2
            df2 =   lambda s,t: d(s,t)*f(s,t)*2
            dg2 =   lambda s,t: d(s,t)*g(s,t)*2
            dh2 =   lambda s,t: d(s,t)*h(s,t)*2
            di2 =   lambda s,t: d(s,t)*I(s,t)*2
            dj2 =   lambda s,t: d(s,t)*J(s,t)*2
            
              
            ef2 =   lambda s,t: e(s,t)*f(s,t)*2
            eg2 =   lambda s,t: e(s,t)*g(s,t)*2
            eh2 =   lambda s,t: e(s,t)*h(s,t)*2
            ei2 =   lambda s,t: e(s,t)*I(s,t)*2
            ej2 =   lambda s,t: e(s,t)*J(s,t)*2
            
              
            fg2 =   lambda s,t: f(s,t)*g(s,t)*2
            fh2 =   lambda s,t: f(s,t)*h(s,t)*2
            fi2 =   lambda s,t: f(s,t)*I(s,t)*2
            fj2 =   lambda s,t: f(s,t)*J(s,t)*2
            
              
            gh2 =   lambda s,t: g(s,t)*h(s,t)*2
            gi2 =   lambda s,t: g(s,t)*I(s,t)*2
            gj2 =   lambda s,t: g(s,t)*J(s,t)*2
            
              
            hi2 =   lambda s,t: h(s,t)*I(s,t)*2
            hj2 =   lambda s,t: h(s,t)*J(s,t)*2
            
              
            ij2 =   lambda s,t: I(s,t)*J(s,t)*2
            
            # f_error = lambda s, t: (f1(s, t) - K[i, j] * pow(n, 0.5) * pow(n, 0.5)) *\
            #     (f1(s, t) - K[i, j] * pow(n, 0.5) * pow(n, 0.5))
            a_2_mat[i,j] = quad(a_2,[i/float(n), (i+1)/float(n)] , [j/float(n),(j+1)/float(n)] , method='gauss-legendre')
            print a_2_mat[i,j]
            b_2_mat[i,j] = quad(b_2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            c_2_mat[i,j] = quad(c_2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            d_2_mat[i,j] = quad(d_2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            e_2_mat[i,j] = quad(e_2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            f_2_mat[i,j] = quad(f_2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            g_2_mat[i,j] = quad(g_2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            h_2_mat[i,j] = quad(h_2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            i_2_mat[i,j] = quad(i_2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            j_2_mat[i,j] = quad(j_2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            ab2_mat[i,j] = quad(ab2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            ac2_mat[i,j] = quad(ac2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            ad2_mat[i,j] = quad(ad2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            ae2_mat[i,j] = quad(ae2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            af2_mat[i,j] = quad(af2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            ag2_mat[i,j] = quad(ag2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            ah2_mat[i,j] = quad(ah2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            ai2_mat[i,j] = quad(ai2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            aj2_mat[i,j] = quad(aj2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            bc2_mat[i,j] = quad(bc2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            bd2_mat[i,j] = quad(bd2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            be2_mat[i,j] = quad(be2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            bf2_mat[i,j] = quad(bf2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            bg2_mat[i,j] = quad(bg2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            bh2_mat[i,j] = quad(bh2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            bi2_mat[i,j] = quad(bi2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            bj2_mat[i,j] = quad(bj2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            cd2_mat[i,j] = quad(cd2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            ce2_mat[i,j] = quad(ce2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            cf2_mat[i,j] = quad(cf2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            cg2_mat[i,j] = quad(cg2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            ch2_mat[i,j] = quad(ch2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            ci2_mat[i,j] = quad(ci2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            cj2_mat[i,j] = quad(cj2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            de2_mat[i,j] = quad(de2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            df2_mat[i,j] = quad(df2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            dg2_mat[i,j] = quad(dg2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            dh2_mat[i,j] = quad(dh2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            di2_mat[i,j] = quad(di2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            dj2_mat[i,j] = quad(dj2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            ef2_mat[i,j] = quad(ef2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            eg2_mat[i,j] = quad(eg2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            eh2_mat[i,j] = quad(eh2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            ei2_mat[i,j] = quad(ei2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            ej2_mat[i,j] = quad(ej2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            fg2_mat[i,j] = quad(fg2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            fh2_mat[i,j] = quad(fh2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            fi2_mat[i,j] = quad(fi2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            fj2_mat[i,j] = quad(fj2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            gh2_mat[i,j] = quad(gh2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            gi2_mat[i,j] = quad(gi2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            gj2_mat[i,j] = quad(gj2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            hi2_mat[i,j] = quad(hi2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            hj2_mat[i,j] = quad(hj2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
            ij2_mat[i,j] = quad(ij2,[i/float(n), (i+1)/float(n)],[j/float(n),(j+1)/float(n)],method="gauss-legendre")
    return a_2_mat,b_2_mat,c_2_mat,d_2_mat,e_2_mat,f_2_mat,g_2_mat,h_2_mat,i_2_mat,j_2_mat,ab2_mat,ac2_mat,ad2_mat,ae2_mat,af2_mat,ag2_mat,ah2_mat,ai2_mat,aj2_mat,bc2_mat,bd2_mat,be2_mat,bf2_mat,bg2_mat,bh2_mat,bi2_mat,bj2_mat,cd2_mat,ce2_mat,cf2_mat,cg2_mat,ch2_mat,ci2_mat,cj2_mat,de2_mat,df2_mat,dg2_mat,dh2_mat,di2_mat,dj2_mat,ef2_mat,eg2_mat,eh2_mat,ei2_mat,ej2_mat,fg2_mat,fh2_mat,fi2_mat,fj2_mat,gh2_mat,gi2_mat,gj2_mat,hi2_mat,hj2_mat,ij2_mat
if __name__=="__main__":
    # print smrt_error(4,1)
    dist=0.25
    f = lambda s, t: dist*dist/ (2*pow(((s - t) * (s - t) + dist*dist), 1.5))
    f1 = lambda s, t: f(s,t)*f(s,t)
    print quad(f1,[0,1],[0,1])