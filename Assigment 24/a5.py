


class User:
    def __init__(self):
        self.name=input("enter your name")
        self.age=int(input("enter user age"))
        self.email=input("enter your email")
        
    def getData(self):
        print(self.name)
        print(self.email)
        print(self.age)
        del self.age
        
    def after(self):
        print("after delete")
        print(self.name)
        print(self.email)    
        
        
        
        
obj=User()
obj.getData() 
obj.after()   