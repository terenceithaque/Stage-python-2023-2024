"score.py gère le score du joueur"
import os
fichier_score = os.path.abspath("2048\\score.txt") # Fichier qui contient le meilleur score du joueur, sous forme de texte

def obtenir_meilleur_score():
    "Lire le meilleur score du joueur depuis le fichier score.txt"
    try: # Essayer de lire le fichier
        with open(fichier_score, "r") as f: # Ouvrir le fichier en lecture.
            meilleur_score = int(f.read()) # Lire le meilleur score et le convertir sous forme de nombre entier
            print("Meilleur score (lu depuis score.txt) :", meilleur_score)
            f.close() # Fermer le fichier afin de libérer des ressources
            return meilleur_score # Retourner le meilleur score afin de pouvoir l'utiliser dans le reste du programme / module
        
        
    except FileNotFoundError as erreur: # Si le fichier "score.txt" est introuvable
        print(f"Impossible de trouver le fichier score.txt. Le message d'erreur indique : {erreur}")
        meilleur_score = 0 # Initialiser le meilleur score à zéro
        print(f"Meilleur score initalisé :  {meilleur_score}")
        return meilleur_score # Retourner le meilleur score



score = 0 # Score actuel du joueur
print("Score :", score)
meilleur_score = obtenir_meilleur_score() # Meilleur score du joueur

def augmenter_score(montant):
    "Augmenter le score du joueur d'un certain montant en points"
    global score
    score += montant # Augmenter le score en ajoutant le montant en points à ce dernier
    return score # Retourner le score actualisé


score = augmenter_score(7*3) 

print(f"Score actualisé :", score)
