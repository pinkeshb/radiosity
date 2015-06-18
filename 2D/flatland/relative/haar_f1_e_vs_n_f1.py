from matplotlib import pyplot
def haar():

    n2 = [4,8,16]

    error_k_m_2=0.000588413740957945, 1.178576890827816e-05,2.04445118592674e-7
    # 1.05318677716279
    n1 = [4,8,16,32,64]

    error_k_m_1 = [0.0090321523663344,0.000723646210968279,4.75909541744409e-5,3.01062051659074e-6,1.88726971844844e-7]


    n0 = [4,8,16,32,64,128,256]

    error_k = [0.106149444281525,0.0349644581357715,0.00933949276979555,0.0023744714499249,0.000596148650657886,0.000149196250921582,3.73090198532804e-5]
    
    relative_error_k=[error_k[i]/1.05318677716279*100 for i in range(len(error_k))]
    relative_error_k_m_1=[error_k_m_1[i]/1.05318677716279*100 for i in range(len(error_k_m_1))]
    relative_error_k_m_2=[error_k_m_2[i]/1.05318677716279*100 for i in range(len(error_k_m_2))]

    pyplot.plot(n0,relative_error_k,label="m=0")
    pyplot.plot(n1,relative_error_k_m_1,label="m=1")
    pyplot.plot(n2,relative_error_k_m_2,label="m=2")
    pyplot.xlabel('n (Number of interval in [0,1])')
    pyplot.ylabel('Relative Error (%)')
    pyplot.legend( loc=1)
    pyplot.yscale('log')
    pyplot.xscale('log')
    pyplot.show()
haar()