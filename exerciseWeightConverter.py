weight = float(input("Enter your weight: "))
units = input("Kilograms or Pounds? (K, L): ")

if units == "K":
    weight = weight * 2.205   # convert kg → lbs
    units = "Lbs."
    print(f"Your weight is {round(weight, 1)} {units}")
elif units == "L":
    weight = weight / 2.205   # convert lbs → kg
    units = "Kgs."
    print(f"Your weight is {round(weight, 1)} {units}")
else:
    print(f"{units} is not valid")
    exit()  # stop program if invalid input


