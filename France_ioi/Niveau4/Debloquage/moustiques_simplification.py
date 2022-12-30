
def make_grid(x:int,y:int):
    from random import randint
    grid = []
    for i in range(x):
        ligne = ''
        for j in range(y):
            a = randint(0,2)
            if a%2 == 0:
                a = 0
            else:
                a = 1
            ligne += str(a)
        grid.append(ligne)
    
    return grid

def pretty_grid_maker(grid, cases_valides=[]):
    pretty_grid = []
    for ligne in range(len(grid)):
        pretty_line = []
        for element in range(len(grid[0])):
            e = grid[ligne][element]
            if e == '0':
                ep =  f"0"

            else:
                ep = e

            if (ligne, element) in cases_valides:
                ep = f"{e}"

            pretty_line.append(ep)
        pretty_grid.append(pretty_line)
    return pretty_grid


def zone_valide(x:int ,y:int , cote:int, grid:list):

    for i in range(x, x+cote):
        if '1' in ''.join(grid[i][y:y+cote]):
            return -1
    return cote


def max_par_ligne(grid):
    maxis = sorted([ligne.count('0') for ligne in grid], reverse=True)
    i = 0
    while maxis[i] > i+1:
        i += 1
    
    if maxis[i] == i+1:
        i +=1

    return i

def trouver_zone(nbLignes, nbColonnes, grid:list):

    #Toutes les dimentions de carrés possible
    cotes_possibles = [e for e in range(max_par_ligne(grid),0, -1)]
 
    for taille in cotes_possibles:
        for x in range(nbLignes-taille+1):
            for y in range(nbColonnes-taille+1):
                if zone_valide(x, y, taille, grid) != -1:
                    return taille


if __name__ == "__main__":
    import time
    dimentions = [350, 350]#list(map(int, input().split()))
    nbLignes = dimentions[0]
    nbColonnes = dimentions[1]

    #grid = [input().replace(" ", "") for _ in range(nbLignes)]
    
    for i in range(10):
        print()    
        grid = make_grid(nbLignes, nbColonnes)
        a = max_par_ligne(grid)
        print(a)

        start = time.time()    
        print(trouver_zone(nbLignes, nbColonnes, grid))
        end = time.time()
        print(end-start)