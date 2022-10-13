class Arbre_binaire:
    vide = None

    def __init__(self, valeur=None) -> None:
        self.__valeur = valeur
        self.__gauche = Arbre_binaire.vide
        self.__droite = Arbre_binaire.vide
        
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
            return False
        else:
            valeur_x = self.get_valeur()
            if valeur < valeur_x:
                return Arbre_binaire.recherche(self.get_droit(), valeur)
            elif valeur > valeur_x:
                return Arbre_binaire.recherche(self.get_gauche(), valeur)
            else:
                return True
    
    def ajout_infixe(self, list, i=0):
        if not self:
            return []
        else: 
            print(i)
            i += 1
            Arbre_binaire.ajout_infixe(self.get_gauche(), list, i) 
            print(True)
            try : 
                self.set_valeur(list[i])
            except:
                self.set_valeur(None)
            print(self.get_valeur())
            [self.get_valeur()] 
            i += 1
            
            Arbre_binaire.ajout_infixe(self.get_droit(), list, i)
            

            #return Arbre_binaire.ajout_infixe(self.get_gauche()) + [self.get_valeur()] + Arbre_binaire.ajout_infixe(self.get_droit())


def creer_ABR(list):
    list = sorted(list)
    a = [(2**i) for i in range(0,10)]
    b = [sum(a[:i]) for i in range(len(a))]
    for i in b:
        if i >= len(list):
            cases = i
            break
    
    arbre = Arbre_binaire(4)
    if i >= 3:
        arbre.insert_gauche(2)
        arbre.insert_droit(6)
        if i >= 7:
            arbre.get_gauche().insert_gauche(1)
            arbre.get_gauche().insert_droit(3)
            arbre.get_droit().insert_gauche(5)
            arbre.get_droit().insert_droit(7)

    arbre.ajout_infixe(list)  
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

arbre = creer_ABR([1,2,3,4,5])

"""print(arbre.parcours_infixe())
arbre.ajout_infixe()
print(arbre.parcours_infixe())
"""

print(arbre.parcours_infixe())
