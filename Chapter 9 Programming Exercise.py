# IMPORT STATEMENTS

# FUNCTION DEFINITIONS
def add_players(roster):
    while True:
        name = input("Enter player name (or 'quit' to stop): ")
        if name == "quit":
            break
        roster.append(name)
def is_on_roster(roster, player_name):
    for player in roster:
        if player == player_name:
            return True
    return False
# PROGRAM LOGIC
roster = []
add_players(roster)
search_name = input("Who would you like to search for? ")
if is_on_roster(roster, search_name):
    print("Result: Player found!")
else:
    print("Result: Player not found.")
    
