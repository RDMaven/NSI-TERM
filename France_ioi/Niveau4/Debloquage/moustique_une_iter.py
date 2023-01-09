def max_square(table, nbLignes, nbColonnes):
    max_side = 0
    squares_first = []
    squares_all = {}
    for i in range(nbLignes):

        for j in range(nbColonnes):
            if table[i][j] == 0:

                squares_first.append((i,j))

                


    return max_side

if __name__ == "__main__":

    nbLignes, nbColonnes = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(nbLignes)]
    print(max_square(table, nbLignes, nbColonnes))