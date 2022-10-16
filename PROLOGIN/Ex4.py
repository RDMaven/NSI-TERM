"""512 points : optimize ça wsh."""
from typing import List


def trajets_retour(n: int, redirection: List[int]) -> None:
    """
    :param n: le nombre de cinémas
    :param redirection: le lieu de redirection de chaque cinéma
    """
    # TODO Afficher, sur une ligne et séparé par une espace, le nombre de
    # redirections nécessaires en partant de chaque cinéma avant de retomber à
    # nouveau sur un cinéma déjà visité.
    a = [[i+1] for i in range(n)]
    correspondant = dict(zip([i+1 for i in range(n)], redirection))

    for  i in range(n):
        while correspondant[a[i][-1]] not in a[i]:
            a[i].append(correspondant[a[i][-1]])
    
    print(*[len(i) for i in a])


if __name__ == "__main__":
    n = int(input())
    redirection = list(map(int, input().split()))
    trajets_retour(n, redirection)
