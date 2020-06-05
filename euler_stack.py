def one_to_n_euler(n):
    '''returns the euler totient values of numbers from 1 to n'''
    phi = [i for i in range(n)]
    
    for i in range(2,n):
        if phi[i]==i:
            for j in range(i,n,i):
                phi[j]=phi[j] - phi[j]/i
    return phi
print(one_to_n_euler(24))