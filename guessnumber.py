#! /usr/bin/env python3
# we will store the current largest number here
matched = "Well done, Friend! You are free now."

# input the first value
number = int(input("Enter the magic number: "))

while number != 777:
    # is number larger than largest_number?
    if number == matched:
        # yes, update largest_number
        matched = number
    number = int(input("Ha ha! You're stuck in my loop! Try again! "))
        
print(matched)# we will store the current largest number here
matched = "Well done, Friend! You are free now."

# input the first value
number = int(input("Enter the magic number: "))

while number != 777:
    # is number larger than largest_number?
    if number == matched:
        # yes, update largest_number
        matched = number
    number = int(input("Ha ha! You're stuck in my loop! Try again "))
        
print(matched)
