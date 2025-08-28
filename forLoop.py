# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.


#### *** ####
#for x in range(1,11): # start from 1 and end at 10 (11-1)
#    print(x)

#### *** ####
# for x in range(1,11, 3): # start from 1 and end at 10 (11-1), and iterative by 3 (output - 1 4 7 10 )
#    print(x)

#### *** ####
#credit_card = "1234-5678-9012-3456"

#for x in credit_card:
##   print(x)

#### *** ####

#for x in range(1, 21):
#    if x == 13:
#        continue # numbers 1 → 20, skipping 13 because of the 'continue'
#    print(x)

#### *** ####

for x in range(1, 21):
    if x == 13:
        break # loop to stop completely at 13, you’d use break instead:
    print(x)