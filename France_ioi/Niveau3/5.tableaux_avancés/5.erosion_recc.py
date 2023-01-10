
def pixel_check(x:int, y:int, N:int, dessin:list):

    if N == 1:
        return (dessin[x-1][y] == '#') and (dessin[x+1][y] == '#') and (dessin[x][y-1] == '#') and (dessin[x][y+1] == '#')
    
    else:
        return pixel_check(x-1, y, N-1, dessin) and pixel_check(x+1, y, N-1, dessin) and pixel_check(x, y-1, N-1, dessin) and pixel_check(x, y+1, N-1, dessin)
    

def erosion(H:int, L:int, dessin:list, N:int) -> list:
    dessin_f = [['.']*L for _ in range(H)]
        
    for row in range(N, H-N):
        for col in range(N, L-N):
            if dessin[row][col] == '#' and pixel_check(row, col, N, dessin):
                dessin_f[row][col] = '#'
    
    return dessin_f


def main(N:int, H:int, L:int, dessin:list) -> None:

    return print(*["".join(row) for row in erosion(H, L, dessin, N)], sep='\n')


if __name__ == "__main__":

    N = int(input())
    H, L = map(int, input().split())
    dessin = [list(input()) for _ in range(H)]
    main(N, H, L, dessin)
