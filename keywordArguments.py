# keyword Arguments = An argument preceded by an identifier
#                     Helps with readability
#                     Order of arguments doesn't matter
#                     1. Positional, 2. default, 3. KEYWORD, 4. Arbitrary



def hello(greeting, tittle, firstname, lastname):
    print(f"{greeting} {tittle} {firstname} {lastname}")

hello("Hello", "Howdy", "John", "Smith")

#####-----------------#####

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_number = get_phone(country="1", area="567", first="274", last="9166")

print(phone_number)










































