def odd(n):
    if(n==0):
        return 1
    odd(n-1)
    print(2*n-1)
