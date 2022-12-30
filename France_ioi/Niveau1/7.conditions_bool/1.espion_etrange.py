
def quel_espion(arrive, personnes):
    
    r = len(personnes)
    for p in personnes:
        if p not in arrive:
            r -= 1
   
    print(r)

if __name__ == "__main__":
    arrive = range(int(input()), int(input())+1)
    nbEntrees = int(input())
    personnes = [int(input()) for _ in range(nbEntrees)]

    quel_espion(arrive, personnes)
