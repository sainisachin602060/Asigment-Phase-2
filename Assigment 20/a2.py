def f1(x):
    flag=0
    for i in range(2,x):
        if(x%i==0):
            flag=1
            print("value not prime")
            break

    else:
        print("value is prime")
          

            
