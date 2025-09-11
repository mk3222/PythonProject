# Shopping Cart Program

item = input("What is your item: ")
price = float(input("What is the price: $"))
quantity = int(input("What is your quantity: "))

total = price * quantity

print(f"\nYou have bought {quantity} {item}(s).")
print(f"The total price is ${total:.2f}")
