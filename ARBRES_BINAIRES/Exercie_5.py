class Arbre_binaire:
    vide = None

    def __init__(self, valeur=None, i=0):
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
        self.__gauche = Arbre_binaire(valeur)
    def insert_droit(self, valeur):
        self.__droite = Arbre_binaire(valeur)
    
    def gauche_creation(self, valeur):
        self.__gauche= valeur
    def droite_creation(self, valeur):
        self.__droite= valeur

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
        

def creerABR(liste_noeuds:list[int]):

    racine  = Arbre_binaire(liste_noeuds[0])

    for noeud in liste_noeuds[1:]:
        sous_arbre = racine
        place=False

        while place==False:
                
            if noeud < sous_arbre.get_valeur():
                if sous_arbre.get_gauche() != None:
                    sous_arbre = sous_arbre.get_gauche()
                else:
                    place=True
                    sous_arbre.insert_gauche(noeud)
            else:
                if sous_arbre.get_droit() != None:
                    sous_arbre = sous_arbre.get_droit()
                else:
                    place=True
                    sous_arbre.insert_droit(noeud)
    return racine
            
    #pour chaque élément de la liste
        # tant que il est pas a la bonne place
            # prendre le sous arbre gauche si il est plus petit que le parent
            
            # prendre le sous arbre droit si il est plus grand que le parent
            
def creerABR_nul(liste_noeuds, indice=0):
    if len(liste_noeuds)-1 < indice:
        return
    racine  = Arbre_binaire(liste_noeuds[indice])
    if indice*2+1 < len(liste_noeuds):
        racine.gauche_creation(creerABR(liste_noeuds, (indice*2) + 1))
    if indice*2+2 < len(liste_noeuds):
        racine.droite_creation(creerABR(liste_noeuds, (indice*2) + 2))
    
    return racine
    
    """if len(liste_noeuds)==0: 
            return None
        print(valeurs)
        print(f'SELF : {self}')
        if self != None:
            self.__valeur=valeurs[0]
            self.insert_gauche(valeurs[1])
            self.insert_droit(valeurs[2])
           print(valeurs[0])
        
        mid=int(len(liste_noeuds)/2)
        
        self.__valeur=liste_noeuds[mid]
        
        Arbre_binaire.ABR_sorted(self.get_gauche(), liste_noeuds[:mid])
        Arbre_binaire.ABR_sorted(self.get_droit(),liste_noeuds[mid+1:])
    """
   


    


arbre = creerABR([25,60,35,10,5,20,65,45,70,40,50,55,30,15])
print(f"Parcours infixe : {arbre.parcours_infixe()}")

print(arbre.recherche(40))
arbre.ABR_max()
arbre.ABR_min()
print(f"La hauteur de l'arbre est de {arbre.hauteur()}.")

from traceABnx import repr_graph
repr_graph(arbre)
