# or = at least on condition must be true

temp = -5
is_raining = False

if temp > 35:
    print("The outdoor event is cancelled (too hot).")
elif temp < 0:
    print("The outdoor event is cancelled (too cold).")
elif is_raining:
    print("The outdoor event is cancelled (it's raining).")
else:
    print("The outdoor event is still scheduled.")
