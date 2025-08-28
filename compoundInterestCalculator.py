# Python compound interest calculator

while True:
    principle = float(input("Enter your principle amount: "))
    if principle < 0:
        print("Principle can't be less than 0.")
    else:
        break

while True:
    rate = float(input("Enter the interest rate (%): "))
    if rate < 0:
        print("Interest rate cannot be less than 0.")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than 0.")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"\nBalance after {time:.1f} year(s): ${total:,.2f}")
