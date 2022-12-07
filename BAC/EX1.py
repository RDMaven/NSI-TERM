# Exercice 1 : Codage par différence.


def delta(tableau:list):
    """Compresse le tableau d'entrée par codage par différence?

    Args:
        tableau (list): liste d'entiers à compresser.

    Returns:
        _type_: liste des différences des valeurs.
    """

    
    assert tableau != [], 'Tableau vide'
    """
    if tableau == []:
        return
    """

    #Methode 1 :
    """
    tableau_delta = [tableau[0]]
    for i in range(1, len(tableau)-1):
        tableau_delta.append((tableau[i+1]-tableau[i]))

    return tableau_delta

    """

    #Méthode 2 :
    for i in range(len(tableau)-1, 0, -1):
        tableau[i] = tableau[i]-tableau[i-1]

    return tableau

print(delta([1000,800,802,1000,1003]))
print(delta([42]))
print(delta([]))
