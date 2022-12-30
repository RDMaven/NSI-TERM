def alpha(livres:list):
    return print(*sorted(livres), sep='\n')

if __name__ == "__main__":
    nbLivres = int(input())
    livres = [str(input()) for _ in range(nbLivres)]
    alpha(livres)