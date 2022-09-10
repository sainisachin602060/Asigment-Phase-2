x=int(input("Enter a number"))
y=int(input("Enter b number"))
z=int(input("Enter c number"))

if(x>=y and x>=z):
    print(x)

    
elif(y>=x and y>=z):
    print(y)

    
elif(x==y and y==z): 
    print("some data is same")

else:
    print(z)

