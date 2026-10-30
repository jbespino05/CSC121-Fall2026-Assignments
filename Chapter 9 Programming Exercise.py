# IMPORT STATEMENTS

# FUNCTION DEFINITIONS
def add_players(roster):
    while True:
        name = input("Enter player name (or 'quit' to stop): ")
        if name == "quit":
            break
        roster.append(name)
# PROGRAM LOGIC
roster = []
add_players(roster)
print("Current roster:", roster)
