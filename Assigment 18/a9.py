d1={101:"sachin",102:"aman,",105:"mohit"}
d2={108:"s",110:"a,",111:"c"}
#1st way
"""
d4=d1.copy()
d4.update(d2)

print(d4)

"""
#2nd ways
d3={**d1,**d2}
print(d3)
