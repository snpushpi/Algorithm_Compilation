def opt_gcd(a,b):
    '''This is an optimized version of gcd'''
    if a==b:
        return a
    if a==1 or b==1:
        return 1
    if a==0 or b==0:
        return 0
    if a%2==0:
        if b%2==0:
            return 2*opt_gcd(int(a/2),int(b/2))
        else:
            return opt_gcd(int(a/2),b)
    else:
        if b%2==0:
            return opt_gcd(a,int(b/2))
        else:
            if a>b:
                return opt_gcd(b,a-b)
            else:
                return opt_gcd(a,b-a)
print(opt_gcd(18,12))