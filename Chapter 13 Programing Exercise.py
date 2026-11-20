# NAME: journal.py

# IMPORT STATEMENTS

# FUNCTION DEFINITIONS

# Create a function called write_entry
# Accept a filename and journal entry as parameters
def write_entry(filename, entry):
# Open the file in append mode
  file = open(filename, "a")
# Write the entry followed by a newline character
  file.write(entry + "\n")
# Close the file
  file.close()

# Create a function called read_journal
def read_journal(filename):

# Open the file in read mode
  try:
    file = open(filename, "r")
# Read file
    entries = file.read()
# Close the file
    file.close()
# Show the saved journal entries
    print("--- Your Journal ---")
    print(entries)
# Handle the error if the file does not exist
  except FileNotFoundError:
    print("No journal entries found.")
# PROGRAM LOGIC

# Set the filename to journal.txt
filename = "journal.txt"

# Start a while loop to keep the program running
while True:

# Ask the user to write, read, or quit
  choice = input("(W)rite, (R)ead, or (Q)uit? ").upper()

# If the user chooses W, ask for a journal entry
  if choice == "W":
    entry = input("Enter your entry: ")
    write_entry(filename, entry)
    # Tell the user that the entry was saved
    print("Entry saved")
  

# If the user chooses R, call read_journal
elif choice == "R":
# Call
  
  
# If the user chooses Q or types quit, end the loop
elif choice == "Q" or choice == "QUIT":
  print("Goodbye!")
  break
# Otherwise, display an invalid choice message
else:
  print("Invalid choice. Please try again.")
