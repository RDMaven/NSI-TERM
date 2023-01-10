
def gagnant(N:int, board:list, player:int):
    
    pos = []
    for row in range(N):
        for col in range(N):
            if board[row][col] == player:
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

def gomoku(N:int, board:list[list[int]]):
    
    for i in [1,2]:
        winner = gagnant(N, board, i)
        if winner != 0:
            return print(winner)  

    return print(0)



if __name__ == "__main__":

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    gomoku(N, board)



"""
6
0 0 2 0 1 0
0 1 2 2 2 1
0 0 2 0 1 0
0 0 2 1 0 0
0 0 1 0 0 0
0 1 0 0 0 0

6
0 0 2 0 1 0
0 1 2 2 2 1
0 0 2 0 1 0
0 0 2 0 0 0
1 1 1 1 1 0
0 1 0 0 0 0

"""