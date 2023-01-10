def trajets_retour(n: int, redirection: list[int]) -> None:
    """ Affiche, sur une ligne et séparé par une espace, le nombre de redirections nécessaires en partant de chaque cinéma avant de retomber à nouveau sur un cinéma déjà visité.

    Args:
        n (int): le nombre de cinémas
        redirection (list[int]): le lieu de redirection de chaque cinéma
    """    
    # ajouter un élément pour que l'indice de chaque élément correspond à sa valeur.
    redirection.insert(0, 0)
    
    #initialiser le dictonnaire qui contiendra ne nombre de redirections pour chaque cinéma
    final_redirects = {}
    
    # Pour chaque cinéma donné,
    for i in range(1, n+1):
        # ...si on a deja une réponse pour le cinéma, passer au suivant.
        if i in final_redirects:
            continue
        
        # ...sinon, vérifier si la REDIRECTION est dans une boucle deja découverte.
        else:
            
            # Si oui, alors le nombre de redirection sera de : 1 (pour aller a celle connu) + le nombre de la boucle connue.
            if redirection[i] in final_redirects:
                final_redirects[i] = 1 + final_redirects[redirection[i]]

            # Sinon, tant que la redirection n'a pas deja été visitée, on mémorise le nouvel élément.
            else:
                parcours = [i]
                append = parcours.append
                while redirection[parcours[-1]] not in parcours:
                    append(redirection[parcours[-1]])
                # puis, lorsque l'on a terminé le parcours, on retiens l'indice de l'élément qui est deja dans la liste pour savoir ou commence la boucle. EX : "2 → 1 → 3 → 4 → 1" la boucle contient 1, 3 et 4, sa taille est de 3.
                limite = parcours.index(redirection[parcours[-1]])
                taille_parcours = len(parcours)
                taille_boucle = taille_parcours - limite
               
                # Finalement, pour chaque élément du parcours,
                for i_nb in range(taille_parcours):
                    # S'il est avant le début de la boucle, la taille de la redirect est la taille du parcours depuis l'élément.
                    if i_nb < limite:
                        final_redirects[parcours[i_nb]] = taille_parcours - i_nb
                    # Sinon, (l'élément est alors dans la boucle), la taille est celle de la boucle.
                    else:
                        final_redirects[parcours[i_nb]] = taille_boucle
    
    # On termine par afficher, dans l'ordre, le nombre de redirections nécessaires.
    for i in range(1, n+1):
        print(final_redirects[i], end=' ')

if __name__ == "__main__":
    n = int(input())
    redirection = list(map(int, input().split()))
    trajets_retour(n, redirection)