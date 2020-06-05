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
print(e_prime(50))