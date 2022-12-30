"""
Entrée
La première ligne contient l’entier nbMots.
Les nbMots lignes suivantes contiennent chacune deux mots séparés par un espace : un mot dans la première langue et un mot dans la seconde.
Les mots ne contiennent pas d’espaces et sont constitués uniquement de lettres minuscules.
Les couples de mots sont triés selon l’ordre alphabétique des mots de la première langue.

Sortie
Vous devez afficher l’ensemble des couples de mots inversés (d’abord le mot de la seconde langue, puis le mot de la première) triés selon l’ordre alphabétique des mots de la seconde langue.

"""


if __name__ == "__main__":
    nbMots = int(input())
    
    dico = {}
    for _ in range(nbMots):
        couple = list(map(str, input().split()))
        dico[couple[1]] = couple[0]

    for i in sorted(dico.items()):
        print(*i)