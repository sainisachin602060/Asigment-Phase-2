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
t1.fetchName(8393919669)
t1.add()

        
        
            