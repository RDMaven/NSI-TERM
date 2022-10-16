"""PERFECT."""
import re
from typing import List


def nb_pas_malin_drome(n: int, mots: List[str]) -> None:
    """
    :param n: Le nombre de mots de passe contenus dans le fichier de mots de passe de Raphaël
    :param mots: La liste des mots de passe à décoder
    """
    # TODO Afficher le nombre de pas malin-dromes situés dans le fichier de
    # mots de passe de Raphaël
    r = 0
    for mot in mots:    
        nbs = re.sub('[^0-9]', '', mot)
        maj = re.sub('[^A-Z]', '', mot)
        min = re.sub('[^a-z]', '', mot)
        #print(nbs, maj, min)
        if nbs == nbs[::-1] and  maj == maj[::-1] and min == min[::-1]:
            r += 1
    return print(r)


if __name__ == "__main__":
    n = int(input())
    mots = [input() for _ in range(n)]
    nb_pas_malin_drome(n, mots)

