from winreg import REG_NOTIFY_CHANGE_SECURITY


class text:
    def __init__(self):
        try:
            self.a=int(input("enter integer only")) #genrate exception
            self.b=0
            self.c=self.a/self.b    #genrate exception
            
            
        except ZeroDivisionError:
            print("cant dicide by zero")
            
        except ValueError:
            print("enter only integer")
            
            
        except ArithmeticError:
            print("not operation succees")
            
        except  Exception:
            print("Enter your right operation")       
            
            
obj=text()                     