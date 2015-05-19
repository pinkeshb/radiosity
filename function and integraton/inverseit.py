from mpmath import *
import  sympy
mp.dps = 10
A=matrix([[1/sqrt(2),0,0,1/sqrt(2),0,0],
[-sqrt(3)/sqrt(8),1/sqrt(8),0,sqrt(3)/sqrt(8),1/sqrt(8),0],
[0,-sqrt(5)*sqrt(3)/(4*sqrt(2)),1/(4*sqrt(2)),0,sqrt(5)*sqrt(3)/(4*sqrt(2)),1/(4*sqrt(2))],
[1/(3*sqrt(2)),1/sqrt(6),-sqrt(5)/3/sqrt(2),-1/(3*sqrt(2)),+1/sqrt(6),sqrt(5)/3/sqrt(2)],
[0,1/(4*sqrt(2)),sqrt(3)*sqrt(5)/(4*sqrt(2)),0,-1/(4*sqrt(2)),sqrt(3)*sqrt(5)/(4*sqrt(2))],
[-sqrt(5)/6/sqrt(2),-sqrt(5)/2/sqrt(6),-2/(3*sqrt(2)),sqrt(5)/6/sqrt(2),-sqrt(5)/2/sqrt(6),2/(3*sqrt(2))]])

B=matrix([[1/sqrt(2),0,0,1/sqrt(2),0,0],
[-sqrt(3)/sqrt(8),1/sqrt(8),0,sqrt(3)/sqrt(8),1/sqrt(8),0],
[0,-sqrt(5)*sqrt(3)/(4*sqrt(2)),1/(4*sqrt(2)),0,sqrt(5)*sqrt(3)/(4*sqrt(2)),1/(4*sqrt(2))],
[1/(3*sqrt(2)),1/sqrt(6),-sqrt(5)/3/sqrt(2),-1/(3*sqrt(2)),+1/sqrt(6),sqrt(5)/3/sqrt(2)],
[0,1/(4*sqrt(2)),sqrt(3)*sqrt(5)/(4*sqrt(2)),0,-1/(4*sqrt(2)),sqrt(3)*sqrt(5)/(4*sqrt(2))],
[-sqrt(5)/6/sqrt(2),-sqrt(5)/2/sqrt(6),-2/(3*sqrt(2)),sqrt(5)/6/sqrt(2),-sqrt(5)/2/sqrt(6),2/(3*sqrt(2))]])
print A
print (A**-1).transpose()