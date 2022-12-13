def uniques(morceau:str):
        
    lettres = ["aa", "bb", "cc", "dd", "ee", "ff", "gg"]
    #baaabbacddc

    while any([l in morceau for l in lettres]):
        for double in lettres:
            morceau = morceau.replace(double, "")

    print(morceau)

if __name__ == "__main__":
    morceau = str(input())
    uniques(morceau)
    
    """
    Les notes de musiques sont représentées par les lettres 'a', 'b', 'c', 'd', 'e', 'f' et 'g'.

Votre programme doit lire une seule ligne de texte représentant le morceau de musique (composé de moins de 500 notes) et doit afficher la version du morceau "corrigée" où tous les doublons sont supprimés tant qu'il en existe.
    """