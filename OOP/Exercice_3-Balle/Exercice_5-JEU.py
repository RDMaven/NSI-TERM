import time
from tkinter import Label, IntVar, Tk, Canvas, Button
from math import cos, sin, radians
from random import randrange


###################################################################################
class Balle :
    """Création d'une balle à l'écran."""
    
    def __init__(self, zone, d:int, couleur:str, angle:int, vitesse:int, x=0, y=0):
        """
        Parametres
        ----------
        zone (class:canvas) : la zone de jeu.
        d : le diamètre de la balle.
        couleur : la couleure de la balle.
        angle ([20;360]) : angle de départ de la balle.
        vitesse : la vitesse de la balle.
        x,y : position de création de la balle.
        """
        
        # +-- Redefinition des parametres --+ #
        self.zoneJ = zone
        self.size = d
        self.angle = angle
        self.v = vitesse
        # +---------------------------------+ #

        # +-- Nouveaux attributs --+ #
        self.hauteurzoneJ = self.zoneJ.winfo_reqheight()
        self.largeurzoneJ = self.zoneJ.winfo_reqwidth()
        self.x = cos(radians(self.angle))
        self.y = sin(radians(self.angle))
        # +------------------------+ #

        # +-- Création balle --+ #
        self.balle = self.zoneJ.create_oval(x, y, x+d, y+d, fill=couleur, tag='balle')
        self.zoneJ.move(self.balle, self.largeurzoneJ/2, self.hauteurzoneJ/2)
        # +--------------------+ #


    def deplacer(self) :
        self.rebondir() # Pour les paroies (haut, gauche, droite) et raquette.
        self.zoneJ.detec_fin() # paroie du bas.

        self.zoneJ.move(self.balle, self.x*self.v, self.y*self.v) # deplacement
    
    def rebondir(self) :
                
        # +-- Paroies --+ #
        p_balle = self.get_position()
        touche_haut     = p_balle[1] <= 0
        touche_gauche   = p_balle[0] <= 0
        touche_droite   = p_balle[2] >= self.largeurzoneJ
        # +-------------+ #

        # +-- Raquette --+ #
        p_raquette = self.zoneJ.raquette.get_position()
        #milieu_raquette = self.zoneJ.raquette.longueur
        au_dessus = p_balle[0]+self.size > p_raquette[0] and p_balle[2]-self.size < p_raquette[2]
        meme_hauteur = p_balle[3] >= p_raquette[1]
        #dans_cote_gauche = p_balle[2] >= p_raquette[0] and p_balle[2] <= p_raquette[0] + milieu_raquette
        #dans_cote_droite = p_balle[0] <= p_raquette[2] and p_balle[0] >= p_raquette[2] - milieu_raquette

        touche_raquette = au_dessus and meme_hauteur
        # +--------------+ #
        
        # +-- Actions --+ #
        if touche_haut :
            self.y *= -1 
        if touche_gauche or touche_droite :
            self.x *= -1
        if touche_raquette :
            #print(p_raquette, p_balle)
            self.y *= -1
            #time.sleep(0.5)
            self.zoneJ.coords(self.balle, p_balle[0], p_raquette[1]-self.size, p_balle[2], p_raquette[1])
            #self.v = randrange(1,10,1)
            
            #self.zoneJ.update()
            #time.sleep(0.5)

        for brique in self.zoneJ.briques:
            brique_coord = brique.get_position()
            meme_hauteur_brique = p_balle[1] <= brique_coord[3]
            au_dessus_brique = p_balle[0]+self.size >= brique_coord[0] and p_balle[2]-self.size <= brique_coord[2]
            touche_brique = meme_hauteur_brique and au_dessus_brique

            if touche_brique:
                self.zoneJ.set_score(self.zoneJ.get_score()+1)
                brique.effacer()
                self.y = abs(self.y)
                
                break


        # +-------------+ #

    def get_position(self):
        return self.zoneJ.coords(self.balle)

# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= #
###################################################################################


###################################################################################
class Raquette:
    """Création d'une raquette à l'écran."""

    def __init__(self, zone, x, y, longueur:int, h):
        """
        Parametres
        ----------
        zone    (class:canvas) : la zone de jeu.
        x,y : position de création de la raquette.
        longueur : longueur de la raquette. 
        """

        # +-- Redefinition des parametres --+ #
        self.zoneJ = zone
        self.longueur = longueur
        self.height = h
        self.y = y
        # +---------------------------------+ #

        # +-- Création raquette --+ #
        self.raquette = self.zoneJ.create_rectangle(x, y, x+self.longueur, y+h)
        # +-----------------------+ #
        
        # +-- Association au curseur --+ #
        #self.zoneJ.bind('<Motion>', self.deplacer)
        # +----------------------------+ #


    def deplacer(self): # Déplacer la raquette selon la position du curseur.
        pos_raquette = self.get_position()
        #milieu_raquette = pos_raquette[0] + (self.longueur/2)
        p_balle = self.zoneJ.balle.get_position()

        self.zoneJ.coords(self.raquette, p_balle[0]-8, self.y, p_balle[2]+8, self.y+self.height)
        

    def get_position(self):
        return self.zoneJ.coords(self.raquette)

# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= #
###################################################################################


###################################################################################
class Brique:
    """Création d'une brique à l'écran."""

    def __init__(self, zone, x, y, l, h):
        """
        Parametres
        ----------
        zone    (class:canvas) : la zone de jeu.
        x,y : position de création de la raquette.
        """
        self.zoneJ = zone
        self.l = l
        self.x = x
        self.y = y
        self.brique = self.zoneJ.create_rectangle(x, y, x+self.l, y+h, tag=f'b-{x}-{y}', fill='red')

    def get_position(self):
        return self.zoneJ.coords(self.brique)
    
    def effacer(self):
        self.zoneJ.delete(f'b-{self.x}-{self.y}') #effacer l'élément à l'écran
        index = self.zoneJ.briques.index(self)  
        del self.zoneJ.briques[index] # le supprimer de la liste des briques
    
    def deplacer(self):
        self.zoneJ.move(self.brique, 0, 0.1) # deplacement


# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= #
###################################################################################


###################################################################################
class ZoneDeJeu(Canvas) :
    """Créer une zone de jeu, basé sur le Canvas de Tkinter."""

    def __init__(self, largeur:int, hauteur:int):
        """
        Parametres
        ----------
        largeur, hauteur : ...de la zone de jeu.
        """

        # +-- Initialisation Canvas --+ #
        Canvas.__init__(self, width = largeur, height = hauteur, bg='white')
        self.nbr_briques = 0
        # +---------------------------+ #
        
        self.debuter_partie()

        # +-- Création du jeu --+ #
        self.Game = True
        self.grid(row=0, column=0, columnspan=3)
        self.score = IntVar()
        # +---------------------+ #
    
    def creerBalle(self, size=16, couleur='red'):
        angle = randrange(45,135,30)
        vitesse = 5
        self.balle = Balle(self, size, couleur, angle, vitesse)
    
    def creerRaquette(self):
        x = self.winfo_reqwidth()/2 - 50
        y = self.winfo_reqheight() - 20
        self.raquette = Raquette(self, x, y, 10, 10)

    def creerBriques(self, l=50, h=10, columns=20):
        self.briques = []
        self.columns = columns
        self.l = self.winfo_reqwidth()//l
        for i in range(self.l):
            for j in range(self.columns):
                self.briques.append(Brique(self, l*i,j*h, l, h))
        
    def afficher_balle(self):
        if self.Game == True:    
            self.balle.deplacer()
            try : 
                self.raquette.deplacer()
            except :pass
            self.update()
            self.after(1, self.afficher_balle)

    def detec_fin(self):
        p_balle = self.balle.get_position()
        touche_bas = p_balle[3] >= self.winfo_reqheight()
        plus_de_briques = self.briques == []
        the_end = touche_bas or plus_de_briques

        if the_end:
            if touche_bas: message = f"Oh no ! Tu es mort... Points : {self.get_score()}"
            elif plus_de_briques: message = f'Bravo, tu as gagné. Points : {self.get_score()}'
            print(message)
            self.set_score(0)
            self.effacer()
            self.unbind("<Motion>")
            self.Game = False
        
    def debuter_partie(self):
        self.creerBalle()
        self.creerRaquette()
        self.jouer()

    def effacer(self):
        self.delete('balle')
        #self.delete('brique')

    def jouer(self):
        self.Game = True
        self.effacer()
        self.creerBalle()
        self.creerBriques()
        self.afficher_balle()
        #self.bind('<Motion>', self.raquette.deplacer)

    def get_score(self):
        return self.score.get()

    def set_score(self, val):
        self.score.set(val)

# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= #
###################################################################################


###################################################################################
class Application(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Jeu de balles")
        self.zoneJ = ZoneDeJeu(400, 400)
        #self.zoneJ2 = ZoneDeJeu(100, 300)
        self.btn_Q = Button(self, text = "Quitter", command = self.quitter)
        self.btn_P = Button(self, text = "Jouer", command = self.zoneJ.jouer)
        self.score = Label(self, textvariable=self.zoneJ.score)

        self.btn_Q.grid(row=1, column=0)
        self.btn_P.grid(row=1, column=1)
        self.score.grid(row=1, column=2)
        
    def quitter(self):
        self.destroy()
    
# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= #
###################################################################################

Application().mainloop()