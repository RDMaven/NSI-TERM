
def gagnant(nbLignes, nbColonnes, grid):
    
    pos = []
    for row in range(nbLignes):
        for col in range(N):
            if grid[row][col] == 0:
                pos.append((row, col))
    
    for p in range(len(pos)):
            
            x, y = pos[p]
            line_valid = True
            col_valid = True
            diag_gauche = True
            diag_droite = True

            i = 1
            while i in range(1,5) and (line_valid or col_valid or diag_gauche or diag_droite): # vérifier si les 4 suivant sur la ligne sont au meme joueur
                # en ligne
                if (x, y+i) not in pos:
                    line_valid = False

                # en colonne
                if (x+i, y) not in pos:
                    col_valid = False

                # en diagonale
                if (x+i, y-i) not in pos:
                    diag_gauche = False
                if (x+i, y+i) not in pos:
                    diag_droite = False
                
                i += 1
        
            if line_valid or col_valid or diag_gauche or diag_droite :
                return player
                #return print("Ligne valid {0:}. Joueur {1:}".format((x,y), player))

    return 0


def trouver_zone(nbLignes, nbColonnes, grid):
    
    gagnant(nbLignes, nbColonnes, grid)
    

if __name__ == "__main__":

    nbLignes, nbColonnes = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(nbLignes)]
    #grid = make_grid(nbLignes, nbColonnes)

    trouver_zone(nbLignes, nbColonnes, grid)
    