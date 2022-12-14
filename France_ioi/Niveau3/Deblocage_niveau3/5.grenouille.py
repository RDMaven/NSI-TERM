
def course(nbGrenouilles:int, nbTours:int, tours:list):
    print()

    #print([g for g in range(1, nbGrenouilles+1)])
    
    jeu = [[0]*nbGrenouilles]

    for i in range(nbTours-1):
        ele = jeu[-1].copy()
        ele[tours[i][0]-1] += tours[i][1]
        jeu.append(ele)
    #print(*jeu, sep='\n')
    
    maxi_etapes = {i:0 for i in range(1, nbGrenouilles+1)}
    print(maxi_etapes)
    for etape in jeu:
        valeur_maxi = 0
        indice_maxi = 1
        unique= False
        for gre in range(len(etape)):
            if etape[gre] > valeur_maxi and unique==False:
                unique=True
                valeur_maxi = etape[gre]
                indice_maxi = gre+1
                maxi_etapes[indice_maxi+1] += 1
                print(f"{etape}, val={valeur_maxi}, i={indice_maxi}")
    print(maxi_etapes)


if __name__ == "__main__":
    nbGrenouilles = int(input())
    nbTours = int(input())
    tours = [tuple(map(int, input().split())) for _ in range(nbTours)]

    course(nbGrenouilles, nbTours, tours)