# Shopping Cart Program

item = str(input("What is your item: "))
price = float(input("What is the price: "))
quantity = int(input("What is your quantity: "))
total = price * quantity

print(f"You have bought {quantity} {item}.")
print(f"The total price is ${total}.")