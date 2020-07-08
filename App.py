# All string - series of characters
print("Josh Heyer")
print('o----') 
print(' ||||')

# Multiply string by mulitiplier 
# This is an expression -- a piece of code that produces a value. Here it produces ten *
print('*' * 10)

# Variables - python stores value 10 to price in memory. Can use variable anywhere in program to access value  
# Alway make variable lowercase values 
# Storing simple values in memory. Can store intergers, floats, strings, boolean values, lists 
# This is an interger
price = 10
# Python interpreter executes line by line. Will change variable to 20 
price = 20
# This is a float 
price = 4.9
# Can have boolean values (True or False)
is_published = False 
print(price) 

# Exercise
full_name = 'John Smith' 
age = 20 
is_new = True 

# Functions for common tasks 
# raw_input function used in python 2.7 changed to input in python 3.x
# Parenthesis call and execute function. Like pressing a button on a remote control 
# The input function will print this string and wait for an input (the space included after ?) 
name = raw_input('What is your name? ')
favorite_color = raw_input('What is your favorite color? ') 
# Concatenating or combining strings. Example of an expression - piece of code that produces a value 
print(name + ' likes ' + favorite_color) 


# Can only subtract same operands (e.g. string - string or a int - int, not an int - string)  
birth_year = raw_input("Birth Year: ") 
# built in functions. Here type is a built in function
print(type(birth_year))
# Use int function to convert a string to an interger. Pass birth_year variable through int function 
age = 2020 - int(birth_year) 
print(type(age))
print(age)
