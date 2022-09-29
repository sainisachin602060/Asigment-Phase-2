def rec(n):     
    if n%10==0:
        return 0
    return rec(n//10)+n%10  



print(rec(156))