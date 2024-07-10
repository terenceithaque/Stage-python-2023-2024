"deplacements.py gère les différents déplacements de nombres dans une grille"

def deplacerHaut(grille, direction="haut", score_var=0, max_score_var=0):
    "Déplacer les nombres vers le haut et mettre à jour le score et le meilleur score du joueur"
    if direction == "haut": # Si on doit déplacer les nombres vers le haut
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
                        else: # Sinon 
                            continue # Continuer la boucle en ignorant le reste

        for r in range(len(grille)): # Pour autant de lignes qu'il n'y a dans la grille              
            for ligne in range(len(grille) -1): # Pour chaque ligne de la grille
                for colonne in range(len(grille[ligne])): # Pour chaque colonne de la ligne
                    case_suivante = grille[ligne +1][colonne] # Case de la ligne suivante
                    if grille[ligne][colonne] == 0: # Si la case actuelle est vide
                    
                        if case_suivante > 0: # Si la case suivante n'est pas vide
                            grille[ligne][colonne] = case_suivante # Déplacer le nombre de la case suivante sur la case actuelle
                            grille[ligne+1][colonne] = 0 # On vide la case suivante
                            
                        #grille[ligne +1][colonne] = generer_nombre_a_apparaitre() # On génère un nouveau nombre dans la case vidée  



def deplacerGauche(grille, direction="gauche", score_var=0, max_score_var=0):
    "Déplacer les nombres vers la gauche et mettre à jour le score et le meilleur score du joueur"
    if direction == "gauche":
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
                            score_var.augmenter(grille[ligne][colonne]) # Augmenter le score du joueur
                            max_score_var.actualiser(score_var.valeur) # Actualiser le meilleur score
                            max_score_var.sauvegarder() # Sauvegarder le meilleur score

                    else: # Si la case suivante est vide
                        print(f"La case (coords. {ligne}, {colonne2}) est vide")
                        if grille[ligne][colonne] > 0: # Mais que l'actuelle ne l'est pas
                            grille[ligne][colonne2] = grille[ligne][colonne] # Déplacer le nombre de la colonne actuelle vers la colonne suivante
                            grille[ligne][colonne] = 0 # Vider la case actuelle
                        #grille[ligne][colonne] = generer_nombre_a_apparaitre() # On vide la case actuelle



def deplacerBas(grille, direction="bas", score_var=0, max_score_var=0):
    "Déplacer les nombres vers le bas et mettre à jour le score et le meilleur score du joueur"
    if direction == "bas":
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