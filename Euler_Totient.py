import math
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
print(phi(49))