def f1(n):
    if(n==1):
        return 1
    
    return n*f1(n-1)


print(f1(2))