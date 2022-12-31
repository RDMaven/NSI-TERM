

def stabilite_maximale(n: int, k: int, p: int, accroches: list[int]) -> None:
    """
    :param n: nombre d'accroches
    :param k: nombre de stabilisateurs
    :param p: indice de stabilité parfaite
    :param accroches: hauteur de chaque accroche
    """
    stabiliteF = [0]

    if n < 4: #on ne peut rien stabiliser
        return print(0)
    
    #trier la liste des accroches
    accroches.sort()

    if n >= 4 and k >= 1: 
        #print("n >= 4 and k >= 1 : ")
        accroches4 = []
        for i in range(n-3):
            stabilite = p - (accroches[i+3]-accroches[i])**2
            #print(accroches[i:i+4], stabilite)
            accroches4.append(stabilite)

    stabiliteF.extend(accroches4)

    if n >= 8 and k >= 2:
        #print("n >= 8 and k >= 2 : ")
        for i in range(n-7):
            stabilite = accroches4[i] + accroches4[i+4]
            #print(accroches[i:i+8], stabilite)
            stabiliteF.append(stabilite)
    
    if n >= 12 and k >= 3:
        stabilite = accroches4[0] + accroches4[4] + accroches4[8]
        #print(accroches, stabilite)
        stabiliteF.append(stabilite)
    print(stabiliteF)
    return print(max(stabiliteF))

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = int(input())
    accroches = list(map(int, input().split()))
    stabilite_maximale(n, k, p, accroches)
