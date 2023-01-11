
def combinaison(k:int, p:int, out=0, i=0):
    """ Trouver récursivement toutes les combinaisons de taille k.

    Args:
        k (int): taille de la combinaison
        temp (list): liste temporaire qui retient le résultat de la plus grande combinaison
        p (int): indice de stabilité parfaite
        out (int, optional): Entier qui retien la somme des instabilités, defaut à 0.
        i (int, optional): indice de l'élément dans la liste delta. Defaults to 0.
    """
    # Si on a compléter un élément, on l'ajout a la liste de réponse, et on passe au suivant.

    if k == 0:
        global maxi
        if p > out and maxi < p - out:
            maxi = p - out
        return
 
    # On commence par l'index suivant jusqu'au dernier
    for j in range(i, taille):
        # On ajoute l'élément liste[j] à la solution traitée et on passe au prochain index j+1 par récc, en essayant de compléter pour k-1 (un élément à été trouvé).
        combinaison(k - 1, p, out + deltas[j], j + 4)

    """
    while k > 0:
        for j in range(taille):
            temp_out = out + deltas[j]
            temp_k = k - 1

            # If we have completed an element, we add it to the answer list and move on to the next one.
            if temp_k == 0:
                if p > temp_out and temp[0] < p - temp_out:
                    temp.pop()
                    temp.append(p - temp_out)
                return
            else:
                combination(temp_k, temp, p, temp_out)

        k -= 1
    """

def stabilite_maximale(n: int, k: int, p: int, accroches: list[int]) -> None:
    """
    :param n: nombre d'accroches
    :param k: nombre de stabilisateurs
    :param p: indice de stabilité parfaite
    :param accroches: hauteur de chaque accroche
    """
    # déterminer le nombre maximum de stabilisateurs en fonction du nb d'accroches et du nb de stabilisateurs
    k = k if n//4 >= k else n//4

    if n < 4: #on ne peut rien stabiliser
        return print(0)

    global taille, deltas, maxi
    taille = n-3
    
    deltas = {i:(accroches[i+3]-accroches[i])**2 for i in range(taille)}
    deltas = dict(sorted(deltas.items(), key=lambda item: item[1]))
    iter_deltas = iter(deltas)
    best_value_1 = p - deltas[next(iter_deltas)]
   
    maxi = best_value_1 if best_value_1 > 0 else 0

    for n in range(2, k + 1):
        combinaison(k=n, p=p*n)

    return print(maxi)



    
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = int(input())
    accroches = sorted(list(map(int, input().split())))
    stabilite_maximale(n, k, p, accroches)
    
