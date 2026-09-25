# IMPORT STATEMENTS
# (NONE)

# FUNCTION DEFINITIONS 
# 1. Define calculate_ticket(age, hour)
# 2. Logic: If age <= 12 or age >= 65, price = 8. Otherwise, price = 12.
# 3. Logic: If hour < 17, subtract 2 from the price.
# 4. Print the final price.

# PROGRAM LOGIC
# 1. input() for age (int)
# 2. input() for movie hour (int)
# 3. Call calculate_ticket()

def calculate_ticket(age, hour):
  if age <= 12 or age >= 65:
    price = 8
  else: 
    price = 12
    print(price)

calculate_ticket(20,19)
