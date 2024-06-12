# Jeu de puissance 4 en ligne de commande

grille = [] # Grille du jeu

def reset_grille():
    "Vider entièremment la grille de jeu"
    grille = []

    print(f"Grille réinitialisée ! {grille}")    

def initialiserGrille():
    "Initialiser la grille du jeu"
    reset_grille() # Remettre la grille de jeu à zéro, en supprimant chaque colonne et son contenu
    
    # ligne = [0,0,0,0,0,0,0] # Liste qui sert de "modèle" pour chaque colone qu'on va créer
    # for i in range(6): # On cherche à créer 6 lignes
    #     grille.append(ligne) # On ajoute une nouvelle ligne à la grille en s'aidant du modèle
    grille = [[0 for x in range(7)] for y in range(6)]
    return grille # On retourne la nouvelle grille de jeu

def recuperer_symbole(numero_du_joueur):
    "Récupérer et retourner un symbole différent en fonction du numéro du joueur"
    if numero_du_joueur == 1: # Si on veut récupérer le symbole du joueur n°1
        return "x"
    elif numero_du_joueur == 2: # Si on veut récupérer le symbole du joueur n°2
        return "y"

def afficher_grille(grille):
    "Afficher la grille de jeu"
    for ligne in range(len(grille)): # Pour chaque ligne qu'on trouve sur toute la longueur de la grille de jeu
       # print(ligne)
        if ligne == 0: # Si on est à la première ligne de la grille
                for case in range(len(grille[ligne])): # Pour chaque case de la ligne
                    print("-", end= " ")
                print()
        for colonne in range(len(grille[ligne])): # Pour chaque colonne de la ligne courante
            #print("Contenu de la colonne :", grille[ligne][colonne])

               
            #print(grille[ligne][colonne])
            if grille[ligne][colonne] == 1: # On vérifie si la case courante est occupée par le joueur 1 en vérifiant si le numéro contenu est 1
                 print("x", end=" ") # Et si c'est le cas on ajoute un "x" dans la grille de jeu pour représenter le joueur 1
                 
            elif grille[ligne][colonne] == 2: # On vérifie si la case courante est occupée par le joueur 2 en vérifiant si le numéro contenu est 2
                 print("y", end=" ") # Et si c'est le cas on ajoute un "y" dans la grille de jeu pour représenter le joueur 2


            else: # Si le numéro de case courante est différent de 1 ou 2
                print("|", end=" ")     
                 

           
        print()


        if ligne == 5: # Si on est à la dernière ligne de la grille
                for case in range(len(grille[ligne])): # Pour chaque case de la ligne
                    print("-", end= " ")
                print()




def ligneLibreDeLaColonne(colonne):
     "Trouver la dernière ligne libre d'une colonne donnée"
     nombre_a_comparer = 0 # Nombre que l'on doit comparer au contenu de la colonne
     for ligne in range(len(grille)-1,-1,-1): # Pour chaque ligne de la colonne
          try:
            if grille[ligne][colonne] == nombre_a_comparer:
               return ligne
            
          except TypeError:
              continue    
     return -1


def demanderColonne(joueur):
     "Demander à un joueur de saisir le numéro de la colonne dans laquelle il souhaite placer un jeton"
     try :
        colonne = int(input(f"Joueur n°{joueur}, saisissez le numéro de la colonne où placer un jeton:")) # Demander le numéro de la colonne au joueur
        ligne = ligneLibreDeLaColonne(colonne)
        while ligne == -1: # S'il n'y a aucune ligne libre dans la colonne
          print(f"La colonne n°{colonne} est déjà pleine, veuillez saisir le numéro d'une autre colonne.")
          colonne = int(input(f"Joueur n°{joueur}, saisissez le numéro de la colonne où placer un jeton:")) # Demander le numéro de la colonne au joueur

        return colonne        
  

     except ValueError: # Exception si on ne peut pas convertir la saisie du joueur en nombre entier
          print("Valeur de la saisie invalide. Veuillez ne fournir strictement qu'un nombre entier.")  

          colonne = int(input(f"Joueur n°{joueur}, saisissez le numéro de la colonne où placer un jeton:")) # Demander le numéro de la colonne au joueur
          ligne = ligneLibreDeLaColonne(colonne)
          while ligne == -1: # S'il n'y a aucune ligne libre dans la colonne
            print(f"La colonne n°{colonne} est déjà pleine, veuillez saisir le numéro d'une autre colonne.")
            colonne = int(input(f"Joueur n°{joueur}, saisissez le numéro de la colonne où placer un jeton:")) # Demander le numéro de la colonne au joueur
       
            return colonne

    

        


def placerJeton(joueur, colonne):
     "Placer le jeton d'un joueur"
     symbole = recuperer_symbole(joueur)
     ligne = ligneLibreDeLaColonne(colonne)
     print(f"Ligne libre : n°{ligne}")
     if ligne != -1:
          print("Des lignes sont libres")
         # print("Contenu de la colonne :", grille[colonne])
          print(grille[ligne][colonne])

          longueur_ligne = len(grille[ligne])
          for i in range(longueur_ligne):
               if i == ligne:

                    grille[ligne][colonne] = joueur

                    
                    
               
          
          

          #print("Grille :", grille[colonne])

     else:
          print("Aucune ligne n'est libre")



def verifierHorizontalement(joueur):
    "Vérifier que le numéro d'un joueur apparaît quatre fois à l'horizontale. Cela nous permet de déterminer s'il a gagné ou non."
    for ligne in grille: # Pour chaque ligne de la grille
        apparitions_numero_joueur = 0 # Nombre d'apparitions du numéro du joueur
        #print("Ligne :", ligne)
        for numero in ligne: # Pour chaque numéro trouvé dans la ligne
            if numero == joueur: # Si on trouve le numéro correspondant au joueur
               
                apparitions_numero_joueur += 1 # Alors on augmente le nombre de vues du numéro de 1

            else: # Si on trouve un autre numéro6
                 apparitions_numero_joueur = 0 # On remet le compteur à zéro pour éviter que le joueur puisse gagner sans que ses pions soient alignés consécutivement

            if apparitions_numero_joueur == 4: # Si le numéro du joueur apparaît 4 fois horizontalement, alors ce dernier gagne la partie
                    return joueur # Alors on retourne le numéro du joueur gagnant pour pouvoir gérer la victoire de celui-ci

    return -1 # Si aucun joueur n'a placé 4 jetons horizontalement, on retourne -1 pour dire qu'il n'y a pas victoire


def verifierVerticalement(joueur):
     "Vérifier que le numéro d'un joueur apparaît quatre fois à la verticale. Cela nous permet de déterminer s'il a gagné ou non"
     colonnes_parcourues = 0 # Nombre de colonnes parcourues pour chaque ligne de la grille
     numeros_joueur_trouves = 0 # Nombre de fois qu'on trouve le numéro du joueur donné en paramètre dans la grille
     for colonne in range(len(grille[0])):
          for ligne in range(len(grille)-1, -1, -1):
               if grille[ligne][colonne] == joueur:
                    numeros_joueur_trouves += 1

                    if numeros_joueur_trouves == 4: # Si on a trouvé 4 fois le numéro d'un même joueur
                         return joueur # On retourne le numéro de ce joueur afin d'indiquer qu'il a gagné la partie 
               
               else:
                    numeros_joueur_trouves = 0



                        



          

     return -1 # Si aucun joueur n'a placé 4 jetons verticalement, alors on retourne -1 pour dire que personne n'a gagné


def verifierDiagonale(joueur):
     "Vérifier que le numéro d'un joueur apparaît quatre fois en diagonale. Cela nous permet de déterminer s'il a gagné ou non"
     numeros_joueus_trouve = 0 # Nombre de fois que l'on rencontre le numéro du joueur donné en paramètre en diagonale
     for ligne in range(len(grille)-1,2 ,-1):
          print("ligne :", grille[ligne])
          for colonne in range(len(grille[ligne])-1, 2,-1):
               if grille[ligne][colonne] == joueur and grille[ligne-1][colonne-1] == joueur and grille[ligne-2][colonne-2] == joueur and grille[ligne-3][colonne-3] == joueur:
                    numeros_joueus_trouve = 4

               if numeros_joueus_trouve == 4: # Si on a trouvé 4 fois le numéro d'un même joueur en diagonale de la droite vers la gauche, on considère qu'il a gagné
                    return joueur # donc on retourne son numéro
               

     for ligne in range(len(grille)-1,2,-1):
          for colonne in range(len(grille[ligne]) -3):
               if grille[ligne][colonne] == joueur and grille[ligne-1][colonne + 1] == joueur and grille[ligne-2][colonne + 2]== joueur and grille[ligne-3][colonne + 3] == joueur: # Si on a trouvé 4 fois le numéro d'un même joueur en diagonale de la gauche vers la droite, on considère qu'il a gagné
                    return joueur   # Donc on retourne son numéro      
     
     return -1 # On retourne -1 si aucun joueur n'a placé 4 jetons en diagonale               

          
                

                         
                         
def verifierGrillePleine():
     "Véfirifier si la grille de jeu est pleine ou non"
     for ligne in grille: # Pour chaque ligne de la grille
          if 0 in ligne: # S'il y a des 0 dans la ligne, alors c'est que cette ligne est libre
               return False # Dans ce cas là, on retourne False pour indiquer la grille est libre
     
     
     return True # Toutes les lignes sont pleines, on retourne True pour indiquer que la grille est pleine


          
    
        


def partie_gagnee(liste_de_joueurs):
    "Vérifier si la partie a été gagnée par un joueur ou non" 
    
    for joueur in liste_de_joueurs: # Pour chaque joueur de la liste des joueurs
          numero_joueur = joueur # Numéro du joueur
          resultats = [] # Résultats des vérifications pour le joueur courant
          verification_horizontale = verifierHorizontalement(joueur) # On vérifie si le joueur a placé 4 jetons horizontalement
          verification_verticale = verifierVerticalement(joueur) # on vérifie aussi si le joueur a placé 4 jetons verticalement
          verification_diagonale = verifierDiagonale(joueur)
          if verification_horizontale != -1 or verification_verticale != -1 or verification_diagonale!= -1: # Si on trouve un résultat qui correspond au numéro du joueur, en sachant que chaque vérification retourne un numéro de joueur si elle est vraie
               return numero_joueur # On retourne le numéro du joueur
          
          
    return -1 # On retourne -1 si aucun joueur n'a rempli une des conditions pour gagner la partie 



          

          
          


grille = initialiserGrille()

def boucleDeJeu():
    "Boucle principale du jeu"
    joueurs = [1,2]
    joueur_gagnant = -1

    while joueur_gagnant == -1: # Tant qu'aucun joueur n'a gagné la partie
          

          afficher_grille(grille)
          print(grille)
          for i in range(len(joueurs)):
               col = demanderColonne(joueurs[i])
               placerJeton(joueurs[i], col)
               
                   


               afficher_grille(grille)

               
               joueur_gagnant = partie_gagnee(joueurs)  

               if joueur_gagnant != - 1:         

                    print(f"Le joueur gagnant est {joueur_gagnant} !")
                    break


               grille_pleine = verifierGrillePleine() # On vérifie si la grille de jeu est pleine ou non
               if grille_pleine == True: # Si la grille est effectivement pleine
                    print("Fin de la partie : la grille est pleine.")
                    return


def demanderRejouer():
     "Demander au joueur s'il souhaite rejouer" 
     rejouer = input("Voulez-vous rejouer ? (oui/non) :")  # On demande au joueur s'il souhaite lancer une nouvelle partie
     

     return rejouer   






                   

          
          
rejouer = None                    

while rejouer != "non": # Tant que le joueur ne saisit pas 'non', on considère qu'il veut rejouer
     grille = initialiserGrille() # On réinitialise la grille de jeu
     boucleDeJeu() # On démarre le jeu une nouvelle fois
     rejouer = demanderRejouer() # Une fois la partie terminée, on demande au joueur s'il souhaite rejouer. 


print("Fin de partie")     
     







                          
