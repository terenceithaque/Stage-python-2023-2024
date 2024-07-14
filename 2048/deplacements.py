"deplacements.py gère les différents déplacements de nombres dans une grille"
from score import *




def deplacerHaut(grille, score_var=Score(), max_score_var=MeilleurScore()):
    "Déplacer les nombres vers le haut et mettre à jour le score et le meilleur score du joueur"
        #print("Déplacement vers le haut")

        # Logique du déplacement à mettre ci-dessous

    for ligne in range(len(grille) -1) : # Pour chaque ligne du jeu
            for colonne in range(len(grille[ligne])): # Pour chaque colonne de la ligne
                nombre_case_actuelle = grille[ligne][colonne] # Nombre contenu dans la case actuelle
                for ligne2 in range(ligne+1, len(grille)): # Parcourir toutes les lignes à partir de l'actuelle (précédant donc l'actuelle dans l'autre sens)
                    if nombre_case_actuelle > 0: # Si le nombre est supérieur à zéro

                        case_suivante = grille[ligne2][colonne] # Case dans la ligne suivante
                        """if case_precedente == 0 :# Si la case sur la ligne précédente est vide
                            case_precedente = nombre_case_actuelle # Mettre à jour le nombre de la case sur la ligne précédente"""
                        
                        if case_suivante== nombre_case_actuelle: # Si le nombre dans la case sur la ligne précédente correspond à celui de la case actuelle
                            grille[ligne2][colonne] = 0 # Mettre la case précédente à 0
                            grille[ligne][colonne] = nombre_case_actuelle*2 # Déplacer le nombre de la case sur la ligne précédente sur la case actuelle

                            score_var.augmenter(nombre_case_actuelle*2) # Augmenter le score du joueur
                            max_score_var.actualiser(score_var.valeur) # Actualiser le meilleur score
                            max_score_var.sauvegarder() # Sauvegarder le meilleur score
                            break # Arrêter la boucle

                        else: # Sinon 
                            break

    for r in range(len(grille)): # Pour autant de lignes qu'il n'y a dans la grille              
            for ligne in range(len(grille) -1): # Pour chaque ligne de la grille
                for colonne in range(len(grille[ligne])): # Pour chaque colonne de la ligne
                    case_suivante = grille[ligne +1][colonne] # Case de la ligne suivante
                    if grille[ligne][colonne] == 0: # Si la case actuelle est vide
                    
                        if case_suivante > 0: # Si la case suivante n'est pas vide
                            grille[ligne][colonne] = case_suivante # Déplacer le nombre de la case suivante sur la case actuelle
                            grille[ligne+1][colonne] = 0 # On vide la case suivante
                            
                        #grille[ligne +1][colonne] = generer_nombre_a_apparaitre() # On génère un nouveau nombre dans la case vidée  

    
def deplacerGauche(grille, score_var=Score(), max_score_var=MeilleurScore()):
    "Déplacer les nombres vers la gauche et mettre à jour le score et le meilleur score du joueur"
    for ligne in range(len(grille)): # Pour chaque ligne de la grille
            #print(f"Longueur de la ligne n°{ligne} :", len(grille[ligne]))
            for colonne in range(1, len(grille[ligne])): # On parcoure les colonnes de la ligne
                #print("Case actuelle :", grille[ligne][colonne], end=" ")
                #print(f"Colonne dans la ligne n°{ligne} :", colonne)
                for colonne2 in range(colonne-1, colonne): # Pour chaque colonne dans la ligne avant l'actuelle
                    case_precedente = grille[ligne][colonne2] # Nombre contenu dans la case avant
                    #print("Case suivante :", case_suivante, end= " ")
                    if case_precedente > 0: # Si le nombre de la case précédente est supérieur à 0
                        if grille[ligne][colonne] == case_precedente: # Si le nombre dans la case actuelle correspond à celui dans la case précédente
                            print("Le nombre de la case actuelle est égal à celui de la suivante (gauche).")
                            grille[ligne][colonne2] = grille[ligne][colonne]*2 # On fusionne les nombres de la case actuelle et de la case précédente par une multiplication
                            grille[ligne][colonne] = 0 # On vide la case actuelle
                            score_var.augmenter(grille[ligne][colonne2]) # Augmenter le score du joueur
                            max_score_var.actualiser(score_var.valeur) # Actualiser le meilleur score
                            max_score_var.sauvegarder() # Sauvegarder le meilleur score

                        else: # Si la case actuelle et la case suivante contiennent des nombres différents
                             print("Le nombre de la case actuelle n'est pas égal à celui de la case suivante (gauche).")
                             break

                    else: # Si la case suivante est vide
                        print(f"La case suivante (coords. {ligne}, {colonne2}) est vide (gauche)")
                        if grille[ligne][colonne] > 0: # Mais que l'actuelle ne l'est pas
                            grille[ligne][colonne2] = grille[ligne][colonne] # Déplacer le nombre de la colonne actuelle vers la colonne suivante
                            grille[ligne][colonne] = 0 # Vider la case actuelle
                        #grille[ligne][colonne] = generer_nombre_a_apparaitre() # On vide la case actuelle

    



def deplacerBas(grille, score_var=Score(), max_score_var=MeilleurScore()):
    "Déplacer les nombres vers le bas et mettre à jour le score et le meilleur score du joueur"
    for ligne in range(len(grille)): # On parcoure les lignes de la grille
            #print("Numéro de la ligne :", ligne)
            for colonne in range(len(grille[ligne])): # Pour chaque colonne de la ligne
                nombre_case_actuelle = grille[ligne][colonne] # Nombre dans la case actuelle
                for ligne2 in range(ligne-1, -1, -1): # Pour chaque ligne avant la ligne actuelle
                    #print("Ligne précédent la ligne actuelle :", ligne2)
                    if grille[ligne2][colonne] == nombre_case_actuelle and grille[ligne2][colonne] > 0: # Si le nombre contenu dans une des cases précédentes correspond au nombre de la case actuelle
                        grille[ligne2][colonne] = 0 # On vide la case précédente
                        grille[ligne][colonne] *= 2 # On fusionne les nombres des deux cases par une multiplication
                        score_var.augmenter(grille[ligne][colonne]*2) # Augmenter le score du joueur
                        max_score_var.actualiser(score_var.valeur) # Actualiser le meilleur score
                        max_score_var.sauvegarder() # Sauvegarder le meilleur score
                        break

                    
                    
                    else:
                        break

                      




                    

                

                        
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

                    else: # Si la case suivante n'est pas vide
                        break # On s'arrête ici

    

def deplacerDroite(grille, score_var=Score(), max_score_var=MeilleurScore()):
    "Déplacer les nombres vers la droite et mettre à jour le score et le meilleur score du joueur"
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
                        score_var.augmenter(grille[ligne][colonne2]) # Augmenter le score du joueur
                        max_score_var.actualiser(score_var.valeur) # Actualiser le meilleur score
                        max_score_var.sauvegarder() # Sauvegarder le meilleur score
                        break

                    elif case_apres == 0: # Si la case suivante est vide
                        grille[ligne][colonne2] = case_actuelle # Déplacer le nombre de la case actuelle vers la case vide
                        grille[ligne][colonne] = 0 # Vider la case actuelle

    