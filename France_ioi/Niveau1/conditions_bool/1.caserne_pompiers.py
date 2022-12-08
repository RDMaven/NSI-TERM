
def intersect(nbMarchands:int, prixGalettes:list):
    print(nbMarchands - prixGalettes[::-1].index(min(prixGalettes)))


if __name__ == "__main__":
    paires_de_zones = int(input())
    zones = {}
    for i in range(paires_de_zones):
        zones[i] = {int(input()) for _ in range(8)}
        

    print(zones)