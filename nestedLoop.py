# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#               inner loop:


#### *** ####
# for i in range(1, 10):
#    print(i, end=" ") # start from 1 and ends at 9

#### *** ####
#for i in range(3):
#    for j in range(1, 10):
#        print(j, end=" ")
#    print()


#### 3×9 multiplication table: ####
#for i in range(1, 4):      # rows
#    for j in range(1, 10): # columns
#        print(f"{i*j:2}", end=" ")
#    print()


#### *** ####
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print()  # new line after each row









