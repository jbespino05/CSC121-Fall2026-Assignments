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
      grade = float(input("Enter" + student_name + "'s grade: "))
      # Store the student's name and grade
      gradebook[student_name] = grade
      
# PROGRAM LOGIC
# Create an empty dictionary to store the student's grades
gradebook = {}

# Call the function to add students
add_students(gradebook)

# Display the dictionary to check that it works
print(gradebook)
