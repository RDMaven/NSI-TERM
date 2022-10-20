"Fails at test 6"
from typing import List


def stabilite_maximale(n: int, k: int, p: int, accroches: List[int]) -> None:
    """
    :param n: nombre d'accroches
    :param k: nombre de stabilisateurs
    :param p: indice de stabilité parfaite
    :param accroches: hauteur de chaque accroche
    """
    # TODO Afficher l'indice de stabilité maximal obtenable.

    accroches.sort()
    """
    N : [1;12]
    K : [1;N]
    P : [1;100 000]
    accroches : [1;1 000 000 000]
    """


    r = []
    if n < 4:
        r.append(0)

    # 1 stabilisateur
    if n >= 4: # and k >= 1 toujours vrai...
        diff = []
        for i in range(len(accroches)-3):
            diff.append(accroches[i+3]-accroches[i])
        r.append(p-(min(diff)**2))

    # 2 stabilisateurs
    if k >= 2 and n >= 8 :
        accroches_8 = [accroches[i:i+8] for i in range(len(accroches)%8+1)]
        
        sum_carre = p*2
        for grp in accroches_8:        
            if ((grp[3]-grp[0])**2 + (grp[7]-grp[4])**2) < sum_carre:
                sum_carre = (grp[3]-grp[0])**2 + (grp[7]-grp[4])**2

        r.append(p*2 - sum_carre)
    

    # 3 stabilisateurs
    if k == 3 and len(accroches) == 12:
        a3 = accroches
        r.append((p*3 -((a3[3]-a3[0])**2 + (a3[7]-a3[4])**2 + (a3[11]-a3[8])**2)))
   
    return print(max(r))

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = int(input())
    accroches = list(map(int, input().split()))
    stabilite_maximale(n, k, p, accroches)
