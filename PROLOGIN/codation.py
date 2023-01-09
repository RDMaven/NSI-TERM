def dicochaudmie():
    
nb_accroche=int(input())
nb_stabilisateur = int(input())
indice_parfait = int(input())
coo = sorted(list(map(int, input().split(" "))))
liste_derivee=[]
for i in range(len(coo)-3):
    liste_derivee.append(coo[i+3]-coo[i])
liste_derivee=sorted(liste_derivee)
