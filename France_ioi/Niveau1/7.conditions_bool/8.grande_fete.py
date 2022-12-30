"""
On vous donne une période de temps à étudier, et les dates d'arrivée et de départ d'un certain nombre d'invités d'une fête. Écrivez un programme qui détermine combien d'invités ont été présents à un moment de la période étudiée.

Votre programme doit d'abord lire deux entiers : la date de début et la date de fin de la période étudiée. L'entier suivant, nbInvites, est le nombre total d'invités. Pour chaque invité, votre programme doit ensuite lire deux entiers : sa date d'arrivée et de départ. Un invité est suspect si la période à laquelle il a été présent intersecte la période étudiée. Votre programme doit afficher le nombre d'invités suspects.

"""


def fete(debut, fin, personnes):
    r = 0
    for p in personnes:
        if not ((p[1] < debut) or (p[0] > fin)):
            r += 1
    return r

if __name__ == "__main__":
    debut = int(input())
    fin =  int(input())
    nbInvites = int(input())
    personnes = [(int(input()), int(input())) for _ in range(nbInvites)]

    print(fete(debut,fin, personnes))