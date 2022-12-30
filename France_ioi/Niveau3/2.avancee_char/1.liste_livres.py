"""
La première ligne contient un entier nbLivres, le nombre de livres.

Les nbLivres lignes suivantes contiennent chacune un titre de livre.

Les livres sont classés du moins intéressant au plus intéressant.
"""


def inverser(livres:list):
    return print(*livres[::-1], sep='\n')


if __name__ == "__main__":
    nbLivres = int(input())
    livres = [str(input()) for _ in range(nbLivres)]
    inverser(livres)
