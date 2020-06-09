import Inverse_FFT
import FFT
def polynomial_multi(pol1, pol2):
    '''returns the multiplication of two polynomials, parameters are lists of co-efficients here.'''
    l1 = len(pol1)
    l2 = len(pol2)
    large = l1 if l1>l2 else l2
    exp2 = FFT.nearest_2_exp(large) 
    pol1_padded = FFT.zero_padder(pol1,2*exp2)
    pol2_padded = FFT.zero_padder(pol2,2*exp2)
    #we will now evaluate the polynomials at 2*exp2 values which is at least equal to the length of the multiplied poly
    DFT1 = FFT.discrete_fourier_transform(pol1_padded)
    DFT2 = FFT.discrete_fourier_transform(pol2_padded)
    DFT_mult_pol = [DFT1[i]*DFT2[i] for i in range(2*exp2)]
    #Now we will apply inverse fft here to get the co-efficients
    co_eff_list = Inverse_FFT.inverse_discrete_fourier_transform(DFT_mult_pol)
    return co_eff_list
print(polynomial_multi([1,3,5],[2,4]))
