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
# Test the function using a length of 5 and width of 10
print(calculate_rectangle(5,10))
