#creer le plateau de jeu V
#definir les emplacements (0-9) V
#definir joueurs
#attribuer signe
#definit tour

#variable tour
#variable joueur 1
#variable joureur 2/IA  algorithme

#creer Ia algorithme


    #plateau
    #emplacemnt vide [0] = " " 
    #colonne |

# |1|2|3|
# |4|5|6|
# |7|8|9|

# |space1|spac

# #|[0]||
# list_tempoaire=(0)

import random  #useless now

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

# board={"emplacement1" : " ",
#        "emplacement2" : " ",
#        "emplacement3" : " ",
#        "emplacement4" : " ",
#        "emplacement5" : " ",
#        "emplacement6" : " ",
#        "emplacement7" : " ",
#        "emplacement8" : " ",
#        "emplacement9" : " ",
#         }

#IA focntion


# def ia(board,signe):
#     #choirisr un emplacemnt inocupé
#     #
#     board[0]=signe
    
#     return board[] #emplacemnt



while tour <10: #le jeu continu tant que 9 tour ne sont pas passé
    #player1
    choix_joueur1=int(input("selectionner emplacement: ")) #ajouter template
    if board[choix_joueur1]==variable_vide: #ajouter exeption si choix du joueur est >9
        board[choix_joueur1]=signe_joueur
    print("Tour :",tour, "Joueur1")
    print(mur,board[0],mur,board[1],mur,board[2],mur)
    print(mur,board[3],mur,board[4],mur,board[5],mur)
    print(mur,board[6],mur,board[7],mur,board[8],mur)

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
        #IA temporaire
    choix_IA=random.randrange(0,8)       #valeur retourné par la fonction a changer
    if board[choix_IA]==variable_vide:
        board[choix_IA]=signe
    else:
        choix_IA=random.randrange(0,8)  #trying for looping test, need to change with alogrythm

    print("Tour :",tour, "Ai choix :",choix_IA)
    print(mur,board[0],mur,board[1],mur,board[2],mur)
    print(mur,board[3],mur,board[4],mur,board[5],mur)
    print(mur,board[6],mur,board[7],mur,board[8],mur)

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
    # else:
    #     print("emplacement occupé") # try again a faire

    # print("Tour:",tour)




    # def plateau(n):
    # print(mur,list_vide[0],mur,list_vide[1],mur,list_vide[2],mur)
    # print(mur,list_vide[3],mur,list_vide[4],mur,list_vide[5],mur)
    # print(mur,list_vide[6],mur,list_vide[7],mur,list_vide[8],mur)
    # plateau(3)

    #condition de victoire
    #si board[0],1 ,2 == "X"



    

    #si //same =="O"
        #joueur win
    #si tour 9 and no winnder, draw






    

