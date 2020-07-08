# Cool things to do with Python strings 

course = 'Python for Beginners'

# Calculate number of characters in string 
# Can enforce limit on characters in input field with len general purpose function. Not limited to just strings (e.g. Can use with lists)
print(len(course))

# If type . after string "course" all the methods specific to strings will show up in drop down menu
# Functions can be used on different types of data, methods are specific to a type of data (e.g. upper() is a method specific to strings)
# When use print here it does not modify original variable 
print(course.upper())
print(course.lower())

# Will return index of first P in string 
print(course.find('P'))

# Can replace characters or sequence of characters
# This is case sensitive 
print(course.replace('Beginners', 'Absolute Beginners'))

# See if Python is in course variable 
# Returns boolean variable
print('Python' in course)

