
def cadre(nb:int):
        
    lettres = "abcdefghijklmnopqrstuvwxyz"
    
    tab = [lettres[:i] + lettres[i]*((2*nb-1)-(2*i)) + lettres[:i][::-1] for i in range(nb)]
    tab.extend(tab[:-1][::-1])
    
    print(*tab, sep='\n')

if __name__ == "__main__":
    nbLettres = int(input())
    cadre(nbLettres)
    
    