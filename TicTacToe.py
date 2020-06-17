import time
#The board in which We'll be playing TicTacToe
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]
#The Below Three Variables are Global Variables.
# Which are altered by the functions Below 
#If the first variable Becomes False.Then the game ends
game_still_going = True
#The Second Variable tells who is the winner or whether it is a tie
winner = None
#This Variable Tells us whose turn it is.
current_player = 'X'

#This Function will display the board and it's in the subsequent turns
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    
#The actions on the board will be performed Here
def play_game():
    display_board()
    #This is to check the status of the game on the board
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    #This block of code will tell us Who won or whether it's a Tie
    if winner == 'X' or winner == 'O':
        print(winner + " Wins")
    elif winner == None:
        print("Tie")
    time.sleep(10)
        

#This Function tells us whose turn it is and
# what is the status of the board.
# What are slots available in the Board etc.
def handle_turn(current_player):
    print(current_player + "'s Turn.")
    position = input("Choose a position from 1-9 : ")
    valid =False
#This loop ask us to put the piece in the right spot on the board
#If the user violates the rules by
#placing in taken spot or by
#entering values outside of the range of values
#which are asked, then the program will consistenly ask the user to
#the right thing
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position from 1-9 : ")
        position = int(position) - 1
        if board[position] == '-':
            valid = True
        else:
            print("Please don't violate the rules.")
#The spot the board will be filled by either
# 'X' or 'O'
    board[position] = current_player
    display_board()
    
#This Function Tells whether is game has ended or not
def check_if_game_over():
    check_for_winner()
    check_if_tie()
    
#This Function tells us Who won the game by
#checking the row and columns and diagonal
def check_for_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    
    
#This Function checks the rows to determine which piece has won    
def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    

#This Function checks the columns to determine which piece has won
def check_columns():
    global game_still_going
    columns_1 = board[0] == board[3] == board[6] != "-"
    columns_2 = board[1] == board[4] == board[7] != "-"
    columns_3 = board[2] == board[5] == board[8] != "-"
    if columns_1 or columns_2 or columns_3:
        game_still_going = False
    if columns_1:
        return board[0]
    elif columns_2:
        return board[1]
    elif columns_3:
        return board[2]
    
    
#This Function determines which piece has won by checking the diagonals
def check_diagonals():
    global game_still_going
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"
    
    if diagonals_1 or diagonals_2:
        game_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]
    
    
#This Function Determines whether it is a Tie or not
#It figures out by checking whether
#there are any empty slots in the board or not
def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False
        
    
#This Function is used to Exchange the turns
def flip_player():
    global current_player
    if current_player == 'X':
        
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
            
    
#We'll call this function to start the game
play_game()
    
    
