def gcd(a,b):
    d = 0
    while b>=1:
        d = b
        b = a%b
        a = d
    return a
print(gcd(6,7))
