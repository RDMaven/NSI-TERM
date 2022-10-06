import time
import random
from tabulate import tabulate


def pretty_print(list, head=['Nom', 'Sexe', 'Race', 'Année', "Age"]):
    print()
    print(tabulate(list, headers=head, tablefmt='orgtbl'))
    print()


chiens = []
class Chien:
    def __init__(self, nom, race, sexe, annee):
        """
        Params
        ----------
        nom : str(nom du chien)
        race : tuple (une seule race si le chien est pure race,
        deux ou plusieurs races dans le cas d'un croisement 
        les races sont des chaines de caactères)
        sexe : str("male" ou "femelle")
        annee : int(année de naissance du chien)
        """

        self._nom = nom
        self._race = race
        self._annee = annee
        self._sexe = sexe
        chiens.append(self)
    
    def nom(self):
        return self._nom
    
    def male_femelle(self):
        return self._sexe
    
    def race(self):
        return self._race
    
    def annee(self):
        return self._annee
    
    def age(self):
        today = time.gmtime().tm_year
        return today - self._annee

    def pure_race(self):
        return len(self._race) == 1
    
    def __str__(self):
        #tabulate([[self.nom(), self.male_femelle(), self.race(), self.annee(), self.age()]], headers=['Nom', 'Sexe', 'Race', 'Naissance', "Age"], tablefmt='orgtbl')
        return f"{self.nom()} ({self.male_femelle()}): {self.race()}. Naissance : {self.annee()} ({self.age()} ans)."
    

def nouveau_nom(chien1, chien2):
    nom1 = chien1.nom()
    nom2 = chien2.nom()

    return nom1[:round(len(nom1)/2)] + nom2[round(len(nom2)/2):] 

def bebe(chien1, chien2):
    name = nouveau_nom(chien1, chien2)
    rand_s = random.randint(1,2)
    if rand_s ==1: sexe = "male"
    else : sexe = "femelle"
    today = time.gmtime().tm_year
    nv_race = (chien2.race() + tuple(r for r in chien1.race() if r not in chien2.race()))
    return Chien(name, nv_race, sexe, today)

def compatible(chien1, chien2):
    compatible = False
    for race in chien1.race():
        if race in chien2.race(): compatible = True
    return compatible

def chercher_partenaires(chien, chiens):
    """
    Params
    -------
    chien : Chien(chien pour lequel on cherche un partenaire)
    chiens : list(liste de chiens (instances de Chien) dans laquelle on cherche un partenaire)

    Returns
    --------
    une liste d'instances de la classe Chien
    la liste renvoyée est la liste des partenaires possibles pour chien parmi la liste chiens
    Un parteaire est un chien de sexe opposé et 'compatible'
    """
    partenaires_particuliers = []
    for dog in chiens:
        if dog.male_femelle() != chien.male_femelle():
            if compatible(dog,chien):
                partenaires_particuliers.append(dog)
    return partenaires_particuliers




## Definition des OG dogs.##
medor     = Chien("Medor", ("Berger allemand",), "male", 2018)
loula     = Chien("Loula", ("Caniche","Cocker",), "femelle", 2019)
roberto   = Chien("Roberto", ("Caniche","Cocker","Berger allemand",), "male", 1875)
ricarda   = Chien("Ricarda", ("Cocker",), "femelle", 0)
eden      = Chien("Eden", ("Caniche","Cocker",), "femelle", 192)
ilestbeau = Chien("Ilestbeau", ("Caniche",), "male", 1929)
############################

## Print des OG dogs. ##
tableau = []
for ch in chiens:  tableau.append([ch.nom(), ch.male_femelle(), ch.race(), ch.annee(), ch.age()])
pretty_print(tableau)
########################


## Création des bébés. ##
bebes = []
bebes_n = []
for j in range(len(chiens)):
    for i in range(len(chiens)):
        if chiens[i] != chiens[j] and (nouveau_nom(chiens[i], chiens[j]) not in bebes_n):
            bebes.append(bebe(chiens[i], chiens[j]))
            bebes_n.append(nouveau_nom(chiens[i], chiens[j]))

#########################

## Print des bébés. ##
tableau = []
for ch in bebes:   tableau.append([ch.nom(), ch.male_femelle(), ch.race()])
pretty_print(tableau, ['Nom', 'Sexe', 'Race'])
######################


"""
partenaires = chercher_partenaires(bebes[1], chiens)
for i in partenaires:
    print(f"Partenaire {partenaires.index(i)+1} : {i.nom()}")

"""