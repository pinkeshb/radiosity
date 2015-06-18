def copyit(B1_pre,B1):
    for i in range(n):
        for j in range(n):
            B1_pre[i][j]=B1[i][j]
def iterit(B,E,K,B_pre):
    print "E",E
    print "B",B
    print "B_pre",B_pre
    print "K",K
    for i in range(n):
        for j in range(n):
            sum=0
            for i1 in range(n):
                for j1 in range(n):
                    print "sum",sum
                    sum=sum+B_pre[i1][j1]*K[i][j][i1][j1]
            print "B[i][j]",B[i][j]
            print "E[i][j]",E[i][j]
            B[i][j]=E[i][j]+sum
    print B,E,B_pre
n=4
K = [[[[1 for x in range(n)] for x in range(n)] for x in range(n)] for x in range(n)] 
B = [[0 for x in range(n)] for x in range(n)] 
E = [[1 for x in range(n)] for x in range(n)] 
B_pre = [[0 for x in range(n)] for x in range(n)] 
# E1 = [[1 for x in range(n)] for x in range(n)] 
copyit(B_pre,B)
iterit(B,E,K,B_pre)
copyit(B_pre,B)
iterit(B,E,K,B_pre)
copyit(B_pre,B)
iterit(B,E,K,B_pre)
# for i in range(n):
#     for j in range(n):
#         if i>=3*n/4 and j>=3*n/4:
#             E1[i][j]=1.0/n
# c=0
# n=2
# for i in range(n):
#     for j in range(n):
#         for i1 in range(n):
#             for j1 in range(n):
#                 K[i][j][i1][j1]=c
#                 c=c+1
# print K
# for iter in range(10):
#     for i in range(n):
#         for j in range(n):
#             sum=0
#             for i1 in range(n):
#                 for j1 in range(n):
#                     print "sum",sum
#                     print "K",K[i][j][i1][j1]
#                     print B[i1][j1]
#                     sum=sum+B[i1][j1]*K[i][j][i1][j1]
#             print E[i][j]
#             B[i][j]=E[i][j]+sum
#             # print B
