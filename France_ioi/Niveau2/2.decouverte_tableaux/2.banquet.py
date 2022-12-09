
def places(numeros:dict, changements:list):
    
    for ch in changements:
        numeros[ch[0]],numeros[ch[1]] = numeros[ch[1]], numeros[ch[0]]

    print(*[v for v in numeros.values()], sep='\n')

if __name__ == "__main__":
    nb_positions = int(input())
    nb_changements = int(input())
    numeros = {i:int(input()) for i in range(nb_positions)}
    changements = [(int(input()), int(input())) for _ in range(nb_changements)]
    places(numeros, changements)

