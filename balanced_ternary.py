def dec_to_ternary(n):
    ''' Normal Number -> Normal Ternary'''
    string = ''
    while n>1:
        r = n%3
        string += str(r)
        n = int(n/3)
    return string[::-1]
def balanced_ternary(n):
    '''Normal Number -> Normal Ternary -> Balanced Ternary'''
    Flag = False
    new_string = ''
    normal_ternary = dec_to_ternary(n)
    l = len(normal_ternary)
    for i in range(l,0,-1):
        if normal_ternary[i-1]=='0':
            new_string+='0'
        elif normal_ternary[i-1]=='1':
            new_string+='1'
        elif normal_ternary[i-1]=='2':
            print('hi')
            new_string+='Z'
            normal_ternary = normal_ternary[:i-2]+str(int(normal_ternary[i-2])+1)+ normal_ternary[i-1:]
        elif normal_ternary[i-1]=='3':
            new_string+= '0'
            normal_ternary = normal_ternary[:i-2]+str(int(normal_ternary[i-2])+1)+ normal_ternary[i-1:]
            if i-1==0:
                Flag = True
    if Flag == True:
        new_string+='1'
    return new_string[::-1]



