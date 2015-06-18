from matplotlib import pyplot
def haar():
# 0.0917499295928161

    n2 = [4,8,16]

    error_k_m_2=[2.78427713366587e-5, 1.67165095084357e-6,1.1193557998261939e-07]
    # 0.0917499295928161
    n1 = [4,8,16,32,64]

    error_k_m_1 = [0.00027712759288543,3.37106982543309e-5,4.4998103153013e-06,5.791578507067786e-07,7.242948460820537e-08]


    n0 = [4,8,16,32,64,128,256]

    error_k = [0.00102848347632868,0.000265239226728829,6.68221831822243e-5 ,1.67376618854259e-5,4.18642421035427e-6,1.04673160803925e-6 ,2.61690735256112e-7 ]
    
    relative_error_k=[error_k[i]/0.0917499295928161*100 for i in range(len(error_k))]
    relative_error_k_m_1=[error_k_m_1[i]/0.0917499295928161*100 for i in range(len(error_k_m_1))]
    relative_error_k_m_2=[error_k_m_2[i]/0.0917499295928161*100 for i in range(len(error_k_m_2))]

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