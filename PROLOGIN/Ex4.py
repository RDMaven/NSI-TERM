"""512 points : optimize ça wsh."""

def trajets_retour_dummy(n: int, redirection: list[int]) -> None:
    """
    :param n: le nombre de cinémas
    :param redirection: le lieu de redirection de chaque cinéma
    """
    # TODO Afficher, sur une ligne et séparé par une espace, le nombre de
    # redirections nécessaires en partant de chaque cinéma avant de retomber à
    # nouveau sur un cinéma déjà visité.
    
    correspondant = dict(zip([i for i in range(1, n+1)], redirection))
    
    a = [[i+1] for i in range(n)]

    print(correspondant, a)
    for  i in range(n):
        while correspondant[a[i][-1]] not in a[i]:
            a[i].append(correspondant[a[i][-1]])
    
    print(*[len(i) for i in a])


def trajets_retour_optimeV1(n, redirection):
    elements = [i for i in range(1, n+1)]
    correspondant = dict(zip(elements, redirection))

    #print(correspondant)    

    final_redirects = {}
    for i in range(1, n+1):
        if i in final_redirects:
            #print(final_redirects[i], end=' ')
            continue
        else:
            # check si la redirection est dans une boucle deja découverte
            if correspondant[i] in final_redirects:
                # si oui, alors le nombre de redirection sera de 1 (pour aller a celle connu) + le nombre de la boucle connue.
                final_redirects[i] = 1 + final_redirects[correspondant[i]]
            else:
                # sinon, tant que la redirection n'a pas deja été visitée, on mémorise le nouvel élément
                parcours = [i]
                while correspondant[parcours[-1]] not in parcours:
                    parcours.append(correspondant[parcours[-1]])
                # puis, lorsque l'on a terminé le parcours, on retiens l'indice de l'élément qui est deja dans la liste pour savoir ou commence la boucle.
                limite = parcours.index(correspondant[parcours[-1]])
                taille_parcours = len(parcours)
                taille_boucle = taille_parcours - limite
                # pour chaque élément avant le début de la boucle, on connait la taille de la redirect : la taille du parcours depuis l'élément.
                for i_nb in range(taille_parcours):
                    if i_nb < limite:
                        final_redirects[parcours[i_nb]] = taille_parcours - i_nb
                    else:
                        final_redirects[parcours[i_nb]] = taille_boucle
        #print(parcours)
        #print(final_redirects)
        #print(final_redirects[i], end=' ')
    
    for i in range(1, n+1):
        print(final_redirects[i], end=' ')

def trajets_retour_optimeV2(n:int, correspondant:list): 
    # ajouter un élément pour que l'indice de chaque élément correspond à sa valeur.
    correspondant.insert(0, 0)
    
    final_redirects = {}
    for i in range(1, n+1):
        
        if i in final_redirects:
            print(final_redirects[i], end=' ')
            continue
        else:
            # check si la redirection est dans une boucle deja découverte
            if correspondant[i] in final_redirects:
                # si oui, alors le nombre de redirection sera de 1 (pour aller a celle connu) + le nombre de la boucle connue.
                final_redirects[i] = 1 + final_redirects[correspondant[i]]
            else:
                # sinon, tant que la redirection n'a pas deja été visitée, on mémorise le nouvel élément
                parcours = [i]
                while correspondant[parcours[-1]] not in parcours:
                    parcours.append(correspondant[parcours[-1]])
                # puis, lorsque l'on a terminé le parcours, on retiens l'indice de l'élément qui est deja dans la liste pour savoir ou commence la boucle.
                limite = parcours.index(correspondant[parcours[-1]])
                taille_parcours = len(parcours)
                taille_boucle = taille_parcours - limite
                # pour chaque élément avant le début de la boucle, on connait la taille de la redirect : la taille du parcours depuis l'élément.
                for i_nb in range(taille_parcours):
                    if i_nb < limite:
                        final_redirects[parcours[i_nb]] = taille_parcours - i_nb
                    else:
                        final_redirects[parcours[i_nb]] = taille_boucle
        #print(parcours)
        #print(final_redirects)
        print(final_redirects[i], end=' ')


if __name__ == "__main__":
    n = int(input())
    redirection = list(map(int, input().split()))
    trajets_retour_optimeV2(n, redirection)
