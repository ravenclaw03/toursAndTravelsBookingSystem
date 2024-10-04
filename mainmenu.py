#mainmenu
import flights
import charter
import packages
import trains
import Hotels
import cabs
import exist
print("")
print("")
print(" "*27,"Welcome To"," "*25)
print("_"*20,"WORLD TOURS AND TRAVELS","_"*25)
print("")
print("")
print(" "*5,"'WE TRAVEL not to escape life BUT FOR LIFE not to escape us'"," "*5)
print("")
print("")
print('''
                       HERE ARE THE SERVICES WE PROVIDE:        
                                 1)Flights
                                 2)Trains
                                 3)Hotels
                                 4)Charters
                                 5)Cabs
                                 6)Packages
                         _____________________________''')
print("")
print("")
u=""
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="sqlconnect1224")
mycursor=mydb.cursor()
while True:
    u=input("Are you an Existing user Y/N ")
    if u=='Y' or u=='y':
        print("")
        print("-----------------------------LOGIN SCREEN-------------------------------")
        print("")
        logn=input("Enter userid ")
        psd=input("Enter password ")
        exist.exist(logn,psd)
        break      
    else:
        print("")
        print("-----------------------------SIGNUP SCREEN-------------------------------")
        print("")
        l=[]
        l1=[]
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
            pass
        else:
            mycursor.execute("create table customer(C_ID char(10) NOT NULL,password char(20),DateOfDeparture char(8),DateOfArrival char(8),FromDestination char(10),ToDestination char(10),Type char(10))")
        print("To create new account ")
        logn=input("Enter new login ID ")
        psd=input("Enter new password ")
        dte1=input("Enter journey date(DD/MM/YY) ")
        dte2=input("Enter return date(DD/MM/YY) ")
        ch=int(input("enter choice"))
        if ch==1:
            print('''
                         ------------------DESTINATION------------------------
                                              DELHI
                                              MUMBAI
                                              LUCKNOW
                         -----------------------------------------------------''')
            st1=input("Enter departure destination ")
            st2=input("Enter arrival destination ")
            ty="Flight"
            flights.flights(st1,st2)
        elif ch==2:
            print('''
                          Available Stations:   ______________________
                                                1)NEW DELHI - NDLS
                                                2)LUCKNOW NR - LKO
                                                3)MUMBAI CENTRAL - BCT
                                               _______________________''')
            st1=input("Enter departure destination code ")
            st2=input("Enter arrival destination code ")
            ty="Train"
            trains.trains(st1,st2)
        elif ch==3:
            print('''Available Locations:______________________
                                                1)NEW DELHI 
                                                2)LUCKNOW 
                                                3)MUMBAI 
                                                4)GOA
                                
                                            _______________________''')
            st1=input("Enter departure destination ")
            st2="-"
            ty="Hotel"
            Hotels.hotels(st1,st2)
        elif ch==4:
            print("---------------DESTINATION---------------------------")
            print("DELHI")
            print("MUMBAI")
            print("BENGALURU")
            print("-------------------------------------------------------")
            st1=input("Enter departure destination ")
            st2=input("Enter arrival destination ")
            ty="Charter"
            charter.charter(st1,st2)
        elif ch==6:
            print('''------------------DESTINATION------------------------
                               GOA
                               SHIMLA
                               KERALA
                               NEW DELHI
                    -----------------------------------------------------''')
            st1=input("Enter departure destination ")
            st2="-"
            ty="Package"
            packages.packages(st1,st2)
        elif ch==5:
            st1=input("Enter departure destination ")
            st2=input("Enter arrival destination ")
            ty="Cab"
            cabs.cabs(st1,st2)
        else:
            print("Not found")
        mycursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s)",(logn,psd,dte1,dte2,st1,st2,ty))
        mydb.commit()
        break
            
    


def show():
    mycursor.execute("select * from customer")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print(x)
def locate():
    user1=input("Enter user-id to be searched")
    mycursor.execute("select * from customer where C_ID=%s",(user1,))
    myrecords=mycursor.fetchall() 
    for x in myrecords:
        print(x)
def update():
    print("To update date")
    user1=input("Enter user-id to be updated")
    date1=input("enter new date of departure")
    date2=input("enter new date of arrival")
    mycursor.execute("update customer set DateOfDeparture=%s where C_ID=%s",(date1,user1))
    mydb.commit()
    mycursor.execute("update customer set DateOfArrival=%s where C_ID=%s",(date2,user1))
    mydb.commit()
    mycursor.execute("select * from customer where C_ID=%s",(user1,))
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print(x)
    print("UPDATED")
def delete():
    user1=input("Enter user-id to be deleted")
    mycursor.execute("delete from customer where C_ID=%s",(user1,))
    mydb.commit()
    print("DELETED")
print("")
print("")
print("FINAL INFORMATION:",end='')
mycursor.execute("use tourist")
mycursor.execute("select * from customer where C_ID=%s",(logn,))
myrecords=mycursor.fetchall() 
for x in myrecords:
    print(x)
print("")
print("")    
print("____________________THANK YOU FOR USING OUR SERVICES____________________")
print("")
print("For making any changes you can choose from the following options")
print('''
         _________________________________
         1.Update
         2.Search
         3.Show
         4.Delete
         5.Exit
         _________________________________''')

while True:
    a=int(input("enter choice"))
    if a==1:
     update()
    elif a==2:
     locate()
    elif a==3:
     show()
    elif a==4:
        delete()
    elif a==5:
        break
    conti=input("Do you want to choose another option?y/n")
    if conti=='n':
      break
print("")
print("")
print("Final information is")
print("LOGIN  PASSWORD DEPARTURE-DATE ARRIVAL-DATE DEPARTURE ARRIVAL TYPE")
mycursor.execute("select * from customer where C_ID=%s",(logn,))
myrecords=mycursor.fetchall()
for x in myrecords:
    print(x)
print("")
print("")
print("____________________THANK YOU FOR USING OUR SERVICES____________________")
print("WORLD TOURS AND TRAVELS BRINGS YOU THE BEST SERVICES AT AFFORDABLE COSTS")
print("___________DO VISIT AGAIN. FOR MORE QUERIES CONTACT:9812345670___________")
print("___________________________Copyright:2020________________________________")

