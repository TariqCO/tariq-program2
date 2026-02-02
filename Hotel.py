print("======== Hotel Booking Management ========\n")


WEEKEND_CHARGE = 20
FESTIVAL_CHARGE = 50
LOYALTY_DISCOUNT = 10


name = input("Enter your name: ")
print("\n=============================================")
email = input("Enter your email: ")
print("\n=============================================")
number = input("Enter your contact number: ")
print("\n=============================================")


durInNum = int(input("How many days do you want to stay? "))
print("\n=============================================")
guest = input("Number of guests between (1 - 4): ")
print("\n=============================================")
amenities = input("Enter amenities (Pool,Gym,Spa): ")
print("\n=============================================")
loyal = int(input("Are you a loyalty member? \n1. Yes \n2. No: \n\n --> |  "))
print("\n=============================================")


roomTyp = int(input("Select Room Types \n1. Standard \n2. Deluxe \n3. Suit \n\n --> | "))


if roomTyp == 1:
    room_name = "Standard"
    pricePerNight = 17000
    total_amt = durInNum * pricePerNight

    season = int(input("Enter Season \n1. Peak \n2. Off-peak \n3. Festival \n\n --> | "))

    if season == 1:         # Peak
        weekend_charge = (WEEKEND_CHARGE / 100) * total_amt
        subtotal = total_amt + weekend_charge

        print("\n =============================================")
        print("          BOOKING SUMMARY")
        print(" =============================================")
        print(f"Guest Name          : {name}")
        print(f"Contact             : {number}")
        print(f"Email               : {email}")
        print(f"Nights              : {durInNum}")
        print(f"Guests              : {guest}")
        print(f"Amenities           : {amenities}")
        print(f"Room Type           : {room_name}")
        print(f"Price per night     : {pricePerNight} Rs")
        print(" =============================================")
        print(f"Amount         : {total_amt} Rs")
        print(f"Weekend Charge   : {weekend_charge} Rs")
        print(" =============================================")
        if loyal == 1:
            print(f"Loyalty Discount    : {LOYALTY_DISCOUNT}%")
            total_af_dis = (LOYALTY_DISCOUNT / 100) * subtotal
            final_amount = subtotal - total_af_dis
            print(f"---------------------------------------------")
            print(f"Final Payable       : {final_amount} Rs")
        else:
            final_amount = subtotal
            print(f"Final Payable       : {final_amount} Rs")
        
        print(f"---------------------------------------------")
        print("Thank you for choosing us!\n")        
    elif season == 2:       # Off-peak
        weekend_charge = 0
        subtotal = total_amt

        print("\n =============================================")
        print("          BOOKING SUMMARY")
        print(" =============================================")
        print(f"Guest Name          : {name}")
        print(f"Contact             : {number}")
        print(f"Email               : {email}")
        print(f"Nights              : {durInNum}")
        print(f"Guests              : {guest}")
        print(f"Amenities           : {amenities}")
        print(f"Room Type           : {room_name}")
        print(f"Price per night     : {pricePerNight} Rs")
        print(" =============================================")
        print(f"Amount : {total_amt} Rs")
        print(f"Weekend Charge   : {weekend_charge} Rs")
        print(" =============================================")
        if loyal == 1:
            print(f"Loyalty Discount    : {LOYALTY_DISCOUNT}%")
            total_af_dis = (LOYALTY_DISCOUNT / 100) * subtotal
            final_amount = subtotal - total_af_dis
            print(f"-------------------------------------------------")
            print(f"Final Payable       : {final_amount} Rs")
        else:
            final_amount = subtotal
            print(f"Final Payable       : {final_amount} Rs")
        
        print("===============================================")
        print("Thank you for choosing us!\n")    
    elif season == 3:       # Festival
        festival_charge = (FESTIVAL_CHARGE / 100) * total_amt
        subtotal = total_amt + festival_charge

        print("\n ==========================================")
        print("          BOOKING SUMMARY")
        print("==========================================")
        print(f"Guest Name          : {name}")
        print(f"Contact             : {number}")
        print(f"Email               : {email}")
        print(f"Nights              : {durInNum}")
        print(f"Guests              : {guest}")
        print(f"Amenities           : {amenities}")
        print(f"Room Type           : {room_name}")
        print(f"Price per night     : {pricePerNight} Rs")

        print(f"Amount         : {total_amt} Rs")
        print(f"Festival Charge   : {festival_charge} Rs")

        if loyal == 1:
            print(f"Loyalty Discount    : {LOYALTY_DISCOUNT}%")
            total_af_dis = (LOYALTY_DISCOUNT / 100) * subtotal
            final_amount = subtotal - total_af_dis
            print(f"------------------------------------------")
            print(f"Final Payable       : {final_amount} Rs")
        else:
            final_amount = subtotal
            print(f"Final Payable       : {final_amount} Rs")
        
        print("===============================================")
        print("Thank you for choosing us!\n")   
    else:
        print("Invalid season selected!")
       

elif roomTyp == 2:
    room_name = "Deluxe"
    pricePerNight = 21500
    total_amt = durInNum * pricePerNight

    season = int(input("Enter Season \n1. Peak \n2. Off-peak \n3. Festival \n\n --> | "))

    if season == 1:
        weekend_charge = (WEEKEND_CHARGE / 100) * total_amt
        subtotal = total_amt + weekend_charge

        print("\n ==========================================")
        print("          BOOKING SUMMARY")
        print("==========================================")
        print(f"Guest Name          : {name}")
        print(f"Contact             : {number}")
        print(f"Email               : {email}")
        print(f"Nights              : {durInNum}")
        print(f"Guests              : {guest}")
        print(f"Amenities           : {amenities}")
        print(f"Room Type           : {room_name}")
        print(f"Price per night     : {pricePerNight} Rs")

        print(f"Amount         : {total_amt} Rs")
        print(f"Weekend Charge   : {weekend_charge} Rs")

        if loyal == 1:
            print(f"Loyalty Discount    : {LOYALTY_DISCOUNT}%")
            total_af_dis = (LOYALTY_DISCOUNT / 100) * subtotal
            final_amount = subtotal - total_af_dis
            print(f"--------------------------------------------------")
            print(f"Final Payable       : {final_amount} Rs")
        else:
            final_amount = subtotal
            print(f"Final Payable       : {final_amount} Rs")
        
        print("===============================================")
        print("Thank you for choosing us!\n")        
    elif season == 2:
        weekend_charge = 0
        subtotal = total_amt

        print("\n ==========================================")
        print("          BOOKING SUMMARY")
        print("==========================================")
        print(f"Guest Name          : {name}")
        print(f"Contact             : {number}")
        print(f"Email               : {email}")
        print(f"Nights              : {durInNum}")
        print(f"Guests              : {guest}")
        print(f"Amenities           : {amenities}")
        print(f"Room Type           : {room_name}")
        print(f"Price per night     : {pricePerNight} Rs")

        print(f"Amount         : {total_amt} Rs")
        print(f"Weekend Charge   : {weekend_charge} Rs")

        if loyal == 1:
            print(f"Loyalty Discount    : {LOYALTY_DISCOUNT}%")
            total_af_dis = (LOYALTY_DISCOUNT / 100) * subtotal
            final_amount = subtotal - total_af_dis
            print(f"--------------------------------------------------")
            print(f"Final Payable       : {final_amount} Rs")
        else:
            final_amount = subtotal
            print(f"Final Payable       : {final_amount} Rs")
        
        print("===============================================")
        print("Thank you for choosing us!\n")   
    elif season == 3:
        festival_charge = (FESTIVAL_CHARGE / 100) * total_amt
        subtotal = total_amt + festival_charge

        print("\n ==========================================")
        print("          BOOKING SUMMARY")
        print("==========================================")
        print(f"Guest Name          : {name}")
        print(f"Contact             : {number}")
        print(f"Email               : {email}")
        print(f"Nights              : {durInNum}")
        print(f"Guests              : {guest}")
        print(f"Amenities           : {amenities}")
        print(f"Room Type           : {room_name}")
        print(f"Price per night     : {pricePerNight} Rs")

        print(f"Amount         : {total_amt} Rs")
        print(f"Festival Charge   : {festival_charge} Rs")

        if loyal == 1:
            print(f"Loyalty Discount    : {LOYALTY_DISCOUNT}%")
            total_af_dis = (LOYALTY_DISCOUNT / 100) * subtotal
            final_amount = subtotal - total_af_dis
            print(f"--------------------------------------------------")
            print(f"Final Payable       : {final_amount} Rs")
        else:
            final_amount = subtotal
            print(f"Final Payable       : {final_amount} Rs")
        
        print("===============================================")
        print("Thank you for choosing us!\n")   
    else:
        print("Invalid season selected!")


elif roomTyp == 3:
    room_name = "Suite"
    pricePerNight = 32000
    total_amt = durInNum * pricePerNight

    season = int(input("Enter Season \n1. Peak \n2. Off-peak \n3. Festival \n\n --> | "))

    if season == 1:
        weekend_charge = (WEEKEND_CHARGE / 100) * total_amt
        subtotal = total_amt + weekend_charge

        print("\n ==========================================")
        print("          BOOKING SUMMARY")
        print("==========================================")
        print(f"Guest Name          : {name}")
        print(f"Contact             : {number}")
        print(f"Email               : {email}")
        print(f"Nights              : {durInNum}")
        print(f"Guests              : {guest}")
        print(f"Amenities           : {amenities}")
        print(f"Room Type           : {room_name}")
        print(f"Price per night     : {pricePerNight} Rs")

        print(f"Amount         : {total_amt} Rs")
        print(f"Weekend Charge   : {weekend_charge} Rs")

        if loyal == 1:
            print(f"Loyalty Discount    : {LOYALTY_DISCOUNT}%")
            total_af_dis = (LOYALTY_DISCOUNT / 100) * subtotal
            final_amount = subtotal - total_af_dis
            print(f"--------------------------------------------------")
            print(f"Final Payable       : {final_amount} Rs")
        else:
            final_amount = subtotal
            print(f"Final Payable       : {final_amount} Rs")
        
        print("===============================================")
        print("Thank you for choosing us!\n")   
    elif season == 2:
        weekend_charge = 0
        subtotal = total_amt

        print("\n ==========================================")
        print("          BOOKING SUMMARY")
        print("==========================================")
        print(f"Guest Name          : {name}")
        print(f"Contact             : {number}")
        print(f"Email               : {email}")
        print(f"Nights              : {durInNum}")
        print(f"Guests              : {guest}")
        print(f"Amenities           : {amenities}")
        print(f"Room Type           : {room_name}")
        print(f"Price per night     : {pricePerNight} Rs")

        print(f"Amount         : {total_amt} Rs")
        print(f"Weekend Charge   : {weekend_charge} Rs")

        if loyal == 1:
            print(f"Loyalty Discount    : {LOYALTY_DISCOUNT}%")
            total_af_dis = (LOYALTY_DISCOUNT / 100) * subtotal
            final_amount = subtotal - total_af_dis
            print(f"--------------------------------------------------")
            print(f"Final Payable       : {final_amount} Rs")
        else:
            final_amount = subtotal
            print(f"Final Payable       : {final_amount} Rs")
        
        print("===============================================")
        print("Thank you for choosing us!\n")   
    elif season == 3:
        festival_charge = (FESTIVAL_CHARGE / 100) * total_amt
        subtotal = total_amt + festival_charge
        print("\n ==========================================")
        print("          BOOKING SUMMARY")
        print("==========================================")
        print(f"Guest Name          : {name}")
        print(f"Contact             : {number}")
        print(f"Email               : {email}")
        print(f"Nights              : {durInNum}")
        print(f"Guests              : {guest}")
        print(f"Amenities           : {amenities}")
        print(f"Room Type           : {room_name}")
        print(f"Price per night     : {pricePerNight} Rs")

        print(f"Amount         : {total_amt} Rs")
        print(f"Festival Charge   : {festival_charge} Rs")

        if loyal == 1:
            print(f"Loyalty Discount    : {LOYALTY_DISCOUNT}%")
            total_af_dis = (LOYALTY_DISCOUNT / 100) * subtotal
            final_amount = subtotal - total_af_dis
            print(f"--------------------------------------------------")
            print(f"Final Payable       : {final_amount} Rs")
        else:
            final_amount = subtotal
            print(f"Final Payable       : {final_amount} Rs")
        
        print("===============================================")
        print("Thank you for choosing us!\n")   
    else:
        print("Invalid season selected!")

else:
    print("Invalid Room Type selected!")



