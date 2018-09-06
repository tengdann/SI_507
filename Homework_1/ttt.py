'''
SI 507 Fall 2018 Homework 1
'''

# Create board - Setup the data structure for storing board data
    
bd = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ] # Indexed from bottom left; refer to keypad on keyboard 
    
print ("Welcome to tic-tac-toe! Moves will correspond to the numeric keypad on your keyboard. Enjoy!")

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

# Step 2: Player 1 moves; check to see if valid; edits bd
def player_one_move(bd):
    player_move = int(input("Player 1's move > "))

    while bd[player_move - 1] != ' ':
        print ("Sorry, invalid move!")
        player_move = int(input("Player 1's move > "))
        
    bd[player_move - 1] = 'X'

# Step 3: Print new board, and check if game is over

# Step 4: Player 2 moves; check to see if valid
def player_two_move(bd):    
    player_move = int(input("Player 2's move > "))
    
    while bd[player_move - 1] != ' ':
        print ("Sorry, invalid move!")
        player_move = int(input("Player 2's move > "))

    bd[player_move - 1] = 'O'
# Step 5: Print new board, and check if game is over

# Step 6: Determine if game is over
'''
Take in the current board data and determine if one player wins the game or the game draws. If the game is over,
terminate the loop, or continue the loop.
parameter: bd - current board data
return: information about current game status
'''

def determine_over(bd):
    # Need to do 9 checks; more elegent method?
    
    # First row matching
    if (' ' not in (bd[0], bd[1], bd[2]) and bd[0] == bd[1] == bd[2]):
        game_over_text(bd[1])
        return False
        
    # Second row matching
    elif (' ' not in (bd[3], bd[4], bd[5]) and bd[3] == bd[4] == bd[5]):
        game_over_text(bd[4])
        return False
        
    # Third row matching
    elif (' ' not in (bd[6], bd[7], bd[8]) and bd[6] == bd[7] == bd[8]):
        game_over_text(bd[7])
        return False
        
    # First column matching
    elif (' ' not in (bd[0], bd[3], bd[6]) and bd[0] == bd[3] == bd[6]):
        game_over_text(bd[3])
        return False
        
    # Second column matching
    elif (' ' not in (bd[1], bd[4], bd[7]) and bd[1] == bd[4] == bd[7]):
        game_over_text(bd[4])
        return False
        
    # Third column matching
    elif (' ' not in (bd[2], bd[5], bd[8]) and bd[2] == bd[5] == bd[8]):
        game_over_text(bd[5])
        return False
        
    # TL-BR diagonal matching
    elif (' ' not in (bd[6], bd[4], bd[2]) and bd[6] == bd[4] == bd[2]):
        game_over_text(bd[4])
        return False
        
    # TR-BL diagonal matching
    elif (' ' not in (bd[8], bd[4], bd[0]) and bd[8] == bd[4] == bd[0]):
        game_over_text(bd[4])
        return False
        
    # Cat's game
    elif bd.count(' ') == 1:
        print("Cat's game! No one wins :(")
        return False

    else:
        return True
    
    
def game_over_text(str):
    if str == 'X':
        print ("Player 1 wins!")
    elif str == 'O':
        print ("Player 2 wins!")


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
