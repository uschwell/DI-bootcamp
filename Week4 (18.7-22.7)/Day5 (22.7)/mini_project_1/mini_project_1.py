
 #relevant data for the game overall (accesable for/by most of the functions)
 #I used this as a common reference point-this will make it easier to expand the game in the future if I want to
GUI_data={"width":15, "height":7, "horizontal_lines":"---"}

player_moves=[
    [' ',' ', ' '],
    [' ',' ', ' '],
    [' ',' ', ' ']
]
global game_flag


#draws a box-the middle space will be written with whatever the relevant 'content' is
def draw_box(content):
    temp_string=''
    temp_string+=(" "+str(content)+" ")
    return temp_string

#will draw a row (built of several boxes)
def draw_row(matrix_row):
    print_string='* '
    for box in range(len(matrix_row)):
        print_string+=draw_box(matrix_row[box])
        #we print a | between each box (except the last one)
        if(box<(len(matrix_row)-1)):
            print_string+="|"
    #finally, we add the last " *" to the row
    print_string+=" *"
    print(print_string)

#will draw the "dividing line" between rows
def draw_divider():
    print("* ---|---|--- *")


#draws the entire "game board"
def display_board():
    #top line
    for x in range(GUI_data["width"]):
        print("*", end='')
    print('')
    #we draw each line of boxes
    for row in range(len(player_moves)):
        draw_row(player_moves[row])
        #if we aren't on the last row-we add the "in between" row
        if(row<(len(player_moves)-1)):
            draw_divider()

    #bottom line
    for x in range(GUI_data["width"]):
        print("*", end='')
    print('')





def player_input(player, player_moves):
    listOfGlobals = globals()
    print("Player "+player+"'s Turn....")
    row=input("Enter row: ")
    col=input("Enter column: ")
    #we check if that is a legal move or if the person wants to quit
    if((row=='q')or(col=='q')):
        listOfGlobals['game_flag']=(-1)
    elif((player_moves[int(row)-1][int(col)-1])==' '):
         ##if it is- we then add that move to the game board
        player_moves[int(row)-1][int(col)-1]=str(player)
    else:
        print("that space is already taken!")
















#this function will be used to check our 'win' condition- it sees if there are any 'chains' of at least 3 consecutive entries from the same player
def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0

def check_manager(board):
    #transposition to check rows, then columns
    for newBoard in [board]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)



def check_win(player, player_moves):
    listOfGlobals = globals()
    print("entered check_win!")
    answer=check_manager(player_moves)
    if(answer=='X')or(answer=='Y'):
        return 1
    else:
        return 0




def play():
    print("Welcome to Tic Tac Toe!")
    listOfGlobals = globals()
    listOfGlobals['game_flag']=1
    print(listOfGlobals['game_flag'])
    #upon starting the game- we run this loop until the "win" condition is acheived (as determined by 'check_win()')
    while(listOfGlobals['game_flag']):
        #we build our basic GUI game board
        display_board()

        #then we check for player input
        player_input('X',player_moves)
        #check our flag to see if anyone 'quit' the game
        if(listOfGlobals['game_flag']!=1):
            break
        #we check if X just won-if yes, we end the game
        if(check_win('x', player_moves)):
            display_board()
            print("X has won the game!")
            break
        #we display the updated board
        display_board()

        player_input('O',player_moves)
        #check our flag to see if anyone 'quit' the game
        if(int(listOfGlobals['game_flag'])!=1):
            break

        #we check if Y just won
                #we check if X just won-if yes, we end the game
        if(check_win('y', player_moves)):
            display_board()
            print("Y has won the game!")
            break
        
        #we display the updated board
        display_board()




#we start our game
play()