def empruntabliite(clients:list):
    livres_empruntes={}
    for c in clients:
        if c[0] in livres_empruntes:
            if bool(set(livres_empruntes[c[0]]).intersection(c[1])) == False:
                livres_empruntes[c[0]] = c[1]
                print(1)
            else:
                print(0)
        else:
            livres_empruntes[c[0]] = c[1]
            print(1)


if __name__ == "__main__":
    data = list(map(int, input().split()))
    #nbLivres= data[0]
    nbJours = data[1]
    clients = []
    for j in range(nbJours):
        nbClients = int(input())
        for c in range(nbClients):
            dataC = list(map(int, input().split()))
            clients.append((dataC[0], range(j,j+dataC[1])))

    empruntabliite(clients)
    