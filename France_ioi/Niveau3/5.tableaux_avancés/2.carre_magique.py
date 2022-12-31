
def carre_magique(N:int, carre:list, nbs:list):
    
    if set(nbs) != {i for i in range(1, N**2+1)}:
        return print('no')

    somme = sum(carre[0])
    
    somme_diag_g = 0
    somme_diag_d = 0

    for i in range(N):

        # somme lignes
        if sum(carre[i]) != somme:
            return print('no')
        
        # somme colonnes
        if sum([l[i] for l in carre]) != somme:
            return print('no')
     
        # somme diagonales
        somme_diag_g  += carre[i][i]
        somme_diag_d  += carre[N-1-i][i]
    
    if somme_diag_d != somme or somme_diag_g != somme:
        return print("no")

    return print("yes")


if __name__ == "__main__":
    N = int(input())
    carre = [list(map(int, input().split())) for _ in range(N)]
    nbs = sum(carre, [])
    carre_magique(N, carre, nbs)