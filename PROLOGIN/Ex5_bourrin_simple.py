
def combinaison(liste:list, k:int, reponses:list, out=(), i=0):
    length = len(liste)
    # Condition d'arrete sur l'entrée
    if length == 0 or k > length:
        return
 
    # Si on a compléter un élément, on l'ajout a la liste de réponse, et on passe au suivant.
    if k == 0:
        reponses.append(out)
        return
 
    # On commence par l'index suivant jusqu'au dernier
    for j in range(i, length):
        # On ajoute l'élément liste[j] à la solution traitée et on passe au prochain index j+1 par récc, en essayant de compléter pour k-1 (un élément à été trouvé).
        combinaison(liste, k - 1, reponses, out + (liste[j],), j + 4)


def stabilite_maximale(n: int, k: int, p: int, accroches: list[int]) -> None:
    """
    :param n: nombre d'accroches
    :param k: nombre de stabilisateurs
    :param p: indice de stabilité parfaite
    :param accroches: hauteur de chaque accroche
    """

    k = k if n//4 >= k else n//4

    #trier la liste des accroches
    accroches.sort()

    if n < 4: #on ne peut rien stabiliser
        return print(0)

    else: 
        deltas = [p - (accroches[i+3]-accroches[i])**2 for i in range(n-3)]

    list_combinations = list()

    for n in range(k + 1):
        reponses = []
        combinaison(deltas, n, reponses=reponses)
        list_combinations += reponses

    return print(max([sum(a) for a in list_combinations]))

    
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = int(input())
    accroches = list(map(int, input().split()))
    stabilite_maximale(n, k, p, accroches)
    
