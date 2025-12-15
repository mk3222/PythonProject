# default arguments = A default value for certain parameters
#                     Default is used when that argument is omitted
#                     Make your function more flexible, reduces # of arguments
#                     1. Positional, 2. DEFAULT, 3. Keyboard, 4. Arbitrary
import time


def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1+tax)

print(net_price(500))
print(net_price(500,0.1))
print(net_price(500,0.1, 0))

#####-------------------------#####

def count(start, end):
    for x in range(start, end):
        print(x)
        time.sleep(1)
    print("DONE!")

count(0,10)














































