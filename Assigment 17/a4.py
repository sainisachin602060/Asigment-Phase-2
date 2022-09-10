s1={"java","python","django","sql"}
flag=1
for i in s1:
    if(i=="python"):
        flag=0
        break
    flag=1        
         
if(flag==0):
    print("yes pythoni have")
else:
    print("not have")
    
