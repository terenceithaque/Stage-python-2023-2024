# Programme pour produire un L-système

alphabet = ["A", "B"] # Ensemble des caractères que le L-système pourra utiliser

def afficher_generation(counter):
  "Afficher une génération de l'algue"
  i = 0
  while i < counter:
    nom = "" # Nom de la génération courante
    for j in range(0, i):
      if j >= 0: # Si c'est la première génération
        print("Génération", j, ":", alphabet[j], end=" ")
        j = 0  # Réinitialiser j


    i += 1    


afficher_generation(6)        





