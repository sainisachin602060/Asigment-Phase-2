def ispangaram(str):
    alpha="abcdefghijklmnopqrstuvwxyz"
    for i in alpha:
        if i not in str.lower():
            return False
        
    return True


if(ispangaram("abcdef ghijklm opqr stuvwxyz")==True):
    print("yes")
    
else:
    print("no")       