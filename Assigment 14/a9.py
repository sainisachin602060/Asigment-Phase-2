from xml.dom.minidom import Element


c1=[eval(e) for e in input("enter list element:").split(',')]
element=eval(input("enter element value"))
index=0
while(index<len(c1)):
    if(c1[index]==element):
        print(index,end=' ')
    index=index+1    