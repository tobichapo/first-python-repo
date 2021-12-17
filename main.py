import sys

def lire_longueur_largeur():
    longueur = float(input("Quelle est la longueur du rectangle? (en metre) "))
    largeur = float(input("Quelle est la largeur du rectangle? (en metre) "))
    return (longueur, largeur)

def lire_cote():
    cote = float(input("Quel est le côté du carré? (en metre) "))
    return cote

def lire_base_hauteur():
    base = float(input("Quelle est la base du parallélogramme? (en metre) "))
    hauteur = float(input("Quelle est la hauteur du parallélogramme? (en metre) "))
    return (base, hauteur)

def lire_type():
    type_quadrilatere = input("Quel est le type de quadrilatère?\n carré (c), rectangle (r), losange (l), parallélogramme (p): ")
    return type_quadrilatere[0]

def surface_rectangle(longueur, largeur):
    surface = longueur*largeur 
    return surface

if __name__ == '__main__':
    print("Ce programme calcule la surface d'un quadrilatère régulier")
    type_quadrilatere = lire_type()
    if type_quadrilatere == 'r': # rectangle
        longueur, largeur = lire_longueur_largeur()
        surface = surface_rectangle(longueur, largeur)
    elif type_quadrilatere == 'c': # carre
        cote    = lire_cote()
        surface = surface_rectangle(cote, cote)
    elif type_quadrilatere == 'l' or type_quadrilatere == 'p': # losange ou parallélogramme
        base, hauteur = lire_base_hauteur()
        surface = surface_rectangle(base, hauteur)
    else:
        print(f"Erreur: '{type_quadrilatere}' ne correspond à aucun quadrilatère connu!")
        sys.exit()

    print(f"La surface du quadrilatère est {surface} m²")
