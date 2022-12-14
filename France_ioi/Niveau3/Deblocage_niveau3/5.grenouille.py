
def course(nbGrenouilles:int, tours:list):

    maxi_etapes = [0]*nbGrenouilles
    etape = [0]*nbGrenouilles

    for tour in tours[:-1]:
        etape[tour[0]-1] += tour[1]
        
        valeur_maxi = max(etape)
        indice_maxi = etape.index(valeur_maxi)

        nbMax = 0
        i = 0
        while nbMax <=1 and i < nbGrenouilles:
            if etape[i] == valeur_maxi:
                nbMax +=1
            i += 1
            
        if nbMax == 1:
            maxi_etapes[indice_maxi] += 1

    

    print(1+maxi_etapes.index(max(maxi_etapes)))



if __name__ == "__main__":
    nbGrenouilles = int(input())
    nbTours = int(input())
    tours = [tuple(map(int, input().split())) for _ in range(nbTours)]

    course(nbGrenouilles, tours)