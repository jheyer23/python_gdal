# Unpacking - powerful in python 

# Create tuple 
coordinates = (1, 2, 3) 

# Get values and use values
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x * y * z 

# Unpacking - achieve above with less code 

x, y, z = coordinates # Gets first item in tuple and assigns to x, second item and assings to y, etc. 
print(x)