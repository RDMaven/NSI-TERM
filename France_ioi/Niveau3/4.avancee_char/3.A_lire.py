def a_lire(livres:list):
    alpha = sorted(livres)
    valide = []
    maxi = -1
    for i in livres:
        pos = alpha.index(i)
        if pos > maxi:
            maxi = pos
            valide.append(i)

    print(*valide, sep='\n')

if __name__ == "__main__":
    nbLivres = int(input())
    livres = [str(input()) for _ in range(nbLivres)]
    a_lire(livres)



"""
ANNA KARENINE
JACQUES LE FATALISTE ET SON MAITRE
LA PESTE
SUR LA ROUTE
"""