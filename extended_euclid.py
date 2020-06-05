def ext_gcd(a,b):
    '''returns the numbers x, y suhc that ax+by=gcd(a,b)'''
    if b==0:
        x = 1
        y = 0
        return x,y
    x1, y1 = ext_gcd(b,a%b)
    x = y1
    y = x1- y1*int(a/b)
    return x,y
print(ext_gcd(12,3))
