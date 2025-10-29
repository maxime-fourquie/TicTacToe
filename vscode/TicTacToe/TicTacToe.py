import random 

#Variables
variable_vide=" "
mur="|"
tour=1
board=[variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide]
signe_joueur1=""
signe_joueur2=""
signe=""
signX="X"
signO="O"
choix_IA=""
corner=(0,2,6,8)
center=(1,3,5,7)

def template(mur): #template for grid
    print(mur,"0",mur,"1",mur,"2",mur) 
    print(mur,"3",mur,"4",mur,"5",mur)
    print(mur,"6",mur,"7",mur,"8",mur)
    print()

def draw_board(board): 
    """docstring commentaire fonction"""
    print(mur,board[0],mur,board[1],mur,board[2],mur) 
    print(mur,board[3],mur,board[4],mur,board[5],mur)
    print(mur,board[6],mur,board[7],mur,board[8],mur)

input("TiTacToe Game modes :\n-2 Players\n-Vs AI\n Press enter to continue") 
mode_de_jeu_reponse=input("Do you want to play the 2 players mode ? Y/N \n") #choose game mode

#load 2 player mode
if mode_de_jeu_reponse=="Y": 
    print("________________________________________")
    print("Loading 2 player mode")
    print()

    #player 1 choose a signe
    signe_joueur1=input("Player 1 choose a sign: O or X\n")
    if signe_joueur1==signO:
        signe_joueur2=signX
    elif signe_joueur1==signX: 
        signe_joueur2=signO
    else:
        input("Invalide input. Quitting")

    print("player 1 sign :",signe_joueur1,"\nPlayer 2 sign: ",signe_joueur2)
    print("________________________________________")
    print()
    template(mur)

    #game start max 10 turn
    while tour <10:
        #player 1 turn
        choix_joueur1=int(input("Player 1 turn \n Choose a number(0-8): ")) #ask the player for a number
        while board[choix_joueur1]==signe_joueur1 or board[choix_joueur1]==signe_joueur2: #if signe already used on the board, ask again
            print("Already used") 
            choix_joueur1=int(input(" Choose a number(0-8): "))

        if board[choix_joueur1]==variable_vide: 
            board[choix_joueur1]=signe_joueur1

        print("________________________________________")
        print()
        print("Turn :",tour, "| Player 1 choice :",choix_joueur1)
        draw_board(board)

        #winning condition for player 1
        if (((board[0]==signe_joueur1 and board[1]==signe_joueur1 and board[2])==signe_joueur1)or
            ((board[3]==signe_joueur1 and board[4]==signe_joueur1 and board[5])==signe_joueur1)or
            ((board[6]==signe_joueur1 and board[7]==signe_joueur1 and board[8])==signe_joueur1) or
            ((board[0]==signe_joueur1 and board[3]==signe_joueur1 and board[6])==signe_joueur1) or
            ((board[1]==signe_joueur1 and board[4]==signe_joueur1 and board[7])==signe_joueur1) or
            ((board[2]==signe_joueur1 and board[5]==signe_joueur1 and board[8])==signe_joueur1) or
            ((board[0]==signe_joueur1 and board[4]==signe_joueur1 and board[8])==signe_joueur1) or
            ((board[2]==signe_joueur1 and board[4]==signe_joueur1 and board[6])==signe_joueur1)):
            print("Player 1 win !")
            break
        tour+=1

        if tour>9:
            print("Draw !")
            break

        #player 2 turn
        choix_joueur2=int(input("Player 2 turn \n Choose a number(0-8): "))
        while board[choix_joueur2]==signe_joueur1 or board[choix_joueur2]==signe_joueur2:
            print("Already used")
            choix_joueur2=int(input(" Choose a number(0-8): "))

        if board[choix_joueur2]==variable_vide: 
            board[choix_joueur2]=signe_joueur2

        print("________________________________________")
        print()
        print("Turn :",tour, "| Player 2 choice :",choix_joueur2)
        draw_board(board)
        #winning condition for Player 2
        if (((board[0]==signe_joueur2 and board[1]==signe_joueur2 and board[2])==signe_joueur2) or
        ((board[3]==signe_joueur2 and board[4]==signe_joueur2 and board[5])==signe_joueur2) or
        ((board[6]==signe_joueur2 and board[7]==signe_joueur2 and board[8])==signe_joueur2) or
        ((board[0]==signe_joueur2 and board[3]==signe_joueur2 and board[6])==signe_joueur2) or
        ((board[1]==signe_joueur2 and board[4]==signe_joueur2 and board[7])==signe_joueur2) or
        ((board[2]==signe_joueur2 and board[5]==signe_joueur2 and board[8])==signe_joueur2) or
        ((board[0]==signe_joueur2 and board[4]==signe_joueur2 and board[8])==signe_joueur2) or
        ((board[2]==signe_joueur2 and board[4]==signe_joueur2 and board[6])==signe_joueur2)):
            print("Player 2 win !")
            break
        tour+=1
    
    #game mode VS IA
elif mode_de_jeu_reponse=="N":
    print("________________________________________")
    print("loading VS IA mode")
    print()
    #choosing a sign
    signe_joueur1=input("Player 1 choose a sign: O or X\n")
    if signe_joueur1==signO:
        signe=signX
    elif signe_joueur1==signX: 
        signe=signO
    else:
        input("Invalide input. Quitting")

    print("player 1 sign :", signe_joueur1,"\n AI sign :", signe)
    print("________________________________________")
    print()
    template(mur)

    #game start
    while tour <10: 
        #player1 turn
        choix_joueur1=int(input("Player 1 turn\n Choose a number(0-8): ")) 
        while board[choix_joueur1]==signe_joueur1 or board[choix_joueur1]==signe:
            print("Already used")
            choix_joueur1=int(input(" Choose a number(0-8): "))

        if board[choix_joueur1]==variable_vide: 
            board[choix_joueur1]=signe_joueur1
            
        print("________________________________________")
        print()
        print("Turn :",tour, "| Player 1 choice :",choix_joueur1)
        draw_board(board)

        #winning condition for player 1
        if (((board[0]==signe_joueur1 and board[1]==signe_joueur1 and board[2])==signe_joueur1) or
        ((board[3]==signe_joueur1 and board[4]==signe_joueur1 and board[5])==signe_joueur1) or
        ((board[6]==signe_joueur1 and board[7]==signe_joueur1 and board[8])==signe_joueur1) or
        ((board[0]==signe_joueur1 and board[3]==signe_joueur1 and board[6])==signe_joueur1) or
        ((board[1]==signe_joueur1 and board[4]==signe_joueur1 and board[7])==signe_joueur1) or
        ((board[2]==signe_joueur1 and board[5]==signe_joueur1 and board[8])==signe_joueur1) or
        ((board[0]==signe_joueur1 and board[4]==signe_joueur1 and board[8])==signe_joueur1) or
        ((board[2]==signe_joueur1 and board[4]==signe_joueur1 and board[6])==signe_joueur1)):
            print("Player 1 win !")
            break
        tour+=1

        if tour>9:
            print("Draw")        
            break
       
        #AI turn     (IA lvl 2 - most played placement)
        def ia(board,signe):
            if board[4]==variable_vide:
                choix_IA=4
            elif (board[0]==variable_vide or board[2]==variable_vide or board [6]==variable_vide or board[8]==variable_vide):
                    choix_IA=random.choice(corner)
                    while board[choix_IA]==signe_joueur1 or board[choix_IA]==signe:
                        choix_IA=random.choice(corner)
            elif (board[1]==variable_vide or board[3]==variable_vide or board [5]==variable_vide or board[7]==variable_vide):
                    choix_IA=random.choice(center)
                    while board[choix_IA]==signe_joueur1 or board[choix_IA]==signe:
                        choix_IA=random.choice(center)
            else:
                return False
            return choix_IA
        choix_IA=ia(board,signe) 

        #choice of placement of IA
        if board[choix_IA]==variable_vide: 
            board[choix_IA]=signe  

        print("________________________________________")
        print()
        print("Turn :",tour, "| Ai choice :",choix_IA)
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
            break
        tour+=1

else:
    print("incorret input. Quitting")



    #____________________________________________________________________________________

        #     #IA temporaire
        # if difficulty==0:
        #     print("diffuclty selected :",difficulty)

        #     choix_IA=random.randrange(0,8)       #valeur retourné par la fonction a changer
        #     while board[choix_IA]==signe or board[choix_IA]==signe_joueur1:
        #         choix_IA=random.randrange(0,8) #make an or with if
        #     # elif board[choix_IA]==signe_joueur:
        #         choix_IA=random.randrange(0,8)  #trying for looping test, need to change with alogrythm
        #     board[choix_IA]=signe
    #____________________________________________________________________________________

            #IA fonction lvl 1 - randomness
        # if difficulty==1:
        #     print("diffuclty selected :",difficulty)

        #     def ia(board,signe): #simple ia
        #         choix_IA=random.randrange(0,8) #choix de lia est egale a un chiffre leatoire entre 0 et 8
        #         if board[choix_IA]==signe or board[choix_IA]==signe_joueur1: #tant que le chiffre de lia est egale a son sign ou celui du joueur
        #             choix_IA=random.randrange(0,8) #make an or with if --  continue de chosir
        #         else:
        #             return False
        #         return choix_IA # retourne le choix de l'emplacement
        #             #else retrn false to addN
        #     choix_IA=ia(board,signe) #variable conentant l'emplacement updated
        #     #need this last one activated
    #_________________________________________________________________________________
        


    # # ia  block player
    
    #     def ia(board,signe):
    #         # 

    #         if board[4]==variable_vide:
    #             choix_IA=4
    #         elif (board[0]==variable_vide or board[2]==variable_vide or board [6]==variable_vide or board[8]==variable_vide): #choose 8
    #                 choix_IA=random.choice(corner)
    #                 while board[choix_IA]==signe_joueur1 or board[choix_IA]==signe:
    #                     choix_IA=random.choice(corner)
    #         elif (board[1]==variable_vide or board[3]==variable_vide or board [5]==variable_vide or board[7]==variable_vide):
    #                 choix_IA=random.choice(center)
    #                 while board[choix_IA]==signe_joueur1 or board[choix_IA]==signe:
    #                     choix_IA=random.choice(center)
    #         else:
    #             return False
    #         return choix_IA
    #     choix_IA=ia(board,signe) #activate this
    # #     def ia(board,signe):
    # #         if signe_joueur1 in row1:
    # #             print("what")


    #         # if board[0]==signe_joueur1 or board[1]==signe_joueur1 or board[2] ==signe_joueur1:
    #         #     choix_IA=random.choice(row1)
    #         # elif board[3]==signe_joueur1 or board[4]==signe_joueur1 or board[5] ==signe_joueur1:
    #         #     choix_IA=random.choice(row2)
    #         # elif board[6]==signe_joueur1 or board[7]==signe_joueur1 or board[8] ==signe_joueur1:
    #         #     choix_IA=random.choice(row3)

    #     ia(board,signe)
            
            # if board[4]==variable_vide:
            #     choix_IA=4
            # elif board[0]==signe_joueur:
            #     choix_IA=8
            # elif board[1]==signe_joueur:
            #     choix_IA=7
            # elif board[2]==signe_joueur:
            #     choix_IA=6
            # elif board[3]==signe_joueur:
            #     choix_IA=5
            # elif board[5]==signe_joueur:
            #     choix_IA=3
            # elif board[6]==signe_joueur:
            #     choix_IA=2
            # elif board[7]==signe_joueur:
            #     choix_IA=1
            # elif board[8]==signe_joueur:
            #     choix_IA=0
            # elif board[1]==signe_joueur or board[3]==signe_joueur or board[5] ==signe_joueur or board[7]==signe_joueur:
            #     choix_IA=random.choice(corner)

            #efif any player emplacemnt : place 
            # for i in range(8):






            # elif (board[0]==variable_vide or board[2]==variable_vide or board [6]==variable_vide or board[8]==variable_vide): #choose 8
            #         choix_IA=random.choice(corner)
            #         while board[choix_IA]==signe or board[choix_IA]==signe_joueur:
            #             choix_IA=random.choice(corner)
            # else:
            #     choix_IA=random.choice(center)
            #     while board[choix_IA]==signe or board[choix_IA]==signe_joueur:
            #             choix_IA=random.choice(center)
            
        #     return choix_IA #activate this
        #        #else return false to add
        # choix_IA=ia(board,signe) #activate this


        
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