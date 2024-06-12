# Programme pour créer une canevas tkinter
from tkinter import * # Importation de tkinter
import random 

formes = []


# Création de la fenêtre avec son titre
maFenetre = Tk()
maFenetre.title("Interface graphique avec Tkinter")

# Définiton de la taille de la fenêtre : 600x600 positionnée en x=150 et y=100
maFenetre.geometry("600x600+150+150")


# Création de 2 zones
cadre1 = Frame(maFenetre)
cadre2 = Frame(maFenetre)


# Création d'un canevas de couleur verte et de dimension 400x500
canevas = Canvas(maFenetre, width=400, height=500, bg="white")

# Création d'une étiquette texte - texte de couleur bleu (navy) et fond jaune
etiquette = Label(maFenetre, text="Exemple de widget Label", fg="navy", bg="white")

# Création d'un bouton Quitter pour fermer la fenêtre
bouton_Quitter = Button(maFenetre, text="Quitter", command=maFenetre.destroy)



# Création d'un rectangle dans le canevas de la position (x=50,y=50) à la position (100,100) rempli en jaune
rectangle = canevas.create_rectangle(50,50,100,100, fill="yellow")
formes.append(rectangle)

# Création d'un carré dans le canevas de la position (x=150,y=50) à la position (250,100) rempli en vert
carre = canevas.create_rectangle(150,50,250,100, fill="green")
formes.append(carre)

# Création d'une ellipse ou d'un cercle de rayon 25 en position x=325,y=75
# Les coordonnées de ce cercle sont donc x1=325-25 y1=75-25 - x2=325+25, y2=75+25
cercle = canevas.create_oval(300,50,350,100, fill="orange")
formes.append(cercle)


# -----------

cadre1.pack(side=LEFT,padx=5,pady=5)
cadre2.pack(side=RIGHT,padx=5,pady=5)

# Ajout de l'étiquette à la fenêtre
etiquette.pack(side=TOP, padx=5, pady=5)


def supprimerForme(event):
    #positionForme = random.randrange(len(formes))
    #forme = formes[positionForme]
    x = event.x
    y =event.y
    closest = canevas.find_closest(x, y)
    forme = closest[0]
    canevas.delete(forme)
# Ajout du canevas à la fenêtre
canevas.pack(padx=5, pady=5)
canevas.bind("<Button-1>", supprimerForme)


# Ajout du bouton dans la fenetre, en bas (BOTTOM), avec une marge de 5 de # chaque coté
bouton_Quitter.pack(side=BOTTOM, padx=5, pady=5)





# Exécution de la boucle principale
maFenetre.mainloop()