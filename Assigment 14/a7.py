"""
a=["sachhin",True,101,4.5,89]

b=[i for i in a if(type(i)==int)]
       
        
print(b)
"""

#2nd way"

a=["True",12,2.3,11,"my name",59,11.1]
b=[]
for x in a:
   if(type(x)==int):
         b.append(x)
   
print(b)   
   
