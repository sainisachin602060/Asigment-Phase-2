f=open("t1.text","w")
a="hello Django"
f.write(a)
print(f.mode)
print(f.name)
print(f.closed)

f.close()
