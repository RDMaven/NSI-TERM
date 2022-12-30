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

def pretty_grid_maker(grid, cases_valides=[]):
    pretty_grid = []
    for ligne in range(len(grid)):
        pretty_line = []
        for element in range(len(grid[0])):
            e = grid[ligne][element]
            if e == '0':
                ep =  f"\033[32;1m0\033[0m"

            else:
                ep = e

            if (ligne, element) in cases_valides:
                ep = f"\033[31;1m{e}\033[0m"

            pretty_line.append(ep)
        pretty_grid.append(pretty_line)
    return pretty_grid


def cases_possibles(nbLignes:int, nbColonnes:int):
    """Obtenir toutes les premières cases des carrés possibles.

    Args:
        nbLignes (int): Le nombre de lignes de la zone donnée.
        nbColonnes (int): Le nombre de colonnes de la zone donnée.
    """
    Dt = min(nbLignes, nbColonnes)

    #Toutes les dimentions de carrés possible
    cotes_possibles = [e for e in range(Dt, 1, -1)]
    premieres_cases = {}
    for i in cotes_possibles:
        premieres_cases[i] = []
        for x in range(nbLignes-i+1):
            for y in range(nbColonnes-i+1):
                premieres_cases[i].append((x,y))
    
    #print(premieres_cases)
    return premieres_cases
                

def carre_valide(zone:list, cote:int):
    if '1' not in ''.join(zone):
        return cote
    else:
        return -1

def sub_zone(x:int,y:int, cote:int, grid:list):
    sub = []
    for i in range(x, cote+x):
        sub.append(grid[i][y:y+cote])
    return sub

def zone_valide(x:int ,y:int , cote:int, grid:list):
    zone = sub_zone(x,y,cote,grid)
    return carre_valide(zone, cote)

def trouver_zone(premieres_cases, grid):

    for taille, cases in premieres_cases.items():
        for c in cases:
            if zone_valide(c[0], c[1], taille, grid) != -1:
                #return print(taille)
                print(f"Un carré de coté {taille}, de première case {c} est libre.")
                cases_valides = [(x,y) for y in range(c[1], c[1]+taille) for x in range(c[0], c[0]+taille)]
                return pretty_grid_maker(grid, cases_valides)

if __name__ == "__main__":
    
    dimentions = list(map(int, input().split()))
    nbLignes = dimentions[0]
    nbColonnes = dimentions[1]

    #grid = [input().replace(" ", "") for _ in range(nbLignes)]
    grid = make_grid(nbLignes, nbColonnes)

    #print(grid)

    pretty_grid = pretty_grid_maker(grid)
    for i in pretty_grid:
        print(*i, sep='  ')


    premieres_cases = cases_possibles(nbLignes, nbColonnes)
    
    pretty_fin = trouver_zone(premieres_cases, grid)
    
    for i in pretty_fin:
        print(*i, sep="  ")