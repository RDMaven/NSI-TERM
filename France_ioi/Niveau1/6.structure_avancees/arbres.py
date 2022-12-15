"""Il existe 4 types d'arbres :

le "Tinuviel" fait moins de 5 mètres de haut et ses feuilles sont composées de plus de 8 folioles
le "Calaelen" fait plus de 10 mètres de haut et ses feuilles sont composées de plus 10 folioles
le "Falarion" fait moins de 8 mètres de haut et ses feuilles sont composées de moins de 5 folioles
le "Dorthonion" fait plus de 12 mètres de haut et ses feuilles sont composées de moins de 7 folioles


Tinuviel   : h <= 5               f >= 8
Calaelen   : h >= 10              f >= 10
Falarion   : h <= 8               f <= 5 
Dorthonion : h >= 12              f <= 7

h:
<= 8 
    <= 5 : Tin
    Fala

>= 10 : 
    >= 12 : Dorth
    Cale

f:
<= 7 
    <= 5 : Fala
    Dorth

>= 8
    >= 10 : Cale
    Tinu


"""

def arbre(hauteur, feuilles):

    h = []
    if hauteur <= 8:
        if hauteur <= 5:
            h.append("Tinuviel")
        h.append("Falarion")

    elif hauteur >= 10:
        if hauteur >= 12:
            h.append("Dorthonion")
        h.append("Calaelen")

    f = []
    if feuilles <= 7:
        if feuilles <= 5:
            f.append("Falarion")
        f.append("Dorthonion")

    elif feuilles >= 8:
        if feuilles >= 10:
            f.append("Calaelen")
        f.append("Tinuviel")

    #print(f, h)
    print(*set(f).intersection(h))

if __name__ == "__main__":
    hauteur = int(input())
    nbFeuilles = int(input())

    arbre(hauteur, nbFeuilles)