age = int(input("Enter the age: "))

if age < 0:
    print("You haven't been born yet!")
elif age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("You are now signed up!")
else:
    print("You must be 18+ to sign up")
