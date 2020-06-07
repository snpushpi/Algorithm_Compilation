def factorial_mod_p(n,p):
    '''returns f(n!)%p when f(x) is a function which gives the value we get after diving itby the largest power of p it can be divided by'''
    result = 1
    while n>1:
        if int(n/p)%2!=0:
            result = (result*(p-1))%p
        val = n%p+1
        for i in range(1,val):
            result = (result*i)%p
        n = int(n/p)
    return result%p
    