def valueEroor():
    try:
        x=int(input("enter a number"))
        if(x<=0):
            raise valueEroor()
        
        
    except ValueError:
        print("only integer hogi ")    
        
    except Exception:
        print("kuch to gadbad hai") 
    else:
        print(x)    
        
valueEroor()          