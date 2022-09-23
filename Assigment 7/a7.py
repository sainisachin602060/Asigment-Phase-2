x=int(input("enter  a number"))

match x:
    case x if x==0:
        print("value is zero")

    case x if x<0:
        print("negative")

    case x if x>0:
        print("positive")
        
    
      
