# LOGICAL OPERATORS
# Use when have multiple conditions 
# Logical operator AND used to combine two conditions 
# Logical operator OR used to do certain things if conditions are true: At least one condition needs to be true
# Logical operator Not 



has_high_income = True
has_good_credit = True 

if has_high_income and has_good_credit:
    print("Eligible for loan")

# Only one condition has to be true 
if has_high_income or has_good_credit:
    print("Eligible for loan")


has_good_credit = True 
has_criminal_record = False 

# print message not printed if second condition is false 
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")