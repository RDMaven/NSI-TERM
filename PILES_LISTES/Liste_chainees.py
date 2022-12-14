
class Cellule:

    def __init__(self, x, suivant=None) -> None:
        self.val = x
        self.suivant = suivant


class ListChainee:
    def __init__(self) -> None:
        self.premier = None

    def est_vide(self):
        return self.premier == None
    
    def ajouter(self, x):
        if self.est_vide():
            self.premier = Cellule(x, self.premier)
        else:
            element = self.premier
            while element.suivant is not None:
                element = element.suivant
            element.suivant = Cellule(x)
    
    def longueur(self):
        assert not self.est_vide(), "VIDE"
        element = self.premier
        l = 1
        while element.suivant is not None:
            element = element.suivant
            l +=1
        return l

    def n_val(self,n):
        assert not self.est_vide(), "VIDE"
        assert n <= self.longueur(), "Impossible."
        
        element = self.premier
        i = 1
        
        while element.suivant is not None and n != i:
            element = element.suivant
            i +=1
        return element.val
        

import random
malist = ListChainee()
for i in range(1,100):
    e = random.randrange(1,100)
    malist.ajouter(e)
malist.ajouter(2)
malist.ajouter(4)
malist.ajouter(6)
malist.ajouter(8)
print(malist.longueur())
print(malist.n_val(4))
