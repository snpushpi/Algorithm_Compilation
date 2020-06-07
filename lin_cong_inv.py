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
def mod_inverse(a,m):
    '''returns a number x such that ax is congruent to 1 mod(m)'''
    x,y = ext_gcd(a,m)
    g = a*x+m*y
    if g!=1:
        return 'No Solution'
    else:
        x = (x%m+m)%m
        return x
def linear_congruence_inverse(a,b,n):
    '''Returns all x such less than n such that ax equals n mod b'''
    gcd = ext_gcd(a,n)
    if b%gcd!=0:
        return 'No Solution'
    else:
        a1 = int(a/gcd)
        n1 = int(n/gcd)
        b1 = int(b/gcd)
        a_inv = mod_inverse(a1,n1)
        x = ((a_inv*b1)%n1+n1)%n1
        list_num = []
        for i in range(gcd):
            list_num.append(x+i*n1)
            
        return list_num



