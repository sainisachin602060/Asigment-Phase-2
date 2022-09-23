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
        
        
class calculator2(calculator):
    def divide(self):
        self.div=self.num1//self.num2
        print("divison is",self.div)
        

    def multi(self):
        self.mul=self.num1*self.num2
        print("multiply is",self.mul) 
        
        
        
        
        
c1=calculator2()        
c1.addition()
c1.subtraction()
c1.divide()
c1.multi()   
        
               