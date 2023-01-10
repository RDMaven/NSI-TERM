"Fails at test 6"


def stabilite_maximale(n: int, k: int, p: int, accroches: list[int]) -> None:
    """
    :param n: nombre d'accroches
    :param k: nombre de stabilisateurs
    :param p: indice de stabilité parfaite
    :param accroches: hauteur de chaque accroche
    """
    # TODO Afficher l'indice de stabilité maximal obtenable.

    """
    N : [1;12]
    K : [1;N]
    P : [1;100 000]
    accroches : [1;1 000 000 000]
    """

    
    def subsets(accroches):
        if accroches == []:
            return [[]]
        x = subsets(accroches[1:])
        return x + [[accroches[0]] + y for y in x]
       
    rep = set([tuple(sorted(x)) for x in subsets(accroches) if len(x)==4])
    print(rep)
    stabilite  = {}
    smart_choices = {}

    for x in rep:
        stab = p-(max(x)-min(x))**2
        stabilite[x] = stab
        if stab >= 0:
            smart_choices[x] = stab

    combs = [k for k,v in smart_choices.items()]

    answ = [tuple(sorted(x)) for x in subsets(combs) if len(x)<=k]
    

    stabilite_tuples={}
    for comb in answ:
        somme = 0
        for t in comb:
            somme =+ p-(max(t)-min(t))**2
        stabilite_tuples[comb] = somme
    
    best = -1

    for k,v in stabilite_tuples.items():
        if v > best:
            best = v
     
    print(best)
    

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = int(input())
    accroches = list(map(int, input().split()))
    stabilite_maximale(n, k, p, accroches)



"""

9
2
10
3 1 4 5 5 9 2 5 7


"""