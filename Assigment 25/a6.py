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
        
        
c1=calculator()      
c1.addition()
c1.subtraction()  