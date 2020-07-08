# TUTORIAL ON STRINGS #

# Have to use double quotes if use apostraphe like we do here with Python's 
course = "Python's Course for Begninners"

# If want to put a word in double quoats do the following 
course = 'Python Course for "Begninners"' 

# Three quotes for multiline strings 
course = '''
Hi John, 

Here is our first email to you. 

Thank you, 

The support team

'''

print(course)

# How to index python string 
# Here [0] will get first element in string, the letter P, and return it
course2 = 'Python for Beginners'
print(course2[0])

# Can use a negative index to get characters stored from the end 
# Negative 1 [-1] is the index of the last character. Here it returns s, the last letter in Beginners 
course3 = 'Python for Beginners' 
print(course3[-1])

# Return range of characters from index 
# Will return all characters up to last number - here letters 0-2, last index is 3
course4 = 'Python for Beginners'
print(course4[0:3])

# Can also return all the characters after ith index 
course5 = 'Python for Beginners' 
print(course5[2:])

# Return all variables in string and copy to another variable 
another = 'Python for Beginners'
print(another[:])