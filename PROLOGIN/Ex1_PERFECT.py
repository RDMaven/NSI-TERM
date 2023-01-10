def nombre_films(adore: list[str], deteste: list[str]) -> None:
    """ Affiche, sur une ligne, le nombre de films qui sont uniquement adorés.

    Args:
        adore (List[str]): liste des noms du film adoré de chaque personne
        deteste (List[str]): liste des noms du film détesté de chaque personne

    Returns:
        None : Affichage du nombre de films uniquement adorés.
    """
    
    # Calcul la différence entre le nombre de films uniques au total (adoré ou detesté) et le nombre de films uniques detestés.
    # suivant l'égalité :    uniques_adorés + uniques_détéstés = uniques_total
    #                     => uniques_adorés = uniques_total - uniques_détéstés
    return print(len(set(adore+deteste))-len(set(deteste)))


if __name__ == "__main__":
    adore = [input() for _ in range(6)]
    deteste = [input() for _ in range(6)]
    nombre_films(adore, deteste)
