
def nombre_livres(somme_argent, prix_livre):
   print(somme_argent//prix_livre)

if __name__ == "__main__":
    somme_argent = int(input())
    prix_livre = int(input())
    
    nombre_livres(somme_argent, prix_livre)
