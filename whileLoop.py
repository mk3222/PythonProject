# while loop = execute some code WHILE some condition remains true

#### ***** ####
name = input("Enter your name: ")
while name.strip() == "":   # Used .strip() so spaces " " don’t count as a valid name.
    print("You did not enter your name!")
    name = input("Enter your name: ")
print(f"Hello, {name}!")

#### ***** ####
age = input("Enter your age: ")
while not age.isdigit():   # ensures only digits / Added isdigit() to check that the age is actually numeric instead of crashing if someone types "abc".
    print("You did not enter a valid age!")
    age = input("Enter your age: ")
age = int(age)

print(f"Hello, you are {age} years old.")

#### ***** ####
food = input("Enter a food you like (q to quit): ")

while food.lower() != "q":   # works for both 'q' and 'Q' / Used .lower() so typing Q also works.
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")

print("Thank you for sharing your favorite foods! 🍴")

#### ***** ####

while True:
    try:
        num = int(input("Enter a number between 1 and 10: "))
        if 1 <= num <= 10:
            break
        else:
            print(f"{num} is not a valid number. Please try again.")
    except ValueError:
        print("That's not a number. Please enter a number between 1 and 10.")

print(f"Your number is {num}.")






















