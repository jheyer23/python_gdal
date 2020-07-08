# For loops 
# Use to iterate over items of a collection. For example iterate over each character in a string then do something with it. String is a sequence of charcacters so it looks like a collection 

# Loop variable. For each iteration this variable will hold one item 
# For each iteration the variable "item" will hold one character at a time. 1st iteration "item" set to P, then Y in the second iteration, etc. 
for item in 'Python':
    print(item)
    
# Define a list with [] brackets
# Prints one name per iteration on new line 
for item in ['Josh', 'Karina', 'Kiara']:
    print(item)

# Iterate over a large amount of numbers - use range function (creates an object that we can iterate over)
for item in range(10):
    print(item)

for item in range(5, 10):
    print(item)

# Can take a step (every 2 in this case) 
for item in range(6, 12, 2):
    print(item)
    
# Exercise - write program to calculate total cost of all items in a shopping cart 

prices = [10, 20, 30, 40]

total = 0

for item_price in prices:  # For each iteration "item_price" holds one value. Holds 10, then 20, then 30, then 40
    total += price  # augmented operator += is same as total + item_price - define this variable to calculate total price. For each iteration get item price and add to total  
print(f"Total: {total}")  # use formated string to dynamically include "total" variable value in string  