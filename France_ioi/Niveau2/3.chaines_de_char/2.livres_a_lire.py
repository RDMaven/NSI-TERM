
def a_lire(livres:list):
    maxi = 0
    for livre in livres:
        if len(livre) > maxi:
            maxi = len(livre)
            print(livre)

if __name__ == "__main__":
    nbLivres = int(input())
    livres = [str(input()) for _ in range(nbLivres)]
    a_lire(livres)

