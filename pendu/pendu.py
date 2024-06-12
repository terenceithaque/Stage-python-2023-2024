# Jeu du pendu en Python
import random
import choisir_mot

liste_lettres_trouvees = []  # Liste des lettres trouvées
n_lettres_ajoutees = 0  # Variable pour compter le nombre de lettres trouvées
mot_a_trouver = None  # Mot à trouver
lettres_essayees = []  # Liste des lettres essayées


def ajouter_accents(lettre, mot_a_trouver):
    "Ajouter accents d'un mot"
    lettre_accent = "".join(lettre)
    lettres_avec_accents = {"a" : ["a","â","ä"],
                            "e": ["e", "é", "è", "ê"],
                            "u" : ["u","ù","û" ]
    }
    for l in lettres_avec_accents:
        if lettre in lettres_avec_accents[l]:
            for car in lettres_avec_accents[l]:
                if lettre != car and car in mot_a_trouver:
                    liste_lettres_trouvees.append(car)
                    lettres_essayees.append(car)

            

    



def afficher_mot(mot_a_trouver, lettres_trouvees):
    "Afficher le mot avec les lettres trouvées et des _ pour les lettres manquantes"
    


    for car in mot_a_trouver:  # Pour chaque caractère du mot
        if car not in lettres_trouvees:  # Si le caractère n'a pas été trouvé pas le joueur
            print("_", end=" ")

        else:
            print(car, end=" ")

    print("\n") # On appelle la fonction print() pour faire un saut à la ligne


def is_in_lettres_essayees(lettre):
    "Vérifier si une lettre a déjà été essayée par l'utilisateur"
    if lettre in lettres_essayees:
        return True
    return False


def demander_lettre(erreurs_possibles, mot):
    "Demander à l'utilisateur quelle lettre essayer"
    print(f"Mot à trouver : {mot}")
    lettre = input("Saisissez la lettre à essayer:")
    while is_in_lettres_essayees(lettre) and lettre != "/end": 
        print(
            f"Vous avez déjà utilisé la lettre {lettre} ! Il vous reste {erreurs_possibles} erreurs possibles.")
        lettre = input("Saisissez la lettre à essayer:")

    else:
        while len(lettre) > 1 and lettre != "/end" and lettre != mot:
            print(f"Lettre essayée : {lettre}")
            if lettre != mot:
                print("Ne veuillez saisir qu'une seule lettre !")
                lettre = input("Saisissez la lettre à essayer :")



        lettres_essayees.append(lettre)

    return lettre


def verifier_lettres_a_trouver(mot):
    "Vérifier les lettres à trouver"
    mot = "".join(mot)
    mot_sans_cars_rep = ""  # Mot sans les caractères répétés
    for caractere in mot:
        if caractere in mot_sans_cars_rep:
            continue
        else:
            mot_sans_cars_rep += caractere

    return list(mot_sans_cars_rep)


"""def ajouter_lettre_trouvee(mot, lettre):

    "Ajouter une lettre trouvée par l'utilisateur"
    n_occurence_lettre = 0
    for car in mot:
        if car in liste_lettres_trouvees:


    return liste_lettres_trouvees"""


def afficher_statut(mot, lettres_trouvees, nb_essais):
    "Afficher le statut de la partie"
    print("Statut de la partie :")
    print(f"Lettres trouvées : {lettres_trouvees}")
    print(f"Nombre d'essais restant avant le Game Over : {nb_essais}")

def compter_lettres_trouvees():
    "Compter le nombre de lettres trouvées par le joueur"
    lettres_trouvees = 0
    while lettres_trouvees < len(liste_lettres_trouvees):
        lettres_trouvees += 1
    return lettres_trouvees

def reinitialiser_listes(listes):
    "Réinitialiser une ou plusieurs listes"
    for liste in listes: # Pour chaque liste qu'on doit réinitialiser
        liste.clear()  # Réinitialiser la liste    


def jeu():
    "Jeu"
    reinitialiser_listes([liste_lettres_trouvees, lettres_essayees])
    print("Remarque importante : Il n'y a aucune majuscule dans les mots.")
    erreurs_restantes = 5  # Nombre d'erreurs encore possibles pour le joueur
    mot_a_trouver = choisir_mot.choisir_mot()  # Demander le mot à trouver
    # Si toutes les lettres ont été trouvées
    lettres_a_trouver = verifier_lettres_a_trouver(mot_a_trouver)

    # Faire une liste de toutes les lettres du mot.
    lettres = list(mot_a_trouver)

    #n_lettres_trouvees = 0

    while erreurs_restantes > 0:  # Tant que le joueur n'a pas perdu tous ses essais
        # Demander la lettre à essayer
        n_lettres_trouvees = compter_lettres_trouvees() # Compter le nombre de lettres trouvées par le joueur.
        afficher_mot(mot_a_trouver, liste_lettres_trouvees)
        lettre = demander_lettre(erreurs_restantes, mot_a_trouver)
        lettre = lettre.lower() # Convertir la lettre saisie en minuscules
        ajouter_accents(lettre, mot_a_trouver)
        if lettre == "/end":
            quitter = input("Voulez-vous arrêter la partie ? (o/n)")
            if quitter == "o":
                print("Partie arrêtée")
                return
        str_lettres_essayees = "".join(lettres_essayees)
        print("Caractères essayés :", str_lettres_essayees)
        if lettre in lettres_a_trouver and lettre  not in liste_lettres_trouvees:
            liste_lettres_trouvees.append(lettre)
            n_lettres_trouvees += 1

        if lettre not in lettres_a_trouver and lettre != "/end" and lettre != mot_a_trouver:
            erreurs_restantes -= 1
            print(
                f"La lettre {lettre} n'est pas présente dans le mot à deviner. Il vous reste {erreurs_restantes} erreur(s) possible(s).")

        if n_lettres_trouvees == len(lettres_a_trouver) or lettre == mot_a_trouver:
            print(
                f"Bravo ! Vous avez découvert toutes les lettres du mot : {mot_a_trouver}. ")
            
            rejouer = input("Voulez-vous rejouer ? (o/n)")
            if rejouer != "o":
                print("Fin de partie.")
                break # On quitte la boucle principale plus tôt que prévu car le joueur a gagné.
            else:
                jeu() # Démarrer le jeu à nouveau

        afficher_statut(mot_a_trouver, "".join(
            liste_lettres_trouvees), erreurs_restantes)

    if erreurs_restantes == 0:  # Si le joueur a atteint le nombre maximum d'erreurs possibles
        print(f"Vous avez perdu(e) ! Le mot à deviner était {mot_a_trouver}")
        rejouer = input("Voulez-vous rejouer ? (o/n)")
        if rejouer != "o":
            print("Fin de partie.")
            return # Quitter le jeu
        else:
            jeu()


jeu()  # Lancer la boucle du jeu
