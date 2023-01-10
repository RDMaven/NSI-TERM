
def erosion(H:int, L:int, dessin:list) -> list:
    dessin_f = [['.']*L]
    autour = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

    for row in range(1, H-1):
        ligne = []
        for col in range(1, L-1):
            
            if dessin[row][col] == '#':      

                possible = True
                i = 0
                
                while i in range(4) and possible:
                    if dessin[row+autour[i][0]][col+autour[i][1]] != '#':
                        possible = False
                        ligne.append('.')
                    i += 1
                
                if possible:
                    ligne.append('#')
            else:
                ligne.append('.')

        dessin_f.append(['.'] + ligne + ['.'])        
    
    dessin_f.append(['.']*L)
    return dessin_f


def main(N:int, H:int, L:int, dessin:list) -> None:
    for _ in range(N):
        dessin = erosion(H, L, dessin)
    
    return print(*["".join(row) for row in dessin], sep='\n')


if __name__ == "__main__":

    N = int(input())
    H, L = map(int, input().split())
    dessin = [list(input()) for _ in range(H)]
    main(N, H, L, dessin)
