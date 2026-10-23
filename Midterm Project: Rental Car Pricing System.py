# NAME: rentalcar.py
# IMPORT STATEMENTS

# FUNCTION DEFINITIONS

# Function 1: Get the car type and its daily cost
def get_car_info(car_type):
  if car_type == "B":
    return "Budget", 40
  elif car_type == "S":
    return "Standard", 60
  elif car_type == "L":
    return "Luxury", 80
else:
  return None, 0
# Input: B, S, or L
# Output: Name and daily cost of the car

# Function 2: Calculate mileage
def calculate_miles(start_miles, end_miles):
    total_miles = end_miles - start_miles

    if total_miles > 100:
        charged_miles = total_miles - 100
    else:
        charged_miles = 0

    return total_miles, charged_miles
  
# Input: Starting and ending odometer readings
# Output: Total miles and miles charges

# Function 3: Calculate the rental bill
def calculate_bill(daily_rate, days_rented, charged_miles):
  rental_cost = daily_rate * days_rented
  mileage_cost = charged_miles * 0.35

  total_bill = rental_cost + mileage_cost
  return total_bill
# Input: Daily cost, days rented, and miles charged 
# Output: Total bill 

# PROGRAM LOGIC
car_type = input("Enter classification code (B, S, L): ").upper()

while car_type not in ("B", "S", "L"):
  print("Invalid classification. Please try again.")
  car_type = input("Enter classification code (B, S, L): ").upper()
car_name, daily_rate = get_car_info(car_type)
start_miles = int(input("Start odometer: "))
end_miles = int(input("End odometer: "))

total_miles, charged_miles = calculate_miles(start_miles, end_miles)
days_rented = int(input("Days Rented: "))
total_bill = calculate_bill(daily_rate, days_rented, charged_miles)

# Show the final rental summary
print()
print("---RENTAL SUMMARY--")
print("Classification:", car_name)
print("Total Miles:", total_miles)
print("Charged Miles:", charged_miles)
print(f"Total Bill: ${total_bill:.2f}")

# Ask user for car type (B, S, or L)
# Check if the car type is valid
# If invalid, ask the user to enter it again

# Ask for starting odometer reading
# Ask for ending odometer reading
# Ask for number of days rented

# Use functions to calculate miles and total bill

# Display rental summary
# Show full car type name
# Show total miles driven
# Show miles charged
# Show final bill amount

