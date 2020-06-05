def bin_exp_multiply(a,b,m):
    '''returns a*b mod m'''
    result = 0
    if a == 0:
        return 0
    if a%2==0:
        return bin_exp_multiply(int(a/2),b,m)
    if a%2==1:
        return bin_exp_multiply(int((a-1)/2),b,m)
