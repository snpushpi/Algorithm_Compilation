def mat_mul(M_1,M_2):
    '''They are two nested lists. Considering them as matrixes, we find their multiplications.'''
    M = [[0,0],[0,0]]
    M[0][0]= M_1[0][0]*M_2[0][0]+M_1[0][1]*M_2[1][0]
    M[0][1]= M_1[0][0]*M_2[0][1]+M_1[0][1]*M_2[1][1]
    M[1][0] = M_1[1][0]*M_2[0][0]+M_1[1][1]*M_2[1][0]
    M[1][1] = M_1[1][0]*M_2[0][1]+M_1[1][1]*M_2[1][1]
    return M 
def mat_pow(n,P):
    '''raises a matrix to nth power'''
    result = [[1,0],[0,1]]
    while n>0:
        if n%1==2:
            result = mat_mul(result,P)
        P = mat_mul(P,P)
        n = int(n/2)
    return result 
def fib_n(n):
    '''returns n and n+1 th fibonacci number'''
    P = [[0,1],[1,1]]
    p_n = mat_pow(n, P)
    F_n = p_n[1][0]
    return F_n

