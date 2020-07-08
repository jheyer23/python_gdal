# Lists 
# Can index individual items from list 

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary'] # Five strings in this list 
print(names[0]) 
print(names[2])

# last item in list 
print(names[-1]) 

# Use colon to select range of items 
print(names[2:])
print(names[2:4]) # Does not include item at index four 

# Can modify names in list 
# Remove h in John

names[0] = 'Jon' 
print(names) 

# Write a program to find largest number in list 
numbers = [100, 200, 10, 50]
max = numbers[0] # Assuming first item is list is largest. Assumption is probably wrong 

# max will reset until largest number found 
for number in numbers: 
    if number > max: 
        max = number 
print(max) 

