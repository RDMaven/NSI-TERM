
def gomoku(N:int, board:list[list[int]]):
    
    # trouver en colonne
    colonne1, colonne2 = {}, {} # {position : count}
    
    # trouver en diagonale
    diagonale1g, diagonale1d, diagonale2g, diagonale2d = {}, {}, {}, {} # {position : count}
    

    for row in range(N):
        # trouver en ligne
        c1, c2 = 0, 0

        for col in range(N):

            case = board[row][col]

            # trouver en ligne
            if   case == 1: c1, c2 = c1+1, 0
            elif case == 2: c1, c2 = 0, c2+1
            else: c1, c2 = 0, 0
            if c1 >= 5: return print(1)
            if c2 >= 5: return print(2)

    for row in range(N-1):
        if row != N-1:

            for col in range(N):
                case = board[row][col]
                # trouver en colonne
                if case == 1:
                    colonne1[col] = 1 if col not in colonne1 else colonne1[col] + 1
                    diagonale1g[col] = 1 if col not in diagonale1g else diagonale1g[col] + 1
                    diagonale1d[col] = 1 if col not in diagonale1d else diagonale1d[col] + 1
                if case == 2:
                    colonne2[col] = 1 if col not in colonne2 else colonne2[col] + 1
                    diagonale2g[col] = 1 if col not in diagonale2g else diagonale2g[col] + 1
                    diagonale2d[col] = 1 if col not in diagonale2d else diagonale2d[col] + 1

            # trouver en colonne
        
            for pos in colonne1:
                if board[row+1][pos] != 1:
                    colonne1[pos] = 0
                if colonne1[pos] >= 5:
                    return print(1)
            
            for pos in colonne2:
                if board[row+1][pos] != 2:
                    colonne2[pos] = 0
                if colonne2[pos] >= 5:
                    return print(2)

            # diagonale
            """for pos in diagonale1g:
                if board[row+1][pos-1] != 1:
                    diagonale1g[pos] = 0
                else:
                    diagonale1g[pos-1] = diagonale1g[pos]
                    diagonale1g[pos] = 0

                if diagonale1g[pos] >= 5:
                    return print(1)
            
            for pos in diagonale1d:
                if board[row+1][pos+1] != 1:
                    diagonale1d[pos] = 0
                else:
                    diagonale1d[pos-1] = diagonale1d[pos]
                    diagonale1d[pos] = 0

                if diagonale1d[pos] >= 5:
                    return print(1)

            for pos in diagonale2g:
                if board[row+1][pos-1] != 1:
                    diagonale2g[pos] = 0
                else:
                    diagonale2g[pos-1] = diagonale2g[pos]
                    diagonale2g[pos] = 0

                if diagonale2g[pos] >= 5:
                    return print(1)
            
            for pos in diagonale2d:
                if board[row+1][pos+1] != 1:
                    diagonale2d[pos] = 0
                else:
                    diagonale2d[pos-1] = diagonale2d[pos]
                    diagonale2d[pos] = 0

                if diagonale2d[pos] >= 5:
                    return print(1)"""
    

    return print(0)


if __name__ == "__main__":

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    gomoku(N, board)