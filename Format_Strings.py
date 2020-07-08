# Formated strings tutorial 
# Useful when want to dynamically generate text with variables 

first = 'Josh'
last = 'Heyer'

# This method to concatenate strings works but is not good in complicated scenarios
message = first + ' [' + last + '] is a coder'
print(message)

# Create a formated string - make it easier to visualize output. Prefixed with f
# {} are "holds in the string. When run program the holds are filled with variable 

# f only works in Python 3.6+
#msg = f'{first} [{last}] is a coder'
#print(msg)
