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
def mod_inverse(a,m):
    '''returns a number x such that ax is congruent to 1 mod(m)'''
    x,y = ext_gcd(a,m)
    g = a*x+b*y
    if g!=1:
        returns 'No Solution'
    else:
        x = (x%m+m)%m
        returns x