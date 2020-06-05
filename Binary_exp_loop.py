def bin_exp_loop(a,b):
    '''This implementation is faster than recursive one'''
    res = 1
    while b>0:
        if b%2==1:
            res = res*a
        a = a*a
        b = int(b/2)
    return res
print(bin_exp_loop(6,6))