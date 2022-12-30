
def numeroMois(nMois):
    
    mois = {
        1:30, 
        2:30, 
        3:30,   
        4:31, 
        5:31, 
        6:31, 
        7:30, 
        8:30, 
        9:30, 
        10:31, 
        11:29
    }

    return print(mois[nMois])
    

if __name__ == "__main__":
    nMois = int(input())
    numeroMois(nMois)
