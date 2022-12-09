
def emplacements(numeros:dict):
    
    print(*[k for k, v in sorted(numeros.items(), key=lambda item: item[1])], sep='\n')

if __name__ == "__main__":
    nbEmplacements = int(input())
    numeros = {i:int(input()) for i in range(nbEmplacements)}
    emplacements(numeros)

