
def diparue(recherche, personnes):
    
    if recherche in personnes:
        print("Sorti de la ville")
    else:
        print("Encore dans la ville")

if __name__ == "__main__":
    recherche = int(input())
    tailleListe = int(input())

    personnes = [int(input()) for _ in range(tailleListe)]

    diparue(recherche, personnes)
