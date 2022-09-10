from datetime import datetime
x=datetime.today()
print(x)


y=x.strftime("%d-%m-%y and %I:%M:%p")
print(y)


y=x.strftime("%B %d %y")
print(y)
print()



y=x.strftime("%d/%b/%y")
print(y)
print()


y=x.strftime("%H:%M:%S")
print(y)
print()

y=x.strftime("%d:%m:%y")
print(y)
print()
