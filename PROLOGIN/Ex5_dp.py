def plotter(dico:dict, accroches:list):
    import matplotlib.pyplot as plt
    import numpy as np


    keys = list(dico.keys())
    values = list(d[0] for d in dico.values())

    indices = np.array(keys)
    stabilite = np.array(values)
    diffs = [accroches[i+3]-accroches[i] for i in range(len(indices))]
    accroches = np.array(accroches)
    #plt.plot(indices, stabilite)
    plt.plot(diffs, 'o:g')
    plt.plot(accroches, 'o:r')
    
    
    plt.yticks([i for i in range(max(accroches)+1)])
    plt.xticks([i for i in range(len(accroches)+1)])
    plt.grid()
    plt.show()

def stabilite_maximale(n: int, k: int, p: int, accroches: list[int]) -> None:
    """
    :param n: nombre d'accroches
    :param k: nombre de stabilisateurs
    :param p: indice de stabilité parfaite
    :param accroches: hauteur de chaque accroche
    """
    # TODO Afficher l'indice de stabilité maximal obtenable.
    accroches.sort()

    

    difference = {i:(p-(accroches[i+3]-accroches[i])**2, 1) for i in range(n-3)}
    
    plotter(difference, accroches)

    for i in range(1, n-3):
        S = [j for j in range(i-3) if difference[j][0]>0]
        if difference[i][1] < k:
            
            difference[i] = (difference[i][0] + max([difference[j][0] for j in S], default=0), difference[i][1] + 1)
    

    return max(max([d[0] for d in difference.values()], default=0), 0)
    
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = int(input())
    accroches = list(map(int, input().split()))
    stabilite_maximale(n, k, p, accroches)
    
