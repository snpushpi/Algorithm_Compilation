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
print(ext_gcd(12,3))


def find_all_linear_sols(a,b,c):
    '''This equation finds all linear solutions a*x+b*y=c'''
    g = opt_gcd(a,b)
    if c%g!=0:
        return 'No Solution'
    else:
        x_g, y_g = ext_gcd(a,b)
        x_0, y_0 = (x_g)*(c/g),y_g*(c/g)
        x = x_0 + k*(b/g)
        y = y_0 - k*(a/g) # value of k will be fized depending on the interveal we 
        #are looking for 


        
