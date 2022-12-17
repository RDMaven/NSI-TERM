
def pretty_grid_maker(grid, cases_valides=[]):
    pretty_grid = []
    for ligne in range(len(grid)):
        pretty_line = []
        for element in range(len(grid[0])):
            e = grid[ligne][element]
            if e == 0:
                e = str(e)
                ep =  f"\033[32;1m0\033[0m"

            else:
                e = str(e)
                ep = e

            if (ligne, element) in cases_valides:
                ep = f"\033[31;1m{str(e)}\033[0m"

            pretty_line.append(ep)
        pretty_grid.append(pretty_line)
    return pretty_grid

def make_grid(x:int,y:int):
    from random import randint
    grid = []
    for i in range(y):
        ligne = []
        for j in range(x):
            a = randint(0,2)
            if a == 0 or a == 2:
                a = 0
            ligne.append(a)
        grid.append(ligne)
    
    return grid

def espace(grid:list, dim:list):
    
    # -- Init
    # Dimention du terrain
    Dx = dim[0]
    Dy = dim[1]
    print("Dimentions : Dx={0:} Dy={1:}".format(Dx, Dy))

    # Taille maximale d'un carré libre / La dimention testée
    Dt = min(dim)
    print("Taille maximale d'un carré : Dt={:}".format(Dt))
    
    if Dt == 1:
        return 1

    # -- Maximum de 0 consécutifs sur chaque ligne, triés (croissant)
    max_par_ligne = []
    for ligne in range(Dy):
        ligne_str = ''.join([str(e) for e in grid[ligne]])
        # On récupère le nombre de 0 maximal donc on part du plus grand vers 0...
        for i in range(Dt, 0, -1): 
            if '0'*i in ligne_str:
                max_par_ligne.append(i)
                # ...et on arrete des qu'on a une valeur convenable
                break
    max_par_ligne.sort(reverse=True)
    print(f'Nombre maximum de 0s par lignes : {max_par_ligne}')


    # L'index de l'élément dans la liste triée +1 = le nombre de lignes qui contiennent ce element.
    # [9,9,6,4,3, ...] : 9 et 6 sont les (1,2,3)e elements, alors seules 3 lignes les ont. Or 4 est contenu dans 4 lignes...
    i = 0
    while max_par_ligne[i] > i+1:
        i += 1
    
    if max_par_ligne[i] == i+1:
        i +=1

    possibles = [e for e in range(i, 1,-1)]
    print(possibles)    


    # On a mntnt une liste contenant tout les elements possibles.
    apparitions = []
    for taille_carre in possibles:
        ap_ligne = []
        for ligne in range(Dy):
            ligne_str = ''.join([str(i) for i in grid[ligne]])
            _0s_ = '0'*taille_carre
            print(ligne_str, _0s_)
            
            decalage = 0
            while _0s_ in ligne_str:
                ap = ligne_str.index(_0s_)
                print("ligne_str={:}, decalage={:}, ap={:}".format(ligne_str, decalage, ap))
                print((decalage + ap, decalage + ap+taille_carre-1))
                ap_ligne.append((decalage + ap, decalage + ap+taille_carre-1))
                ligne_str = ligne_str[decalage+ap+taille_carre:]


        apparitions.extend(ap_ligne)
    print(apparitions)
    """
    pour chaque possibilité:
        pour chaque ligne
            pour chaque apparition des 0 consécutifs:
                retenir les indices de début et de fin

    
    """
    
    
    
    
    """
    # Pour chaque largeur possible,
    for largeur_possible in possibles:
        print("\033[33;1mTest de largeur = {:}\033[0m".format(largeur_possible))
        # Déterminer le nombre de sous carrés à tester

        cases = [(y,x) for x in range(Dx-Dt+1) for y in range(Dy-Dt+1)]
        #print("Les premières cases des carrés à tester : cases={:}".format(cases))
        print("Nombre de cases à tester : {:}".format(len(cases)))
        # Pour chaque sous carré possible
        for coords in cases:
            #print("Test du carré de première case {:}".format(coords))
            # Pour chaque ligne sous carré
            noLigne = coords[0]
            cases_valides = []
            #print(f"Les lignes correspondantes : {grid[coords[0]:coords[0]+Dt]}")
            for ligne in grid[coords[0]:coords[0]+Dt]:
                # Si Dt [0] ne sont pas alignés sur la ligne // s'il n'y a pas un espace de Dt sur la ligne 
                if not ('0'*Dt in ''.join([str(i) for i in ligne])):
                    #print("La ligne {0:} n'a pas {1:}.".format(ligne, [0]*Dt))
                    break
                else:
                    #print("La ligne {0:}       a {1:}.".format(ligne, [0]*Dt))
                    for e in range(len(ligne)):
                        if ligne[e:e+Dt] == [0]*Dt:
                            cases_valides.extend([(noLigne, i) for i in range(e,e+Dt)])
                            break

                    if noLigne == coords[0]+Dt-1:
                        print("\033[34;1mC'EST GAGNÉ ! : Dt={:}\033[0m".format(Dt))

                        pretty_grid = pretty_grid_maker(grid, cases_valides)
                        for i in pretty_grid:
                            print(*i, sep='  ')

                        return Dt
                noLigne += 1
        Dt -= 1"""

    # si le tableau contient au moins un 0
    # si le tableau ne contient aucun 0.

    """
    retenir le plus petit des deux dimentions qui correspond à la lmax du carré recherché, comme Dt, la dimention testée
    Dx, Dy = dimentions du grid
    tant que le carré n'est pas trouvé et tant que Dt != 0.
        le nombre de tests a faire est de : (le nombre de première case pour chaque sous carré)
        -  Dx - Dt, Dy - Dt 
        -- (EX : Dx=6, Dy=7; pour Dt = 6: tests = grid[0][0], grid[1][0] )
        --- cases = []
        --- for y in range(Dy-Dt+1) # = 1+1 = 2 [0,1]
                for x in range(Dx-Dt+1) # = 0+1 = 1 [0]
                    cases.append((y,x))

        pour chaque sous carré possible:   
            pour chaque ligne du tableau,
                si il n'y a pas un espace de Dt sur la ligne:
                    passer au prochain sous carré
                sinon : 
                    regarder pour la ligne suivante.
                si on a atteint la Dt-ième ligne:
                    alors le carré est formé, renvoyer Dt.


    """

if __name__ == "__main__":
    dim = list(map(int, input().split()))
    #grid =  [list(map(int, input().split())) for i in range(dim[1])]
    
    grid = make_grid(dim[0], dim[1])
    pretty_grid = pretty_grid_maker(grid)
    for i in pretty_grid:
        print(*i, sep='  ')
    espace(grid, dim)
    
  