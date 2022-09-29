


class SmartPhone():
    def smart(self):
        print("its class smart also")
       
    def calling(self):
        print("calling to customer")    
        
    def extra_fe(self,t1):
        t1.fetchName(82789456125)
        
        
        
        
class Truecaller:
    def __init__(self):
        self.d1={8393919669:"sachin",68946826846:"mohan",4555:"amit",82789456125:"ajay"}
                
        
    def fetchName(self,no):
        x=self.d1[no]
        print(x)
        
    def add(self):
        a=int(input("enter key"))
        b=input("enter data")
        self.d1[a]=b
        for i in self.d1:
            print(i,self.d1[i])
        
          
        
        
        
t1=Truecaller()
s1=SmartPhone()   
s1.extra_fe(t1)
s1.calling()