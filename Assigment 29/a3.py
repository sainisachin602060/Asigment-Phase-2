try:
    f=open("myfile.txt","r")
    a=f.read()
    print(a)
    f.close()
    
except FileNotFoundError:
    print("file not fund me")    