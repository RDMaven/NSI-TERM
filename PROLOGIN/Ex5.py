"Fails at test 6"
from typing import List


def stabilite_maximale(n: int, k: int, p: int, accroches: List[int]) -> None:
    """
    :param n: nombre d'accroches
    :param k: nombre de stabilisateurs
    :param p: indice de stabilité parfaite
    :param accroches: hauteur de chaque accroche
    """
    
    r = []
    accroches.sort()
    
    # Si moins de 4 accroches sont données, on ne peut stabiliser aucun stabilisateur.
    if n < 4 :
        r.append(0)

    else: # n >= 4
        
        # Pour un premier stabilisateur, 
        if k >= 1 and n >= 4 :
            decalage = 4
            desequilibre_4 = [accroches[i+decalage-1]-accroches[i] for i in range(n-decalage+1)]
            r.append(p-(min(desequilibre_4)**2))

        # Pour 2 stabilisateurs (si plus de 8 accroches...)
        if k >= 2 and n >= 8 : 
            decalage = 8
            accroches_8 = [accroches[i:i+decalage] for i in range(n-decalage+1)]
            for grp in accroches_8:
                desequilibre_8 = 2*p - ((grp[3]-grp[0])**2 + (grp[7]-grp[4])**2)
                r.append(desequilibre_8)

        # 3 stabilisateurs
        if k >= 3 and n == 12:
            grp = accroches
            r.append(3*p - ((grp[3]-grp[0])**2 + (grp[7]-grp[4])**2 + (grp[11]-grp[8])**2))

        if n > 12:
            r.append(0)

    return print(max(r))


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = int(input())
    accroches = list(map(int, input().split()))
    stabilite_maximale(n, k, p, accroches)

    
