# IMPORT STATEMENTS
# 1. Import math
import math

# FUNCTION DEFINITIONS

# 1. Define area(radius): returns pi * r squared
def area(radius):
  return math.pi * radius ** 2
# 2. Define circumference(radius): returns 2 * pi * r
def circumference(radius):
  return 2 * math.pi * radius
# 3. Define volume(radius, height): 
#    - Call area(radius) and multiply by height.
#    - Return the result.

# PROGRAM LOGIC
# 1. Input for radius (float)
radius = float(input("Enter radius: "))
# 2. Call and print area and circumference.
print("Area:", area(radius))
print("Circumference:", circumference(radius))
# 3. Input for height (float)
# 4. Call and print volume.


