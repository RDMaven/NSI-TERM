
def note_karvas(karvas:dict, nb_karvas: int):
    for i in range(nb_karvas):
        print(karvas[i][0] + karvas[i][2]*karvas[i][3])
    


if __name__ == "__main__":
    nb_karvas = int(input())
    karvas = {}
    for i in range(nb_karvas):
        karvas[i] = [int(input()) for _ in range(4)]
        
    note_karvas(karvas, nb_karvas)

"""
Votre programme doit d'abord lire le nombre de Karvas en compétition. Ensuite, pour chaque Karva, il doit :

lire 4 entiers : son poids, son âge, la longueur de ses cornes et la hauteur au garrot ;
afficher sa note, sachant qu'elle s'obtient en multipliant la longueur des cornes par la hauteur au garrot, valeur à laquelle on ajoute le poids.

2
100
5
25
90
300
10
15
120

"""