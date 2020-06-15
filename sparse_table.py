import math
def buildsparsetable(arr,n):
    '''We will build a lookup table where lookup[i][j] indicates the minimum number from
    i to i+2^j-1 in the array 'arr'''
    z = math.ceil(math.log(n,2))
    lookup = [[0 for i in range(z)] for j in range(n)]
    for i in range(n):
        lookup[i][0]=arr[i]
    for j in range(1,z):
        for i in range(n):
            if (i+1)+2**j-1<=n:
                lookup[i][j]= min(lookup[i][j-1],lookup[i+2**(j-1)][j-1])
    return lookup
print(buildsparsetable([7,2,3,0,5,10,3,12,18],9))
def query(L,R,n,arr):
    '''Two indices in a particular array whose sparse table have been made and now we will 
    just do query operation.'''
    lookup_table = buildsparsetable(arr,n)
    j = math.floor(math.log(R-L+1,2))
    return min(lookup_table[L][j],lookup_table[R-2**j+1][j])
print(query(4,6,9,[7,2,3,0,5,10,3,12,18]))