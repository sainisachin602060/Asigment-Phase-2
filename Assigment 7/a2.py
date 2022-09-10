print("1.Addiiton")
print("2.Substarction")
print("3.Multiply")
print("4.Divide")
print("5.exit()")
print("6.continue")


op=int(input("enter your choice"))
    
match op:
    case 1:
        a=int(input("enter a number "))
        b=int(input("enter  b number "))
        print(a+b)
            
    case 2:
        a=int(input("enter a number "))
        b=int(input("enter  b number "))
        print(a-b)

    case 3:
        a=int(input("enter a number "))
        b=int(input("enter  b number "))
        print(a*b)

    case 4:
        a=int(input("enter a number "))
        b=int(input("enter  b number "))
        print(a//b)

    case 5:
        exit()


    case _:
         print("enter correct operator")

