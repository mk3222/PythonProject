# return = statement used to end a function
#          and send a result back to the caller

def add(x,y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z


def divide(x,y):
    z = x / y
    return z

print(add(3,4))
print(subtract(3,4))
print(multiply(3,4))
print(divide(3,4))

#####---------------------#####

def create_name(first_name,last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return f"{first_name} {last_name}"

full_name=create_name("Mohammad", "Karim")
print(full_name)























