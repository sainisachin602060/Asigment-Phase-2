x=int(input("enter a number"))
a=[]
while(x>1):
  
    a.append(x%8)
    x=x//8
a.reverse()
for i in a:
    print(i,end="")
  
