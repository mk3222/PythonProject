# format specifiers = {value:flags} format a value based on what flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :number = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3.14
price2 = 987.65
price3 = 12.34

# Fixed point with 2 decimals
print(f"Price 1 is ${price1:.2f}")

# Allocate 10 spaces, right align
print(f"Price 2 is ${price2:10.2f}")

# Allocate 10 spaces, left align
print(f"Price 3 is ${price3:<10.2f}")

# Show + sign for positive numbers
print(f"Price 1 (signed) is ${price1:+.2f}")

# Zero padding
print(f"Price 2 (zero-padded) is ${price2:010.2f}")

# Center align
print(f"Price 3 (centered) is ${price3:^10.2f}")

# Comma separator (good for big numbers)
big_price = 1234567.89
print(f"Big price is ${big_price:,.2f}")
