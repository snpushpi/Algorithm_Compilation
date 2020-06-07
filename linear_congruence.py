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

def lin_congruence(a,b,n):
    '''returns the solution of ax equals b mod n.
    We can treat this as an equation ax+ny=b and find 
    the solution.'''
    gcd = opt_gcd(a,n)
    if b%gcd!=0:
        return 'No Solution'
    else:
        a_1 = int(a/gcd)
        n_1 = int(n/gcd)
        b_1 = int(b/gcd)
        x_1,y_1 = ext_gcd(a_1,n_1)
        #a_1*x_1+n_1*y_1=1
        x_1b = (x_1*b_1)%n
    return x_1b
