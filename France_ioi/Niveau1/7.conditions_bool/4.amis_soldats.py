
def amitie(soldat1, soldat2):
    
    if bool(set(soldat1).intersection(soldat2)):
        print("Amis")
    else:
        print("Pas amis")
     
    

if __name__ == "__main__":
    soldat1 = range(int(input()), int(input())+1)
    soldat2 = range(int(input()), int(input())+1)

    amitie(soldat1, soldat2)
