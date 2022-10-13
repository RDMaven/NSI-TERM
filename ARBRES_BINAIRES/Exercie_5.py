class Arbre_binaire:
    vide = None

    def __init__(self, valeur=None) -> None:
        self.__valeur = valeur
        self.__gauche = None
        self.__droite = None
        
    def __str__(self) -> str:
        """Renvoyer une chaine de charactère d'un tuple récursif représentant l'arbre."""
        return f'({self.get_valeur()}, {self.get_gauche()}, {self.get_droit()})'

    def get_gauche(self):
        """Renvoyer l'étiquette de l'enfant gauche."""
        return self.__gauche

    def get_droit(self):
        """Renvoyer l'étiquette de l'enfant droit."""
        return self.__droite

    def get_valeur(self):
        """Renvoyer l'étiquette de parent"""
        return self.__valeur

    def set_valeur(self, valeur):
        self.__valeur = valeur
    

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

    def parcours_largeur(self):
        file = [self]
        largeur = []
        while file:
            noeud1 = file.pop(0)
            if noeud1:
                largeur += noeud1.get_valeur()
                file.append(noeud1.get_gauche())
                file.append(noeud1.get_droit())                
        return largeur

    def parcours_prefixe(self):
        if not self:
            return []
        else:
            return [self.get_valeur()] + Arbre_binaire.parcours_prefixe(self.get_gauche()) + Arbre_binaire.parcours_prefixe(self.get_droit())

    def parcours_infixe(self):
        if not self:
            return []
        else: 
            return Arbre_binaire.parcours_infixe(self.get_gauche()) + [self.get_valeur()] + Arbre_binaire.parcours_infixe(self.get_droit())

    def parcours_postfixe(self):
        if not self:
            return []
        else: 
            return Arbre_binaire.parcours_postfixe(self.get_gauche()) + Arbre_binaire.parcours_postfixe(self.get_droit()) + [self.get_valeur()]

    def _ABR(self) -> bool:
        nombres = self.parcours_infixe()
        for i in range(len(nombres)-1) :
            if nombres[i] >= nombres[i+1]:
                return False
        return True
    
    """
    def _ABR(self):
        return self.parcours_infixe() == sorted(self.parcours_infixe())
    """
    
    def recherche(self, valeur):
        if not self:
            return f"{valeur} n'est pas dans l'arbre :("
        else:
            valeur_x = self.get_valeur()
            if valeur < valeur_x:
                return Arbre_binaire.recherche(self.get_gauche(), valeur)
            elif valeur > valeur_x:
                return Arbre_binaire.recherche(self.get_droit(), valeur)
            else:
                return f"{valeur} est dans l'arbre !"
    
    def ABR_max(self):
        if not self:
            return -1
        else:
            while self.get_droit() and self.get_droit().get_valeur():
                self = self.get_droit()
            return print(f"Maximum : {self.get_valeur()}")
    
    def ABR_min(self):
        if not self:
            return -1
        else:
            while self.get_gauche() and self.get_gauche().get_valeur():
                self = self.get_gauche()
            return print(f"Minimum : {self.get_valeur()}")
        

    def ABR_sorted(self, sortedlist):
        if len(sortedlist)==0: 
            return None
        
        mid=int(len(sortedlist)/2)
        
        self.__valeur=sortedlist[mid]
        
        Arbre_binaire.ABR_sorted(self.get_gauche(), sortedlist[:mid])
        Arbre_binaire.ABR_sorted(self.get_droit(),sortedlist[mid+1:])
        
        return self
    
   


def creer_ABR(list):
    ls = sorted(list)
    a = [(2**i) for i in range(0,10)]
    nodes_number = [sum(a[:i]) for i in range(len(a))]
    for i in nodes_number:
        if i >= len(list):
            cases = i
            break    
    if cases >= nodes_number[1]: # 1+
        arbre = Arbre_binaire(None)
        arbre.insert_gauche(None)
        arbre.insert_droit(None)
        if cases > nodes_number[2]: # 4+
            arbre.get_gauche().insert_gauche(None)
            arbre.get_gauche().insert_droit(None)
            arbre.get_droit().insert_gauche(None)
            arbre.get_droit().insert_droit(None)
            if cases > nodes_number[3]: # 7-14
                arbre.get_gauche().get_gauche().insert_gauche(None)
                arbre.get_gauche().get_gauche().insert_droit(None)
                arbre.get_gauche().get_droit().insert_gauche(None)
                arbre.get_gauche().get_droit().insert_droit(None)
                arbre.get_droit().get_gauche().insert_gauche(None)
                arbre.get_droit().get_gauche().insert_droit(None)
                arbre.get_droit().get_droit().insert_gauche(None)
                arbre.get_droit().get_droit().insert_droit(None)
                

    arbre.ABR_sorted(ls)

    return arbre
    

    

"""
racine = Arbre_binaire(50)
racine.insert_gauche(17)
noeud_g1 = racine.get_gauche()
noeud_g1.insert_gauche(9)
noeud_g1.insert_droit(23)

racine.insert_droit(76)
noeud_d1 = racine.get_droit()
noeud_d1.insert_gauche(54)

print(racine)
print(racine.parcours_infixe())
print(racine._ABR())
print(racine.recherche(50))

"""

arbre = creer_ABR([25,60,35,10,5,20,65,45,70,40,50,55,30,15])
print(f"Parcours infixe : {arbre.parcours_infixe()}")

print(arbre.recherche(70))
arbre.ABR_max()
arbre.ABR_min()
print(f"La hauteur de l'arbre est de {arbre.hauteur()}.")

from traceABnx import repr_graph
repr_graph(arbre)



