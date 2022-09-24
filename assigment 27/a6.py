class Calculator:
    def __init__(self):
        try:
            print("press 1 for additon")
            print("press 2 for subtraction")
            print("press 3 for multiply")
            print("press 4 for divide")
            self.n=int(input("enter your choice"))
            self.a=int(input("enter  a number"))
            self.b=int(input("enter b number"))
        
            
            match self.n:
                case 1:
                    print(self.a+self.b)
                
                case 2:
                    print(self.a-self.b)
                 
                case 3:
                    print(self.a*self.b) 
                
                case 4:
                    print(self.a/self.b)
                
                
        except ValueError:
           print("input must be integer only")
           
        except ZeroDivisionError:
            print("can not divde by 0")
            
        except ArithmeticError:
            print("unlegal operation ")
            
        except:
            print("something went wrong")
            
            
          
obj=Calculator()            
                        
           
                       
                
                    
            
               
            
      
            