class er:
    def __init__(self):
        self.a=int(input("enter a number"))
        self.b=int(input("enter b number"))
     
        try:
            if(self.b<=0):
                raise ArithmeticError()
            
        except ArithmeticError :
            print("value is not right") 
           
               
            
        except Exception:    
            print("value not good")  
            
            
            
obj=er()               
        

            