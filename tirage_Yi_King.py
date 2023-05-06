# Cette fonction renvoit et affiche l'hexagramme du Yi King correspondant à un paquet donné, dont il faut donner le contenu dans le terminal lorsque demandé.


def schema_yi_jing():

    yin = "--   --"
    yang = "-------"
    yin_mutant = "-- x --"
    yang_mutant = "---o---"

    rouge = int(input("nombre de M&M's rouge dans le paquet : "))
    orange = int(input("nombre de M&M's orange dans le paquet : "))
    jaune = int(input("nombre de M&M's jaune dans le paquet : "))
    vert = int(input("nombre de M&M's vert dans le paquet : "))
    bleu = int(input("nombre de M&M's bleu dans le paquet : "))
    marron = int(input("nombre de M&M's marron dans le paquet : "))
    ensemble = [rouge, orange, jaune, vert, bleu, marron]
    total = 0
    for nb in ensemble:
        total += nb
    dessin = []

    for nb_couleur in ensemble:
        sous_tot = total - nb_couleur
        if (nb_couleur % 2) == 0:  # Yin
            if sous_tot % 8 == 0:  # Yin mutant
                dessin.append(yin_mutant)
            else:  # Yin jeune
                dessin.append(yin)
        else:  # Yang
            if (sous_tot % 8) in [1, 2, 3]:  # Yang mutant
                dessin.append(yang_mutant)
            else:  # Yang jeune
                dessin.append(yang)

    for i in range(len(dessin)-1, -1, -1):
        print(dessin[i])
    return(dessin)


schema_yi_jing()
