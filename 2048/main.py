# Jeu de 2048 en ligne de commande
import random
from score import * # Importer l'entièreté du module score
from deplacements import *




meilleur_score = MeilleurScore() # Meilleur score du joueur
score = Score()# Score actuel du joueur. S'il est supérieur au meilleur score, le meilleur score sera actualisé.



touches = ["z","q","s","d"] # Listes des touches auxquelles le jeu réagit

coords_cases_occuppees = [] # Coordonnées des cases occupées 


nombre_final = 2048 # Nombre final que le joueur doit obtenir pour gagner

touches_directions = {
    "z":"haut",
    "q":"gauche",
    "s":"bas",
    "d":"droite"
} # Dictionnaire qui liste pour chaque touche la direction dans laquelle elle va déplacer les nombres de la grille

def generer_grille():
    "Générer une grille de jeu de dimensions 4x4"
    grille = [[0,0,0,0] for i in range(4)] # Générer une grille de quatre case par ligne
    return grille









def mettre_a_jour_grille(grille, ligne=0, colonne=0,nombre=2):
    "Mettre à jour la grille de jeu"
    grille[ligne][colonne] = nombre # Mettre à jour la case aux coordonnées (ligne, colonne) avec le nouveau nombre
    coords_cases_occuppees.append((ligne, colonne)) # Ajouter les coordonnées aux coordonnées occupées
    print("Coordonnées des cases occupées :", coords_cases_occuppees)


def coords_aleat(grille):
    "Générer des coordonnées aléatoires à partir d'une grille"
    ligne = random.randint(0, len(grille) -1) # Générer un numéro de ligne ligne aléatoire
    colonne = random.randint(0, len(grille[ligne]) -1) # Générer un numéro de colonne aléatoire dans la ligne
    while grille[ligne][colonne] > 0: # Si la case aux coordonnées générées est déjà prise
        # On génère un nouveau nombre pour la ligne et la colonne, jusqu'à ce que la case aux coordonnées nouvellement générées soit libre
        ligne = random.randint(0, len(grille) -1) 
        colonne = random.randint(0, len(grille[ligne]) -1) 


    coords = (ligne, colonne) # coords est un tuple contenant les coordonnées
    return coords # Retourner le tuple des coordonnées



def entree_utilisateur():
    "Demander une entrée à l'utilisateur. On s'en servira pour déterminer le sens dans lequel doivent être déplacés les nombres de la grille. Si la touche pressé n'est pas définie dans le dictionnaire touches_directions, alors redemande la saisie d'une touche à l'utilisateur jusqu'à ce que celle-ci soit définie"
        
    touche = input("Appuyez sur une seule touche (z, q, s ou d) et appuyez sur Entrée:") # Demander à l'utilisateur de presser une touche du clavuer
    while touche not in touches: # Si l'utilisateur a appuyé sur une touche qui n'est pas comprise par le jeu
            print("La touche saisie n'est pas valide. Veuillez réessayer :") # Afficher un message à l'utilisateur pour indiquer qu'il doit réessayer
            touche = entree_utilisateur() # Redemander à l'utilisateur de saisir une touche et mettre à jour la variable contenant le résultat de la saisie pour éviter une boucle infinine

    return touche # Si l'utilisateur a saisi une touche valide, la retourner


def generer_nombre_a_apparaitre():
    "Générer le nombre qui devra apparaître dans la grille quand l'utilisateur déplace des nombre dans la grille"
    probabilite_4 = random.randint(0, 100) # Probabilité que le nombre 4 apparaisse
    print(f"Probabilité qu'un 4 apparaisse dans la grille : {probabilite_4} %")
    if probabilite_4 >= 67: # S'il y a 67 % de chances que le nombre 4 apparaisse
        nombre_a_apparaitre = 4 # On fait apparaître un 4

    else: # Si la probabilité est inférieure à 67 %
        nombre_a_apparaitre = 2 # On fait apparaître un 2 à la place

    return nombre_a_apparaitre # Retourner le nombre généré


def afficher_grille(grille): 
    "Afficher la grille de jeu"
    for ligne in grille: # Pour chaque ligne de la grille
        print(ligne) # Afficher la grille



def determiner_nouvel_objectif(liste_objectifs, objectif_actuel=2048):
    "Déterminer le prochain objectif que le joueur devra atteindre"
    for objectif in liste_objectifs: # Pour chaque objectif de la liste
        if objectif > objectif_actuel: # Si l'objectif est supérieur à l'actuel
            return objectif # Retourner cet objectif


def grille_pleine(grille):
    "Vérifier si la grille de jeu est pleine"
    lignes_pleines = [] # Listes des lignes pleines
    for ligne in range(len(grille)): # Pour chaque ligne de la grille
        if not 0 in grille[ligne]: # Si aucune case n'est libre dans la ligne
            lignes_pleines.append(grille[ligne]) # Ajouter la ligne à la liste des lignes pleines

    if lignes_pleines == grille: # Si la liste des lignes pleines correspond à la grille de jeu, c'est que la grille est entièrement vide
        return True # On indique que la grille est vide

    return False # Sinon, on indique que la grille n'est pas vide 



def objectif_atteint(grille, objectif=2048):
    "Vérifier si le joueur atteint l'objectif (le nombre à obtenir pour gagner), par défaut 2048"
    for ligne in range(len(grille)): # Pour chaque ligne de la grille
        if objectif in grille[ligne]: # Si la ligne possède une case contenant le nombre à atteindre
            return True # L'objectif est atteint, on retourne alors True
        
    return False # Si l'objectif n'est pas atteint, ou retourne False    








def deplacer_nombres(grille, direction):
    "Déplacer des nombres de la grille selon une direction précise"
    global score
    if direction == "haut": # Si on doit déplacer les nombres vers le haut
        #print("Déplacement vers le haut")

        # Logique du déplacement à mettre ci-dessous

        deplacerHaut(grille, direction=direction, score_var=score, max_score_var=meilleur_score) # Déplacer les nombres vers le haut et mettre à jour le score
        

        coords_apparation_nombre = coords_aleat(grille) # Générer des coordonnées aléatoires pour le nouveau nombre à générer
        print("Coordonnées du nombre à apparaitre :", coords_apparation_nombre)
        ligne_nombre = coords_apparation_nombre[0] # Ligne dans laquelle le nombre doit apparaître
        #print("Ligne dans laquelle le nombre doit apparaitre :", ligne_nombre)
        colonne_nombre = coords_apparation_nombre[1] # Colonne de la ligne dans laquelle le nombre doit apparaître
        #print("Colonne de la ligne dans laquelle le nombre doit apparaitre :", colonne_nombre)

        grille[ligne_nombre][colonne_nombre] = generer_nombre_a_apparaitre() # Générer le nombre et le placer dans la grille aux coordonnées choisies
                        

                        
                        





                        



                    

    if direction == "gauche": # Si on doit déplacer les nombres vers la gauche
        #print("Déplacement vers la gauche")   

        # Logique du déplacement à mettre ci-dessous

        for ligne in range(len(grille)): # Pour chaque ligne de la grille
            #print(f"Longueur de la ligne n°{ligne} :", len(grille[ligne]))
            for colonne in range(len(grille[ligne]) -1): # On parcoure les colonnes de la ligne
                #print("Case actuelle :", grille[ligne][colonne], end=" ")
                #print(f"Colonne dans la ligne n°{ligne} :", colonne)
                for colonne2 in range(colonne+1, len(grille[ligne])): # Pour chaque colonne dans la ligne après la colonne actuelle
                    case_suivante = grille[ligne][colonne2] # Nombre contenu dans la case après
                    #print("Case suivante :", case_suivante, end= " ")
                    if case_suivante > 0: # Si le nombre de la case suivante est supérieur à 0
                        if grille[ligne][colonne] == case_suivante: # Si le nombre dans la case actuelle correspond à celui dans la case suivante
                            grille[ligne][colonne] = grille[ligne][colonne2]*2 # On fusionne les nombres de la case actuelle et de la case suivante par une multiplication
                            grille[ligne][colonne2] = 0 # On vide la case actuelle
                            score.augmenter(grille[ligne][colonne]) # Augmenter le score du joueur
                            meilleur_score.actualiser(score.valeur) # Actualiser le meilleur score
                            meilleur_score.sauvegarder() # Sauvegarder le meilleur score

                    else: # Si la case suivante est vide
                        print(f"La case (coords. {ligne}, {colonne2}) est vide")
                        if grille[ligne][colonne] > 0: # Mais que l'actuelle ne l'est pas
                            grille[ligne][colonne2] = grille[ligne][colonne] # Déplacer le nombre de la colonne actuelle vers la colonne suivante
                            grille[ligne][colonne] = 0 # Vider la case actuelle
                        #grille[ligne][colonne] = generer_nombre_a_apparaitre() # On vide la case actuelle



        coords_apparation_nombre = coords_aleat(grille) # Générer des coordonnées aléatoires pour le nouveau nombre à générer
        print("Coordonnées du nombre à apparaitre :", coords_apparation_nombre)
        ligne_nombre = coords_apparation_nombre[0] # Ligne dans laquelle le nombre doit apparaître
        #print("Ligne dans laquelle le nombre doit apparaitre :", ligne_nombre)
        colonne_nombre = coords_apparation_nombre[1] # Colonne de la ligne dans laquelle le nombre doit apparaître
        #print("Colonne de la ligne dans laquelle le nombre doit apparaitre :", colonne_nombre)

        grille[ligne_nombre][colonne_nombre] = generer_nombre_a_apparaitre() # Générer le nombre et le placer dans la grille aux coordonnées choisies
        
        


    if direction == "bas": # Si on doit déplacer les nombres vers le bas
        #print("Déplacement vers le bas")

        # Logique du déplacement à mettre ci-dessous


        for ligne in range(len(grille)): # On parcoure les lignes de la grille
            #print("Numéro de la ligne :", ligne)
            for colonne in range(len(grille[ligne])): # Pour chaque colonne de la ligne
                nombre_case_actuelle = grille[ligne][colonne] # Nombre dans la case actuelle
                for ligne2 in range(ligne-1, -1, -1): # Pour chaque ligne avant la ligne actuelle
                    #print("Ligne précédent la ligne actuelle :", ligne2)
                    if grille[ligne2][colonne] == nombre_case_actuelle and grille[ligne2][colonne] > 0: # Si le nombre contenu dans une des cases précédentes correspond au nombre de la case actuelle
                        grille[ligne2][colonne] = 0 # On vide la case précédente
                        grille[ligne][colonne] *= 2 # On fusionne les nombres des deux cases par une multiplication
                        score.augmenter(grille[ligne][colonne]*2) # Augmenter le score du joueur
                        meilleur_score.actualiser(score.valeur) # Actualiser le meilleur score
                        meilleur_score.sauvegarder() # Sauvegarder le meilleur score
                        break

                    elif grille[ligne2][colonne] == 0 and nombre_case_actuelle > 0: # Si la case précédente est vide mais que l'actuelle ne l'est pas
                        grille[ligne2][colonne] = nombre_case_actuelle # On déplace le nombre de la case actuelle sur la case précédente
                        grille[ligne][colonne] = 0 # On vide la case actuelle




                    

                

                        
        for ligne in range(len(grille) -1): # Pour chaque ligne de la grille après la première
            print("Numéro de la ligne :", ligne)
            #print("Ligne actuelle :", grille[ligne])

            if ligne == len(grille) -1:
                print(f"La ligne n°{ligne} (compte à partir de 0) est la dernière de la grille !")
                
            for colonne in range(len(grille[ligne])): # Pour chaque colonne de la ligne
                case_actuelle = grille[ligne][colonne] # Case actuelle
                for ligne2 in range(ligne+1, len(grille)): # Pour chaque ligne après la ligne actuelle
                    #print(ligne2)
                    lignes_entre = grille[ligne+1: ligne2] # Lignes comprises entre la ligne actuelle et chaque ligne suivante
                    print(f"Lignes entre {ligne} et {ligne2}: {lignes_entre}")
                    case_suivante = grille[ligne2][colonne] # Case dans la ligne suivante

                    

                    if case_suivante == 0 and case_actuelle > 0: # Si la case de la ligne suivante est vide et que l'actuelle ne l'est pas
                        grille[ligne2][colonne] = case_actuelle # Déplacer le nombre de la case actuelle vers la ligne en-dessous
                        grille[ligne][colonne] = 0 # On vide la ligne actuelle
                        break # On quitte la boucle immédiatement 

                    else:
                        break

                                                 
                
                    
        
       
                

        coords_apparation_nombre = coords_aleat(grille) # Générer des coordonnées aléatoires pour le nouveau nombre à générer
        print("Coordonnées du nombre à apparaitre :", coords_apparation_nombre)
        ligne_nombre = coords_apparation_nombre[0] # Ligne dans laquelle le nombre doit apparaître
        #print("Ligne dans laquelle le nombre doit apparaitre :", ligne_nombre)
        colonne_nombre = coords_apparation_nombre[1] # Colonne de la ligne dans laquelle le nombre doit apparaître
        #print("Colonne de la ligne dans laquelle le nombre doit apparaitre :", colonne_nombre)

        grille[ligne_nombre][colonne_nombre] = generer_nombre_a_apparaitre() # Générer le nombre et le placer dans la grille aux coordonnées choisies
                        

    if direction == "droite": # Si on doit déplacer les nombres vers la droite
        print("Déplacement vers la droite")


        # Logique du déplacement à mettre ci-dessous    
        for ligne in range(len(grille)): # Pour chaque ligne de la grille
            for colonne in range(len(grille[ligne])-1): # Pour chaque colonne de la grille
                #print(f"Coords. de la case actuelle : {ligne} (ligne) {colonne} (colonne)")
                case_actuelle = grille[ligne][colonne] # Case actuelle
                for colonne2 in range(colonne+1, len(grille[ligne])): # Pour chaque colonne qui suit l'actuelle
                    #print(f"Coords. de la case suivante : {ligne} (ligne) {colonne2} (colonne)")
                    case_apres = grille[ligne][colonne2] # Case après l'actuelle
                    cases_entre = grille[ligne][colonne+1:colonne2] # cases entre la case actuelle et les suivantes
                    print(f"Cases entre la colonne n° {colonne} et la colonne n°{colonne2} (compte à partir de zéro):", cases_entre)
                    """for case in colonnes_entre: # Pour chaque case dans les colonnes situées entre la colonne actuelle et les suivantes
                        if case > 0 and case != case_actuelle: # Si le contenu de la case est supérieur à zéro et que son contenu est différent de celui de la case actuelle
                            break"""
                    
                    if any(case!=0 for case in cases_entre): # Si des cases comprises entre l'actuelle et l'une des suivantes ne sont pas vides
                        continue # Ignorer la case actuelle et continuer la boucle

                    elif case_actuelle == case_apres: # Si le contenu de la case actuelle vaut celui d'une des cases
                        grille[ligne][colonne2] = grille[ligne][colonne]*2 # On fusionne les deux cases par une multiplication
                        grille[ligne][colonne] = 0 # On vide la case actuelle
                        score.augmenter(grille[ligne][colonne2]) # Augmenter le score du joueur
                        meilleur_score.actualiser(score.valeur) # Actualiser le meilleur score
                        meilleur_score.sauvegarder() # Sauvegarder le meilleur score
                        break

                    elif case_apres == 0: # Si la case suivante est vide
                        grille[ligne][colonne2] = case_actuelle # Déplacer le nombre de la case actuelle vers la case vide
                        grille[ligne][colonne] = 0 # Vider la case actuelle

        
        coords_apparation_nombre = coords_aleat(grille) # Générer des coordonnées aléatoires pour le nouveau nombre à générer
        print("Coordonnées du nombre à apparaitre :", coords_apparation_nombre)
        ligne_nombre = coords_apparation_nombre[0] # Ligne dans laquelle le nombre doit apparaître
        #print("Ligne dans laquelle le nombre doit apparaitre :", ligne_nombre)
        colonne_nombre = coords_apparation_nombre[1] # Colonne de la ligne dans laquelle le nombre doit apparaître
        #print("Colonne de la ligne dans laquelle le nombre doit apparaitre :", colonne_nombre)

        grille[ligne_nombre][colonne_nombre] = generer_nombre_a_apparaitre() # Générer le nombre et le placer dans la grille aux coordonnées choisies
                                        

                    

                    
                    

                    

                              



"""
def verifier_nombres_equivalents(direction):
    "Vérifier si deux nombres équivalents peuvent être additionnés dans une certaine direction"
    pass
"""


def afficher_score():
    "Afficher le score du joueur"
    print(f"Score : {score.valeur}", end=" ")
    print(f"Meilleur : {meilleur_score.valeur}")



def jeu():
    "La fonction jeu génère une nouvelle grille via generer_grille et démarre une nouvelle boucle de jeu"
    grille = generer_grille() # Générer une nouvelle grille de jeu
    grille[0][0] = generer_nombre_a_apparaitre() # Générer un nombre (2 ou 4) pour permettre au joueur de commencer la partie
    objectif = 2048 # Objectif que le joueur doit atteindre
    objectifs = [objectif, objectif*2] # Liste des objectifs de nombres à atteindre que le joueur peut réaliser, s'il dépasse l'objectif initial de 2048. Chaque nouvel objectif correspond au précédent multiplié par deux
    for i in range(1, 4): # Ajouter trois objectifs
        objectifs.append(objectifs[i]*2) # Chaque nouvel objectif correspond au précédent multiplié par 2
    
    print("Objectifs :", objectifs)
    """for i in range(2):
        nombre = generer_nombre_a_apparaitre() # Générer un premier nombre, soit un 2, soit un 4
        if i == 0:
            mettre_a_jour_grille(grille=grille, ligne=0, colonne=0, nombre=nombre) # Mettre à jour la grille pour qu'elle contienne le premier nombre généré
        if i == 1:
            mettre_a_jour_grille(grille=grille, ligne=1, colonne=0, nombre=nombre) # Mettre à jour la grille pour qu'elle contienne le premier nombre généré
            """
    
    afficher_score() # Afficher le score du joueur
    afficher_grille(grille) # Afficher la grille

    while not grille_pleine(grille):  # Tant que la grille de jeu n'est pas pleine
        touche = entree_utilisateur() # Demander la direction dans laquelle déplacer les nombres à l'utilisateur. S'il appuie sur z:vers le haut, q:vers la gauche, s:vers le bas et d:vers la droite
        
        direction = touches_directions[touche] # Direction correspondante à la touche pressée
        deplacer_nombres(grille, direction) # Déplacer les nombres de la grille dans la direction correspondante à la touche
        afficher_score() # Afficher le score du joueur
        afficher_grille(grille) # Afficher la grille

        if objectif_atteint(grille, objectif=objectif) and objectif != objectifs[len(objectifs) -1]: # Si l'objectif actuel a été atteint et qu'il ne s'agissait pas du dernier
            objectif_suivant = determiner_nouvel_objectif(liste_objectifs=objectifs, objectif_actuel=objectif) # Déterminer quel sera l'objectif suivant
            print(f"Vous avez atteint l'objectif de {objectif}. Félicitations !")
            continuer = input(f"Désirez-vous continuer à jouer ? Votre objectif sera modifié, vous devrez essayer d'atteindre {objectif_suivant} (oui/non): ") # Demander au joueur s'il souhaite continuer avec un nouvel objectif
            if continuer.lower() == "oui": # Si le joueur veut continuer à jouer
                objectif = objectif_suivant
                continue
            else:
                return
            
        elif objectif == objectifs[len(objectifs) -1]: # Si le joueur a atteint tous les objectifs du jeu
            print("Vous avez atteint tous les objectifs et terminé(e) la partie. Félicitations !") # Afficher un message de victoire au joueur
            return

    if grille_pleine(grille): # Si la grille de jeu est pleine
        print("Fin de la partie ! La grille est pleine.")



while True:
    """Cette boucle démarre une nouvelle partie puis demande au joueur s'il souhaite rejouer à chaque partie terminée. S'il répond 'oui', alors une nouvelle partie est créée, 
    sinon la boucle s'arrête ici."""
    jeu() # Lancer une nouvelle partie
    rejouer = input("Voulez vous rejouer (oui/non) ? ")  # Demander au joueur s'il souhaite rejouer
    if rejouer.lower() == "oui": # Si le joueur veut rejouer
        jeu()

    else: # Si le joueur veut arrêter de jouer
        break  # On quitte la boucle, ce qui arrête le jeu  


print("Vous avez quitté(e) le jeu.")      









