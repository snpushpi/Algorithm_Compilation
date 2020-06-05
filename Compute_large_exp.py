def bin_exp_mod(a,b,m):
    '''calculate a^b mod m'''
    a = a%m 
    res = 1 
    while b>0:
        if b%2==1:
            res = (res*a)%m
        a = (a*a)%m
        b = int(b/2)
    return res
print(bin_exp_mod(6,7,100))