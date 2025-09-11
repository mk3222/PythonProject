num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:      # use 'row' here
    for num in row:      # then loop over each element inside the row
        print(num, end=" ")
    print()
