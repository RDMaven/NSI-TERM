"""
Entrée
Sur la première ligne, un acronyme, uniquement constitué de lettres majuscules.

Sur la seconde ligne, un entier nbLivres, le nombre de titres de livres.

Sur les nbLivres lignes suivantes les titres de livres, uniquement constitués de lettres ou d’espaces, sans accents.

Les mots de chaque titre sont toujours séparés par un seul espace.

Sortie
Vous devez afficher chaque titre de livre qui correspond à l’acronyme, en mettant toutes ses lettres en minuscules sauf la première lettre de chaque mot, qui doit être en majuscule.

"""


def livresPossibles(acronyme:str, titres:list[str]):
    for t in titres:
        mots = t.split()
        premieresLettres = [m[0].upper() for m in mots]
        if "".join(premieresLettres) == acronyme:
            print(" ".join([m[0].upper() + m[1:].lower() for m in mots]))

if __name__ == "__main__":
    acronyme = str(input())
    nbLivres = int(input())
    titres = [str(input()) for _ in range(nbLivres)]
    livresPossibles(acronyme, titres)