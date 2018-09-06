'''
SI 507 Fall 2018 Homework 1
'''

# Create board - Setup the data structure for storing board data
    
board_data = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ] # Indexed from bottom left; refer to keypad on keyboard 
game_status = True
    
print ("Welcome to tic-tac-toe! Moves will correspond to the numeric keypad on your keyboard. Enjoy!")

# Loop until game is over

# Step 1: Print board
'''
This function will take in current board data and print out the board in the console as shown 
in the instruction.
parameter: board_data - a data structure used for holding current moves on the board
return: None
'''
def print_board(board_data):
	print ("CURRENT BOARD: ")
	print (' ' + board_data[6] + ' | ' + board_data[7] + ' | ' + board_data[8] + ' ')
	print ('-----------')
	print (' ' + board_data[3] + ' | ' + board_data[4] + ' | ' + board_data[5] + ' ')
	print ('-----------')
	print (' ' + board_data[0] + ' | ' + board_data[1] + ' | ' + board_data[2] + ' ')

# Step 2: Player 1 moves; check to see if valid; edits board_data
def player_one_move(board_data):
    player_move = int(input("Player 1's move > "))

    while board_data[player_move - 1] != ' ':
        print ("Sorry, invalid move!")
        player_move = int(input("Player 1's move > "))
        
    board_data[player_move - 1] = 'X'

# Step 3: Print new board, and check if game is over

# Step 4: Player 2 moves; check to see if valid
def player_two_move(board_data):    
    player_move = int(input("Player 2's move > "))
    
    while board_data[player_move - 1] != ' ':
        print ("Sorry, invalid move!")
        player_move = int(input("Player 2's move > "))

    board_data[player_move - 1] = 'O'
# Step 5: Print new board, and check if game is over

# Step 6: Determine if game is over
'''
Take in the current board data and determine if one player wins the game or the game draws. If the game is over,
terminate the loop, or continue the loop.
parameter: board_data - current board data
return: information about current game status
'''

def determine_over(board_data):
    # Need to do 9 checks; more elegent method?
    
    # First row matching
    if board_data[0] == board_data[1] == board_data[2]:
		game_over_text(board_data[1])
		return False
        
    # Second row matching
    if board_data[3] == board_data[4] == board_data[5]:
		game_over_text(board_data[4])
		return False
        
    # Third row matching
    if board_data[6] == board_data[7] == board_data[8]:
		game_over_text(board_data[7])
		return False
        
    # First column matching
    if board_data[0] == board_data[3] == board_data[6]:
		game_over_text(board_data[3])
		return False
        
    # Second column matching
    if board_data[1] == board_data[4] == board_data[7]:
		game_over_text(board_data[4])
		return False
        
    # Third column matching
    if board_data[2] == board_data[5] == board_data[8]:
		game_over_text(board_data[5])
		return False
        
    # TL-BR diagonal matching
    if board_data[6] == board_data[4] == board_data[2]:
		game_over_text(board_data[4])
		return False
        
    # TR-BL diagonal matching
    if board_data[8] == board_data[4] == board_data[0]:
		game_over_text(board_data[4])
		return False
        
    # Cat's game
    if board_data.count(' ') == 1:
        print("Cat's game! No one wins :(")
        return False
		
	return True
    
    
def game_over_text(str):
    if str == 'X':
        print ("Player 1 wins!")
    elif str == 'O':
        print ("Player 2 wins!")


# Actual game function                

while True:
    print()
    print_board(board_data)

    # Step 2: Player 1 moves; check to see if valid
        
    player_one_move(board_data)

    # Step 3: Print new board and check if game is over
    
    print_board(board_data)
    if not determine_over(board_data): break

    # Step 4: Player 2 moves; check to see if valid
    
    player_two_move(board_data)
    
    # Step 5: Print new board and check if game is over
    
    print_board(board_data)
    if not determine_over(board_data): break
    
    # Step 6: Determine if the game is over
    if not determine_over(board_data): break
