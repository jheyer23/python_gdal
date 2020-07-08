# Storing items in dictionary 
# Different attributes - name, email, phone, etc. 
# Key value pairs (Key: name, email, phone). Each key has value 
# Keys need to be unique in a dictionary - cannot duplicate 
# Values of keys can be any data type 

customer = {
    "name": "John", 
    "age": 30, 
    "is_verified": True
}

print(customer["name"])

# Doesn't yell at us if specify a key that does not exist here. Can add default value (e.g. Jan 1 1980)
print(customer.get("birthdate", "Jan 1 1980"))

# Update key 
customer["name"] = "Jack Smith" 
print(customer["name"]) 

# Exercise 
# Program asks for phone number 

phone = input("Phone: ")
# Need dictionary to map key to a value 

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = ""

for ch in phone: 
    output += digits_mapping.get(ch, "!") + " " # For each iteration get this and add to output string. If number is not in dictionary the exclamation mark is printed 
print(output)