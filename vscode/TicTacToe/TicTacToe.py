import random 
import sys
#Variables
wall="|"

def template(wall): #possible placement on the board
    print(wall,"0",wall,"1",wall,"2",wall) 
    print(wall,"3",wall,"4",wall,"5",wall)
    print(wall,"6",wall,"7",wall,"8",wall)

def draw_board(board): 
    """fonction that print the updated board with sign"""
    print(wall,board[0],wall,board[1],wall,board[2],wall) 
    print(wall,board[3],wall,board[4],wall,board[5],wall)
    print(wall,board[6],wall,board[7],wall,board[8],wall)
    print_line()

def print_line():
    print("________________________________________")

def game_launch():
    empty=" "
    board=[empty,empty,empty,empty,empty,empty,empty,empty,empty]
    signX="X"
    signO="O"

    def is_player1_winning():#winning condition for player 1
        if (((board[0]==player1_sign and board[1]==player1_sign and board[2])==player1_sign)or
        ((board[3]==player1_sign and board[4]==player1_sign and board[5])==player1_sign)or
        ((board[6]==player1_sign and board[7]==player1_sign and board[8])==player1_sign) or
        ((board[0]==player1_sign and board[3]==player1_sign and board[6])==player1_sign) or
        ((board[1]==player1_sign and board[4]==player1_sign and board[7])==player1_sign) or
        ((board[2]==player1_sign and board[5]==player1_sign and board[8])==player1_sign) or
        ((board[0]==player1_sign and board[4]==player1_sign and board[8])==player1_sign) or
        ((board[2]==player1_sign and board[4]==player1_sign and board[6])==player1_sign)):
            return True
                
    def is_player2_winning():#winning condition for Player 2           
        if (((board[0]==player2_sign and board[1]==player2_sign and board[2])==player2_sign) or
        ((board[3]==player2_sign and board[4]==player2_sign and board[5])==player2_sign) or
        ((board[6]==player2_sign and board[7]==player2_sign and board[8])==player2_sign) or
        ((board[0]==player2_sign and board[3]==player2_sign and board[6])==player2_sign) or
        ((board[1]==player2_sign and board[4]==player2_sign and board[7])==player2_sign) or
        ((board[2]==player2_sign and board[5]==player2_sign and board[8])==player2_sign) or
        ((board[0]==player2_sign and board[4]==player2_sign and board[8])==player2_sign) or
        ((board[2]==player2_sign and board[4]==player2_sign and board[6])==player2_sign)):   
            return True   

    def is_ai_winning():#winning condition for AI
        if (((board[0]==player1_sign and board[1]==player1_sign and board[2])==player1_sign)or
        ((board[3]==player1_sign and board[4]==player1_sign and board[5])==player1_sign)or
        ((board[6]==player1_sign and board[7]==player1_sign and board[8])==player1_sign) or
        ((board[0]==player1_sign and board[3]==player1_sign and board[6])==player1_sign) or
        ((board[1]==player1_sign and board[4]==player1_sign and board[7])==player1_sign) or
        ((board[2]==player1_sign and board[5]==player1_sign and board[8])==player1_sign) or
        ((board[0]==player1_sign and board[4]==player1_sign and board[8])==player1_sign) or
        ((board[2]==player1_sign and board[4]==player1_sign and board[6])==player1_sign)):
            return True      

    print_line()
    input("TiTacToe Game modes :\n-2 Players\n-Vs AI\n Press enter to continue") #introduction
    game_mode_=input("Do you want to play the 2 players mode ? Y/N \n") #choose game mode

    #game mode 2 players
    if game_mode_=="Y": 
        #variable
        print_line()
        print("Loading 2 player mode\n")
        player1_sign=""
        player2_sign=""

        #player 1 choose a signe
        player1_sign=input("Player 1 choose a sign: O or X\n")
        if player1_sign==signO:
            player2_sign=signX
        elif player1_sign==signX: 
            player2_sign=signO
        else:
            input("Invalide input. Quitting")
            sys.exit()
            

        print("player 1 sign :",player1_sign,"\nPlayer 2 sign: ",player2_sign)
        print_line()
        template(wall)

        #game start max 10 turn
        turn=1
        while turn <10:
        #player 1 turn
            player1_choice=int(input("Player 1 turn \n Choose a number(0-8): ")) #ask the player for a number
            while board[player1_choice]==player1_sign or board[player1_choice]==player2_sign: #if signe already used on the board, ask again
                print("Already used") 
                player1_choice=int(input(" Choose a number(0-8): "))

            if board[player1_choice]==empty: 
                board[player1_choice]=player1_sign

            print_line()
            print("Turn :",turn, "| Player 1 choice :",player1_choice)
            draw_board(board)
            
            if is_player1_winning() ==True:
                print("Player 1 win !")
                game_launch() #restart the game
                
            turn+=1
            if turn>9:
                print("Draw !")
                game_launch() 

        #player 2 turn
            player2_choice=int(input("Player 2 turn \n Choose a number(0-8): "))
            while board[player2_choice]==player1_sign or board[player2_choice]==player2_sign:
                print("Already used")
                player2_choice=int(input(" Choose a number(0-8): "))

            if board[player2_choice]==empty: 
                board[player2_choice]=player2_sign

            print_line()
            print("Turn :",turn, "| Player 2 choice :",player2_choice)
            draw_board(board)

            if is_player2_winning() ==True:
                print("Player 2 win !")
                game_launch() #restart the game
                
            turn+=1
    #game mode VS IA
    elif game_mode_=="N":
        print_line()
        print("loading VS IA mode")
        player1_sign=""
        signe=""

        #choosing a sign
        player1_sign=input("Player 1 choose a sign: O or X\n")
        if player1_sign==signO:
            signe=signX
        elif player1_sign==signX: 
            signe=signO
        else:
            input("Invalide input. Quitting")
            sys.exit()

        print("player 1 sign :", player1_sign,"\n AI sign :", signe)
        print_line()
        template(wall)

        #game start
        turn=1
        while turn <10: 

            #player1 turn
            player1_choice=int(input("Player 1 turn\n Choose a number(0-8): ")) 
            while board[player1_choice]==player1_sign or board[player1_choice]==signe:
                print("Already used")
                player1_choice=int(input(" Choose a number(0-8): "))

            if board[player1_choice]==empty: 
                board[player1_choice]=player1_sign
                
            print_line()
            print("Turn :",turn, "| Player 1 choice :",player1_choice)
            draw_board(board)

            if is_player1_winning() ==True:
                print("Player 1 win !")
                game_launch() #restart the game
            turn+=1

            if turn>9:
                print("Draw")        
                game_launch() 
        
            #AI turn     (IA lvl 2 - most played placement)
            def ia(board,signe):
                AI_choice=""
                corner=(0,2,6,8)
                middle=(1,3,5,7)
                if board[4]==empty: #if placement 4 possible, do it
                    AI_choice=4
                elif (board[0]==empty or board[2]==empty or board [6]==empty or board[8]==empty): #else randomly take corner until there is none left
                        AI_choice=random.choice(corner)
                        while board[AI_choice]==player1_sign or board[AI_choice]==signe: #while there is a sign there, ai choose again
                            AI_choice=random.choice(corner)
                elif (board[1]==empty or board[3]==empty or board [5]==empty or board[7]==empty): #else randomly take middle
                        AI_choice=random.choice(middle)
                        while board[AI_choice]==player1_sign or board[AI_choice]==signe:
                            AI_choice=random.choice(middle)
                else:
                    return False
                return AI_choice
            AI_choice=ia(board,signe) 

            #choice of placement of IA
            if board[AI_choice]==empty: 
                board[AI_choice]=signe  

            print_line()
            print("Turn :",turn, "| Ai choice :",AI_choice)
            draw_board(board)

            if is_ai_winning() ==True:
                print("AI win !")
                game_launch() #restart the game
            turn+=1

    else:
        print("incorret input. Quitting")
        sys.exit
game_launch()
