# IF STATEMENT TUTORIAL ########
# Makes a decision based on a set of conditions. If condition is true will do one thing, if the condition is false we'll do other things

# Define boolean variable 

is_hot = False 
is_cold = False

# if true we'll do certain things

# First rule
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
#What if it is neither hot nor cold?
#Factor condition needed (e.g. otherwise)
#Use elif statement 
#Add second rule - if not hot, is it cold? If it is cold execute next lines and print different message
#This next block of code is executed if the first condition is not true
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")    
# None of the conditions are true
#Add third rule - if neither hot or cold execute next lines and print different message
else:
    print("It's a lovely day")
 

    
print("Enjoy your day")




# Change boolean value to false, first message dissapears 

is_hot = False

# if true we'll do certain things

if is_hot:
    print("It's a hot day")
print("Enjoy your day")

# Exersice - house is $1M 
   # If buyer has good credit, they need to put down 10%
   # Otherwise they need to put down 20% 
   # Print the down payment 

house_price = 1000000  
good_credit = True 
bad_credit = False

if good_credit:
    downpayment_good = 0.1 * house_price
    print("Down Payment:" + str(downpayment_good))  # Have to cast float object to string before concatenating 
else:
    downpayment_bad = 0.2 * house_price
    print("Down Payment:" + str(downpayment_bad))
    
    