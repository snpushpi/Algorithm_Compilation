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
def phi(n):
    '''Euler totient function'''
    result = n
    sqrt_n = int(math.sqrt(n))
    for i in range(2,sqrt_n+1):
        if n%i==0:
            while n%i==0:
                n = int(n/i)
            result = result - int(result/i)
    if n>1:
        result = result - result/n
    return result   
def bin_exp_mod(a,b,m):
    '''calculate a^b mod m'''
    a = a%m 
    res = 1 
    while b>0:
        if b%2==1:
            res = (res*a)%m
        a = (a*a)%m
        b = int(b/2)
    return res
def power_checker(g, power_list,n):
    '''parameters are g and power_list , for each power it checks whether g^pow is congruent to 1.
    returns bool var'''
    for pow in power_list:
        if bin_exp_mod(g,pow,n)==1:
            return False
    return True
def primitive_root(n):
    '''In mod arithmetic, a number g is called a primitive root of n if every coprime to 
    n is congrunet to a power of g modulo n.
    Structure -
    1. Factorize phi(n)
    1. For very number  in [1,n-1]:
     a. check whether g ^ (phi(n)/p_i)
     b. If all of them are different from n, return g'''
    prim_root_list = []
    phi_n = phi(n)
    prime_fact_dict = prime_factor(phi_n)
    power_list = []
    for prime in prime_fact_dict:
        power_list.append(int(phi_n/prime))
    for i in range(1,n):
        if power_checker(i, power_list, n):
            prim_root_list.append(i)
    return prim_root_list

