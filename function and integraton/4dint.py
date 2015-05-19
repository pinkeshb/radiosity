from mpmath import *
# f=lambda x1,x2,y1,y2:1/((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

def fun(x2,y2):
    fi=lambda x1,y1:1/((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    print "x2,y2",x2,y2
    # fi=lambda x1,y1:x2*y2*x1*y1

    return quad(fi,[0,1],[0,1],method='gauss-legendre')
f=lambda x2,y2: fun(x2,y2)
print f(0,0)
print quad(f,[0,1],[0,1],method='gauss-legendre')

# f=lambda x1,x2,y1,y2:1/((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
# i=0
# n=4
# fi=lambda x1,x2:quad(f(x1,x2), [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)])
# quad(fi, [i / float(n), (i + 1) / float(n)], [j / float(n), (j + 1) / float(n)])
# print integrate(f(x1,x2,y1,y2), (x1, -1, 1),(x2, -1, 1),(y1, -1, 1),(y2, -1, 1))
