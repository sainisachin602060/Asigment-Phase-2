def f1(s):
    u=0
    l=0
    for i in s:
        x=ord(i)
        if(x>=65 and x<=90):
            u=u+1
        elif(x>=97 and x<=122):
            
            l=l+1
    print("big character is ",u)
    print("small charcter is ",l)

