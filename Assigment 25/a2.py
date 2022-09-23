class profile:
    def __init__(self):
        self.name=input("enter your name")
        self.age=int(input("enter your age"))
        self.gmail=input("enter your gmail")
      
       
        
        
        
    def info(self):
        print(self.name,self.age,self.gmail,sep='\n')
        print(type(self.age))
        
            
        
p1=profile()        
p1.info()
        