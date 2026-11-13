# NAME: rectangle.py


# IMPORT STATEMENTS


# FUNCTION DEFINITIONS 
# Define a function that takes the length and width of a rectangle
def calculate_rectangle(length, width):
  # Calculate the area of the rectangle
  area = length * width
  # Calculate the perimeter of the rectangle
  perimeter = 2 * (length + width)
  # Return the area and perimeter together as a tuple
  return (area, perimeter)

# PROGRAM LOGIC
# Ask the user to enter the length of the rectangle
length = float(input("Enter length: "))
# Ask the user to enter the width of the rectangle
width = float(input("Enter width: "))
# Call the function and unpack the returned tuple
my_area, my_perimeter = calculate_rectangle(length, width)
# Show the calculated area and perimeter 
print("--- Results ---")
print("The Area is:", my_area)
print("The perimeter is:", my_perimeter)
