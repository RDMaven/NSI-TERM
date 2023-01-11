
def mise_en_boite(n: int, restes: list[int], boites: list[int], i:int, r:int) -> None:
    """ Affiche sur une ligne le nombre maximum de restes que l'on peut mettre en boîte.

    Args:
        n (int): Le nombre de boîtes et de restes
        restes (list[int]): Liste des volumes des restes
        boites (list[int]): Liste des volumes des boîtes

    Returns:
        _type_: _description_
    """
    if i == n:
        return print(r)
    else:        
        if restes[0] > boites[0]:
            r -= 1
        else:
            boites = boites[1:]

        mise_en_boite(n, restes[1:], boites, i+1, r)


if __name__ == "__main__":
    n = int(input())
    restes = list(map(int, input().split()))
    boites = list(map(int, input().split()))
    restes.sort(reverse=True)
    boites.sort(reverse=True)
    mise_en_boite(n, restes, boites, i=0, r=n)