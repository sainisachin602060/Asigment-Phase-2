import pickle
     

l1=['Roorkee','Bhopal','Punjab','Delhi']
f1=open("fourth.txt","wb")
l1.append(['Laksar','Amratsar',',Mumbai'])
pickle.dump(l1,f1)
f1.close()

#startng method also


def searching(filename,word):
    for i in l1:
        if(i==word):
            return True
        else:
            return False
   
   


r=searching('fourth.txt',"Mumbai") 
print(r)
