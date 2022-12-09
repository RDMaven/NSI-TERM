
def impaires(nbLignes:int, texte:list):
    for i in range(nbLignes):
        if i%2 == 0:
            print(texte[i])

if __name__ == "__main__":
    nbLignes = int(input())
    texte = [str(input()) for _ in range(nbLignes)]
    impaires(nbLignes, texte)

