import math
import cmath
def nearest_2_exp(n):
    '''returns the exp of 2 nearest n and bigger than n'''
    Flag = True
    i=0
    while Flag:
        if 2**i<n:
            i+=1
        else:
            return 2**i
def zero_padder(m,n):
    '''For a list of length m, it returns a list of length n'''
    zero_list = [0 for i in range(n-len(m))]
    return m + zero_list

def inverse_discrete_fourier_transform(a_list):
    '''takes a list of n integers as input, so a_0,a_1,a_2,a_3..., a_n-1. If n is not a power of 2,
    we pad zeros to make the length of list equal to the nearest power of 2.This function returs y_0,y_1,y_2,y_3,
    y_n, or the polynomial evaluated at n points and these n points are n roots of unity.''' 
    if len(a_list)==1:
        return a_list
    exp2 = nearest_2_exp(len(a_list))
    modif_list = zero_padder(a_list,exp2)
    a_even_list = [modif_list[i] for i in range(0,exp2,2)]
    a_odd_list = [modif_list[i] for i in range(1,exp2,2)]
    half_n_unity_root_even_val = inverse_discrete_fourier_transform(a_even_list)
    half_n_unity_root_odd_val = inverse_discrete_fourier_transform(a_odd_list)
    result_list = [0 for i in range(exp2)]
    exponent = (2j*cmath.pi)/exp2
    for i in range(int(exp2/2)):
        frac = 1/cmath.exp(i*exponent)
        result_list[i]=(half_n_unity_root_odd_val[i]+frac*half_n_unity_root_even_val[i])
        result_list[i+int(exp2/2)]=(half_n_unity_root_odd_val[i]-frac*half_n_unity_root_even_val[i])
    new_r_list = [elt/exp2 for elt in result_list]
    return new_r_list

