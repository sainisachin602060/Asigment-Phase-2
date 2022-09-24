class x:
    def __init__(self):
        try:
            self.a=int(input("enter a number"))
            self.b=int(input("enter b number"))
            
            self.c=self.a/self.b
            
        except ZeroDivisionError:
            print("zero se divide nhi ho skta") 
            
        except ValueError:
            print("value int se alag nhi ho skti") 
            
        except Exception:
            print("kuch to gadbad hai")
        
        else:
            print(self.c)  
            
obj=x()
                            