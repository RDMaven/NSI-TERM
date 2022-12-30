
def simultaneite(nbPersonnes:int, chronologie:list):
    
    maxi_abs = 0
    maxi_local = 0

    for n in chronologie:
        if n > 0:
            maxi_local += 1
        else:
            maxi_local -= 1
        
        if maxi_local > maxi_abs:
            maxi_abs = maxi_local

    return print(maxi_abs)
    

if __name__ == "__main__":
    nbPersonnes = int(input())
    chronologie = [int(input()) for _ in range(nbPersonnes*2)]

    simultaneite(nbPersonnes, chronologie)
