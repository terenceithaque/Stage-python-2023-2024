"score.py contient deux classes (Score et MeilleurScore) qui servent à gérer le score du joueur"
import os


class Score:
    "Objet représentant le score du joueur"
    def __init__(self):
        "Constructeur de la classe Score"
        self.valeur = 0 # Valeur initiale du score du joueur

    def augmenter(self, montant=1):
        "Augmenter le score du joueur d'un certain montant en points. Si aucun montant n'est fourni, alors il sera mis à 1 par défaut."
        self.valeur += montant # Additionner le montant en points 
        return self.valeur # Retourner le score augmenté
    


class MeilleurScore:
    "Meilleur score réalisé par le joueur"
    def __init__(self): 
        self.fichier = os.path.abspath("2048\\score.txt") # Fichier contenant le meilleur score du joueur
        self.valeur = self.lire_meilleur_score() # Valeur du meilleur score, obtenue depuis le fichier score.txt

    def actualiser(self, valeur_score_actuel):
        "Actualiser le meilleur score si le joueur a battu un nouveau record de points"
        if valeur_score_actuel > self.valeur: # Si la valeur du score actuel est supérieure à celle du meilleur score
            self.valeur = valeur_score_actuel# Mettre à jour la valeur du meilleur score

        return self.valeur

    def lire_meilleur_score(self):
        "Obtenir le meilleur score réalisé par le joueur en lisant le fichier score.txt"   
        try: # Tenter de lire le fichier score.txt
            with open(self.fichier, "r") as f: # Ouvrir le fichier score.txt en lecture
                try: # Tenter de convertir le contenu du fichier en un nombre entier
                    self.valeur = int(f.read()) # Lire le contenu du fichier et le convertir en un entier pouvant être traité par le jeu
                    f.close()

                except ValueError: # En cas d'erreur avec le contenu du fichier (par exemple, si le fichier est vide)
                    self.valeur = 0 # Initialiser la valeur du meilleur score à zéro


                return self.valeur # Retourner la valeur du meilleur score enregistré dans le fichier score.txt    

        except FileNotFoundError as erreur: # Si le fichier score.txt est introuvable
            print(f"Le fichier score.txt est introuvable. Le message d'erreur indique : {erreur}")
            self.valeur = 0 # Initialiser la valeur du meilleur score à zéro
            return self.valeur
        

    def sauvegarder(self):
        "Sauvegarder le meilleur score dans le fichier score.txt"
        with open(self.fichier, "w") as f: # Ouvrir le fichier score.txt en écriture
            f.write(str(self.valeur)) # Convertir la valeur du meilleur score en chaîne de caractères et l'écrire dans le fichier texte
            f.close() # Fermer le fichier






      

