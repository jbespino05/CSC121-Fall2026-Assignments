# IMPORT STATEMENTS
# (NONE)

# FUNCTION DEFINITIONS 
# 1. Define print_bio with three parameters: name, age, and goal.
# 2. Inside the function, use string multiplication (*) for a border line. 
# 3. Print the bio details using the parameter names. 

# PROGRAM LOGIC 
# 1. Call print_bio using my own info
# 2. Call print_bio using Keanu Reeves 
# 3. Call print_bio using Batman 

def print_bio(name, age, goal):
  print("*" * 25)
  print("name:", name)
  print("age:", age)
  print("goal:", goal)
  print("*" * 25)
  
print_bio("Jose", 20, "Become a structural engineer")
print()
print_bio("Keanu Reeves", 62, "Continue acting career")
print()
print_bio("Batman", 67, "Protect Gotham City")
