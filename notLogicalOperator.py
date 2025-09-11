# not = inverts the condition (not False, not True)

temp = 0
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY ☀")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀")
elif 0 < temp < 28 and is_sunny:
    print("It is WARM outside 🙂")
    print("It is SUNNY ☀")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside 🥵")
    print("It is CLOUDY ☁")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside 🥶")
    print("It is CLOUDY ☁")
elif 0 < temp < 28 and not is_sunny:
    print("It is WARM outside 🙂")
    print("It is CLOUDY ☁")

else:
    print("The weather is unclear.")
