####################################################################################################
# ==================================== # TP : Rendu monnaie # ==================================== #
####################################################################################################

# +------------------------------------------------------+ #
# ++++++++++++++++++ Approche glouonne +++++++++++++++++++ #
# +------------------------------------------------------+ #

def AlgoGlouton(r,k,tp,ln):
    
    for i in range(k-1,-1,-1):
        ln[i] += r//tp[i]
        r -= (r//tp[i])*tp[i]            
    return ln

"""
tp = (1,2,5,10,20,50,100)
r = 231
k = len(tp)
ln = [0]*k
print(AlgoGlouton(r,k,tp,ln))
try:
    assert(AlgoGlouton(r,k,tp,ln))==[1, 0, 0, 1, 1, 0, 2]
except:
    print("\nC'est pas encore ça !")
else:
    print("\nbravo !")
"""
# +------------------------------------------------------+ #
# +------------------------------------------------------+ #


# +------------------------------------------------------+ #
# ++++++++++++++++++ Approche récursive ++++++++++++++++++ #
# +------------------------------------------------------+ #

from math import inf
from time import time

def enregistre(ln):
    global M,best
   
    # si le contenu de ln n'est pas dans M alors
    if ln not in M:
        # M ← contenu de ln
        M.append(list(ln))
    # si somme(best) > somme(ln) alors
    if sum(list(best)) > sum(list(ln)):
        # best ← contenu de ln
        best = list(ln)

def RenduExhaustif(k,tp,r,ln,i=0):
    global cpt #pour comptabiliser le nombre de récursions
    cpt += 1
    # si r = 0 alors renvoyer 0
    if r == 0:
        return 0
    # sinon si r < 0 alors renvoyer ∞
    elif r < 0:
        return inf
    # sinon pour i de 0 à k faire
    else:
        for i in range(k):
        # incrémenter ln(i)
            ln[i]+=1
            # x ← RenduExhaustif(k,tp,r-tp[i],ln,i) 
            x = RenduExhaustif(k,tp,r-tp[i],ln,i)
            # si x = 0 alors
            if x == 0: 
                # enregistre(ln) 
                enregistre(ln)
            # décrémenter ln(i)
            ln[i]-= 1
"""
tp = (1,2,5,10,20,50,100,200) #Valeurs du système monétaire
r = 9
k = len(tp)
ln = [0]*k #Nombre de pièces à rendre par valeur
cpt = 0 #compteur d’appels de boucle récursive
M = list() #enregistrement des combinaisons de pièces à rendre par valeur
best=[inf for i in range(k)] #Meilleure solution
RenduExhaustif(k,tp,r,ln)
print("compteur récursif = ",cpt)
print("M : ",M)
print("nombre de solutions",len(M))
print("La meilleur solution est ",best)
"""
# +------------------------------------------------------+ #
# +------------------------------------------------------+ #


# +------------------------------------------------------+ #
# ++++++++++++++++++ Approche récursive ++++++++++++++++++ #
# +------------------------------------------------------+ #

from math import inf
from time import time

def enregistre(ln):
    global M,best
   
    # si le contenu de ln n'est pas dans M alors
    if ln not in M:
        # M ← contenu de ln
        M.append(list(ln))
    # si somme(best) > somme(ln) alors
    if sum(list(best)) > sum(list(ln)):
        # best ← contenu de ln
        best = list(ln)

def RenduExhaustif(k,tp,r,ln,i=0):
    global cpt #pour comptabiliser le nombre de récursions
    cpt += 1
    if r == 0:
        return 0
    elif r > 0:
        for i in range(k):
            if r-tp[i] >= 0:
                ln[i]+=1
                # x ← RenduExhaustif(k,tp,r-tp[i],ln,i) 
                x = RenduExhaustif(k,tp,r-tp[i],ln,i)
                # si x = 0 alors
                if x == 0: 
                    enregistre(ln)
                ln[i]-= 1
"""
tp = (1,2,5,10,20,50,100,200) #Valeurs du système monétaire
r = 9
k = len(tp)
ln = [0]*k #Nombre de pièces à rendre par valeur
cpt = 0 #compteur d’appels de boucle récursive
M = list() #enregistrement des combinaisons de pièces à rendre par valeur
best=[inf for i in range(k)] #Meilleure solution
RenduExhaustif(k,tp,r,ln)
print("compteur récursif = ",cpt)
print("M : ",M)
print("nombre de solutions",len(M))
print("La meilleur solution est ",best)
"""
# +------------------------------------------------------+ #
# +------------------------------------------------------+ #


# +------------------------------------------------------+ #
# ++++++++++++++++ Programmation dynamique +++++++++++++++ #
# +------------------------------------------------------+ #

def RenduDynamique(k,tp,r,ln,ajou,i=0): 
    global cpt #pour comptabiliser le nombre de récursions
    if r == 0 : return 0
    #sinon si liste ajou(r) différent de () alors
    elif ajou[r]:
        for element in ajou[r]:
            #créer une liste "solution" de k valeurs
            solution = [0 for i in range(k)]
            for a in range(k):
                solution[a] = ln[a]+element[a]
            enregistre(solution)
            #copier la liste "élément" dans une liste "Najou"
            Najou = element.copy()
            Najou[i] += 1
            ajou[r+tp[i]].append(list(Najou))

    #sinon pour i de 0 à k faire
    else : 
        for i in range(k):
            if r-tp[i] > 0:
                ln[i] += 1
                x = RenduExhaustif(k,tp,r-tp[i],ln,i)
                if x==0:
                    enregistre(ln)
                    #créer une liste "Najou" de k valeurs
                    Najou = [0 for i in range(k)]
                    Najou[i] += 1
                    ajou[r] += Najou
            ln[i] -= 1
    


t1 = time() #temps de début du traitement 
tp = (1,2,5,10,20,50,100,200) #Valeurs du système monétaire
r = 23
k = len(tp)
ln = [0]*k #Nombre de pièces à rendre par valeur
cpt = 0 #compteur d’appels de boucle récursive
M = list() #enregistrement des combinaisons de pièces à rendre par valeur
best=[inf for i in range(k)] #Meilleure solution
ajou={1+d:[] for d in range(r)} #valeur à ajouter au nombre de pièce lors de la mémoïsation
RenduDynamique(k,tp,r,ln,ajou)
print("durée du traitement = ",time()-t1,"s")
print("compteur récursif = ",cpt)
print("M : ",M)
print("nombre de solutions",len(M))
print("La meilleure solution est ",best)

# +------------------------------------------------------+ #
# +------------------------------------------------------+ #
