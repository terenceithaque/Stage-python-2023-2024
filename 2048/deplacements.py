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
    pass