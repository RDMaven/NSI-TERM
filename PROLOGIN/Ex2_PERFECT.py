def mise_en_boite(n: int, restes: list[int], boites: list[int]) -> None:
    """ Affiche sur une ligne le nombre maximum de restes que l'on peut mettre en boîte.

    Args:
        n (int): Le nombre de boîtes et de restes
        restes (list[int]): Liste des volumes des restes
        boites (list[int]): Liste des volumes des boîtes

    Returns:
        _type_: _description_
    """
    
    # On parcours les listes tant que tout n'est pas rempli ou que l'on a plus de restes a ranger. 
    while n and restes:
        #print(restes, boites)
        # si le reste le plus grand ne peut pas être rangé, alors on aura un reste en moins a ranger...
        if restes[0] > boites[0]:
            n -= 1
        # sinon on peut ranger les restes le plus grands et on enlève la boite (la plus grande)
        else:
            boites.pop(0)
        # enfin on enlève le reste car il est soit rangé, soit impossible a ranger.
        restes.pop(0)
    
    return print(n)

if __name__ == "__main__":
    n = int(input())
    restes = list(map(int, input().split()))
    boites = list(map(int, input().split()))
    restes.sort(reverse=True)
    boites.sort(reverse=True)
    mise_en_boite(n, restes, boites)