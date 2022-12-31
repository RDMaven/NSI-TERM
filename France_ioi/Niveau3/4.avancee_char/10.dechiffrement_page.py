
"""
La première ligne de l'entrée contient la grille de décryptage, composée de 26 caractères minuscules. La première lettre correspond à la lettre par laquelle il faut remplacer tous les 'a' du texte crypté, la deuxième tous les 'b', etc.

La deuxième ligne de l'entrée contient le texte crypté.

Il n’y a pas d’accents, mais il peut y avoir des espaces, de la ponctuation, etc.

Sortie
Vous devez afficher une ligne sur la sortie : le texte décrypté.

Chaque lettre cryptée doit être remplacée par la lettre décryptée. Les autres caractères (ponctuation, '_', espaces, chiffres), sont laissés tels quels.

Vous devez respecter la casse : si une lettre était en majuscule (ou minuscule), elle doit le rester !

"""

def decryptage(grille, texte):
    
    ans = ""
    for char in texte:
        if ord(char) >= ord("A") and ord(char) <= ord("Z"):
            ans += grille[ord(char)-ord("A")].upper()
        elif ord(char) >= ord("a") and ord(char) <= ord("z"):
            ans += grille[ord(char)-ord("a")]
        else:
            ans += char

    return print(ans)

if __name__ == "__main__":
    grille = str(input())
    texte = str(input())

    decryptage(grille, texte)

"""
qwertyuiopasdfghjklzxcvbnm
Xiyqigd !
"""