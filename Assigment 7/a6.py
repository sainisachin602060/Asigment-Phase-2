s=input("enter a string")

match s:
    case s if ' ' in s:
        print("its multiword")
    case s if ' ' not in s:
        print("not multiword")
