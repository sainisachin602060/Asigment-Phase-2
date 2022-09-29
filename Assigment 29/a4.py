import pickle
l1=['Roorkee','Bhopal','Punjab','Delhi']
f1=open("fourth.txt","wb")
pickle.dump(l1,f1)
f1.close()