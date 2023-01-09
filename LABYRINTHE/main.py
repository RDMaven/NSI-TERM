import matplotlib.pyplot as plt
from random import choice

# Constante et variables du programme
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Directions possibles en x et y
larg = 5
haut = 5
# listes des points pour la construction du labyrinthe
coordx = []
coordy = []

def traiter_case(i, j):
    # Vérifie si la case est possible
    if 0 <= i < larg and 0 <= j < haut:
        return T[j][i] # nouvelle case 'False' ou case déjà visitée 'True'
    else:
        return True # bord du labyrinthe

def choisir_chemin(case):
    # Sélection des cases voisines
    i,j = case # case de départ
    if not traiter_case(i, j):
        T[j][i] = True
    L = []
    for a,b in DIR: # pour chaque case voisine
        if not traiter_case(i+a, j+b):
            L.append((i+a, j+b))
    return L

def construire_laby(case):
    # Obtenir recursivement les coordonnées de chaque point du labyrinthe
    L = choisir_chemin(case) # on récupère les voisins du point de départ
    if L == []:
        return
    else:
        sc = choice(L) # choix du point d'arrivée parmi les voisins
        coordx.append((case[0], sc[0])) # ajout des points de départ et d'arrivée dans les listes
        coordy.append((case[1], sc[1]))
        construire_laby(sc)
        construire_laby(case)

def tracer():
    # effectue le tracé du labyrinthe
    for i in range(len(coordx)):
        ax.plot([coordx[i][0],coordx[i][1]], [coordy[i][0],coordy[i][1]], 'w', lw=35)

# Programme principal
assert larg*haut <= 14400, "largeur X hauteur doit être < 7200" # limitation mémoire
T = [[False for j in range(larg)] for i in range(haut)] # cases à traiter
fig1 = plt.figure(figsize=(larg, haut))
ax = fig1.add_subplot(1,1,1)
ax.set_facecolor('black')
ax.set_xlim(-0.25, larg-1+0.25)
ax.set_ylim(-0.25, haut-1+0.25)
ax.grid(True, linestyle="-", color="red", lw="2")
ax.set_xticks([x for x in range(larg)])
ax.set_yticks([y for y in range(haut)])
debut = (0, 0) # départ du labyrinthe
construire_laby(debut)
tracer()

print(coordx)
print(coordy)


def construire_matrice(matrice, coordx, coordy):
    # Crée la matrice du labyrinthe à partir du tracé
    #coords = []
    matrice[0][0] = 1
    for c in range(len(coordx)):
        [x1, x2], [y1, y2] = coordx[c], coordy[c]
        matrice[y2*2][x2*2] = 1
        matrice[(y1*2+y2*2)//2][(x1*2+x2*2)//2] = 1    
    return matrice
        
matrice = [[0 for j in range(2*larg-1)] for i in range(2*haut-1)]
print(matrice)
matrice = construire_matrice(matrice, coordx, coordy)
print("Matrice de construction :")
for j in range(len(matrice)):
    for i in range(len(matrice[j])):
        if matrice[j][i] == 1:
            print('\033[91;1m',"1", end="   ") # code ANSI rouge, gras
        else:
            print('\033[0m',"0", end="   ") # RESET Color, Style
    print("\n")
print('\033[0m',"", end="")
plt.show()


def afficher(mat):
    
    fig2 = plt.figure()
    ax = fig2.add_subplot(1,1,1)
    ax.imshow(mat, cmap='gray', vmin=0, vmax=1)
    plt.show()
    plt.close(fig2)

matrice[0][0] = 0.8 # point de début
matrice[2*haut-2][2*larg-2] = 0.8 # point de fin
afficher(matrice)