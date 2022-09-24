from logging import exception


class x:
    def __init__(self):
        try:
            self.name=int(input("enter a number"))
            
            
        except ArithmeticError:
            print("enter a integer only")
            
        except ValueError:
            print("enter only integer")
         
       
            
        except exception:
            print(" integer only")
         
        else:
            print("good job")   
            
            
obj=x()                        
       