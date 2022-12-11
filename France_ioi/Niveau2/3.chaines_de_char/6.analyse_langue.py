import time
def apparitions(lettre, textes:list[str]):
    for text in textes:
        #print(text, len(text))
        for l in " ABCDEFGHIJKLMNOPQRSTUVWXYZ".replace(lettre, ""):
            text = text.replace(l, "")
        print(text, len(text))

def apparitions2(lettre, textes:list[str]):
    
    print(sum([text.count(lettre) for text in textes]))
        

if __name__ == "__main__":
    lettre = str(input())
    nbLignes = int(input())
    textes = [str(input()) for _ in range(nbLignes)]

    start = time.time()
    apparitions(lettre, textes)
    print(time.time() - start)

    start = time.time()
    apparitions2(lettre, textes)
    print(time.time() - start)
    