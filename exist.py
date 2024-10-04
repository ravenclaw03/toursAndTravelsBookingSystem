import flights
import charter
import packages
import trains
import Hotels
import cabs
def exist(logn,psd):

    l=[]
    l1=[]
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="sqlconnect1224")
    mycursor=mydb.cursor()
    mycursor.execute("show databases")
    myrecords=mycursor.fetchall() 
    for x in myrecords:
        l.append(x)
    i=('tourist',)
    if i in l:
         mycursor.execute("use tourist")
    else:
        mycursor.execute("create database tourist")
        mycursor.execute("use tourist")
    mycursor.execute("show tables")
    myrecords=mycursor.fetchall() 
    for x1 in myrecords:
        l1.append(x1)
    cust=('customer',)
    if cust in l1:
        mycursor.execute("select * from customer where C_ID=%s and password=%s",(logn,psd,))
        myrecords=mycursor.fetchall() 
        for x in myrecords:
            print(x)
    else:
        mycursor.execute("create table customer(C_ID char(10) NOT NULL,password char(20),DateOfDeparture char(8),DateOfArrival char(8),FromDestination char(10),ToDestination char(10),Type char(10))")
      
    if myrecords==[]:
        print("Username not present or Password error")
        exit()
    else:
        pass
