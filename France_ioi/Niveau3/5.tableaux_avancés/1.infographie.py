
def infographie(nbLignes:int, nbColonnes:int, nbRectangles:int, rectangles:list):
    
    tableau = [['.']*nbColonnes for _ in range(nbLignes)]

    for rect in rectangles:
        x1, y1 = int(rect[0]), int(rect[1])
        x2, y2 = int(rect[2]), int(rect[3])
        char = rect[4]

        for l in range(x1,x2+1):
            for c in range(y1,y2+1):
                tableau[l][c] = char

    for l in tableau:
        print(*l, sep='')


if __name__ == "__main__":
    nbDim = list(map(int, input().split()))
    nbLignes = nbDim[0]
    nbColonnes = nbDim[1]
    nbRectangles = int(input())

    rectangles = [input().split() for _ in range(nbRectangles)]

    infographie(nbLignes, nbColonnes, nbRectangles, rectangles)