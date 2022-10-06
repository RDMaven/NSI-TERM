class Arbre_binaire:
    vide = None

    def __init__(self, valeur) -> None:
        self.__valeur = valeur
        self.__gauche = Arbre_binaire.vide
        self.__droite = Arbre_binaire.vide
        
    def __str__(self) -> str:
        """Renvoyer une chaine de charactère d'un tuple récursif représentant l'arbre."""
        return f'({self.__valeur}, {self.__gauche}, {self.__droite})'

    def get_gauche(self):
        """Renvoyer l'étiquette de l'enfant gauche."""
        return self.__gauche

    def get_droit(self):
        """Renvoyer l'étiquette de l'enfant droit."""
        return self.__droite

    def get_valeur(self):
        """Renvoyer l'étiquette de parent"""
        return self.__valeur

    def insert_gauche(self, valeur):
        if self.__gauche == Arbre_binaire.vide:
            self.__gauche = Arbre_binaire(valeur)
        else :
            new_node = Arbre_binaire(valeur)
            new_node.__gauche
            self.__gauche = new_node
        
    def insert_droit(self, valeur):
        if self.__droite == Arbre_binaire.vide:
            self.__droite = Arbre_binaire(valeur)
        else :
            new_node = Arbre_binaire(valeur)
            new_node.__droite
            self.__droite = new_node

    def taille(self):
        if not self: return 0
        return 1 + Arbre_binaire.taille(self.__gauche) + Arbre_binaire.taille(self.__droite)
        
    def hauteur(self):
        if not self:
            return -1
        return 1 + max(Arbre_binaire.hauteur(self.__gauche), Arbre_binaire.hauteur(self.__droite))

        
    """
    p = '('
    g = f"{self.__gauche}"
    d = f"{self.__droite}"
    p_gauche = [i for i in g if i in p]
    p_droite = [i for i in d if i in p] 

    if len(p_gauche) < len(p_droite):return len(p_droite)-1
    else : return len(p_gauche)-1
    """

racine = Arbre_binaire("A")
racine.insert_gauche("B")
noeud_b = racine.get_gauche()
noeud_b.insert_gauche("D")
noeud_b.insert_droit("E")

noeud_e = noeud_b.get_droit()
noeud_e.insert_gauche('G')

racine.insert_droit("C")
noeud_c = racine.get_droit()
noeud_c.insert_droit("F")
print(racine)

print(racine.taille())
print(racine.hauteur())