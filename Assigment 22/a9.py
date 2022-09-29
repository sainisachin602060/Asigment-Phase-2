""""
def p_oct(n):
    if n==1:
        return oct(1)
    return oct(n)
print(p_oct(8))
"""



"""
def f1(n):
    a=0
    b=1
   
    i=0
    print(a)
    print(b)
    while(i<n-2):
        c=a+b
        print(c)
        
        a=b
        b=c
        i+=1
        
        
f1(20)  

"""
def f1(n):
    if(n<=1):
        return n
    return f1(n-1)+f1(n-2)

for i in range(6):
    print(f1(i))     