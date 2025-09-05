# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end: step]

credit_number= "1234-5678-9012-3456"

# print(credit_number[0]) # start
# print(credit_number[0:4]) # 0 and before 4th index
# print(credit_number[:4]) # 0 and before 4th index
# print(credit_number[5:9]) # starting index 5th  and ending index 9th [-1]
# print(credit_number[5:]) # starting index 5th and to the end
# print(credit_number[-1]) # last character of the string
# print(credit_number[-2]) # 2nd last character of the string
# print(credit_number[-3]) # 3rd last character of the string
# print(credit_number[-4]) # 4th last character of the string
# print(credit_number[-5]) # 4th last character of the string
# print(credit_number[::2]) # step - every 2nd character of the string

# last_digit = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digit}")

credit_number= credit_number[::-1]
print(credit_number)