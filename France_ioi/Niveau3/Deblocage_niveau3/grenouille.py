def course(nbGrenouilles, tours:list):
    positions = [0 for _ in range(nbGrenouilles)]
    gagnant = {i:0 for i in range(1, nbGrenouilles+1)}
    w = 1
    for tup in tours[:-1]:
        positions[tup[0]-1] += tup[1]
        print(*positions)
        maxi = max(positions)
        w = positions.index(maxi)+1
        bis = 0
        for pos in positions:
            if pos == maxi:
                bis += 1
        if bis == 1:
            gagnant[w] += 1
    print(w)

if __name__ == "__main__":
    nbGrenouilles = int(input())
    nbTours = int(input())
    tours = [tuple(map(int, input().split())) for _ in range(nbTours)]

    course(nbGrenouilles, tours)


    """
nbGrenouilles numérotées de 1 à nbGrenouilles sont placées sur une ligne de départ. À chaque tour, on vous indique le numéro de la seule grenouille qui va sauter lors de ce tour, et la distance qu'elle va parcourir en direction de la ligne d'arrivée.

pour chaque tour:
    ajouter la distance à la position de la grenouille
    si il n'y a qu'une grenouille en tête, 
        incrémenter le nombre de tours gagnés par la grenouille
    sinon passer.

Écrivez un programme qui détermine laquelle des grenouilles a été strictement en tête de la course au début du plus grand nombre de tours. Notez que comme on s'intéresse à qui est en tête au début de chaque tour, le bond du dernier tour ne sert à rien car même si la grenouille concernée passe en tête, la course est finie (il est purement honorifique selon la tradition algoréenne).
    """