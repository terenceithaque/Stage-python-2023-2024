"score.py gère le score du joueur"
import os
fichier_score = os.path.abspath("2048\\score.txt") # Fichier qui contient le meilleur score du joueur, sous forme de texte

def obtenir_meilleur_score():
    "Lire le meilleur score du joueur depuis le fichier score.txt"
    try: # Essayer de lire le fichier
        with open(fichier_score, "r") as f: # Ouvrir le fichier en lecture.
            global meilleur_score
            try:
                meilleur_score = int(f.read()) # Lire le meilleur score et le convertir sous forme de nombre entier
            
            except ValueError: # En cas d'erreur avec la valeur du contenu du fichier texte (si le fichier est vide, par exemple)
                meilleur_score = 0 # Initialiser le meilleur score à zéro
                
            print("Meilleur score (lu depuis score.txt) :", meilleur_score)
            f.close() # Fermer le fichier afin de libérer des ressources
            return meilleur_score # Retourner le meilleur score afin de pouvoir l'utiliser dans le reste du programme / module
        
        
    except FileNotFoundError as erreur: # Si le fichier "score.txt" est introuvable
        print(f"Impossible de trouver le fichier score.txt . Le message d'erreur indique : {erreur}")
        meilleur_score = 0 # Initialiser le meilleur score à zéro
        print(f"Meilleur score initalisé :  {meilleur_score}")
        return meilleur_score # Retourner le meilleur score



score = 0 # Score actuel du joueur
print("Score :", score)
meilleur_score = obtenir_meilleur_score() # Meilleur score du joueur

def augmenter_score(montant):
    "Augmenter le score du joueur d'un certain montant en points"
    global score
    global meilleur_score
    score += montant # Augmenter le score en ajoutant le montant en points à ce dernier

    meilleur_score = mettre_a_jour_meilleur_score() # Mettre à jour le meilleur score du joueur
    return score # Retourner le score actualisé


def mettre_a_jour_meilleur_score():
    "Mettre à jour le meilleur score du joueur si ce dernier a battu un nouveau record de points"
    global meilleur_score
    if score > meilleur_score: # Si le score actuel est strictement supérieur au meilleur score
        meilleur_score = score # Mettre à jour le meilleur score sur le score actuel du joueur
        print(f"Meilleur score actualisé : {meilleur_score}")
    return meilleur_score # Retourner le meilleur score actualisé


def sauvegarder_score():
    "Sauvegarder le meilleur score du joueur dans le fichier score.txt"
    global meilleur_score
    with open(fichier_score, "w") as f: # Ouvrir le fichier "score.txt" en écriture
        f.write(str(meilleur_score)) # Convertir le meilleur score en chaîne de caractères, puis l'écrire dans le fichier texte
        f.close() # Fermer le fichier pour libérer des ressources
        print("Meilleur score enregistré dans le fichier ", os.path.abspath(fichier_score))



"""
score = augmenter_score(120)
print(f"Score augmenté :", score)
sauvegarder_score()        
"""