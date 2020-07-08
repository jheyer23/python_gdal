# List methods 

numbers = [5, 2, 1, 7, 4, 5] 

# With . can see all the methods that we can perform on list 
numbers.append(20) # 20 is added at end of list 
print(numbers) 

# Add number at certain point in list 
numbers.insert(0,10) # First item (0) is index, second item is what will be added. Here 10 will be added as first item in list 
print(numbers)

# Remove an item 
numbers.remove(5)
print(numbers)

# Remove all items from list. Empties list 
numbers.clear()
print(numbers)

# Remove last item in list 
numbers.pop()
print(numbers)

# Return index of item in list 
numbers.index(5)
print(numbers)

# Check existance of item in list using in operator 
print(50 in numbers) # Get boolean value - safer to use 

# Count occurance of item 
numbers.count(5)
print(numbers) # Returns 2 because there are 2 5's in list

# Sort list 
numbers.sort()
print(numbers)

# Reverse items in decending order
numbers.reverse()
print(numbers)

# Get copy of list 
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2) 