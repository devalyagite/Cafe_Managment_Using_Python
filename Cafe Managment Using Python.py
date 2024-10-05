#Cafe Managment
menu = {
    "Pizza":120,
    "Pasta":140,
    "Burger":80,
    "Maggiee":80,
    "Cold Coffee":60,
    "Hot Coffee":60
}

#Greetings
print("Welcome To Devalya's Cafe")
print("Pizza = Rs.140\nPasta = Rs. 120\nBurger = Rs.80\nMaggiee = Rs.80\nCold Coffee = Rs.60\nHot Coffee = Rs.60")

order_total = 0

item_1 = input("Enter the Name of item you want to Order :")
if item_1 in menu:
    order_total +=  menu[item_1]
    print(f"{item_1} is Added to your Order")
else:
    print(f"Sorry, {item_1} is not Available yet")

another_order = input("Do you want to add another item to your Order? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter The Second Order:")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} is Added to your Order")
    else:
        print(f"{item_2} is not available yet")
print(f"The Total Amount is to Pay is Rs.{order_total}")
print("Thank You, Visit Again")