# 2D lists 
# Many applications in data science and machine learning 

# matrix - rectangular array of numbers 
# Can model matrix using 2D list in python 

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7,  8, 9]
]

# access one item in list 

print(matrix[0])  # Returns inner list 
print(matrix[0][1]) # Index of 2 in first inner list


matrix[0][1] = 20 # List is modified; 20 is now element 1 in 1st list 
print(matrix) 

# Iterate over matrix and get all items in list 
for row in matrix: 
    for item in row: 
        print(item) 
