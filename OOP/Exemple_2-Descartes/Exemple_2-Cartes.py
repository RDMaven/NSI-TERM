from tkinter import Tk, PhotoImage, Label

class Carte:
    """
    Class pour créer des cartes !
    
    -- Attributs --
    couleur (str)      : T (trefle), P (pique), C (coeur), K (carreau)
    hauteur (int, str) : 1-10 et 'Valet', 'Dame', 'Roi', 'As'
    valeur (str)       : pas identique à la hauteur.
    
    -- Méthodes --
    Getters : get_couleur, get_hauteur, get_valeur
    Setters : set_valeur
    image : obtenir l'image de la carte.
    est_superieur(autre) : comparer la carte à une autre.
    """

    def __init__(self, couleur, hauteur, valeur = 0):
        self.__couleur = couleur
        self.__hauteur = hauteur
        self.__valeur = valeur
        
        self.rebelotte = False

        if self.__valeur == 0: 
            valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Vallet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}
            self.__valeur = valeurs[str(self.__hauteur)]

    def get_couleur(self):
        return self.__couleur

    def get_hauteur(self):
        return self.__hauteur

    def get_valeur(self):
        return self.__valeur
    
    def set_valeur(self, new_val):
        if type(new_val) == int:
            self.__valeur = new_val
        else:
            raise TypeError("La valeur doit être un entier.")

    def __str__(self) -> str:
        hauteur = self.__hauteur
        if   self.__couleur == 'T' : couleur = 'Trefle'
        elif self.__couleur == 'K' : couleur = 'Carreau'
        elif self.__couleur == 'C' : couleur = 'Coeur'
        elif self.__couleur == 'P' : couleur = 'Pique'
        return f"{hauteur} de {couleur}"

    def image(self):
        fichier = "COO/Exemple_2-Descartes/carte/"+str(self.__valeur)+self.__couleur+".GIF"
        fenetre = Tk()
        fenetre.geometry('135x192+1000+400')
        image_carte = PhotoImage(file=fichier)
        label = Label(fenetre, image=image_carte)
        label.pack()
        fenetre.mainloop()

    def est_superieur(self, carte2):
        if self.__valeur > carte2.get_valeur():
            return f"Le {self.__str__()} est plus GRAND que le {carte2.__str__()}."
        elif self.__valeur < carte2.get_valeur():
            return f"Le {self.__str__()} est plus PETIT que le {carte2.__str__()}."
        else:
            return f"Le {self.__str__()} est de même valeur que le {carte2.__str__()}."


roi_carreau = Carte('K', 'Roi', 13)
#roi_carreau.image()
roi_carreauBis = Carte('K', 'Roi', 13)
roi_carreauTer = roi_carreau

print(type(roi_carreau))
print(roi_carreau)
print(roi_carreauBis)
print(roi_carreauTer)
print(f"Class Carte à l'addresse    : {hex(id(Carte))}")
print(f"roi_carreau à l'addresse    : {hex(id(roi_carreau))}")
print(f"roi_carreauBis à l'addresse : {hex(id(roi_carreauBis))}")
print(f"roi_carreauTer à l'addresse : {hex(id(roi_carreauTer))}")

roi_coeur = Carte('C', 'Roi', 13)
_2_pique = Carte('P', 2, 2)
as_trefle = Carte('T', 'As', 14)

#_2_pique.image()

print(as_trefle.est_superieur(_2_pique))
print(as_trefle.est_superieur(roi_carreau))
print(_2_pique.est_superieur(roi_coeur))

dame_pique = Carte('P', 'Dame')
print(dame_pique.get_valeur())