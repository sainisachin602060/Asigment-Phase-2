from ast import match_case


class calculator:
    def __init__(self):
        try:
            self.a=int(input("enter  a number"))
            self.b=int(input("enter b number"))
          
        except ValueError:
            print("enter only integer")
               
            
        except Exception:
            print("plz enter right things")  
            
              
    def add(self):
        self.c=self.a+self.b  
        print("adddito is",self.c)
          
    def sub(self):
        self.c=self.a-self.b
        print("subtarction is",self.c)      
        

    def mul(self):
        self.c=self.a*self.b
        print("multiply is",self.c) 
    
            
        
        
    def div(self):
        try:
            self.c=self.a/self.b
         
        
        except ZeroDivisionError:
            print("zero se divide nhi ho skta")
        
       
        except Exception:
            print("there was a problem")  
            
            
        else:
            print(self.c) 
          
        finally:
            print("all  is good")       
        
 
   
            
   
    
obj=calculator()
obj.add()
obj.sub()
obj.mul() 
obj.div()

 
             
         
        
        
     
            
            
                    
      
        