print("_~_~_~_~_~_~ Resturant Ordering System _~_~_~_~_~_~\n\n")




name=input("Enter Your Name \n\n --> | ")
portionSize=int(input("Enter the Portion size \n1. Single Size \n2. Family Size \n3. Party Size \n\n --> | "))




cuisineTyp=int(input("Enter the cuisine Type  \n1. Chinese \n2. Italian \n3. Pakistani \n\n --> | "))
if cuisineTyp == 1:
    foodCat=int(input("Enter the Food Category  \n1. Vegetarian \n2. Non-Veg \n3. Special \n\n -->| "))
    spiceLevel=int(input("Enter the Spice Level \n1. Mild Level \n2.Medium Level  \n3. Hot Level \n\n --> | "))
    addOn= int(input("Enter Add Ons \n1. Desserts \n2. Drinks \n3. Extras \n\n --> | "))
    if foodCat == 1:
        manchurian= 650
        vegNoodles= 750
        tofu= 850
        print(
        f"\nORDER CONFIRMATIONn"
        f"Dear {name},\n\n"
        f"Thank you for your order! Your order has been confirmed and is now being prepared for delivery \n\n"
        f"Order Details:\n"
        f"1. Cuisine Type   : Chinese\n"
        f"2. Food Category  : Vegetarian\n"
        f"3. Spice Level    : {spiceLevel}\n"
        f"4. Add-ons        : {addOn}\n\n"
        f" Selected Food Items:\n"
        f"- Mild   : Vegetable Manchurian — Rs. {manchurian}\n"
        f"- Medium : Chili Garlic Veg Noodles — Rs. {vegNoodles}\n"
        f"- Hot    : Szechuan Spicy Tofu — Rs. {tofu}\n\n"
        f" We hope you enjoy your meal. Thank you for choosing us!\n")
        
        totalBill = manchurian + vegNoodles + tofu
        fivePerDis = totalBill * 5 / 100
        tenPerDis = totalBill * 10 / 100
        
        if portionSize == 1:
            print(f"\n Your Total Bill is {totalBill}")
            
        elif portionSize == 2:
            print(f"\n Your Total Bill with  5% Discount is  {totalBill - fivePerDis}Rs")
            
        elif portionSize == 3:
            print(f"\n Your Total Bill with  10% Discount is {totalBill - tenPerDis}Rs")
            
        else:
            print(f"Invalid ")
        
        
        
    elif foodCat == 2:
        chickenCornSoup = 450
        kungPaoChicken = 1050
        szechuanChicken = 1150

        print(
            f"\n️ ORDER CONFIRMATION ️\n"
            f"Dear {name},\n\n"
            f"Thank you for your order! Your order has been confirmed and is now being prepared for delivery \n\n"
            f" Order Details:\n"
            f"1. Cuisine Type   : Chinese\n"
            f"2. Food Category  : Non-Vegetarian\n"
            f"3. Spice Level    : {spiceLevel}\n"
            f"4. Add-ons        : {addOn}\n\n"
            f" Selected Food Items:\n"
            f"- Mild   : Chicken Corn Soup — Rs. {chickenCornSoup}\n"
            f"- Medium : Kung Pao Chicken — Rs. {kungPaoChicken}\n"
            f"- Hot    : Szechuan Chili Chicken — Rs. {szechuanChicken}\n\n"
            f" We hope you enjoy your meal. Thank you for choosing us!\n"
        )

        
        totalBill = chickenCornSoup + kungPaoChicken + szechuanChicken
        fivePerDis = totalBill * 5 / 100
        tenPerDis = totalBill * 10 / 100
        
        if portionSize == 1:
            print(f"\n Your Total Bill is {totalBill}")
            
        elif portionSize == 2:
            print(f"\n Your Total Bill with  5% Discount is  {totalBill - fivePerDis}Rs")
            
        elif portionSize == 3:
            print(f"\n Your Total Bill with  10% Discount is {totalBill - tenPerDis}Rs")
            
        else:
            print(f"Invalid ")
    elif foodCat == 3:
        dragonChicken = 1250
        honeySesameBeef = 1350
        prawnTempura = 1450

        print(
            f"\n️ ORDER CONFIRMATION ️\n"
            f"Dear {name},\n\n"
            f"Thank you for your order! Your order has been confirmed and is now being prepared for delivery \n\n"
            f" Order Details:\n"
            f"1. Cuisine Type   : Chinese\n"
            f"2. Food Category  : Special\n"
            f"3. Spice Level    : {spiceLevel}\n"
            f"4. Add-ons        : {addOn}\n\n"
            f" Selected Food Items:\n"
            f"- Special 1 : Dragon Chicken — Rs. {dragonChicken}\n"
            f"- Special 2 : Honey Sesame Beef — Rs. {honeySesameBeef}\n"
            f"- Special 3 : Crispy Prawn Tempura — Rs. {prawnTempura}\n\n"
            f" We hope you enjoy your meal. Thank you for choosing us!\n")

        
        totalBill = dragonChicken + honeySesameBeef + prawnTempura
        fivePerDis = totalBill * 5 / 100
        tenPerDis = totalBill * 10 / 100
        
        if portionSize == 1:
            print(f"\n Your Total Bill is {totalBill}")
            
        elif portionSize == 2:
            print(f"\n Your Total Bill with  5% Discount is  {totalBill - fivePerDis}Rs")
            
        elif portionSize == 3:
            print(f"\n Your Total Bill with  10% Discount is {totalBill - tenPerDis}Rs")
            
        else:
            print(f"Invalid ")

    else:
        print("Invalid Food Category")
            
elif cuisineTyp == 2:
    foodCat=int(input("Enter the Food Category  \n1. Vegetarian \n2. Non-Veg \n3. Special \n\n -->| "))
    spiceLevel=int(input("Enter the Spice Level \n1. Mild Level \n2.Medium Level  \n3. Hot Level \n\n --> | "))
    addOn= int(input("Enter Add Ons \n1. Desserts \n2. Drinks \n3. Extras \n\n --> | "))
    if foodCat == 1:
        alooMatar = 450
        daalFry = 400
        chanaMasala = 450

        print(
            f"\n️ ORDER CONFIRMATION ️\n"
            f"Dear {name},\n\n"
            f"Thank you for your order! Your order has been confirmed and is now being prepared for delivery \n\n"
            f" Order Details:\n"
            f"1. Cuisine Type   : Pakistani\n"
            f"2. Food Category  : Vegetarian\n"
            f"3. Spice Level    : {spiceLevel}\n"
            f"4. Add-ons        : {addOn}\n\n"
            f" Selected Food Items:\n"
            f"- Mild   : Aloo Matar — Rs. {alooMatar}\n"
            f"- Medium : Daal Fry — Rs. {daalFry}\n"
            f"- Hot    : Chana Masala — Rs. {chanaMasala}\n\n"
            f" We hope you enjoy your meal. Thank you for choosing us!\n"
        )

        totalBill = alooMatar + daalFry + chanaMasala
        fivePerDis = totalBill * 5 / 100
        tenPerDis = totalBill * 10 / 100
        
        if portionSize == 1:
            print(f"\n Your Total Bill is {totalBill}")
            
        elif portionSize == 2:
            print(f"\n Your Total Bill with  5% Discount is  {totalBill - fivePerDis}Rs")
            
        elif portionSize == 3:
            print(f"\n Your Total Bill with  10% Discount is {totalBill - tenPerDis}Rs")
            
        else:
            print(f"Invalid ")
            
    elif foodCat == 2:
        chickenKorma = 750
        chickenKarahi = 1100
        beefNihari = 1200

        print(
        f"\n️ ORDER CONFIRMATION ️\n"
        f"Dear {name},\n\n"
        f"Thank you for your order! Your order has been confirmed and is now being prepared for delivery \n\n"
        f" Order Details:\n"
        f"1. Cuisine Type   : Pakistani\n"
        f"2. Food Category  : Non-Vegetarian\n"
        f"3. Spice Level    : {spiceLevel}\n"
        f"4. Add-ons        : {addOn}\n\n"
        f" Selected Food Items:\n"
        f"- Mild   : Chicken Korma — Rs. {chickenKorma}\n"
        f"- Medium : Chicken Karahi — Rs. {chickenKarahi}\n"
        f"- Hot    : Beef Nihari — Rs. {beefNihari}\n\n"
        f" We hope you enjoy your meal. Thank you for choosing us!\n"
        )

        totalBill = chickenKorma + chickenKarahi + beefNihari
        fivePerDis = totalBill * 5 / 100
        tenPerDis = totalBill * 10 / 100
        
        if portionSize == 1:
            print(f"\n Your Total Bill is {totalBill}")
            
        elif portionSize == 2:
            print(f"\n Your Total Bill with  5% Discount is  {totalBill - fivePerDis}Rs")
            
        elif portionSize == 3:
            print(f"\n Your Total Bill with  10% Discount is {totalBill - tenPerDis}Rs")
            
        else:
            print(f"Invalid ")


    elif foodCat == 3:
        chickenBiryani = 650
        muttonHandi = 1600 
        sajji = 1800

        print(
            f"\n️ ORDER CONFIRMATION ️\n"
            f"Dear {name},\n\n"
            f"Thank you for your order! Your order has been confirmed and is now being prepared for delivery \n\n"
            f" Order Details:\n"
            f"1. Cuisine Type   : Pakistani\n"
            f"2. Food Category  : Special\n"
            f"3. Spice Level    : {spiceLevel}\n"
            f"4. Add-ons        : {addOn}\n\n"
            f" Selected Food Items:\n"
            f"- Special 1 : Chicken Biryani — Rs. {chickenBiryani}\n"
            f"- Special 2 : Mutton Handi — Rs. {muttonHandi}\n"
            f"- Special 3 : Sajji — Rs. {sajji}\n\n"
            f" We hope you enjoy your meal. Thank you for choosing us!\n"
        )

        totalBill = chickenBiryani + muttonHandi + sajji
        fivePerDis = totalBill * 5 / 100
        tenPerDis = totalBill * 10 / 100
        
        if portionSize == 1:
            print(f"\n Your Total Bill is {totalBill}")
            
        elif portionSize == 2:
            print(f"\n Your Total Bill with  5% Discount is  {totalBill - fivePerDis}Rs")
            
        elif portionSize == 3:
            print(f"\n Your Total Bill with  10% Discount is {totalBill - tenPerDis}Rs")
            
        else:
            print(f"Invalid ")


    else:
        print("Invalid Food Category")
elif cuisineTyp == 3:
    foodCat=int(input("Enter the Food Category  \n1. Vegetarian \n2. Non-Veg \n3. Special \n\n -->| "))
    spiceLevel=int(input("Enter the Spice Level \n1. Mild Level \n2.Medium Level  \n3. Hot Level \n\n --> | "))
    addOn= int(input("Enter Add Ons \n1. Desserts \n2. Drinks \n3. Extras \n\n --> | "))
    if foodCat == 1:
        margheritaPizza = 900
        alfredoPasta = 1050
        arrabbiataPenne = 1100

        print(
            f"\n️ ORDER CONFIRMATION ️\n"
            f"Dear {name},\n\n"
            f"Thank you for your order! Your order has been confirmed and is now being prepared for delivery \n\n"
            f" Order Details:\n"
            f"1. Cuisine Type   : Italian\n"
            f"2. Food Category  : Vegetarian\n"
            f"3. Spice Level    : {spiceLevel}\n"
            f"4. Add-ons        : {addOn}\n\n"
            f" Selected Food Items:\n"
            f"- Mild   : Margherita Pizza — Rs. {margheritaPizza}\n"
            f"- Medium : Creamy Alfredo Pasta — Rs. {alfredoPasta}\n"
            f"- Hot    : Arrabbiata Penne — Rs. {arrabbiataPenne}\n\n"
            f" We hope you enjoy your meal. Thank you for choosing us!\n"
        )

        totalBill = margheritaPizza + alfredoPasta + arrabbiataPenne
        fivePerDis = totalBill * 5 / 100
        tenPerDis = totalBill * 10 / 100
        
        if portionSize == 1:
            print(f"\n Your Total Bill is {totalBill}")
            
        elif portionSize == 2:
            print(f"\n Your Total Bill with  5% Discount is  {totalBill - fivePerDis}Rs")
            
        elif portionSize == 3:
            print(f"\n Your Total Bill with  10% Discount is {totalBill - tenPerDis}Rs")
            
        else:
            print(f"Invalid ")

    elif foodCat == 2:
        chickenWhitePasta = 1150
        pepperoniPizza = 1300
        chickenLasagna = 1450

        print(
            f"\n️ ORDER CONFIRMATION ️\n"
            f"Dear {name},\n\n"
            f"Thank you for your order! Your order has been confirmed and is now being prepared for delivery \n\n"
            f" Order Details:\n"
            f"1. Cuisine Type   : Italian\n"
            f"2. Food Category  : Non-Vegetarian\n"
            f"3. Spice Level    : {spiceLevel}\n"
            f"4. Add-ons        : {addOn}\n\n"
            f" Selected Food Items:\n"
            f"- Mild   : Chicken White Sauce Pasta — Rs. {chickenWhitePasta}\n"
            f"- Medium : Pepperoni Pizza — Rs. {pepperoniPizza}\n"
            f"- Hot    : Spicy Chicken Lasagna — Rs. {chickenLasagna}\n\n"
            f" We hope you enjoy your meal. Thank you for choosing us!\n"
        )

        totalBill = chickenWhitePasta + pepperoniPizza + chickenLasagna
        fivePerDis = totalBill * 5 / 100
        tenPerDis = totalBill * 10 / 100
        
        if portionSize == 1:
            print(f"\n Your Total Bill is {totalBill}")
            
        elif portionSize == 2:
            print(f"\n Your Total Bill with  5% Discount is  {totalBill - fivePerDis}Rs")
            
        elif portionSize == 3:
            print(f"\n Your Total Bill with  10% Discount is {totalBill - tenPerDis}Rs")
            
        else:
            print(f"Invalid ")


    elif foodCat == 3:
        stuffedRavioli = 1400
        seafoodFettuccine = 1650
        trufflePizza = 1750

        print(
            f"\n️ ORDER CONFIRMATION ️\n"
            f"Dear {name},\n\n"
            f"Thank you for your order! Your order has been confirmed and is now being prepared for delivery \n\n"
            f" Order Details:\n"
            f"1. Cuisine Type   : Italian\n"
            f"2. Food Category  : Special\n"
            f"3. Spice Level    : {spiceLevel}\n"
            f"4. Add-ons        : {addOn}\n\n"
            f" Selected Food Items:\n"
            f"- Special 1 : Stuffed Ravioli — Rs. {stuffedRavioli}\n"
            f"- Special 2 : Seafood Fettuccine — Rs. {seafoodFettuccine}\n"
            f"- Special 3 : Truffle Mushroom Pizza — Rs. {trufflePizza}\n\n"
            f" We hope you enjoy your meal. Thank you for choosing us!\n"
        )

        totalBill = stuffedRavioli + seafoodFettuccine + trufflePizza
        fivePerDis = totalBill * 5 / 100
        tenPerDis = totalBill * 10 / 100
        
        if portionSize == 1:
            print(f"\n Your Total Bill is {totalBill}")
            
        elif portionSize == 2:
            print(f"\n Your Total Bill with  5% Discount is  {totalBill - fivePerDis}Rs")
            
        elif portionSize == 3:
            print(f"\n Your Total Bill with  10% Discount is {totalBill - tenPerDis}Rs")
            
        else:
            print(f"Invalid ")

    else:
        print("Invalid Food Category")
else:
    print("Invalid Cuisine Type")
    
    
    