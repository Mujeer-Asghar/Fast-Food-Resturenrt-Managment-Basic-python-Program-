import pizzaclass
from pizzaclass import pizza, burger, ColdDrink
            
Bill=[]
choice=0
while choice !=7:
    print("Menu:")
    print("1. Pizzas")
    print("2. Burgers")
    print("3. Cold Drinks")
    print('4 for simple deal (1 Pizza + 1 Burger + 1 Cold Drink) for $10.99')
    print('5 for 2 Men Deal (1 Pizza + 1 Burger + 1 Cold Drink) for $25.99')
    print('6 for Family Feast (2 Pizzas + 4 Burgers + unlimited Cold Drinks) for $39.99') 
    print('7 for Billing and Exit')
    choice = int(input("Enter your choice (1-7): "))
    if choice == 1:
         print("1 for Cheese Burst Pizza")  
         print("2 for Pepperoni Pizza")
         print('3 for Veggie Pizza')
         pizza_choice = int(input("Enter your pizza choice (1-3): "))
         if pizza_choice == 1:
             pizza1 = pizza("Cheese Burst Pizza", 12.99)
             Bill.append(pizza1)
             print("added to bill")
         elif pizza_choice == 2:
             pizza2 = pizza("Pepperoni Pizza", 14.99)
             Bill.append(pizza2)
             print("added to bill")
         elif pizza_choice == 3:
             pizza3 = pizza("Veggie Pizza", 10.99)
             Bill.append(pizza3)
             print("added to bill")
         else:
              pizza_choice = int(input("Invalid Enter again pizza choice (1-3): "))
             
             
    elif choice == 2:    
        print("1 for Chicken Burger")
        print("2 for Veggie Burger")
        print("3 for Cheese Burger")
        burger_choice = int(input("Enter your burger choice (1-3): "))
        if burger_choice == 1:
             burger1 = burger("Chicken Burger", 8.99)
             Bill.append(burger1) 
             print("added to bill")
        elif burger_choice == 2:
             burger2 = burger("Veggie Burger", 7.99)
             Bill.append(burger2)
             print("added to bill")
        elif burger_choice == 3:
             burger3 = burger("Cheese Burger", 9.99)
             Bill.append(burger3)
             print("added to bill")
        else:
                print("Invalid choice")
    elif choice == 3:
        print("1 for Cola")
        print("2 for Lemonade")
        print("3 for Iced Tea")
        drink_choice = int(input("Enter your drink choice (1-3): "))
        if drink_choice == 1:
             drink1 = ColdDrink("Cola", 1.99)
             Bill.append(drink1)
             print("added to bill") 
        elif drink_choice == 2:
             drink2 = ColdDrink("Lemonade", 1.49)
             Bill.append(drink2)
             print("added to bill")
        elif drink_choice == 3:
             drink3 = ColdDrink("Iced Tea", 1.79)
             Bill.append(drink3)
             print("added to bill")
        else:
                print("Invalid choice")
    if choice ==4:
            deal1_pizza = pizza("Cheese Burst Pizza", 5.99)
            deal1_burger = burger("Chicken Burger", 4.99)
            deal1_drink = ColdDrink("Cola", 0.99)
            Bill.append(deal1_pizza)
            Bill.append(deal1_burger)
            Bill.append(deal1_drink)
            print("Simple Deal added to your bill for $10.99")
    elif choice ==5:
            deal2_pizza = pizza("Pepperoni Pizza", 14.99)
            deal2_burger = burger("Cheese Burger", 9.99)
            deal2_drink = ColdDrink("Lemonade", 1.49)
            Bill.append(deal2_pizza)
            Bill.append(deal2_burger)
            Bill.append(deal2_drink)
            print('2 Men deal added to your bill for $25.99')
            
    elif choice ==6:
            deal3_pizza1 = pizza("Cheese Burst Pizza", 12.99)
            deal3_pizza2 = pizza("Veggie Pizza", 10.99)
            deal3_burger1 = burger("Chicken Burger", 8.99)
            deal3_burger2 = burger("Veggie Burger", 7.99)
            deal3_burger3 = burger("Cheese Burger", 9.99)
            deal3_burger4 = burger("Chicken Burger", 8.99)
            deal3_drink = ColdDrink("Iced Tea", 1.79)
            Bill.append(deal3_pizza1)
            Bill.append(deal3_pizza2)
            Bill.append(deal3_burger1)
            Bill.append(deal3_burger2)
            Bill.append(deal3_burger3)
            Bill.append(deal3_burger4)
            Bill.append(deal3_drink)
            print("Family Feast added to your bill for $39.99")
            
    elif choice == 7:
        
        
        Bill_Total=0
        print("Your Bill:")
        for item in Bill:
            print(f"{item.name}: ${item.price}")
            Bill_Total += item.price            
            print(f"Total Amount: ${Bill_Total:.2f}")
            print("Thank you for dining with us!")
    
    

    choice = int(input("Enter your choice (1-7): ")) 
        
            
            
            
            
            
