# IMPORT STATEMENTS


# FUNCTION DEFINITIONS 
# Create a function that receives the gradebook 
def add_students(gradebook):
  # Ask for students until the user types in "done"
  while True:
    # Ask the user to enter a student's name
    student_name = input("Enter student name (or 'done'): ")
    # Stop the loop when the user types done
    if student_name == "done":
      break
      # Ask for the student's grade
      grade = float(input("Enter " + student_name + "'s grade: "))
      # Store the student's name and grade
      gradebook[student_name] = grade
      
# Create a function to calculate the class average
def calculate_average(gradebook):
  # Check if the gradebook is empty to avoid dividing by zero
  if len(gradebook) == 0:
    return 0
  # Add all the grades and divide by the number of students
  average = sum(gradebook.values()) / len(gradebook) 
  # Return the average
  return average
    
# PROGRAM LOGIC
# Create an empty dictionary to store the students' grades
gradebook = {}
# Call the function to add students
add_students(gradebook)
# Calculate the class average
class_average = calculate_average(gradebook)
# Show the class report 
print("\n--- Class Report ---")
# Display each student's name and grade
for student_name, grade in gradebook.items():
  print(f"{student_name}: {grade:g}")
# Show the class average with 2 decimal places
print(f"Class Average: {class_average:.2f}")
