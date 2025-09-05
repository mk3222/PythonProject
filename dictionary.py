# dictionary = a collection of {key:value} pairs ordered and changeable. No duplicates

capitals = {"USA":"Washington DC",
            "Bangladesh":"Dhaka",
            "China": "Beijing",
            "Russia":"Moscow",}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))
# print(capitals.get("Japan"))

#### **** ####
# if capitals.get("Japan"):
#    print("That capital exists")
# else:
#    print("That capital doesn't exist")
#
# capitals.update({"Germany":"Berlin"})
# capitals.pop("Germany")
# capitals.popitem()
# capitals.clear()

# keys=capitals.keys()

# print(keys)

# items=capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")

print("====================================")

for i, (country, capital) in enumerate(capitals.items(), start=1):
    print(f"{i}. {country} → {capital}")
print("====================================")



print(f"{'Country':<15} | {'Capital'}")
print("-" * 30)
for country, capital in capitals.items():
    print(f"{country:<15} | {capital}")
print("====================================")





