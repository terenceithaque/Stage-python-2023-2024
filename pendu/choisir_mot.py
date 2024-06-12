"Choisir un mot au hasard dans le fichier mots.txt"
from random import randrange # Importation de la fonction randrange depuis le module random pour nous permettre de choisir un élément au hasard.

file = "mots.txt" # Définir le nom du fichier où les mots sont stockés

      



def choisir_mot():
    "Choisir un mot au hasard"
    
    with open(file, "r", encoding="utf-8") as rf: # Ouvrir le fichier des mots en mode lecture. rf = read file
        contenu = rf.readlines()
        mot = randrange(len(contenu))
        mot_choisi = contenu[mot]
        mot_choisi = mot_choisi.lower() # Convertir chaque caractère du mot en minuscules
        mot_choisi = mot_choisi.rstrip()
        
    

    
    return mot_choisi

