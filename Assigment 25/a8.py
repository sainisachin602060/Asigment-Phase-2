class calculator:
    def __init__(self):
        self.num1=int(input("enter num 1"))
        self.num2=int(input("enter num 2"))
       
       
    def addition(self):
        self.sum=self.num1+self.num2
        print("addition is",self.sum)
        
    
    def subtraction(self):
        self.sum=self.num1-self.num2
        print("subtraction is",self.sum)
        
        
        
class Phone:
    def calling(self):
        print("callig to customer.....")
        
    def sms(self):
        print("sms to customer send")  
         
        


class SmartPhone(calculator,Phone):
    def smart(self):
        print("its class smart also")
        
    
    
s1=SmartPhone()        
s1.addition()
s1.subtraction()
s1.calling()
s1.sms()
s1.smart()  