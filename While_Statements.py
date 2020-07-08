# While Loops 
# Use to execute a block of code multiple times 
# Useful in building interactive programs and games 

# If condition is true, code in block will be repeatidly executed 
# while condition:
    # Block code 

i = 1 

while i <= 5:
    print(i)
    i = i + 1  # prevents an infinite loop. At some point i will be 6, condition will be false, and will jump out of loop 
print("Done")
    
i = 1

# Can print strings 
while i <= 5:
    print('*' * i) # Can repeat a string 
    i = i + 1  # prevents an infinite loop. At some point i will be 6, condition will be false, and will jump out of loop 
print("Done")
