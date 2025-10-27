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

import random 

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
tour=0
# list_vide=[variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide,variable_vide]
signe_joueur="O"
signe="X"

board={"emplacement1" : " ",
       "emplacement2" : " ",
       "emplacement3" : " ",
       "emplacement4" : " ",
       "emplacement5" : " ",
       "emplacement6" : " ",
       "emplacement7" : " ",
       "emplacement8" : " ",
       "emplacement9" : " ",
        }

#IA focntion


def ia(board,signe):
    board["emplacement1"]=signe
    
    return board

print(board)

print(mur,board["emplacement1"],mur,board["emplacement2"],mur,board["emplacement3"],mur)
print(mur,board["emplacement4"],mur,board["emplacement5"],mur,board["emplacement6"],mur)
print(mur,board["emplacement7"],mur,board["emplacement8"],mur,board["emplacement9"],mur)

# while tour <9: #le jeu continu tant que 9 tour ne sont pas passé
#     #player1
#     choix_joueur1=int(input("selectionner emplacement:")) #ajouter template
#     if list_vide[choix_joueur1]==variable_vide: #ajouter exeption si choix du joueur est >9
#         list_vide[choix_joueur1]="O"
        

#     #IA
#     choix_IA=random.randrange(0,8)
#     if list_vide[choix_IA]==variable_vide:
#         list_vide[choix_IA]="X"
#         tour+=1

#     else:
#         print("emplacement occupé") # try again a faire
    
#     print("Tour:",tour)



    # def plateau(n):
    # print(mur,list_vide[0],mur,list_vide[1],mur,list_vide[2],mur)
    # print(mur,list_vide[3],mur,list_vide[4],mur,list_vide[5],mur)
    # print(mur,list_vide[6],mur,list_vide[7],mur,list_vide[8],mur)
    # plateau(3)

#condition de victoire






#emplacemnt utilisé

    
# #def ia algo

#player1

# choix_joueur1=input("selectionner emplacement:")
# if choix_joueur1 == variable_vide:
#     list_vide[choix_joueur1]="O"
