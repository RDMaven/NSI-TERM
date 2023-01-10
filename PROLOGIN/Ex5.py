def stabilite_maximale(n: int, k: int, p: int, accroches: list[int]) -> None:
    """
    :param n: nombre d'accroches
    :param k: nombre de stabilisateurs
    :param p: indice de stabilité parfaite
    :param accroches: hauteur de chaque accroche
    """
    stabiliteF = [0]
    stabiliteF_append = stabiliteF.append

    if n < 4: #on ne peut rien stabiliser
        return print(0)
    
    #trier la liste des accroches
    accroches.sort()

    
    if n >= 4 and k >= 1: 
        #print("n >= 4 and k >= 1 : ")
        accroches4 = []
        accroches4_ap = accroches4.append
        for i in range(n-3):
            stabilite = p - (accroches[i+3]-accroches[i])**2
            #print(accroches[i:i+4], stabilite)
            accroches4_ap(stabilite)

    stabiliteF.extend(accroches4)

    if n >= 8 and k >= 2:
        #print("n >= 8 and k >= 2 : ")
        for i in range(n-8+1):
            grp1 = accroches4[i]
            for j in range(i+4,n-4+1):
                grp2 = accroches4[j]

                stabilite = grp1 + grp2
                #print(accroches[i:i+8], stabilite)
                stabiliteF_append(stabilite)
    
    if n >= 12 and k >= 3:
        stabilite = accroches4[0] + accroches4[4] + accroches4[8]
        #print(accroches, stabilite)
        stabiliteF_append(stabilite)

    #print(stabiliteF)
    return print(max(stabiliteF))
    print("o w o")
    print("u w u")
    print("accrowoches et stabilisatuwurs")

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    p = int(input())
    accroches = list(map(int, input().split()))
    stabilite_maximale(n, k, p, accroches)
    
