
def make_grid(x:int,y:int):
    from random import randint
    grid = []
    for i in range(x):
        ligne = ''
        for j in range(y):
            a = randint(0,2)
            if a == 0 or a == 2:
                a = 0
            ligne += str(a)
        grid.append(ligne)
    
    return grid

def zone_valide(x:int ,y:int , cote:int, grid:list):
    zone = [grid[i][y:y+cote] for i in range(x, x+cote)]
    if '1' not in ''.join(zone):
        return cote
    else:
        return -1

def trouver_zone(nbLignes, nbColonnes, grid:list):
    Dt = min(nbLignes, nbColonnes)

    #Toutes les dimentions de carrés possible
    cotes_possibles = [e for e in range(Dt,0, -1)]
 
    for taille in cotes_possibles:
        for x in range(nbLignes-taille+1):
            for y in range(nbColonnes-taille+1):
                if zone_valide(x, y, taille, grid) != -1:
                    return taille



if __name__ == "__main__":
    import time
    dimentions = list(map(int, input().split()))
    nbLignes = dimentions[0]
    nbColonnes = dimentions[1]

    #grid = [input().replace(" ", "") for _ in range(nbLignes)]
    grid = make_grid(nbLignes, nbColonnes)

    start = time.time()    
    print(trouver_zone(nbLignes, nbColonnes, grid))
    end = time.time()
    print(end-start)