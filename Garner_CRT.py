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
def chinese_rem_theorem(list1, list2):
    '''list1 is the list for As and list2 is the list for Ps.Assuming it has k co-prime numbers
    we can run this algo in O(k^2) complexity.'''
    #First we will make a dict of k(k-1)/2 elements, this keeps track of invesre stuff.
    r_dict = {}
    k = len(list1)
    for i in range(k):
        for j in range(i+1,k):
            r_dict[(i,j)]=mod_inverse(list2[i],list2[j])
    x_list = [0 for i in range(k)]
    for i in range(k):
        temp = list1[i]
        for j in range(i):#we will compute temp values here.
            subtract = temp-x_list[j]
            mult = subtract*r_dict[(j,i)]
            temp = mult
        x_list[i]= temp
    
    #Now the final solution a = x1 + x2p1 + x3p1p2 + x4p1p2p3 + ... + xkp1p2..pk-1
    a = 0
    for i in range(k):
        temp = x_list[i]
        for j in range(i):
            temp = temp*list2[j]

        a+=temp
    return a 




