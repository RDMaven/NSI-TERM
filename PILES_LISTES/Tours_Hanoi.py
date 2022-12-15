    
def creer_pile():
    return []

def est_vide(pile:list):
    return len(pile)==0

def empiler(pile:list,elt):
    pile.append(elt)

def empilerPl(pile:list, elt:list):
    pile.extend(elt)

def depiler(pile:list):
    assert not est_vide(pile), "La pile est vide"
    return pile.pop()

def sommet(pile:list):
    assert not est_vide(pile), "La pile est vide"
    return pile[-1]

def etatPile(pile:list):
    return pile

def deplacer(pileInit, pileDest):
    assert not est_vide(pileInit), "La pile est vide"
    if est_vide(pileDest) or  sommet(pileInit) < sommet(pileDest):
        empiler(pileDest, sommet(pileInit))
        depiler(pileInit)

"""
p0 = creer_pile()
p1 = creer_pile()
p2 = creer_pile()

empilerPl(p0, [4,3,2,1])

deplacer(p0, p2)
deplacer(p0, p1)
deplacer(p2, p1)
"""


def etatTours(px:list): # prends p0, p2, p1 comme entrée.
    return "{0:<12} {1:<12} {2:<12}".format(str(etatPile(px[0])), str(etatPile(px[1])), str(etatPile(px[2])))

def resoudre(n:int, origine:list, cible:list, interm:list, ordre:list):
    """Déplacer n disques de l'origine vers la cible.

    Args:
        n (int): Nombre de disques de la pile de départ à déplacer.
        origine (list): La pile de départ.
        cible (list): La pile d'arrivée.
        interm (list): Une pile intermédiaire.
    """
    if n != 0:
        #deplacer les n-1 disques de l'origine vers l'intermédiaire
        resoudre(n-1, origine, interm, cible, ordre=ordre)
        #déplacer le dernier disque de l'origine vers la cible
        deplacer(origine, cible)
        print(etatTours(ordre))
        #déplacer les n-1 disques de l'intermédiaire vers la cible
        resoudre(n-1, interm, cible, origine, ordre=ordre)


def toursHanoi(disques):
    p0 = creer_pile()
    p1 = creer_pile()
    p2 = creer_pile()

    empilerPl(p0, [i for i in range(disques,0,-1)])
    eI = etatTours([p0, p1, p2])
    print("{0:<12} {1:<12} {2:<12}".format("p0","p1","p2"))
    print(f"\033[32;1mEtat initial du jeu : \n{etatTours([p0, p1, p2])}\033[37;0m")
    resoudre(disques, p0, p2, p1, ordre=[p0,p1,p2])



if __name__ == "__main__":
    toursHanoi(4)

    """print("\033[32;1m", "zjrksmdfqj")
    print("\033[31;1m", "zjrksmdfqj")
    print("\033[37;0m", "zjrksmdfqj")"""