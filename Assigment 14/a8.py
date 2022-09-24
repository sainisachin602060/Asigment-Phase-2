c1=eval(input("enter list"))
freq={}
for e in c1:
    if e in freq:
        freq[e]+=1
    else:
        freq[e]=1
        
print(freq)            