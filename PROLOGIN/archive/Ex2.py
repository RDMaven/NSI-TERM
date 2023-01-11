def mise_en_boite(n: int, restes: list[int], boites: list[int]) -> None:
    """ Affiche sur une ligne le nombre maximum de restes que l'on peut mettre en boîte.

    Args:
        n (int): Le nombre de boîtes et de restes
        restes (list[int]): Liste des volumes des restes
        boites (list[int]): Liste des volumes des boîtes

    Returns:
        _type_: _description_
    """

    while restes:

        if max(restes) > max(boites) :
            n -= 1
        else:
            boites.remove(max(boites))
        restes.remove(max(restes))

    return print(n)

if __name__ == "__main__":
    n = int(input())
    restes = list(map(int, input().split()))
    boites = list(map(int, input().split()))
    mise_en_boite(n, restes, boites)