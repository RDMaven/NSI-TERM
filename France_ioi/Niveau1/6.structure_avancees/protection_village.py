"""
Le programme doit d'abord lire un entier strictement positif correspondant au nombre de maisons. Ensuite, pour chaque maison, il doit lire la position horizontale (l'abscisse, le "x") et sa position verticale (l'ordonnée, le "y") de cette maison. Toutes les abscisses et ordonnées sont des entiers compris entre zéro et 1 million.

Le programme doit alors afficher le périmètre de la plus petite clôture rectangulaire englobant toutes les maisons. Ce rectangle doit avoir ses côtés parallèles aux axes du repère, comme montré sur l'illustration.
"""

def perimetre(x:list, y:list):
    print(2*(max(x)-min(x))+2*(max(y)-min(y)))

if __name__ == "__main__":
    nbMaisons = int(input())
    x, y = [], []
    for _ in range(nbMaisons):
        x.append(int(input()))
        y.append(int(input()))

    perimetre(x, y)