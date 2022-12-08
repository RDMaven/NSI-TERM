
def plus_petit_prix(nbMarchands:int, prixGalettes:list):
    print(nbMarchands - prixGalettes[::-1].index(min(prixGalettes)))


if __name__ == "__main__":
    nbMarchands = int(input())
    prixGalettes = [int(input()) for _ in range(nbMarchands)]
    plus_petit_prix(nbMarchands, prixGalettes)

