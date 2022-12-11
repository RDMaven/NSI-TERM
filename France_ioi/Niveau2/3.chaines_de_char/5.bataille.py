
def bataille(joueur1:str, joueur2:str):

    egal = 0
    while len(joueur1) != 0 or len(joueur2) != 0:
        if len(joueur1) == 0:
            return print(2, egal, sep='\n')
        if len(joueur2) == 0:
            return print(1, egal, sep='\n')

        carte1 = joueur1[0]
        carte2 = joueur2[0]
        if carte1 == carte2:
            egal +=1
        elif carte1 > carte2:
            return print(2, egal, sep='\n')
        else:
            return print(1, egal, sep='\n')
        joueur1 = joueur1[1:]
        joueur2 = joueur2[1:]
    return print('=', egal, sep='\n')

def bataille2(deck1:str, l1:int, deck2:str, l2:int, egal:int=0):
    if l1 == 0 and l2 == 0:
        return print('=', egal, sep='\n')
    if l1 == 0:
        return print(2, egal, sep='\n')
    elif l2 == 0:
        return print(1, egal, sep='\n')
    
    carte1 = deck1[0]
    carte2 = deck2[0]
    
    if carte1 > carte2:
        return print(2, egal, sep='\n')
    elif carte1 < carte2:
        return print(1, egal, sep='\n')
    else :
        egal +=1
    
    bataille2(deck1[1:], len(deck1)-1, deck2[1:], len(deck2)-1, egal)



if __name__ == "__main__":
    joueur1 = str(input())
    joueur2 = str(input())
    print("====")
    bataille(joueur1, joueur2)
    print("====")
    bataille2(joueur1, len(joueur1), joueur2, len(joueur2))

