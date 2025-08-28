unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    result = (temp * 9 / 5) + 32   # Celsius → Fahrenheit
    print(f"The result is {round(result, 1)} °F")
elif unit == "F":
    result = (temp - 32) * 5 / 9   # Fahrenheit → Celsius
    print(f"The result is {round(result, 1)} °C")
else:
    print(f"{unit} is an invalid unit of measurement")
    exit()
