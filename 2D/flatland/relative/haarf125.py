
from matplotlib import pyplot
def haar():

    # 1.05318677716279


    # WAVELET
    # topn = 65536
    # ` = 3.73090198532962e-5
    # topn = 32768
    # error_k = 3.73343048112759e-5
    # topn = 16384
    # error_k = 3.77553961996367e-5
    # topn = 8192
    # error_k = 4.20150121885562e-5
    # topn = 4096
    # error_k = 6.85476335811478e-5
    # topn = 2048
    # error_k = 0.000183487249843989
    # topn = 1024
    # error_k = 0.000506725227785953
    # topn = 512
    # error_k = 0.00129410653496159
    # topn = 256
    # error_k = 0.00332986807738648
    # topn = 128
    # error_k = 0.00817309582306631
    # topn = 64
    # error_k = 0.0204637518497464
    # topn = 32
    # error_k = 0.0489365158276707



    # SACLE
    # topn = 65536
    # error_k = 3.73090198532804e-5
    # topn = 32768
    # error_k = 0.033435865306648
    # topn = 16384
    # error_k = 0.259883934714212
    # topn = 8192
    # error_k = 0.583614356130636
    # topn = 4096
    # error_k = 0.807165389354192
    # topn = 2048
    # error_k = 0.928708186091732
    # topn = 1024
    # error_k = 0.990763211913963
    # topn = 512
    # error_k = 1.0219520255985
    # topn = 256
    # error_k = 1.03756368422039
    # topn = 128
    # error_k = 1.04537523069159
    # topn = 64
    # error_k = 1.04928100392718
    # topn = 32
    # error_k = 1.05123389054498


    error_k_scale = [3.73090198532804e-5,0.033435865306648,0.259883934714212,0.583614356130636,0.807165389354192,0.928708186091732,0.990763211913963,1.0219520255985,1.03756368422039,1.04537523069159,1.04928100392718,1.05123389054498]


    topn = [65536,32768,16384,8192,4096,2048,1024,512,256,128,64,32]
    # topn = 32
    error_k_wave=[3.73090198532962e-5,3.73343048112759e-5,3.77553961996367e-5,4.20150121885562e-5,6.85476335811478e-5,0.000183487249843989,0.000506725227785953,0.00129410653496159,0.00332986807738648,0.00817309582306631,0.0204637518497464,0.0489365158276707]
    # topn = [65536,32768,16384,8192,4096,2048,1024,512,256,128,64,32]
    relative_error_k_wave=[error_k_wave[i]/1.05318677716279*100 for i in range(len(error_k_wave))]
    relative_error_k_scale=[error_k_scale[i]/1.05318677716279*100 for i in range(len(error_k_wave))]

    pyplot.plot(topn,relative_error_k_wave,label="Haar Wavelet")
    pyplot.plot(topn,relative_error_k_scale,label="Haar scale")

    # pyplot.ylabel('Element value')
    # pyplot.plot(m,y_ideal,label="Ideal")
    # pyplot.plot(m,y_error,label="Error")
    pyplot.xlabel('Top n Element')
    pyplot.ylabel('Relative Error %')
    pyplot.legend( loc=2)
    pyplot.yscale('log')
    pyplot.xscale('log')
    pyplot.show()



    pyplot.plot(topn,relative_error_k_wave,label="Haar Wavelet")
    # pyplot.plot(topn,relative_error_k_scale,label="Haar scale")

    # pyplot.ylabel('Element value')
    # pyplot.plot(m,y_ideal,label="Ideal")
    # pyplot.plot(m,y_error,label="Error")
    pyplot.xlabel('Top n Element')
    pyplot.ylabel('Relative Error %')
    pyplot.legend( loc=2)
    pyplot.yscale('log')
    pyplot.xscale('log')
    pyplot.show()



    # pyplot.plot(topn,relative_error_k_wave,label="Haar Wavelet")
    pyplot.plot(topn,relative_error_k_scale,label="Haar scale")

    # pyplot.ylabel('Element value')
    # pyplot.plot(m,y_ideal,label="Ideal")
    # pyplot.plot(m,y_error,label="Error")
    pyplot.xlabel('Top n Element')
    pyplot.ylabel('Relative Error %')
    pyplot.legend( loc=2)
    pyplot.yscale('log')
    pyplot.xscale('log')
    pyplot.show()

def llmw():

    # SCALE
    # topn = 16384
    # error_k = 1.88726971844844e-7
    # topn = 8192
    # error_k = 2.90678742668941e-5
    # topn = 4096
    # error_k = 0.000596116131877433
    # topn = 2048
    # error_k = 0.0341027740091992
    # topn = 1024
    # error_k = 0.260656387045133
    # topn = 512
    # error_k = 0.585000472607163
    # topn = 256
    # error_k = 0.80800898797179
    # topn = 128
    # error_k = 0.929152853778474
    # topn = 64
    # error_k = 0.990808550264467
    # topn = 32
    # error_k = 1.02199766371357
    # topn = 16
    # error_k = 1.03759222043812
    # topn = 8
    # error_k = 1.0453894988004


    # Wavelet
    # topn = 16384
    # error_k = 1.88726971852985e-7
    # topn = 8192
    # error_k = 1.88727810286231e-7
    # topn = 4096
    # error_k = 1.89279269625023e-7
    # topn = 2048
    # error_k = 2.36800496500373e-7
    # topn = 1024
    # error_k = 1.2891859351752e-6
    # topn = 512
    # error_k = 1.14333926198547e-5
    # topn = 256
    # error_k = 9.13684846541906e-5
    # topn = 128
    # error_k = 0.000522824557714731
    # topn = 64
    # error_k = 0.0020432469250234
    # topn = 32
    # error_k = 0.0101946217373199
    # topn = 16
    # error_k = 0.0248584518879141
    # topn = 8
    # error_k = 0.0565279495217267

    error_k_wave = [1.88726971852985e-7,1.88727810286231e-7,1.89279269625023e-7,2.36800496500373e-7,1.2891859351752e-6,1.14333926198547e-5,9.13684846541906e-5,0.000522824557714731,0.0020432469250234,0.0101946217373199,0.0248584518879141,0.0565279495217267]


    error_k_scale = [1.88726971844844e-7,2.90678742668941e-5,0.000596116131877433,0.0341027740091992,0.260656387045133,0.585000472607163,0.80800898797179,0.929152853778474,0.990808550264467,1.02199766371357,1.03759222043812,1.0453894988004]



    topn = [16384,8192,4096,2048,1024,512,256,128,64,32,16,8]


    # topn = 32
    # error_k_wave=
    # topn = [65536,32768,16384,8192,4096,2048,1024,512,256,128,64,32]
    relative_error_k_wave=[error_k_wave[i]/1.05318677716279*100 for i in range(len(error_k_wave))]
    relative_error_k_scale=[error_k_scale[i]/1.05318677716279*100 for i in range(len(error_k_wave))]

    pyplot.plot(topn,relative_error_k_wave,label="LLMW Wavelet")
    pyplot.plot(topn,relative_error_k_scale,label="LLMW scale")

    # pyplot.ylabel('Element value')
    # pyplot.plot(m,y_ideal,label="Ideal")
    # pyplot.plot(m,y_error,label="Error")
    pyplot.xlabel('Top n Element')
    pyplot.ylabel('Relative Error %')
    pyplot.legend( loc=2)
    pyplot.yscale('log')
    pyplot.xscale('log')
    pyplot.show()



    pyplot.plot(topn,relative_error_k_wave,label="LLMW Wavelet")
    # pyplot.plot(topn,relative_error_k_scale,label="Haar scale")

    # pyplot.ylabel('Element value')
    # pyplot.plot(m,y_ideal,label="Ideal")
    # pyplot.plot(m,y_error,label="Error")
    pyplot.xlabel('Top n Element')
    pyplot.ylabel('Relative Error %')
    pyplot.legend( loc=2)
    pyplot.yscale('log')
    pyplot.xscale('log')
    pyplot.show()



    # pyplot.plot(topn,relative_error_k_wave,label="Haar Wavelet")
    pyplot.plot(topn,relative_error_k_scale,label="LLMW scale")

    # pyplot.ylabel('Element value')
    # pyplot.plot(m,y_ideal,label="Ideal")
    # pyplot.plot(m,y_error,label="Error")
    pyplot.xlabel('Top n Element')
    pyplot.ylabel('Relative Error %')
    pyplot.legend( loc=2)
    pyplot.yscale('log')
    pyplot.xscale('log')
    pyplot.show()

def qlmw():

    error_k_scale = [3.73090198532804e-5,0.033435865306648,0.259883934714212,0.583614356130636,0.807165389354192,0.928708186091732,0.990763211913963,1.0219520255985,1.03756368422039,1.04537523069159,1.04928100392718,1.05123389054498]


    topn = [65536,32768,16384,8192,4096,2048,1024,512,256,128,64,32]
    # topn = 32
    error_k_wave=[3.73090198532962e-5,3.73343048112759e-5,3.77553961996367e-5,4.20150121885562e-5,6.85476335811478e-5,0.000183487249843989,0.000506725227785953,0.00129410653496159,0.00332986807738648,0.00817309582306631,0.0204637518497464,0.0489365158276707]
    # topn = [65536,32768,16384,8192,4096,2048,1024,512,256,128,64,32]
    relative_error_k_wave=[error_k_wave[i]/1.05318677716279*100 for i in range(len(error_k_wave))]
    relative_error_k_scale=[error_k_scale[i]/1.05318677716279*100 for i in range(len(error_k_wave))]

    pyplot.plot(topn,relative_error_k_wave,label="Haar Wavelet")
    pyplot.plot(topn,relative_error_k_scale,label="Haar scale")

    # pyplot.ylabel('Element value')
    # pyplot.plot(m,y_ideal,label="Ideal")
    # pyplot.plot(m,y_error,label="Error")
    pyplot.xlabel('Top n Element')
    pyplot.ylabel('Relative Error %')
    pyplot.legend( loc=2)
    pyplot.yscale('log')
    pyplot.xscale('log')
    pyplot.show()



    pyplot.plot(topn,relative_error_k_wave,label="Haar Wavelet")
    # pyplot.plot(topn,relative_error_k_scale,label="Haar scale")

    # pyplot.ylabel('Element value')
    # pyplot.plot(m,y_ideal,label="Ideal")
    # pyplot.plot(m,y_error,label="Error")
    pyplot.xlabel('Top n Element')
    pyplot.ylabel('Relative Error %')
    pyplot.legend( loc=2)
    pyplot.yscale('log')
    pyplot.xscale('log')
    pyplot.show()



    # pyplot.plot(topn,relative_error_k_wave,label="Haar Wavelet")
    pyplot.plot(topn,relative_error_k_scale,label="Haar scale")

    # pyplot.ylabel('Element value')
    # pyplot.plot(m,y_ideal,label="Ideal")
    # pyplot.plot(m,y_error,label="Error")
    pyplot.xlabel('Top n Element')
    pyplot.ylabel('Relative Error %')
    pyplot.legend( loc=2)
    pyplot.yscale('log')
    pyplot.xscale('log')
    pyplot.show()
llmw()