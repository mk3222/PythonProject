# name = input("Enter your name: ")

phone_number = input("Enter your phone number: ")

# Some string methods you can try with name:
# result = len(name)
# result = name.find("B")
# result = name.rfind("B")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()

# For phone numbers
# result = phone_number.count("-")
phone_number = phone_number.replace("-", ".")

# print(result)
# print(name)
print(f"Formatted phone number: {phone_number}")
