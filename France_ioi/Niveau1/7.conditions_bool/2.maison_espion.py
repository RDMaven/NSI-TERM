
def maison_espion(rectX, rectY, maisons):
    
    r = 0
    for maison in maisons:
        if maison[0] in rectX and maison[1] in rectY:
            r +=1
    print(r)

    pass

if __name__ == "__main__":
    rectX = range(int(input()), int(input())+1)
    rectY = range(int(input()), int(input())+1)
    
    nbMaisons = int(input())

    maisons = [(int(input()), int(input())) for _ in range(nbMaisons)]

    maison_espion(rectX, rectY, maisons)
