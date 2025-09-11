### and = both condition must be True


temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY ☀")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀")
elif 0 < temp < 28 and is_sunny:
    print("It is WARM outside 🙂")
    print("It is SUNNY ☀")
else:
    print("The weather is unclear.")
