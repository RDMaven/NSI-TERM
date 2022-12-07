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

    # Initialisation de la sortie
    r = []
    
    # Si moins de 4 accroches sont données, on ne peut stabiliser aucun stabilisateur.
    if n < 4:
        return [0]

    else:
        # Pour un premier stabilisateur, 
        diff = []
        for i in range(len(accroches)-3):
            # Maximum : 12-3 = 9
            #Trouver toutes les différences de 4 accroches les plus proches.
            diff.append(accroches[i+3]-accroches[i])
        r.append(p-(min(diff)**2))

        # Pour 2 stabilisateurs (si plus de 8 accroches...)
        if k >= 2 and n >= 8 : 
            accroches_8 = [accroches[i:i+8] for i in range(len(accroches)%8+1)]
            #print(accroches_8)

            # Indice = p - (max1-min1)^2 + p - (max2-min2)^2 = 2p - [(max1-min1)^2 + (max2-min2)^2]
            indice_stabilite = 2*p
            for grp in accroches_8:
                sum_carre=2*p # Reinitialiser la somme des carrés pour chaque sous groupe.
                for i_grp in range(len(accroches_8[0])%4): # Pour chaque 4 accroches du groupe
                    sum_carre += (grp[i_grp*4+3]- grp[i_grp*4])**2 # Calculer le désiquilibre
                r.append(indice_stabilite - sum_carre)
        
        # 3 stabilisateurs
        if k >= 3 and n == 12:
            sum_carre=0 # Reinitialiser la somme des carrés pour chaque sous groupe.
            for i_grp in range(n%4): # Pour chaque 4 accroches du groupe
                sum_carre += (grp[i_grp*4+3]- grp[i_grp*4])**2 # Calculer le désiquilibre
            r.append(3*p - sum_carre)
        #print(r)
        return print(max(r))

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = int(input())
    accroches = list(map(int, input().split()))
    stabilite_maximale(n, k, p, accroches)
