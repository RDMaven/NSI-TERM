
class CompteBancaire:
    """Classe compte bancaire normal"""
    #variable partagée par tous les objets de cette classe
    nb_compte = 0
    
    def __init__(self, nom, type="Compte normal", solde=0.0):
        #attributes, unique pour chaque objet
        self.__nom = nom
        self.__solde = solde
        self.__type = type
        CompteBancaire.nb_compte += 1

    #Méthodes de l'objet :
    def lire_solde(self):
        return self.__solde
    
    def retrait(self, montant):
        self.__solde -= montant
    
    def depot(self, montant):
        self.__solde += montant
        

class CompteEtudiant(CompteBancaire):
    def __init__(self, nom):
        super().__init__(nom, type="Compte étudiant", solde=50.0)


class CompteEpargne(CompteBancaire):
    def __init__(self, nom, solde=0.0):
        CompteBancaire.__init__(self, nom, "Compte épargne", solde)
        self.interet = 0.3
        self.__solde = solde

    
    def changer_taux(self, taux):
        self.interet = taux
    
    def capitalise(self, nombre_mois = 6):
        self.__solde = self.lire_solde()
        for m in range(nombre_mois):
            self.__solde = self.__solde*(1+self.interet/100)
        print(f"Sur {nombre_mois} mois (taux de {self.interet} %) : {round(self.__solde)}$.")

compte1 = CompteEpargne("Timoto", 100)
compte1.depot(650)
compte1.lire_solde()

compte1.capitalise(12)
compte1.changer_taux(0.5)
compte1.capitalise(6)

compte1.lire_solde()

#print(dir(compte1))