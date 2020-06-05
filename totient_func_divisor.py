def eu_totient_div(n):
    '''This uses the idea that the the sumphi(d)=n where d|n'''
    phi = [i-1 for i in range(n)]
    phi[0]=0
    phi[1]=1
    for i in range(2,n+1):
        for j in range(2*i,n,i):
            phi[j]=phi[j]-phi[i]
    return phi
print(eu_totient_div(20))
