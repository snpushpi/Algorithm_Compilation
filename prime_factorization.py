import math
def e_prime(n):
    '''Finds all prime numbers smaller than n'''
    l_n = [0 for i in range(n)]
    l_n[0]=1
    for i in range(2,n):
        if l_n[i-1]==0:
            val = int(n/i)
            for j in range(2,val+1):
                l_n[i*j-1]=1
    prime_list = [i+1 for i in range(n) if l_n[i]==0]
    return prime_list
def prime_factor(n):
    '''return the prime factorization of n'''
    sqrt_n = int(math.sqrt(n))
    prime_list = e_prime(sqrt_n)
    i = 0
    prime_dict = {}
    while i<len(prime_list):
        if n%prime_list[i]==0:
            if prime_list[i] in prime_dict:
                prime_dict[prime_list[i]]+=1
            else:
                prime_dict[prime_list[i]]=1
            n = int(n/prime_list[i])
        else:
            i+=1
    return prime_dict

