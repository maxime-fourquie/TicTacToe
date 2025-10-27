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
choix_IA=0
#laisser le choix du signe ?

#choix du mode jeu
#2joueurs ou ia
mode_de_jeu=input("Choix du mode de jeu : 2 Joueurs / VS IA:")

    #IA focntion

def ia(board,signe): #simple ia
    choix_IA=random.randrange(0,8)
    while board[choix_IA]==signe or board[choix_IA]==signe_joueur:
        choix_IA=random.randrange(0,8) #make an or with if
    # print("choix ia dans la fonction:",choix_IA)
    return choix_IA #emplacemnt
ia(board,signe)
    

# if tour>9:
#     print("égalité")
# else:

while tour <=9: #le jeu continu tant que 9 tour ne sont pas passé
    #player1

    choix_joueur1=int(input("selectionner emplacement: ")) #ajouter template
    while board[choix_joueur1]==signe or board[choix_joueur1]==signe_joueur:
        print("emplacement occupé") # try again a faire
        choix_joueur1=int(input("selectionner emplacement: "))

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
    tour+=1

        #IA temporaire
    #choix_IA=random.randrange(0,8)       #valeur retourné par la fonction a changer
    while board[choix_IA]==signe or board[choix_IA]==signe_joueur:
        choix_IA=random.randrange(0,8) #make an or with if
    # elif board[choix_IA]==signe_joueur:
    #     choix_IA=random.randrange(0,8)  #trying for looping test, need to change with alogrythm
    
    board[choix_IA]=signe

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
    # if tour==10:
    #     print("égalité")
    #     break


    # print("Tour:",tour)

    #condition exeko a faire


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






    

