# collection = single 'variable' used to store multiple values
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ("Apple", "Banana", "Orange", "Mango")
print("Original:", fruits)

print(fruits.index("Mango"))
print(fruits.count("Mango"))

for fruit in fruits:
    print(fruit)

