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
emplacement1=variable_vide 
emplacement2=variable_vide
emplacement3=variable_vide
emplacement4=variable_vide
emplacement5=variable_vide
emplacement6=variable_vide    
emplacement7=variable_vide
emplacement8=variable_vide
emplacement9=variable_vide
tour=1
board=[variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide]
signe_joueur="O"
signe="X"
choix_IA=""
corner=(0,2,6,8)
center=(1,3,5,7)
#laisser le choix du signe ? TO DO lat8

#choix du mode jeu
#2joueurs ou ia
# input("TiTacToe \n mode de jeu :\n-2 Players\n-Vs AI") # mettre en anglais
# input()
# mode_de_jeu_reponse=input("want to play 2 players mode ? Y/N\n")
# if mode_de_jeu_reponse=="Y": #creer variation de reponse
#     print("loading 2 player mode")#load 2 player mode




# elif mode_de_jeu_reponse=="N":

#template 
def template(mur):
    print(mur,"0",mur,"1",mur,"2",mur) 
    print(mur,"3",mur,"4",mur,"5",mur)
    print(mur,"6",mur,"7",mur,"8",mur)
    print()
template(mur)





    # if tour>9:
    #     print("égalité")
    # else:

while tour <=9: #le jeu continu tant que 9 tour ne sont pas passé
    #player1
    choix_joueur1=int(input("Your turn\nselectionner emplacement: ")) #ajouter template
    while board[choix_joueur1]==signe or board[choix_joueur1]==signe_joueur:
        print("emplacement occupé") # try again a faire
        choix_joueur1=int(input("selectionner emplacement: "))

    if board[choix_joueur1]==variable_vide: #ajouter exeption si choix du joueur est >9
        board[choix_joueur1]=signe_joueur



    print("________________________________________")
    print()
    print("Tour :",tour, "Joueur1 choix :",choix_joueur1)

    def draw_board(board):
        print(mur,board[0],mur,board[1],mur,board[2],mur) 
        print(mur,board[3],mur,board[4],mur,board[5],mur)
        print(mur,board[6],mur,board[7],mur,board[8],mur)
    draw_board(board)

    #winning condition for player - make a fonction later
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
   
    # choix_IA=ia(board,signe) #variable conentant l'emplacement updated
#_________________________________________________________________________________

        # IA fonction lvl 1 - best placement

    def ia(board,signe):
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

    choix_IA=ia(board,signe)
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
#condition de placement
    # if board[choix_IA]==variable_vide: #
    board[choix_IA]=signe




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

    if tour>9:
         print("egalié")
    #condition exeko a faire






    

