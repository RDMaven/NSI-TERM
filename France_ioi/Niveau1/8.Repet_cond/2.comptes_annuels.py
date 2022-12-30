"""
Votre programme devra lire une suite d'entiers positifs et afficher leur somme. On ne sait pas combien il y aura d'entiers, mais la suite se termine toujours par la valeur -1 (qui n'est pas une dépense, juste un marqueur de fin).
"""

def somme():
    sum = 0
    while True:

        entry = int(input())
        
        if entry == -1:
            return sum
        else:
            sum += entry
    

if __name__ == "__main__":
    print(somme())