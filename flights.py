def flights(st1,st2):
    print(" Due to Covid 19 situation date and time of flight may be differ")
    print(" International flights are cancel because of covid 19 situation") 
    
    if st1=="delhi" and st2=="mumbai":
        print("****************DELHI TO MUMBAI************************")
        print(" Indigo  6E-564 09:00 to 10:30  ₹ 5455")
        print("Air Asia i-5789 13:40 to 16:40 ₹ 6555")
        print("Vistara  uk-995 09:25 to 10:55  ₹ 6783")
    elif st1=="delhi" and st2=="lucknow":
        print("****************DELHI TO LUCKNOW************************")
        print("AirIndia AI-411 08:30 to 09:40 ₹ 2,905")
        print("Vistara  UK-641 13:45 to 15:20 ₹ 2,906")
        print("IndiGo   6E-5003 16:20 to 17:30 ₹ 3,116")
    elif st1=="mumbai" and st2=="delhi":
        print("****************MUMBAI TO DELHI************************") 
        print("GoAir G8-101 05:45 to 07:50 ₹ 3,956")
        print("AirAsia I5-548 05:25 to 07:50 ₹ 3,956")
        print("Spicejet SG-263 06:05 to 08:10 ₹ 4,112")
    elif st1=="lucknow" and st2=="delhi":
        print("****************LUCKNOWTO DELHI************************")
        print("AirIndia AI-411 08:30 to 09:40 ₹ 2,905")
        print("Vistara  UK-641 13:45 to 15:20 ₹ 2,906")
        print("IndiGo   6E-5003 16:20 to 17:30 ₹ 3,116")
    elif st1=="mumbai" and st2=="lucknow":
        print("****************MUMBAI TO LUCKNOW************************")
        print("Go Air G8-715 05:50 to 10:25 ₹ 3,295")
        print("Spicejet SG-295 06:05 to 07:30 ₹ 3,430")
        print("IndiGo 6E-2136  6E-2136 to 10:40 ₹ 3,430")
    elif st1=="lucknow" and st2=="mumbai":
        print("****************LUCKNOW TO MUMBAI************************")
        print("IndiGo 6E-2022 05:10 to 11:10 ₹ 4,448")
        print("IndiGo 6E-5034 06:15 to 13:50 ₹ 4,690")
        print("Go Air G8-715  07:15 to 1:10  ₹ 4,448")
    else:
        print("PLEASE ENTER CORRECT INFORMATION")
        










        
