
def avantageEquipe(poids1:int, poids2:int):
    avantage = 1 if poids1 > poids2 else 2
    print("L'équipe ", str(avantage), " a un avantage")
    print("Poids total pour l'équipe 1 : ", str(poids1))
    print("Poids total pour l'équipe 2 : ", str(poids2))
    

if __name__ == "__main__":
    nbMembres = int(input())
    poids1, poids2 = [], []
    for _ in range(nbMembres):
        poids1.append(int(input()))
        poids2.append(int(input()))
        
    avantageEquipe(sum(poids1), sum(poids2))

"""


"""