import turtle


def generation(axiome, regles, n):
    mot_final = axiome
    mot = ""

    gen = 0
    while gen < n:
        mot = ""
        for caractere in mot_final:
            if caractere in regles:
                print("Règle du caractère :", regles[caractere])

                mot += regles[caractere]

            else:
                mot += caractere

        mot_final = mot

        gen += 1

    return mot_final


def tracer(mot, angle, pas, position_initiale, orientation_initiale):
    turt = turtle.Pen()  # Créer un objet Tortue
    liste_positions = []
    liste_orient = []
    # turt.setpos(position_initiale[0], position_initiale[1])
    print(turt.pos())
    turt.speed(0)
    turt.up()
    turt.setpos(position_initiale)
    print(turt.pos())

    turt.setheading(orientation_initiale)
    turt.down()
   # input()
    # turt.setheading(23)

    for symbole in mot:
        if symbole == "F":
            turt.forward(pas)

        if symbole == "+":
            turt.right(angle)

        if symbole == "-":
            turt.left(angle)

        if symbole == "[":
            pos = turt.pos()
            orient = turt.heading()
            liste_positions.append(pos)
            liste_orient.append(orient)

        if symbole == "]":
            pos = liste_positions.pop()
            orient = liste_orient.pop()
            turt.up()
            turt.setpos(pos)
            turt.setheading(orient)
            turt.down()
    return turt


# print(generation("F", {"F": "F+F-F-F+F"}, 2))
mot = generation("F", {"F": "FF-[-F+F+F]+[+F-F-F]"}, 4)
print(mot)
t = tracer(mot, 25, 10, (0, -250), 90)
