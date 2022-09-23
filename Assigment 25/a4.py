class profile:
    def __init__(self):
        self.name="sachin"
        self.gmail="gmail.com"
        self.age=20
     
      
    def info(self):
        print(self.name,self.gmail,self.age,sep='\n')
        
        
       
       
   
class varible:
    @classmethod  
    def class_methods(cls):
        print("hey i am class method")           
        
        
        
            
        
p1=profile()        
p1.info()
p2=varible()
varible.class_methods()

        