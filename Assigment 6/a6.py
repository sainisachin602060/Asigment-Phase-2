"""
x=int(input())
count=0

while(x>0):
    digit=x%10
    x=x//10
    count=count+1

if(count==3):
    print("number is three digit")
else:
    print("number is not three digit")
"""


#simple way
x=int(input())
if(99<x<1000):
    print("three digit")

else:
    print("not three digit")
    
