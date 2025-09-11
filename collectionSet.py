# collection = single 'variable' used to store multiple values
# Set = {} unordered and immutable, but Add/Remove OK and no duplicates

fruits = {"Apple", "Banana", "Orange", "Mango"}
print("Original:", fruits)

fruits.add("Coconut")   # does nothing (already in the set, no duplicates)
print("After add:", fruits)

fruits.remove("Apple")  # removes "Apple"
print("After remove:", fruits)

fruits.pop()            # removes a random element (since sets are unordered)
print("After pop:", fruits)

fruits.clear()          # clears everything
print("After clear:", fruits)

print(fruits)           # prints set() → empty set

