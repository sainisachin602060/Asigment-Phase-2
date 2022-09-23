class profile:
    def __init__(self):
        self.name=input("enter your name")
        self.gmail=input("enter your gmail")
        self.age=int(input("enter your age"))
     
      
       
        
        
        
    def info(self):
        print(self.name,self.gmail,self.age,sep='\n')
        print(type(self.age))
        
            
        
p1=profile()        
p1.info()
        