# IMPORT STATEMENTS
# (None)

# FUNCTION DEFINITIONS
# 1. Define verify_pin():
def verify_pin():
  pin = input("Enter Pin: ")
  while pin != "1234":
    print("Incorrect PIN. Try again.")
    pin = input("Enter PIN: ")

print("PIN verified.")
return True

# 2. Define withdraw(balance, amount):
#    - Check if enough money exists
#    - Return the new (or old) balance

# PROGRAM LOGIC
# 1. Set current_balance to 500
# 2. Call verify_pin()
# 3. Get withdrawal amount from user input
# 4. Update current_balance by calling withdraw()
# 5. Print the final balance
verify_pin()
