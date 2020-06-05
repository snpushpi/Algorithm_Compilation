def bin_pow(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    if b%2==0:
        o = int(b/2)
        return bin_pow(a,o)*bin_pow(a,o)
    else:
        o = int((b-1)/2)
        return bin_pow(a,o)*bin_pow(a,o)*a
print(bin_pow(6,7))