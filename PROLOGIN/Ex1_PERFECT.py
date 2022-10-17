"""PERFECT."""
from typing import List


def nombre_films(adore: List[str], deteste: List[str]) -> None:
    """
    :param adore: liste des noms du film adoré de chaque personne
    :param deteste: liste des noms du film détesté de chaque personne
    """
    # TODO Afficher, sur une ligne, le nombre de films qui sont uniquement
    # adorés.
    return print(len(set(adore+deteste))-len(set(deteste)))


if __name__ == "__main__":
    adore = [input() for _ in range(6)]
    deteste = [input() for _ in range(6)]
    nombre_films(adore, deteste)
