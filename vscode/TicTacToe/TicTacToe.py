#creer le plateau de jeu V
#definir les emplacements (0-9) V
#definir joueurs
#attribuer signe
#definit tour

#variable tour
#variable joueur 1
#variable joureur 2/IA  algorithme

#creer Ia algorithme


import random  #useless later

#Variable
variable_vide=" "
mur= "|"
# emplacement1=variable_vide 
# emplacement2=variable_vide
# emplacement3=variable_vide
# emplacement4=variable_vide
# emplacement5=variable_vide
# emplacement6=variable_vide    
# emplacement7=variable_vide
# emplacement8=variable_vide
# emplacement9=variable_vide
tour=1
board=[variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide]
signe_joueur="O"
signe="X"
choix_IA=""
corner=(0,2,6,8)
center=(1,3,5,7)
row1=(0,1,2)
diffuclty=""
# row2=([3],[4],[5]) #notused
# row3=([6],[7],[8])

#laisser le choix du signe ? TO DO lat8



# elif mode_de_jeu_reponse=="N":

#template 
def template(mur):
    print(mur,"0",mur,"1",mur,"2",mur) 
    print(mur,"3",mur,"4",mur,"5",mur)
    print(mur,"6",mur,"7",mur,"8",mur)
    print()

def draw_board(board):
    print(mur,board[0],mur,board[1],mur,board[2],mur) 
    print(mur,board[3],mur,board[4],mur,board[5],mur)
    print(mur,board[6],mur,board[7],mur,board[8],mur)


def ia1(board,signe):
    if board[4]==variable_vide:
        choix_IA=4
    elif (board[0]==variable_vide or board[2]==variable_vide or board [6]==variable_vide or board[8]==variable_vide): #choose 8
            choix_IA=random.choice(corner)
            while board[choix_IA]==signe or board[choix_IA]==signe_joueur:
                choix_IA=random.choice(corner)
    else:
        choix_IA=random.choice(center)
        while board[choix_IA]==signe or board[choix_IA]==signe_joueur:
                choix_IA=random.choice(center)
    
    return choix_IA
        #else return false to add
choix_IA=ia1(board,signe)

#choix du mode jeu
#2joueurs ou ia
# input("TiTacToe \n mode de jeu :\n-2 Players\n-Vs AI") # mettre en anglais
# input()
mode_de_jeu_reponse=input("want to play 2 players mode ? Y/N\n")


if mode_de_jeu_reponse=="Y": #creer variation de reponse
    
    #load 2 player mode
    print("loading 2 player mode")
    template(mur)
    while tour <10:
        #player1 turn
        choix_joueur1=int(input("Player 1 turn - O\nselectionner emplacement: ")) #ajouter template
        while board[choix_joueur1]==signe or board[choix_joueur1]==signe_joueur:
            print("emplacement occupé") # try again a faire
            choix_joueur1=int(input("selectionner emplacement: "))

        if board[choix_joueur1]==variable_vide: #ajouter exeption si choix du joueur est >9
            board[choix_joueur1]=signe_joueur



        print("________________________________________")
        print()
        # print("Tour :",tour, "Joueur1 choix :",choix_joueur1)


        draw_board(board)

        if (((board[0]==signe_joueur and board[1]==signe_joueur and board[2])==signe_joueur) or
        ((board[3]==signe_joueur and board[4]==signe_joueur and board[5])==signe_joueur) or
        ((board[6]==signe_joueur and board[7]==signe_joueur and board[8])==signe_joueur) or
        ((board[0]==signe_joueur and board[3]==signe_joueur and board[6])==signe_joueur) or
        ((board[1]==signe_joueur and board[4]==signe_joueur and board[7])==signe_joueur) or
        ((board[2]==signe_joueur and board[5]==signe_joueur and board[8])==signe_joueur) or
        ((board[0]==signe_joueur and board[4]==signe_joueur and board[8])==signe_joueur) or
        ((board[2]==signe_joueur and board[4]==signe_joueur and board[6])==signe_joueur)):
            print("Player 1 win")
            break
        tour+=1

        if tour>9:
            print("Draw")
            break

        #player 2 turn
        choix_joueur2=int(input("Player 2 turn - sign = X\nselectionner emplacement: ")) #ajouter template
        while board[choix_joueur2]==signe or board[choix_joueur2]==signe_joueur:
            print("emplacement occupé") # try again a faire
            choix_joueur2=int(input("selectionner emplacement: "))

        if board[choix_joueur2]==variable_vide: #ajouter exeption si choix du joueur est >9
            board[choix_joueur2]=signe



        print("________________________________________")
        print()
        # print("Tour :",tour, "Joueur2 choix :",choix_joueur2)

 
        draw_board(board)

        if (((board[0]==signe and board[1]==signe and board[2])==signe) or

        ((board[3]==signe and board[4]==signe and board[5])==signe) or
        ((board[6]==signe and board[7]==signe and board[8])==signe) or
        ((board[0]==signe and board[3]==signe and board[6])==signe) or
        ((board[1]==signe and board[4]==signe and board[7])==signe) or
        ((board[2]==signe and board[5]==signe and board[8])==signe) or
        ((board[0]==signe and board[4]==signe and board[8])==signe) or
        ((board[2]==signe and board[4]==signe and board[6])==signe)):
            print("Player 2 win")
            break
        tour+=1
    
    #game mode VS IA
elif mode_de_jeu_reponse=="N":
    print("loading VS IA mode")

    #choosing difficulty - not working
    diffuclty=input("Choose IA difficulty 0/1/2")
    if diffuclty==2:
        ia1(board,signe)

    template(mur)
    while tour <10: #le jeu continu tant que 9 tour ne sont pas passé

#_______________________________________________________________
        #player1 turn
        choix_joueur1=int(input("Player 1 turn\nselectionner emplacement: ")) #ajouter template
        while board[choix_joueur1]==signe or board[choix_joueur1]==signe_joueur:
            print("emplacement occupé") # try again a faire
            choix_joueur1=int(input("selectionner emplacement: "))

        if board[choix_joueur1]==variable_vide: #ajouter exeption si choix du joueur est >9
            board[choix_joueur1]=signe_joueur



        print("________________________________________")
        print()
        print("Tour :",tour, "Joueur1 choix :",choix_joueur1)


        draw_board(board)
        

        
    #__________________________________________________________
    #fonction winner wip
        # # def winner():
        # for i in range(0,9,3): #ligne check
        #     if board[i] == board[i+1] == board[i+2] !=variable_vide:
        #         print("ligne win")
        #         # return board[i] #winning symbole
        #         print(board)
        #         #break
        # for i in range(3): #colonne check
        #     if board[i] == board[i+3] == board[i+6] !=variable_vide:
        #         print("colonne win")
        #         # return board[i]
        #         #break
        
        # if board[0] == board[4] == board[8] != variable_vide: #check diagonal
        #     # return board[0]
        # if board[2] == board[4] == board[6] != variable_vide: #check diagonal
        #     # return board[2]
        
        # # return None
        
        # if winner(board)==signe_joueur:
        #     print("winner : joueur 1")
        # elif winner(board)==signe:
        #     print("winner : IA")
    


      
    #______________________________________________________________
      # #winning condition for player - make a fonction later

        if (((board[0]==signe_joueur and board[1]==signe_joueur and board[2])==signe_joueur) or
        ((board[3]==signe_joueur and board[4]==signe_joueur and board[5])==signe_joueur) or
        ((board[6]==signe_joueur and board[7]==signe_joueur and board[8])==signe_joueur) or
        ((board[0]==signe_joueur and board[3]==signe_joueur and board[6])==signe_joueur) or
        ((board[1]==signe_joueur and board[4]==signe_joueur and board[7])==signe_joueur) or
        ((board[2]==signe_joueur and board[5]==signe_joueur and board[8])==signe_joueur) or
        ((board[0]==signe_joueur and board[4]==signe_joueur and board[8])==signe_joueur) or
        ((board[2]==signe_joueur and board[4]==signe_joueur and board[6])==signe_joueur)):
            print("Joueur1 win")
            break
        tour+=1

        if tour>9:
            print("egalié")        
    #____________________________________________________________________________________
        #     #IA temporaire
        # choix_IA=random.randrange(0,8)       #valeur retourné par la fonction a changer
        # while board[choix_IA]==signe or board[choix_IA]==signe_joueur:
        #     choix_IA=random.randrange(0,8) #make an or with if
        # # elif board[choix_IA]==signe_joueur:
        #     choix_IA=random.randrange(0,8)  #trying for looping test, need to change with alogrythm
        # board[choix_IA]=signe
    #____________________________________________________________________________________

            #IA fonction lvl 0 - randomness

        # def ia(board,signe): #simple ia
        #     choix_IA=random.randrange(0,8) #choix de lia est egale a un chiffre leatoire entre 0 et 8
        #     while board[choix_IA]==signe or board[choix_IA]==signe_joueur: #tant que le chiffre de lia est egale a son sign ou celui du joueur
        #         choix_IA=random.randrange(0,8) #make an or with if --  continue de chosir
        #     return choix_IA # retourne le choix de l'emplacement
        #         #else retrn false to add
        # choix_IA=ia(board,signe) #variable conentant l'emplacement updated
        # #need this last one activated
    #_________________________________________________________________________________

            # IA fonction lvl 1 - most played placement



    #_________________________________________________________________________________________

            # ia fonction lvl2 -

    # #comment ia choose to block player

    #     def ia(board,signe):
    #         #if player can win -> block
    #         if row1 in board ==signe_joueur:
    #             print("he gonna win")

    #     #     # for i in range(0,2):
    #     #     #     j=random.sample(row1,2)
    #     #     #     if j == signe_joueur:
    #     #     #         print(i,j , "should work")
    #     ia(board,signe)

        #do the same shit as the previous one but with row ??
        
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

    #_________________________________________________________________________ 

    #condition de placement choix ia
        ia1(board,signe)

        if board[choix_IA]==variable_vide: #
            board[choix_IA]=signe  #   /!\ actuvate for working


        print("Tour :",tour, "Ai choix :",choix_IA)

        draw_board(board)


        #winning condition for ai - make a focntion later
        if (((board[0]==signe and board[1]==signe and board[2])==signe) or

        ((board[3]==signe and board[4]==signe and board[5])==signe) or
        ((board[6]==signe and board[7]==signe and board[8])==signe) or
        ((board[0]==signe and board[3]==signe and board[6])==signe) or
        ((board[1]==signe and board[4]==signe and board[7])==signe) or
        ((board[2]==signe and board[5]==signe and board[8])==signe) or
        ((board[0]==signe and board[4]==signe and board[8])==signe) or
        ((board[2]==signe and board[4]==signe and board[6])==signe)):
            print("AI win")
            break
        tour+=1

    #tryna do a winner fonction
        # def winner():
        # for i in range(0,9,3):
        #     if board[i] == board[i+1] == board[i+2] !=variable_vide:
        #         print(board[i])





        #condition exeko a faire






        

