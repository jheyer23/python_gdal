# Nested loops 
# Adding one loop inside another loop 
# Can generate list of coordinates for example 

# Will iterate through all iterations of inner loop 0 - 2 (range 3). Once the inner loop is complete it goes back to outer-loop and iterates through the second line of outerloop (1)
for x in range(4): # generate values for x coordinates 
    for y in range(3): # generate values of y coordinates in new loop (inner-loop) 
        print(f'({x},{y})')


# Challenge exercise 
# Use nested loops draw f shape from simple list of numbers 
numbers = [5, 2, 5, 2, 2] # Values determine the number of x's we have 

xxxxx
xx
xxxxx
xx
xx

for x_count in numbers: 
    print('x' * x_count) # Can cheat in python and multiply number by count 

# Inner loop will get iterated five times, then two times, then five times, then two times, then two times 
for x_count in numbers:
    output = ''  # After first set of iterations of inner-loop complete, goes back to outer-loop and this string is reset to empty 
    for count in range(x_count): # Use range function to generate range of numbers from zero to first x count in list (5) 
        output += 'x'  # For each iteration append an x to the output variable 
    print(output)  # Prints five x's on the first row, two x's on the second row etc. 