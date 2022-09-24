def nested_Try():
    try:
        x=int(inxput("enter a number"))
        y=int(input("enter b number"))
        if(x<=0):
            raise   ValueError()
        try:
            y=x//y
            if(y==0):
                raise ZeroDivisionError()
        
        except ZeroDivisionError:
            print("% zero nhi  hoga")
            
    except ValueError:
        print("input 0 nhi hoga")  
        
    else:
        print(y)    
        
nested_Try()              
           
       
            
            