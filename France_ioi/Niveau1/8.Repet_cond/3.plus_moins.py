"""
Votre programme doit d'abord lire un entier, le nombre que l'enfant devra trouver. Ensuite, il devra lire les propositions du joueur, et afficher à chaque fois le texte « c'est plus » (l'enfant a proposé un nombre trop petit) ou « c'est moins » (l'enfant a proposé un nombre trop grand) selon les cas, et recommencer tant que l'enfant n'a pas trouvé le bon nombre.

À la fin, il faudra afficher le texte « Nombre d'essais nécessaires : » puis, à la ligne en dessous, le nombre d'essais qui ont été nécessaires.

On vous garantit que l'enfant finira par trouver la bonne valeur !
"""

def cherche(nbSecret):
    tentatives = 0
    while True:
        proposition = int(input())
        if proposition == nbSecret:
            return "Nombre d'essais nécessaires :\n{:}".format(tentatives)
        elif proposition < nbSecret:
            print("c'est plus")
        else:
            print("c'est moins")
        tentatives += 1


if __name__ == "__main__":
    nbSecret = int(input())
    print(cherche(nbSecret))