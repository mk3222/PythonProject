fruits=     ["apple","orange","bananas", "coconut"]
vegetables= ["celery", "carrots", "potatoes"]
meat=       ["chicken","beef","goat"]

groceries=[fruits,vegetables,meat]
print(groceries[1][2]) #  # 👉 "potatoes"


#### see everything ####
for category in groceries:
    for food in category:
        print(food, end=" ")
    print()





