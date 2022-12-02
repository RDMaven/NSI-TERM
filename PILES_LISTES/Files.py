

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



class File2:
    def __init__(self):
        """"Crée une file vide"""
        self.__valeurs = []
        self.__nbval = 0

    def est_vide(self):
        """Renvoie True si la pile est vide, False sinon"""
        return self.__nbval == 0

    def enfile(self, e):
        """Ajoute l'élément e à droite de la file"""
        self.__valeurs.append(e)
        self.__nbval += 1
    
    def defile(self):
        """Retire et renvoie l'élément de gauche de la
        file si elle est non vide"""
        assert not(self.est_vide()), "file vide !"
        self.__nbval -= 1
        return self.__valeurs.pop(0)

    def lireTete(self):
        """lire la valeur à droite de la file"""
        assert not(self.est_vide()), "file vide !"
        return self.__valeurs[-1]

    def __str__(self):
        return f"la file contient {self.__nbval} valeurs : {self.__valeurs}"


f = File2()
f.est_vide()
f.enfile(5)
f.enfile(6)
f.enfile(1)
f.defile()
f.lireTete()
f.defile()
f.enfile(7)
f.lireTete()
f.defile()
f.est_vide()



class File:

    def __init__(self) -> None:
        self.__entree = Pile()
        self.__sortie = Pile()

    def est_vide(self):
        return self.__entree.est_vide() and self.__sortie.est_vide()

    def enfile(self, e):
        self.__entree.empiler(e)

    def defile(self):
        if self.__sortie.est_vide():
            while not self.__entree.est_vide():
                e = self.__entree.lire()
                self.__entree.deplier()
                self.__sortie.empiler(e)
        self.__sortie.deplier()

    def lireTete(self):
        assert not(self.est_vide()), "file vide !"
        if self.__entree.est_vide():
            return self.__sortie.lire()
        else: 
            return self.__entree.lire()

    def getEtat(self):
        return print(self.__entree.getPile(), self.__sortie.getPile())




f = File()
f.est_vide()
f.enfile(5)
f.enfile(6)
f.enfile(1)
f.defile()
f.lireTete()
f.defile()
f.enfile(7)
f.lireTete()
f.defile()
f.est_vide()
f.getEtat()