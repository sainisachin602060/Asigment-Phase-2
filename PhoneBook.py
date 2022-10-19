from ast import Import
from logging import exception
from multiprocessing import connection
from pickle import TRUE
from sqlite3 import Cursor, connect
from typing import final
from unittest import result
from urllib import response
from wsgiref.headers import Headers
import termtables as tt
import psycopg2

print("☎️ Contact  Appliaction ☎️")
print("")
print("")


#connection established
try:
    connection=psycopg2.connect(user="postgres",
                            password="sachin", 
                            host="localhost",
                            port="5432",
                            database="User"
                            )

    cursor=connection.cursor()
   
    
except Exception:
    print("Connection is not secure")
    
    
#we have established secure connection with database
    
    
#Registerd  
def regitration():
    print("")
    print("----------Registerd Here---------------")
    print(" ")
    print("") 
    
    Name=input("USERNAME---🔒 \t")
    print(" ")
    Pass=input("PASSWORD---🔒 \t")
    
    #exiting user check
    try:
        query="select count(*) from users where username=%s"
        query3=(Name,)
        cursor.execute(query,query3)
        result=cursor.fetchall()
        for i in result:
            tup=i
        for j in tup:
            Inte=j
           
        if( Inte>0):
            print("Already Exits❌ Please login✅")
            
        else:
            query1 = " INSERT INTO users VALUES (%s,%s)"
            query2 = (Name,Pass)
            cursor.execute(query1,query2)
            connection.commit()
            print("")
            print("you have to registartion Sucessfull !✅")
            print("")
            input("Do You Want to Login Press ENTER \t")
            login()
            cursor.close()
            connection.close()
                    
    except Exception: 
        print("Your Login first time")  
        input("Continue to press ENTER")
        Menu() 
        
        
#we have suceesfull registration done
def login():
    
    list1=[]
    list2=[]
    count=0
    print(" ")
    User=input("USERNAME--🔒  \t")
    print(" ")
    Pass=input("PASSWORD--🔒 \t")
    tupl=(User,Pass)
   
    query1="select * from users"
    cursor.execute(query1)
    final=cursor.fetchall()
    if(final==[]):
        print("Please Registerd First❌")
        regitration()
    for data in final:
        if(data==tupl):
            count=1
            break
        else:
            count=0
                
             
        
    if(count==0):
        print("username and password incorrect") 
        print("")
        print("Enter right username and password")
        login()
    else:
       
        Menu()
        
        
def Menu():
    print(" \n ""***WELCOME TO  📞 PHONEBOOK APPLICATION 2022** """)
    print("")
    print("🔓  [USER SACHIN 🚹 is Logged in]  🔓")
    print("")
    print(" ")
    print("[add]          | to  Add a New Contact")
    print("")
    print("")
    print("[del]          | Delete a Contact")
    print("")
    print("")
    print("[update]       | Update a contact")
    print("")
    print("")
    print("[view]         | View all Contact")
    print("")
    print("")
    print("[view -a]      | view a specific contact")
    print("")
    print("")
    print("[del all]     | delete all contact")
    print("")
    print("")
    response=input("What Do You Want--------- \t")
   
     
    if(response=="add"):
        add()
    elif(response=="del"):
        delete()
           
    
    elif(response=="update"):
        upd()
        
        
        
    elif(response=="view"):
        view()
        
        
    elif(response=="view -a"):
        viewAS()
        
        
    elif(response=="del all"):
        deleteAS()
        
    else:
        print("Enter Valid Statment❌") 
        print("")
        input("Continue to press ENTER")
        Menu()   
        
        
        
       #New Add Methd Is Here 
def add():
    item=[]
    Name=input("Name------\t")
    print(" ")
    print(" ")
    Fullname=input("FullName------\t")
    print("") 
    print(" ")
    Mobile=int(input("Mobile------\t"))
    print("")
    print(" ")
    Email=input("Email------\t")
    print("")
    print(" ")
    id=int(input("ID-------\t"))
    try:
       query1="INSERT INTO list VALUES (%s,%s,%s,%s,%s)"
       query2=(Name,Fullname,Mobile,Email,id)
       cursor.execute(query1,query2)
       connection.commit()
       print("")
       print("Contact has been saved!✅")
       input("Continue to press ENTER")
       Menu()
       cursor.close()
       connection.close()
       
    except Exception:
       print("You Got an Error.Contact Not be Saved❌")   
       input("Continue to press ENTER")
       Menu()
            
        
def view():
    try:
        cursor.execute("select * from list ")
        headers = ["Name", "FullName", "Mobile","Email","Id"]
        result=cursor.fetchall() 
        if result==[]:
            print("Contact List Empty❗")
            input("Continue to press ENTER")
            Menu()
        tt.print(result, header = headers)
        print("")
        input("Continue to press ENTER")
        Menu()
       
    except Exception:
        print("Not Visible Retry")
        print("")
        input("Continue to press ENTER")
        Menu()

    cursor.close()
    connection.close()
    
    
    
    ## delete method is here   
def delete():
    print("")
    Name=input("Which Contact You Want To Delete----- \t")
    query1="delete from list where name=%s"
    query2=(Name,)
    try:
        cursor.execute(query1,query2)
        connection.commit()
        print("Contact Has been Deleted✅")
        print("")
        input("Continue to press ENTER")
        Menu()
        print("Name is not find")  
        input("Continue to press ENTER")
        Menu() 
            
    except Exception:
        print("Not Found❌")
        input("Continue to press ENTER")
        Menu()
    cursor.close()
    connection.close()

#delete specific method is here
def deleteAS():
    try:
        cursor.execute("delete from list")
        connection.commit()
        print("All Contact Has been Deleted✅")
        input("Continue to press ENTER")
        Menu()
    except Exception:
        print("contact not deleted❌")
        input("Continue to press ENTER")
        Menu()
        print("")
   
    cursor.close()
    connection.close()
    
#view method is here
def viewAS():
    print("")
    
    Name=input("Which Contact You Want To View---- \t")
    query1="select name,fullname,mobile,email,contact_id from list where name=%s"
    query2=(Name,)
    
    try:
        cursor.execute(query1,query2)
        headers = ["Name", "FullName", "Mobile","Email","id"]
    
        result=cursor.fetchall()
        
        if(result==[]):
            print("❓CONTACT NOT FOUND❓")
            input("Continue to press ENTER")
            Menu()
            
        else:
            tt.print(result, header = headers)
            input("Continue to press ENTER")
            Menu()
    except Exception:
        print("Not Found")
        input("Continue to press ENTER")
        Menu()    
    
    cursor.close()
    connection.close()
        
    
#update method is here
def update():
    try:
        print("1. |    Name")
        print("")
        print("2. |    FullName")
        print("")
        print("3. |    Mobile")
        print("")
        print("4. |    Email")  
        print("")
        Choice=int(input("Which Property U Want Update--- \t"))
        
        if(Choice==1):
            name()
        elif(Choice==2):
            Full()
            print('')
            
    
        elif(Choice==3):
            Mobile()
          
        
        elif(Choice==4):
            Email()
            print("email")     
    
        else:
            print("Invalid Input")
            input("Continue to press ENTER")
            Menu()
             
            
    except Exception:
        print("Enter Valid Statement") 
        input("Continue to press ENTER")
        Menu()   
        
        
def upd():
    
    try:
        Name=input("Enter name to view u want to update")
        squery="select * from list where name=%s"
        qr=(Name,)
        cursor.execute(squery,qr)
        print("")   
        headers = ["Name", "FullName", "Mobile","Email","id"]
        result=cursor.fetchall()
        if result==[]:
            print("Empty List❌")
        tt.print(result, header = headers)
        print("")
        
    except Exception:
        print("Name Not Found")    
    
    update()
    

def name(): 
    try:
        query4="select * from list"
        cursor.execute(query4,)
        result2=cursor.fetchall()
        Name=input("Enter New Upadted Name--- \t")
        print("")
        id=int(input("Enter Id NO"))
        query1="update list set name=%s where contact_id=%s"
        query2=(Name,id)
        cursor.execute(query1,query2)
        connection.commit()
        query3="select * from list"
        cursor.execute(query3,)
        result1=cursor.fetchall()
        if(result2==result1):
            print("")
            print("Name is sucessfully not Updated❌ ")
            print("")
        else:
            print(" Update sucessfull✅")
                
        input("Continue to press ENTER")
        Menu()
        cursor.close() 
        connection.close()
        
    except Exception:
        print("Some Issue Name Not Updated.❗  Retry") 
        input("Continue to press ENTER")
        Menu()  
  
  
def Full(): 
    try:
        query4="select * from list"
        cursor.execute(query4,)
        result2=cursor.fetchall()
        Name=input("Enter New Full Name--- \t")
        print("")
        id=int(input("Enter Id NO"))
        query1="update list set fullname=%s where contact_id=%s"
        query2=(Name,id)
        cursor.execute(query1,query2)
        connection.commit()
        query3="select * from list"
        cursor.execute(query3,)
        result1=cursor.fetchall()
        if(result2==result1):
            print("")
            print("FUllName is sucessfully not Updated❌ ")
            print("")
        else:
            print(" Update sucessfull✅")
                
        input("Continue to press ENTER")
        Menu()
        cursor.close() 
        connection.close()
        
    except Exception:
        print("Some Issue Name Not Updated.❗  Retry") 
        input("Continue to press ENTER")
        Menu() 
        
def Mobile(): 
    try:
         
        query4="select * from list"
        cursor.execute(query4,)
        result2=cursor.fetchall()
        mobile=input("Enter New Upadted mobile--- \t")
        print("")
        id=int(input("Enter Id NO"))
        query1="update list set mobile=%s where contact_id=%s"
        query2=(mobile,id)
        cursor.execute(query1,query2)
        connection.commit()
        query3="select * from list"
        cursor.execute(query3,)
        result1=cursor.fetchall()
        if(result2==result1):
            print("")
            print("mobile is sucessfully not Updated❌ ")
            print("")
        else:
            print(" mobile update sucessfull✅")
                
        input("Continue to press ENTER")
        Menu()
        cursor.close() 
        connection.close()
        
    except Exception:
        print("Some Issue Name Not Updated.❗  Retry") 
        input("Continue to press ENTER")
        Menu()  
  
def Email(): 
    try:
         
        query4="select * from list"
        cursor.execute(query4,)
        result2=cursor.fetchall()
        Name=input("Enter New Upadted Email--- \t")
        print("")
        id=int(input("Enter Id NO"))
        query1="update list set email=%s where contact_id=%s"
        query2=(Name,id)
        cursor.execute(query1,query2)
        connection.commit()
        query3="select * from list"
        cursor.execute(query3,)
        result1=cursor.fetchall()
        if(result2==result1):
            print("")
            print("email is  not sucessfully  Updated❌ ")
            print("")
        else:
            print(" email Update sucessfull✅")
                
        input("Continue to press ENTER")
        Menu()
        cursor.close() 
        connection.close()
        
    except Exception:
        print("Some Issue Name Not Updated.❗  Retry") 
        input("Continue to press ENTER")
        Menu()  
  #STARTING YOUR PROGRAM HERE   
    
def option():
    print("1. New User Registration")
    print("")
    print("2. Login")
    print("")
   
    try:
        op=int(input("What Do You Want \t"))
        if(op==1):
            regitration()
        
        elif(op==2):
            login()
        
        else:
            print("Enter valid statement")       
    except Exception:
        print("Choosen Only   1️⃣   or    2️⃣   ") 
        option()  
        
        
option()        
        
        
        
         
           
        








































































































































