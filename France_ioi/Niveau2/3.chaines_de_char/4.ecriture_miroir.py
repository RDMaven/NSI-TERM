
def inverser(texte):
    for p in texte:
        print(p[::-1])

if __name__ == "__main__":
    nbLignes = int(input())
    texte = [str(input()) for _ in range(nbLignes)]
    inverser(texte)

