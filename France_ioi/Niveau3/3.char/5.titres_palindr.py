
def palindation(phrase:str):
    
    for titre in phrase:
        titreP = titre.lower().replace(" ", "")
        m = len(titreP)//2
        if titreP[:m] == titreP[::-1][:m]:
            print(titre)

if __name__ == "__main__":
    nbLivres = int(input())
    phrases = [str(input()) for _ in range(nbLivres)]
    palindation(phrases)