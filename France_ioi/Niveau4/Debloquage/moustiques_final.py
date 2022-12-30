
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

def trouver_zone(premieres_cases:dict, grid:list):
    for taille, cases in premieres_cases.items():
        for c in cases:
            if zone_valide(c[0], c[1], taille, grid) != -1:
                return print(taille)

if __name__ == "__main__":
    
    dimentions = list(map(int, input().split()))
    nbLignes = dimentions[0]
    nbColonnes = dimentions[1]

    grid = [input().replace(" ", "") for _ in range(nbLignes)]

    premieres_cases = cases_possibles(nbLignes, nbColonnes)
    
    trouver_zone(premieres_cases, grid)
    