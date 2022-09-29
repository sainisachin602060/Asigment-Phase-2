import pickle

f1=open("bookfile","rb")
a=pickle.load(f1)
for i in a:
    print(i," ",a[i])
f1.close()    