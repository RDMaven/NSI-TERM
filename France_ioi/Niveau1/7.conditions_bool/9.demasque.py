def demasquage(nbPersonnes:int):
    sortie = ["Impossible", "Peu probable", "Peu probable", "Probable", "Probable", "Très probable"]
    for _ in range(nbPersonnes):
        c = 0
        #taille
        if int(input()) in range(178, 182+1):
            c += 1
        #age    
        if int(input()) >= 34 :
            c += 1
        # poids
        if int(input()) < 70:
            c += 1
        #cheval
        if int(input()) == 0:
            c += 1
        #cheveux
        if int(input()) == 1:
            c += 1
        
        print(sortie[c])

if __name__ == "__main__":
    nbPersonnes = int(input())
    demasquage(nbPersonnes)

