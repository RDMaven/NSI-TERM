def ligne(nb_ligne:int, symb='X', fill=True):
    if fill:
        return symb*nb_ligne
    else:
        return symb +' '*(nb_ligne-2) + symb

def rectangle(nb_lignes:int, nb_colonnes:int, symb="#"):
    if nb_lignes == 1 and nb_colonnes == 1:
        return symb
    if nb_lignes == 1:
        return ligne(nb_colonnes, symb=symb)
    if nb_colonnes == 1:
        return (symb + '\n')*(nb_lignes-1) + symb
    filled = ligne(nb_colonnes, symb=symb)
    spaced = ligne(nb_colonnes, symb=symb, fill=False)
    
    return filled + '\n' + (spaced + '\n')*(nb_lignes-2) + filled

def triangle(cote_tri:int,symb='@'):
    
    if cote_tri == 0:
        return ''
    elif cote_tri == 1:
        return symb
    r = symb + '\n'
    for l in range(2,cote_tri):
        r += (ligne(l, symb=symb, fill=False) + '\n')
    r += ligne(cote_tri, symb=symb)
    return r

if __name__ == "__main__":
    nb_ligne_x = int(input())
    nb_rectangle_l = int(input())
    nb_rectangle_c = int(input())
    nb_triangle = int(input())

    print(ligne(nb_ligne_x))
    print()
    print(rectangle(nb_rectangle_l, nb_rectangle_c))
    print()
    print(triangle(nb_triangle))
    
    