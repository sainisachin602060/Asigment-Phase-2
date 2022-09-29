def f1(n):
    if(n<=1):
        return n
    return f1(n-1)+f1(n-2)

for i in range(6):
    print(f1(i))