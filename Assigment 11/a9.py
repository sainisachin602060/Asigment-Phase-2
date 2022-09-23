x=int(input("enter a nuber"))
a=[]
while(x>=1):
   
      a.append(x%2)
      x=x//2

a.reverse()
for i in a:
      print(i,end="")
      
