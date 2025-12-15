# *args     = Allows you to pass multiple non-key arguments
# **kwargs  = Allows you to pass multiple keyword-arguments
#             * unpacking operator
#             1. Positional, 2. Default, 3. Keyword, 4. ARBITRARY

#####----args----#####

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5))



#####----args----#####

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()

display_name("Mohammad", "Karim")



#####----kwargs----#####

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(
    Street=123,
    City="Sterling",
    State="VA",
    Zip=20166
)



#####----args plus kwargs----#####

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(kwargs.get("Street"))
    print(f"{kwargs.get('City')}, {kwargs.get('State')} {kwargs.get('Zip')}")


shipping_label(
    "Mohammad Karim",
    Street=123,
    City="Sterling",
    State="VA",
    Zip=20166
)






















