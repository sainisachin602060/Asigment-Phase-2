a=input()
b=input()

match (a,b):
    case (a,b) if a==b:
        print("identical string")

    case (a,b)if(a>b):
        print("{} come after {}".format(a,b))


     
    case (a,b)if(a<b):
        print("{} come after {}".format(b,a))
