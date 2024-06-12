# Jeu de puissance 4 en interface graphique
from tkinter import * # Importation de tkinter
from tkinter import messagebox
from tkinter import simpledialog
import random
import threading
import time

jeu = True # Variable pour savoir si le jeu est en cours d'exécution

fenetre = Tk() # Fenêtre du jeu






joueur = 1 # numéro du joueur actuel
label_tour = Label(fenetre, text=f"Au tour du joueur {joueur}", bg="orange")

label_tour.pack()



def demander_quitter(event=None):
    "Quitter le jeu"
    ask = messagebox.askyesno("Arrêter la partie en cours ?", "Voulez-vous quitter le jeu ?") # Demander au joueur s'il souhaite quitter la partie
    if ask: # Si le joueur veut quitter le jeu
        jeu = False # On arrête le jeu
        fenetre.destroy() # Détruire la fenêtre de jeu



        

bouton_relancer = Button(fenetre, text="Quitter", command=demander_quitter) # Bouton pour quitter l'application
bouton_relancer.pack() # Intégrer le bouton "Quitter" dans la fenêtre


canevas_grille = Canvas(fenetre, width=1000, height=1000, bg="white") # Canevas représentant la grille
canevas_grille.pack()


fenetre.title("Puissance 4 en interface graphique") # On donne son titre à la fenêtre du jeu

grille = [] # Grille du jeu
rectangles = {} # Rectangles représentant une case


joueurs_tours_precedents = []  # Liste des joueurs ayant joués aux tours précédents



def recuperer_couleur(joueur=1):
    "Récupérer la couleur d'un joueur à partir de son numéro"
    if joueur == 1: # Si le numéro du joueur est 1
        return "orange" # On retourne la couleur du joueur 1, l'orange
    
    if joueur == 2: # Si le numéro du joueur est 2
        return "yellow" # On retourne la couleur du joueur 2, le jaune


def remplir_grille():
    "Remplir la grille de jeu "
    grille = [] # On réinitialise la grille
    for i in range(6): # On veut ajouter 6 lignes à la grille
        ligne = [0,0,0,0,0,0,0] # Modèle pour chaque ligne de la grille
        grille.append(ligne) # On ajoute la ligne à la grille

    return grille

remplir_grille()

##print(grille)

def dessiner_grille(grille):
    "Dessiner la grille de jeu"
    #print("Grille du jeu :", grille)
    global rectangles



    for ligne in range(len(grille)): # Pour toute la longueur de la grille. Chaque valeur de longueur représente numériquement la position d'une colonne sur la grille
        for col in range(len(grille[ligne])): # Pour toute la largeur de la grille (largeur de la grille = longueur de chaque colonne)
            rectangles[(ligne, col)] = canevas_grille.create_rectangle(50*(col+1), 50*(ligne+1), 50*(col+1)+ 50, 50*(ligne+1) + 50)
            #print(rectangles)
            
            ##print(grille[ligne]) # On affiche la ligne de la colonne courante
            ##print(grille[ligne][col]) # On affiche le contenu de chaque case de la grille 

            # grille[ligne][col] correspond au numéro contenu par chaque case de la grille de jeu telle qu'elle est définie dans le code
            """if grille[ligne][col] == 1: # Si le numéro est 1, c'est que le joueur 1 a placé un pion dans la case correspondante
                    canevas.config(bg=recuperer_couleur(grille[ligne][col])) # On change la couleur de la case (représentée par le canevas)

            if grille[ligne][col] == 2: # Si le numéro est 2, c'est que le joueur 2 a placé un pion dans la case correspondante
                    canevas.config(bg=recuperer_couleur(grille[ligne][col]))  # On change la couleur de la case (représentée par le canevas)7"""


def ligneLibreDeLaColonne(colonne):
     "Trouver la dernière ligne libre d'une colonne donnée"
     nombre_a_comparer = 0 # Nombre que l'on doit comparer au contenu de la colonne
     for ligne in range(len(grille)-1,-1,-1): # Pour chaque ligne de la colonne
          try:
            if grille[ligne][colonne] == nombre_a_comparer:
               return ligne
            
          except TypeError:
              continue    
     return -1



def trouverColonneCliquee(coords):
    "Trouver la colonne dans laquelle l'utilisateur a cliqué"
    global rectangles
    #print("Rectangles :", rectangles)
    if coords in rectangles: # Si les coordonnées sont présentes dans les clés du dictionnaire
        ligne = coords[0] # Ligne dans les coordonnées
        colonne = coords[1] # Colonne dans les coordonnées
        return grille[ligne][colonne]
       


def trouverCase(forme):
     "Trouver la case correspondant à une forme dans le canevas"
     case = 0 # Case trouvée
     coords = () # Coordonnées de la case sous forme de tuple
     #print("grille :", grille)
     try:
        for key in rectangles: # Pour chaque clé (coordonnée) dans le dictionnaire
            if rectangles[key] == forme: # Si la valeur correspond à l'ID de la forme
                coords = key
                #print("Index de la ligne dans la grille:", grille.index(ligne))
                #print("Index de la case dans la ligne:", ligne.index(case))
                #print("Coordonnées de la case correspondante:", coords)
                #print(trouverColonneCliquee(coords))

                
     except:
        raise Exception(print("Impossible de trouver la case correspondante !"))
     
     return coords # On retourne les coordonnées de la case correspondante à la forme



def verifier_formes_colorees():
    "Vérifier que toutes les formes du canevas ont été colorées"
    couleurs = [] # Liste des couleurs pour chaque forme
    for i in canevas_grille.find_all():
        #print("forme: ", i)
        couleurs.append(canevas_grille.itemcget(i, "fill"))
        #print("couleurs :", couleurs)

    return couleurs  
     

    



def compterCases(toutes=True, ligne=0):
    "Compter toutes les cases pour la grille entière ou pour une ligne de la grille. Si ligne égal -1, alors on ne cherche dans aucune ligne particulière"
    n_cases = 0 # Nombre de cases trouvées
    if toutes: # Si on doit compter les cases de toute la grille de jeu. 

        n_cases = len(grille) * len(grille[ligne]) # Le nombre de cases dans toutes la grille correspond au nombre de lignes dans la grille multiplié par le nombre de cases par ligne
        #print("Nombre total de cases dans la grille :", n_cases)
        return n_cases
    
    elif not toutes: # Si on ne doit pas calculer la totalité des cases dans la grille
        if ligne < 0: # Si le numéro de la ligne est inférieur à 0, elle sera introuvable
            #print("Impossible de compter le nombre de cases pour la ligne : numéro de ligne inférieur à zéro") # Afficher un message d'erreur
            return # Arrêter la fonction
        
        else: # Si une ligne a été spécifiée
            n_cases = len(grille[ligne]) # Le nombre de cases correspond au nombre de cases dans la ligne demandée
            return n_cases 
        
    return n_cases # Si aucune des conditions de calcul des cases n'a été remplie, ou retourne n_cases qui vaut 0    
        
        

def mettre_a_jour_grille(ligne=0, colonne=0,nouvelle_valeur=1):
    "Mettre à jour la valeur de la dernière case libre d'une ligne dans la grille"
    #colonnes_vides = grille[ligne] # Liste des colonnes vides dans la ligne. La dernière sera celle où le jeton sera placé. Au départ, elle est égale à la ligne entière, puis on enlèvera les colonnes qui ne sont pas vides
    """for i, colonne in enumerate(grille[ligne]): # Pour chaque colonne de la ligne
        print("Colonne dans la ligne :", colonne)
        if colonne > 0 and i <= len(colonnes_vides) -1: # Si la colonne n'est pas vide et qu'elle est la dernière colonne de la liste des colonnes vides
            print("Liste des colonnes vides mise à jour :", colonnes_vides)
            grille[ligne][colonne] = nouvelle_valeur # Mettre à jour la dernière case disponible avec le numéro du joueur qui a cliqué
            print("Grille mise à jour :", grille)"""
    
    grille[ligne][colonne] = nouvelle_valeur # Mettre à jour la grille
        
            

    #print("Ligne, mise à jour :", grille[ligne])
    print("Grille, mise à jour :", grille)

    return grille # Retourner la version mise à jour de la grille


def verifierHorizontalement(joueur):
    "Vérifier que le numéro d'un joueur apparaît quatre fois à l'horizontale. Cela nous permet de déterminer s'il a gagné ou non."
    for ligne in grille: # Pour chaque ligne de la grille
        apparitions_numero_joueur = 0 # Nombre d'apparitions du numéro du joueur
        #print("Ligne :", ligne)
        for numero in ligne: # Pour chaque numéro trouvé dans la ligne
            if numero == joueur: # Si on trouve le numéro correspondant au joueur
                #print(f"Le numéro du joueur {joueur} a été trouvé dans la ligne {ligne}")
                apparitions_numero_joueur += 1 # Alors on augmente le nombre de vues du numéro de 1

            else: # Si on trouve un autre numéro
                 #print(f"Le numéro du joueur {joueur} n'a pas été trouvé dans la ligne {ligne}")
                 apparitions_numero_joueur = 0 # On remet le compteur à zéro pour éviter que le joueur puisse gagner sans que ses pions soient alignés consécutivement

            if apparitions_numero_joueur == 4: # Si le numéro du joueur apparaît 4 fois horizontalement, alors ce dernier gagne la partie
                    return joueur # Alors on retourne le numéro du joueur gagnant pour pouvoir gérer la victoire de celui-ci

    return -1 # Si aucun joueur n'a placé 4 jetons horizontalement, on retourne -1 pour dire qu'il n'y a pas victoire

def verifierVerticalement(joueur):
     "Vérifier que le numéro d'un joueur apparaît quatre fois à la verticale. Cela nous permet de déterminer s'il a gagné ou non"
     numeros_joueur_trouves = 0 # Nombre de fois qu'on trouve le numéro du joueur donné en paramètre dans la grille
     for colonne in range(len(grille[0])):
          for ligne in range(len(grille)-1, -1, -1):
               if grille[ligne][colonne] == joueur:
                    numeros_joueur_trouves += 1

                    if numeros_joueur_trouves == 4: # Si on a trouvé 4 fois le numéro d'un même joueur
                         return joueur # On retourne le numéro de ce joueur afin d'indiquer qu'il a gagné la partie 
               
               else:
                    numeros_joueur_trouves = 0


def verifierDiagonale(joueur):
     "Vérifier que le numéro d'un joueur apparaît quatre fois en diagonale. Cela nous permet de déterminer s'il a gagné ou non"
     numeros_joueus_trouve = 0 # Nombre de fois que l'on rencontre le numéro du joueur donné en paramètre en diagonale
     for ligne in range(len(grille)-1,2 ,-1):
          #print("ligne :", grille[ligne])
          for colonne in range(len(grille[ligne])-1, 2,-1):
               if grille[ligne][colonne] == joueur and grille[ligne-1][colonne-1] == joueur and grille[ligne-2][colonne-2] == joueur and grille[ligne-3][colonne-3] == joueur:
                    numeros_joueus_trouve = 4

               if numeros_joueus_trouve == 4: # Si on a trouvé 4 fois le numéro d'un même joueur en diagonale de la droite vers la gauche, on considère qu'il a gagné
                    return joueur # donc on retourne son numéro
               

     for ligne in range(len(grille)-1,2,-1):
          for colonne in range(len(grille[ligne]) -3):
               if grille[ligne][colonne] == joueur and grille[ligne-1][colonne + 1] == joueur and grille[ligne-2][colonne + 2]== joueur and grille[ligne-3][colonne + 3] == joueur: # Si on a trouvé 4 fois le numéro d'un même joueur en diagonale de la gauche vers la droite, on considère qu'il a gagné
                    return joueur   # Donc on retourne son numéro      
     
     return -1 # On retourne -1 si aucun joueur n'a placé 4 jetons en diagonale 


def clic(event=None):
    "Gérer les clics de l'utilisateur dans la fenêtre d'application"
    global joueur
    global rectangles





    id = canevas_grille.find_closest(event.x, event.y) # Obtenir les éléments les plus proches du clic
    """for cle in rectangles: # Pour chaque rectangle dessiné
         if rectangles[cle] == coords[0]: 
             forme = rectangles[cle]"""
     
    forme_proche = id[0] # Forme la plus proche du clic de l'utilisateur
    print("Forme la plus proche du clic :", forme_proche)
    print("Dictionnaire des formes :", rectangles)
    

     
     
     #print("Nombre de cases dans la grille:", compterCases(toutes=True)) # Afficher le nombre de total de cases dans la grille
    #for ligne in range(len(grille)): # Pour chaque ligne de la grille
    #    print("Nombre de cases dans la ligne :", compterCases(toutes=False, ligne=ligne))
    coords = trouverCase(forme_proche)

    ligne = coords[0]  # Ligne dans laquelle se trouve la case correspondante à la forme cliquée
    col = coords[1] # Colonne dans laquelle se trouve la case correspondante à la forme cliquée
    ligne_libre = ligneLibreDeLaColonne(col)
    mettre_a_jour_grille(ligne=ligne_libre,colonne=col,nouvelle_valeur=joueur) # Mettre à jour la valeur de la dernière case vide (dont la valeur vaut 0) de la ligne où le joueur a cliqué
    
    print(f"Ligne libre de la colonne {col}: {ligne_libre}")
    couleur = recuperer_couleur(joueur) # Récupérer la couleur du joueur actuel
    if (ligne_libre, col) in rectangles:
        coords_forme_a_colorer = (ligne_libre,col)
        forme_a_colorer = rectangles[coords_forme_a_colorer]
        print("Coordonées de la forme à colorer :", coords_forme_a_colorer)
        changer_couleur(forme_a_colorer,couleur)

        

    

     
     #trouverCase(coords[0]) 

    #verifierHorizontalement(joueur)
    if verifierHorizontalement(joueur)==joueur: # Si le joueur a placé 4 jetons horizontalement
        #print(f"Le joueur {joueur} a placé 4 jetons horizontalement et gagne !")
            messagebox.showinfo(f"Le joueur n°{joueur} a gagné!", f"Le joueur {joueur} a placé 4 jetons horizontalement") # Afficher au joueur actuel qu'il a gagné
            demander_quitter()  # Demander au joueur s'il souhaite quitter le jeu

    if verifierVerticalement(joueur)==joueur: # Si le joueur a placé 4 jetons verticalement
        #print(f"Le joueur {joueur} a placé 4 jetons verticalement et gagne !")

        messagebox.showinfo(f"Le joueur n°{joueur} a gagné!", f"Le joueur {joueur} a placé 4 jetons verticalement") # Afficher au joueur actuel qu'il a gagné
        demander_quitter()  # Demander au joueur s'il souhaite quitter le jeu
    
    
    if verifierDiagonale(joueur)==joueur: # Si le joueur a placé 4 jetons en diagonale
        #print(f"Le joueur {joueur} a placé 4 jetons en diagonale et gagne !")
        messagebox.showinfo(f"Le joueur n°{joueur} a gagné!", f"Le joueur {joueur} a placé 4 jetons en diagonale") # Afficher au joueur actuel qu'il a gagné
        demander_quitter()  # Demander au joueur s'il souhaite quitter le jeu
    
    if joueur == 1: # Le numéro du joueur actuel est 1
        joueur = 2 # C'est le tour du joueur n°2
        fenetre.title(f"Puissance 4 en interface graphique - Au tour du joueur {joueur}") # On donne son titre à la fenêtre du jeu
        label_tour.config(text=f"Au tour du joueur {joueur}", bg=recuperer_couleur(joueur))

    elif joueur == 2: # Si le numéro du joueur actuel est 2
        joueur = 1 # C'est le tour du joueur numéro 1
        fenetre.title(f"Puissance 4 en interface graphique - Au tour du joueur {joueur}") # On donne son titre à la fenêtre du jeu
        label_tour.config(text=f"Au tour du joueur {joueur}", bg=recuperer_couleur(joueur))

    

    if "" not in verifier_formes_colorees(): # Si toutes les formes sont colorées
        demander_quitter()  # Demander au joueur s'il souhaite quitter le jeu




    #print("Coords: ", coords)








     
     





    



def changer_couleur(canevas, couleur):
     "Changer la couleur d'une forme d'une canevas"
     canevas_grille.itemconfig(canevas, fill=couleur)
                    
     
 
     






            
            

        

    







grille = remplir_grille() # Remplir la grille de 6 lignes vides
print("test ", canevas_grille.find_all())
dessiner_grille(grille)




fenetre.bind("<Button-1>", clic) # Permettre à l'utilisateur de changer la couleur des cases via le clic gauche
fenetre.bind("<Button-2>", clic) # L'utilisateur peut changer la couleur des cases via le clic molette
fenetre.bind("<Button-3>", clic) # Permettre à l'utilisateur de changer la couleur des cases via le clic droit


#jeu()

# threading.Thread(target=jeu).start()

fenetre.bind("<Escape>", demander_quitter)  # L'utilisateur peut quitter le jeu en appuyant sur échap
fenetre.protocol("WM_DELETE_WINDOW", demander_quitter) # Si l'utilisateur clique sur le bouton en forme de X du gestionnaire de fenêtres, demander à l'utilisateur s'il souhaite quitter le jeu
fenetre.mainloop() # Démarrer la boucle principale de la fenêtre


 








