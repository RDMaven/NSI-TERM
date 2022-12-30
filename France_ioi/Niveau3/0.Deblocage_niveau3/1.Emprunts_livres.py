import tracemalloc


def pretabilite_livre(demandeJours: dict):

    par_clients = {}

    for clients in demandeJours.values():
        for client, livre in clients.items():
            par_clients[client] = {
                'iL': livre['iL'], 
                'duree': livre['duree']
                }

    livre_pris = {}
    reponse = []
    for client, livre in par_clients.items():
        if livre['iL'] not in livre_pris:
            livre_pris[livre['iL']] = livre['duree']
            reponse.append(1)
        else:
            periode_prise = livre_pris[livre['iL']]
            peride_voulue = livre['duree']
            if bool(set(periode_prise).intersection(peride_voulue)) == False:
                livre_pris[livre['iL']] = livre['duree']
                reponse.append(1)
            else:
                reponse.append(0)
    return reponse

def pretabilite_livre2(demandeJours: dict):

    livre_pris = {}
    reponse = []

    for clients in demandeJours.values():
        for client, livre in clients.items():
            if livre['iL'] not in livre_pris:
                livre_pris[livre['iL']] = livre['duree']
                reponse.append(1)
            else:
                periode_prise = livre_pris[livre['iL']]
                peride_voulue = livre['duree']
                if bool(set(periode_prise).intersection(peride_voulue)) == False:
                    livre_pris[livre['iL']] = livre['duree']
                    reponse.append(1)
                else:
                    reponse.append(0)
    return reponse



if __name__ == "__main__":
    tracemalloc.start()

    nbJours = int(input().split()[1])


    demandeJours = {}
    total_clients = 0

    for j in range(1,nbJours+1):
        nbClients = int(input())

        demandeClients = {}
        for i in range(nbClients):
            dataClient = list(map(int, input().split()))
            demandeClients[i+total_clients] = {"iL": dataClient[0], "duree": range(j,j+dataClient[1])}
        total_clients += nbClients
        demandeJours[j] = demandeClients
    
    print(*pretabilite_livre(demandeJours), sep='\n')
    print(tracemalloc.get_traced_memory())

    print(*pretabilite_livre2(demandeJours), sep='\n')
    print(tracemalloc.get_traced_memory())

    tracemalloc.stop()
