menu={"Pizza":3.00,
      "Nachos":4.50,
      "Popcorn":6.00,
      "Fries":2.50,
      "Chips":1.00,
      "Soda": 3.00,
      "Lemonade": 4.25}

cart=[]
total=0

print("------------MENU------------")
for key, value in menu.items():
    print(f"{key:<12} : ${value:>5.2f}")
print("-----------------------------")

while True:
    food=input("Select a food or type 'q' to quit: ").capitalize()
    if food.lower() == "q":
        break
    elif food in menu:
        cart.append(food)

print("----------YOUR ORDER---------")
for food in cart:
    price = menu[food]
    total += price
    print(f"{food:<12} : ${price:>5.2f}")
print("-----------------------------")
print(f"{'Total':<12} : ${total:>5.2f}")
