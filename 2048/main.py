# Jeu de 2048 en ligne de commande
import random
from score import * # Importer l'entièreté du module score
from deplacements import *
from game_exceptions import *




meilleur_score = MeilleurScore() # Meilleur score du joueur
score = Score()# Score actuel du joueur. S'il est supérieur au meilleur score, le meilleur score sera actualisé.



touches = ["z","q","s","d"] # Listes des touches auxquelles le jeu réagit. Elles déterminent dans quel direction les nombres doivent être déplacés.

coords_cases_occuppees = [] # Coordonnées des cases occupées 



touches_directions = {
    "z":"haut",
    "q":"gauche",
    "s":"bas",
    "d":"droite"
} # Dictionnaire qui liste pour chaque touche la direction dans laquelle elle va déplacer les nombres de la grille

def generer_grille():
    "Générer une grille de jeu de dimensions 4x4"
    grille = [[0,0,0,0] for i in range(4)] # Générer une grille de quatre case par ligne
    return grille # Retourner la grille nouvellement générée pour pouvoir l'utiliser en jeu









def mettre_a_jour_grille(grille, ligne=0, colonne=0,nombre=2):
    "Mettre à jour la grille de jeu"
    grille[ligne][colonne] = nombre # Mettre à jour la case aux coordonnées (ligne, colonne) avec le nouveau nombre
    coords_cases_occuppees.append((ligne, colonne)) # Ajouter les coordonnées aux coordonnées occupées
    print("Coordonnées des cases occupées :", coords_cases_occuppees)


def coords_aleat(grille):
    "Générer des coordonnées aléatoires à partir d'une grille"
    ligne = random.randint(0, len(grille) -1) # Générer un numéro de ligne aléatoire
    colonne = random.randint(0, len(grille[ligne]) -1) # Générer un numéro de colonne aléatoire dans la ligne
    while grille[ligne][colonne] > 0: # Si la case aux coordonnées générées est déjà prise
        # On génère un nouveau nombre pour la ligne et la colonne, jusqu'à ce que la case aux coordonnées nouvellement générées soit libre
        ligne = random.randint(0, len(grille) -1) 
        colonne = random.randint(0, len(grille[ligne]) -1) 


    coords = (ligne, colonne) # coords est un tuple contenant les coordonnées au format (ligne, colonne dans la ligne)
    return coords # Retourner le tuple contenant les coordonées



def entree_utilisateur():
    "Demander une entrée à l'utilisateur. On s'en servira pour déterminer le sens dans lequel doivent être déplacés les nombres de la grille. Si la touche pressé n'est pas définie dans le dictionnaire touches_directions, alors redemande la saisie d'une touche à l'utilisateur jusqu'à ce que celle-ci soit définie"
        
    touche = input("Appuyez sur une seule touche (z, q, s ou d) et appuyez sur Entrée:") # Demander à l'utilisateur de presser une touche du clavier
    while touche not in touches: # Si l'utilisateur a appuyé sur une touche qui n'est pas comprise par le jeu
            print("La touche saisie n'est pas valide. Veuillez réessayer :") # Afficher un message à l'utilisateur pour indiquer qu'il doit réessayer
            touche = entree_utilisateur() # Redemander à l'utilisateur de saisir une touche et mettre à jour la variable contenant le résultat de la saisie pour éviter une boucle infinine

    return touche # Une fois que l'utilisateur a saisi une touche valide, la retourner afin que le reste du jeu puisse déterminer la direction dans laquelle déplacer les nombres


def generer_nombre_a_apparaitre():
    "Générer le nombre qui devra apparaître dans la grille quand l'utilisateur déplace des nombre dans la grille"
    probabilite_4 = random.randint(0, 100) # Probabilité que le nombre 4 apparaisse dans la grille de jeu, en pourcentage
    print(f"Probabilité qu'un 4 apparaisse dans la grille : {probabilite_4} %")
    if probabilite_4 >= 67: # S'il y a 67 % de chances ou plus que le nombre 4 apparaisse
        nombre_a_apparaitre = 4 # On fait apparaître un 4 dans la grille de jeu

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

    if lignes_pleines == grille: # Si la liste des lignes pleines correspond à la grille de jeu, c'est que la grille est entièrement pleine
        return True # On indique que la grille est pleine

    return False # Sinon, on indique que la grille n'est pas pleine



def objectif_atteint(grille, objectif=2048):
    "Vérifier si le joueur a atteint l'objectif (le nombre à obtenir pour gagner), par défaut 2048"
    for ligne in range(len(grille)): # Pour chaque ligne de la grille
        if objectif in grille[ligne]: # Si la ligne possède une case contenant le nombre à atteindre
            return True # L'objectif est atteint, on retourne alors True
        
    return False # Si l'objectif n'est pas atteint, ou retourne False    








def deplacer_nombres(grille, direction):
    "Déplacer des nombres de la grille selon une direction précise"
    global score
    #print("Déplacement vers le haut")
    # Logique du déplacement à mettre ci-dessous
    if direction == "haut": # Si on doit déplacer des nombres vers le haut
        deplacerHaut(grille, score_var=score, max_score_var=meilleur_score) # Déplacer les nombres vers le haut et mettre à jour le score
        coords_apparation_nombre = coords_aleat(grille) # Générer des coordonnées aléatoires pour le nouveau nombre à générer
        print("Coordonnées du nombre à apparaitre :", coords_apparation_nombre)
        ligne_nombre = coords_apparation_nombre[0] # Ligne dans laquelle le nombre doit apparaître
        #print("Ligne dans laquelle le nombre doit apparaitre :", ligne_nombre)
        colonne_nombre = coords_apparation_nombre[1] # Colonne de la ligne dans laquelle le nombre doit apparaître
        #print("Colonne de la ligne dans laquelle le nombre doit apparaitre :", colonne_nombre)
        grille[ligne_nombre][colonne_nombre] = generer_nombre_a_apparaitre() # Générer le nombre et le placer dans la grille aux coordonnées choisies

        


                        

                        
    elif direction == "gauche": # Si on doit déplacer les nombres vers la gauche
        #print("Déplacement vers la gauche")   

        # Logique du déplacement à mettre ci-dessous
        deplacerGauche(grille, score_var=score, max_score_var=meilleur_score) # Déplacer les nombres vers la gauche
        coords_apparation_nombre = coords_aleat(grille) # Générer des coordonnées aléatoires pour le nouveau nombre à générer
        print("Coordonnées du nombre à apparaitre :", coords_apparation_nombre)
        ligne_nombre = coords_apparation_nombre[0] # Ligne dans laquelle le nombre doit apparaître
        #print("Ligne dans laquelle le nombre doit apparaitre :", ligne_nombre)
        colonne_nombre = coords_apparation_nombre[1] # Colonne de la ligne dans laquelle le nombre doit apparaître
        #print("Colonne de la ligne dans laquelle le nombre doit apparaitre :", colonne_nombre)

        grille[ligne_nombre][colonne_nombre] = generer_nombre_a_apparaitre() # Générer le nombre et le placer dans la grille aux coordonnées choisies
                    
    elif direction == "bas": # Si on doit déplacer les nombres vers le bas
        #print("Déplacement vers le bas")

        deplacerBas(grille, score_var=score, max_score_var=meilleur_score) # Déplacer les nombres vers le bas
        coords_apparation_nombre = coords_aleat(grille) # Générer des coordonnées aléatoires pour le nouveau nombre à générer
        print("Coordonnées du nombre à apparaitre :", coords_apparation_nombre)
        ligne_nombre = coords_apparation_nombre[0] # Ligne dans laquelle le nombre doit apparaître
        #print("Ligne dans laquelle le nombre doit apparaitre :", ligne_nombre)
        colonne_nombre = coords_apparation_nombre[1] # Colonne de la ligne dans laquelle le nombre doit apparaître
        #print("Colonne de la ligne dans laquelle le nombre doit apparaitre :", colonne_nombre)

        grille[ligne_nombre][colonne_nombre] = generer_nombre_a_apparaitre() # Générer le nombre et le placer dans la grille aux coordonnées choisies

    elif direction == "droite": # Si on doit déplacer les nombres vers la droite
        print("Déplacement vers la droite")        

        deplacerDroite(grille, score_var=score, max_score_var=meilleur_score) # Déplacer les nombres vers la droite
        coords_apparation_nombre = coords_aleat(grille) # Générer des coordonnées aléatoires pour le nouveau nombre à générer
        print("Coordonnées du nombre à apparaitre :", coords_apparation_nombre)
        ligne_nombre = coords_apparation_nombre[0] # Ligne dans laquelle le nombre doit apparaître
        #print("Ligne dans laquelle le nombre doit apparaitre :", ligne_nombre)
        colonne_nombre = coords_apparation_nombre[1] # Colonne de la ligne dans laquelle le nombre doit apparaître
        #print("Colonne de la ligne dans laquelle le nombre doit apparaitre :", colonne_nombre)

        grille[ligne_nombre][colonne_nombre] = generer_nombre_a_apparaitre() # Générer le nombre et le placer dans la grille aux coordonnées choisies


    else: # Si la direction fournie n'est pas valide
        raise InvalidDirectionException # Déclencher une exception indiquant qu'une direction invalide a été fournie

    

        
                        





                        



    
    
        


                        

                                        

                    

                    
                    

                    

                              





def afficher_score():
    "Afficher le score du joueur"
    print(f"Score : {score.valeur}", end=" ") # Afficher la valeur du score actuel, en indiquant de mettre un espace à la place d'un saut à la ligne à la fin de l'affichage
    print(f"Meilleur : {meilleur_score.valeur}") # Afficher la valeur du meilleur score



def jeu():
    "La fonction jeu génère une nouvelle grille via generer_grille et démarre une nouvelle boucle de jeu"
    grille = generer_grille() # Générer une nouvelle grille de jeu
    coords_depart = coords_aleat(grille)  # Générer des coordonées aléatoires pour le premier nombre à apparaître dans la grille
    ligne_depart = coords_depart[0] # Ligne du premier nombre à apparaître
    col_depart = coords_depart[1] # Colonne du premier nombre à apparaître

    grille[ligne_depart][col_depart] = generer_nombre_a_apparaitre() # Générer un nombre (2 ou 4) pour permettre au joueur de commencer la partie
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
        deplacer_nombres(grille, direction=direction) # Déplacer les nombres de la grille dans la direction correspondante à la touche
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









