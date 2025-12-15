# function = A block of reusable code
#            place () after the function name to invoke it.

def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are now {age} years old!")
    print("Happy Birthday to you!")
    print()

happy_birthday("MK", 48)
happy_birthday("FR", 43)
happy_birthday("ZK1", 16)
happy_birthday("ZK2", 6)


#####--------------------#####

def display_invoice(username, amount, due_date):
    print(f"Hello, {username}")
    print(f"Your bill of ${amount: .2f} is due: {due_date}")

display_invoice("MK", 43.90, "01/12")




















