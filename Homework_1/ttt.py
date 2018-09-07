'''
SI 507 Fall 2018 Homework 1
'''
# SSH test comment
# Create board - Setup the data structure for storing board data
    
bd = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ] # Indexed from bottom left; refer to keypad on keyboard

# For use in determine_game(); stores all possible winning triplets

WIN_COMB = [
(0, 1, 2), # First row
(3, 4, 5), # Second row
(6, 7, 8), # Third row
(0, 3, 6), # First column
(1, 4, 7), # Second column
(2, 5, 8), # Third column
(0, 4, 8), # BR - TL diagonal
(2, 4, 6)  # BL - TR diagonal
]

# Loop until game is over

# Step 1: Print board
'''
This function will take in current board data and print out the board in the console as shown 
in the instruction.
parameter: bd - a data structure used for holding current moves on the board
return: None
'''
def print_board(bd):
    print ("CURRENT BOARD: ")
    print (' ' + bd[6] + ' | ' + bd[7] + ' | ' + bd[8] + ' ')
    print ('-----------')
    print (' ' + bd[3] + ' | ' + bd[4] + ' | ' + bd[5] + ' ')
    print ('-----------')
    print (' ' + bd[0] + ' | ' + bd[1] + ' | ' + bd[2] + ' ')

# Step 2: Player one moves; checks to see move is valid as well
'''
REQUIRES: Board data variable
MODIFIES: Board data
EFFECTS: Checks if input is between 1 and 9, inclusive
         Checks if move has not already been done yet
         Edits board data with the player's move
'''
def player_one_move(bd):
    player_move = int(input("Player 1's move > "))
    
    # Checks if input is numerical value between 1 and 9
    while player_move < 1 or player_move > 9:
        print ("Sorry, invalid input!")
        player_move = int(input("Player 1's move > "))
    
    # Checks if move has not already been done yet
    while bd[player_move - 1] != ' ':
        print ("Sorry, invalid move!")
        player_move = int(input("Player 1's move > "))
    
    # Edits board data w/ player move
    bd[player_move - 1] = 'X'

# Step 3: Print board, and check if game is over

# Step 4: Player 2 moves; checks to see if move is valid
'''
REQUIRES: Board data variable
MODIFIES: Board data
EFFECTS: Checks if input is between 1 and 9, inclusive (sub-problem 1)
         Checks if move has not already been done yet (sub-problem 2)
         Edits board data with the player's move (sub-problem 3)
'''
def player_two_move(bd):
    player_move = int(input("Player 2's move > "))
    
    # Checks if input is numerical value between 1 and 9
    while player_move < 1 or player_move > 9:
        print ("Sorry, invalid input!")
        player_move = int(input("Player 2's move > "))
    
    # Checks if move has not already been done yet
    while bd[player_move - 1] != ' ':
        print ("Sorry, invalid move!")
        player_move = int(input("Player 2's move > "))
    
    # Edits board data w/ player move
    bd[player_move - 1] = 'O'

# Step 5: Print board

# Step 6: Determine if game is over
'''
Take in the current board data and determine if one player wins the game or the game draws. If the game is over,
terminate the loop, or continue the loop.
parameter: bd - current board data
return: information about current game status
'''

def determine_over(bd):        
    for a, b, c in WIN_COMB:
        if bd[a] == bd[b] == bd[c] == 'X':
            print ("Player 1 wins! Game over!")
            return False
        if bd[a] == bd[b] == bd[c] == 'O':
            print ("Player 2 wins! Game over!")
            return False

    if (bd.count(' ') == 0):
        print ("Cat's game, no one wins! :(")
        return False
    
    return True

# Actual game function                

while True:
    print()
    print_board(bd)

    # Step 2: Player 1 moves; check to see if valid
        
    player_one_move(bd)

    # Step 3: Print new board and check if game is over
    
    print_board(bd)
    if not determine_over(bd): break

    # Step 4: Player 2 moves; check to see if valid
    
    player_two_move(bd)
    
    # Step 5: Print new board and check if game is over
    
    print_board(bd)
    
    # Step 6: Determine if the game is over
    if not determine_over(bd): break
