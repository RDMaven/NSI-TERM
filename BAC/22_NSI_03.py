class Noeud:
    """ Arbre binaire pour les expressions arithmétiques.
    """
    def __init__(self, g, v, d):
        """ Initialisation de l'arbre.

        Args:
            g (Noeud): Fils gauche
            v (str): Valeur de la racine.
            d (Noeud): Fils droit.
        """
        self.gauche = g
        self.valeur = v
        self.droit = d
    

    def __str__(self):
        return str(self.valeur)
    

    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None


def expression_infixe(e:Noeud):
    """ Créé l'expression arithmétique représentée par l'arbre binaire.

    Args:
        e (Noeud): Arbre binaire créé apr Noeud.

    Returns:
        str: l'expression arithmétique.
    """

    '''s = ''
    if e.gauche is not None:
        s = s + expression_infixe(e.gauche)
    
    if e.valeur is not None:
        s = s + str(e.valeur)

    if e.droit is not None:
        s = s + expression_infixe(e.droit)
    
    if e.est_une_feuille():
        return s
    
    return '(' + s + ')'
    '''
    
    ###########
    
    s = ''
    if e.gauche is not None:
        s = '('
        s = s + expression_infixe(e.gauche)
    
    if e.valeur is not None:
        s = s + str(e.valeur)

    if e.droit is not None:
        s = s + expression_infixe(e.droit)
        s += ')'
    
    return s



e = Noeud(Noeud(Noeud(None, 3, None), '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))), '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))
print(expression_infixe(e))