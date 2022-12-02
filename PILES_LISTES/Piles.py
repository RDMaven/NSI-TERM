

class Pile:

    def __init__(self) -> None:
        self.__pile = []
        self.__nbval = 0

    def empiler(self, element):
        self.__pile.append(element)
        self.__nbval +=1
    
    def deplier(self):
        assert not self.est_vide(), "Pile vide."
        self.__pile.pop()
        self.__nbval -= 1
    
    def lire(self):
        return self.__pile[-1]
    
    def est_vide(self):
        return self.__nbval == 0
    
    def obtenir(self):
        return len(self.__pile)

    def getPile(self):
        return self.__pile

p = Pile()
p.est_vide()
p.empiler(5)
p.empiler(6)
p.empiler(1)
p.deplier()
p.lire()
p.deplier()
p.empiler(7)
p.lire()
p.deplier()
p.est_vide()

