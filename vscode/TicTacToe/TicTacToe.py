import random 
import sys
#Variables
empty=" "
wall="|"
player1_sign=""
player2_sign=""
signe=""
signX="X"
signO="O"
AI_choice=""
corner=(0,2,6,8)
middle=(1,3,5,7)

def template(wall): #possible placement on the board
    print(wall,"0",wall,"1",wall,"2",wall) 
    print(wall,"3",wall,"4",wall,"5",wall)
    print(wall,"6",wall,"7",wall,"8",wall)
    print()

def draw_board(board): 
    """fonction that print the updated board with sign"""
    print(wall,board[0],wall,board[1],wall,board[2],wall) 
    print(wall,board[3],wall,board[4],wall,board[5],wall)
    print(wall,board[6],wall,board[7],wall,board[8],wall)
    print("________________________________________")

    print()
def game_launch():
    board=[empty,empty,empty,empty,empty,empty,empty,empty,empty]
    print("________________________________________")
    print()
    input("TiTacToe Game modes :\n-2 Players\n-Vs AI\n Press enter to continue") #introduction
    game_mode_=input("Do you want to play the 2 players mode ? Y/N \n") #choose game mode

    #game mode 2 players
    if game_mode_=="Y": 
        print("________________________________________")
        print("Loading 2 player mode")
        print()
        
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
        print("________________________________________")
        print()
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

            print("________________________________________")
            print()
            print("Turn :",turn, "| Player 1 choice :",player1_choice)
            draw_board(board)

            #winning condition for player 1
            if (((board[0]==player1_sign and board[1]==player1_sign and board[2])==player1_sign)or
                ((board[3]==player1_sign and board[4]==player1_sign and board[5])==player1_sign)or
                ((board[6]==player1_sign and board[7]==player1_sign and board[8])==player1_sign) or
                ((board[0]==player1_sign and board[3]==player1_sign and board[6])==player1_sign) or
                ((board[1]==player1_sign and board[4]==player1_sign and board[7])==player1_sign) or
                ((board[2]==player1_sign and board[5]==player1_sign and board[8])==player1_sign) or
                ((board[0]==player1_sign and board[4]==player1_sign and board[8])==player1_sign) or
                ((board[2]==player1_sign and board[4]==player1_sign and board[6])==player1_sign)):
                print("Player 1 win !")
                game_launch() #restart the game
                break
                
            turn+=1
            if turn>9:
                print("Draw !")
                break

        #player 2 turn
            player2_choice=int(input("Player 2 turn \n Choose a number(0-8): "))
            while board[player2_choice]==player1_sign or board[player2_choice]==player2_sign:
                print("Already used")
                player2_choice=int(input(" Choose a number(0-8): "))

            if board[player2_choice]==empty: 
                board[player2_choice]=player2_sign

            print("________________________________________")
            print()
            print("Turn :",turn, "| Player 2 choice :",player2_choice)
            draw_board(board)
            #winning condition for Player 2
            if (((board[0]==player2_sign and board[1]==player2_sign and board[2])==player2_sign) or
            ((board[3]==player2_sign and board[4]==player2_sign and board[5])==player2_sign) or
            ((board[6]==player2_sign and board[7]==player2_sign and board[8])==player2_sign) or
            ((board[0]==player2_sign and board[3]==player2_sign and board[6])==player2_sign) or
            ((board[1]==player2_sign and board[4]==player2_sign and board[7])==player2_sign) or
            ((board[2]==player2_sign and board[5]==player2_sign and board[8])==player2_sign) or
            ((board[0]==player2_sign and board[4]==player2_sign and board[8])==player2_sign) or
            ((board[2]==player2_sign and board[4]==player2_sign and board[6])==player2_sign)):
                print("Player 2 win !")
                game_launch()
                break
            turn+=1
    #game mode VS IA
    elif game_mode_=="N":
        print("________________________________________")
        print("loading VS IA mode")
        print()
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
        print("________________________________________")
        print()
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
                
            print("________________________________________")
            print()
            print("Turn :",turn, "| Player 1 choice :",player1_choice)
            draw_board(board)

            #winning condition for player 1
            if (((board[0]==player1_sign and board[1]==player1_sign and board[2])==player1_sign) or
            ((board[3]==player1_sign and board[4]==player1_sign and board[5])==player1_sign) or
            ((board[6]==player1_sign and board[7]==player1_sign and board[8])==player1_sign) or
            ((board[0]==player1_sign and board[3]==player1_sign and board[6])==player1_sign) or
            ((board[1]==player1_sign and board[4]==player1_sign and board[7])==player1_sign) or
            ((board[2]==player1_sign and board[5]==player1_sign and board[8])==player1_sign) or
            ((board[0]==player1_sign and board[4]==player1_sign and board[8])==player1_sign) or
            ((board[2]==player1_sign and board[4]==player1_sign and board[6])==player1_sign)):
                print("Player 1 win !")
                game_launch()
                break
            turn+=1

            if turn>9:
                print("Draw")        
                break
        
            #AI turn     (IA lvl 2 - most played placement)
            def ia(board,signe):
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

            print("________________________________________")
            print()
            print("Turn :",turn, "| Ai choice :",AI_choice)
            draw_board(board)

            #winning condition for AI 
            if (((board[0]==signe and board[1]==signe and board[2])==signe) or 
            ((board[3]==signe and board[4]==signe and board[5])==signe) or
            ((board[6]==signe and board[7]==signe and board[8])==signe) or
            ((board[0]==signe and board[3]==signe and board[6])==signe) or
            ((board[1]==signe and board[4]==signe and board[7])==signe) or
            ((board[2]==signe and board[5]==signe and board[8])==signe) or
            ((board[0]==signe and board[4]==signe and board[8])==signe) or
            ((board[2]==signe and board[4]==signe and board[6])==signe)):
                print("AI win !")
                game_launch() 
                break
            turn+=1

    else:
        print("incorret input. Quitting")
        sys.exit
game_launch()

    #____________________________________________________________________________________

        #     #IA temporaire
        # if difficulty==0:
        #     print("diffuclty selected :",difficulty)

        #     AI_choice=random.randrange(0,8)       #valeur returnné par la fonction a changer
        #     while board[AI_choice]==signe or board[AI_choice]==player1_sign:
        #         AI_choice=random.randrange(0,8) #make an or with if
        #     # elif board[AI_choice]==signe_joueur:
        #         AI_choice=random.randrange(0,8)  #trying for looping test, need to change with alogrythm
        #     board[AI_choice]=signe
    #____________________________________________________________________________________

            #IA fonction lvl 1 - randomness
        # if difficulty==1:
        #     print("diffuclty selected :",difficulty)

        #     def ia(board,signe): #simple ia
        #         AI_choice=random.randrange(0,8) #choix de lia est egale a un chiffre leatoire entre 0 et 8
        #         if board[AI_choice]==signe or board[AI_choice]==player1_sign: #tant que le chiffre de lia est egale a son sign ou celui du joueur
        #             AI_choice=random.randrange(0,8) #make an or with if --  continue de chosir
        #         else:
        #             return False
        #         return AI_choice # returnne le choix de l'emplacement
        #             #else retrn false to addN
        #     AI_choice=ia(board,signe) #variable conentant l'emplacement updated
        #     #need this last one activated
    #_________________________________________________________________________________
        


    # # ia  block player
    
    #     def ia(board,signe):
    #         # 

    #         if board[4]==variable_vide:
    #             AI_choice=4
    #         elif (board[0]==variable_vide or board[2]==variable_vide or board [6]==variable_vide or board[8]==variable_vide): #choose 8
    #                 AI_choice=random.choice(corner)
    #                 while board[AI_choice]==player1_sign or board[AI_choice]==signe:
    #                     AI_choice=random.choice(corner)
    #         elif (board[1]==variable_vide or board[3]==variable_vide or board [5]==variable_vide or board[7]==variable_vide):
    #                 AI_choice=random.choice(middle)
    #                 while board[AI_choice]==player1_sign or board[AI_choice]==signe:
    #                     AI_choice=random.choice(middle)
    #         else:
    #             return False
    #         return AI_choice
    #     AI_choice=ia(board,signe) #activate this
    # #     def ia(board,signe):
    # #         if player1_sign in row1:
    # #             print("what")


    #         # if board[0]==player1_sign or board[1]==player1_sign or board[2] ==player1_sign:
    #         #     AI_choice=random.choice(row1)
    #         # elif board[3]==player1_sign or board[4]==player1_sign or board[5] ==player1_sign:
    #         #     AI_choice=random.choice(row2)
    #         # elif board[6]==player1_sign or board[7]==player1_sign or board[8] ==player1_sign:
    #         #     AI_choice=random.choice(row3)

    #     ia(board,signe)
            
            # if board[4]==variable_vide:
            #     AI_choice=4
            # elif board[0]==signe_joueur:
            #     AI_choice=8
            # elif board[1]==signe_joueur:
            #     AI_choice=7
            # elif board[2]==signe_joueur:
            #     AI_choice=6
            # elif board[3]==signe_joueur:
            #     AI_choice=5
            # elif board[5]==signe_joueur:
            #     AI_choice=3
            # elif board[6]==signe_joueur:
            #     AI_choice=2
            # elif board[7]==signe_joueur:
            #     AI_choice=1
            # elif board[8]==signe_joueur:
            #     AI_choice=0
            # elif board[1]==signe_joueur or board[3]==signe_joueur or board[5] ==signe_joueur or board[7]==signe_joueur:
            #     AI_choice=random.choice(corner)

            #efif any player emplacemnt : place 
            # for i in range(8):






            # elif (board[0]==variable_vide or board[2]==variable_vide or board [6]==variable_vide or board[8]==variable_vide): #choose 8
            #         AI_choice=random.choice(corner)
            #         while board[AI_choice]==signe or board[AI_choice]==signe_joueur:
            #             AI_choice=random.choice(corner)
            # else:
            #     AI_choice=random.choice(middle)
            #     while board[AI_choice]==signe or board[AI_choice]==signe_joueur:
            #             AI_choice=random.choice(middle)
            
        #     return AI_choice #activate this
        #        #else return false to add
        # AI_choice=ia(board,signe) #activate this


        
        # def ia(board,signe):
            #if player can win:
                #play to block (how?)
            #elif ai can win:
                #play it
            #else:
                #if 4 = vide:
                    #play it
                #elif 0 2 6 8 ==vide:
                    #play it (random?)
                #else:
                    #play 1357 (random?)