import math
def phi_1_m2(x):
    if 0<=x<1:
        return 1.0
    else:
        return 0.0
def phi_2_m2(x):
    # print x
    if 0<=x<1:
        # print "in range"

        return (2*float(x)-1)*1.732050808
    else:
        return 0.0
def dia_trans(x,a,s,f):
    # print x
    if f == phi_2_m2:
        # return f((x-s)/float(a))
        # print "hi"
        return f((x-s)/float(a))/pow(a,0.5)
    return f((x-s)/float(a))/pow(a,0.5)
# print dia_trans(0.49,0.25,0.25,phi_2_m2)
# print pow(1.732050808,math.log(2,2))