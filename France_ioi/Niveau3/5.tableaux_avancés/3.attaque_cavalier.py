
def atk_knight(board:list[list[str]]):
    
    knights = []
    for row in range(8):
        for col in range(8):
            if board[row][col] == 'C':
                knights.append((row, col))
    #print(knights)

    for k in knights:
        x = k[0]
        y = k[1]
        squares = [
            (x+2, y+1), (x+2, y-1),
            (x-2, y+1), (x-2, y-1),
            (x+1, y+2), (x-1, y+2),
            (x+1, y-2), (x-1, y-2)
        ]
        for sq in squares.copy():
            if (sq[0] not in range(8)) or (sq[1] not in range(8)):
                squares.remove(sq)
        #print(squares)
        #print([board[sq[0]][sq[1]] for sq in squares])
        if any([board[sq[0]][sq[1]].islower() for sq in squares]):
            return print("yes")
    
    return print("no")


if __name__ == "__main__":

    board = [list(input()) for _ in range(8)]
    atk_knight(board)