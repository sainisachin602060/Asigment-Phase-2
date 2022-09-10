x=int(input("enter a number"))
sum=0
while(x>0):
    digit=x%10
    x=x//10
    sum=sum+digit

print(sum)    
