from tkinter import Tk, Canvas, Button
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
        #self.zoneJ.detec_colision() # paroie du bas.
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
        au_dessus = p_balle[0]+self.size > p_raquette[0] and p_balle[2]-self.size < p_raquette[2]
        meme_hauteur = p_balle[3] >= p_raquette[1]
        touche_raquette = au_dessus and meme_hauteur
        # +--------------+ #
        
        # +-- Actions --+ #
        if touche_haut :
            self.y *= -1 
        if touche_gauche or touche_droite :
            self.x *= -1
        if touche_raquette :
            self.y *= -1
        # +-------------+ #

    def get_position(self):
        return self.zoneJ.coords(self.balle)

    def effacer(self):
        self.zoneJ.delete("all")

# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= #
###################################################################################


###################################################################################
class Raquette:
    """Création d'une raquette à l'écran."""

    def __init__(self, zone, x, y, longueur:int):
        """
        Parametres
        ----------
        zone    (class:canvas) : la zone de jeu.
        x,y : position de création de la raquette.
        longueur : longueur de la raquette...
        """

        # +-- Redefinition des parametres --+ #
        self.zoneJ = zone
        self.longueur = longueur
        # +---------------------------------+ #

        # +-- Création raquette --+ #
        self.raquette = self.zoneJ.create_rectangle(x, y, x+self.longueur, y+10)
        # +-----------------------+ #
        
        # +-- Association au curseur --+ #
        self.zoneJ.bind('<Motion>', self.deplacer)
        # +----------------------------+ #


    def deplacer(self, event): # Déplacer la raquette selon la position du curseur.
        pos_raquette = self.get_position()
        milieu_raquette = pos_raquette[0] + (self.longueur/2)
        self.zoneJ.move(self.raquette, event.x-milieu_raquette, 0)
        
    def get_position(self):
        return self.zoneJ.coords(self.raquette)

# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= #
###################################################################################


###################################################################################
class ZoneDeJeu(Canvas) :
    """Créer une zone de jeu, basé sur le Canvas de Tkinter."""

    def __init__(self, largeur:int, hauteur:int):
        """
        Parametres
        ----------
        largeur : ...de la zone de jeu.
        hauteur : ...de la zone de jeu.
        """

        # +-- Initialisation Canvas --+ #
        Canvas.__init__(self, width = largeur, height = hauteur, bg='white')
        # +---------------------------+ #
        
        # +-- Création du jeu --+ #
        self.Game = True
        self.pack()
        self.creerBalle()
        self.creerRaquette()
        self.afficher_balle()
        # +---------------------+ #
    
    
    def creerBalle(self, size=16, couleur='red'):
        angle = randrange(45,135,30)
        vitesse = 5
        self.balle = Balle(self, size, couleur, angle, vitesse)
    
    def creerRaquette(self):
        x = self.winfo_reqwidth()/2 - 50
        y = self.winfo_reqheight() - 20
        self.raquette = Raquette(self, x, y, 100)

    def afficher_balle(self):
        if self.Game == True :
            self.balle.deplacer()
            self.update()
            self.after(10, self.afficher_balle)
        
    def detec_colision(self):
        p_balle = self.coords(self.balle)
        if p_balle[3] >= self.winfo_reqheight():
            self.balle.x = 0
            self.balle.y = 0
            print("Jusqu'au décès comme on dit hein, voila.")
            self.Game = False
            self.balle.effacer()
            self.raquette.unbind("<Motion>")
        
    def debuter_partie(self):
        pass

    def jouer(self):
        self.creerBalle()
        self.creerRaquette()
        self.bind('<Motion>', self.raquette.deplacer)

        print(self.balle.Game)
        # reset position balle
        # reset score
        # reset vitesse
        # set to True the game variable
        pass

# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= #
###################################################################################


###################################################################################
class Application(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Jeu de balles")
        self.zoneJ = ZoneDeJeu(300, 300)
        #self.zoneJ2 = ZoneDeJeu(100, 300)
        self.btn_Q = Button(self, text = "Quitter", command = self.quitter)
        self.btn_P = Button(self, text = "Jouer", command = self.zoneJ.jouer)

        self.btn_Q.pack(padx=5, pady=10)
        self.btn_P.pack(padx=5, pady=5)

        self.score = 0
        
    def quitter(self):
        self.destroy()
    
    def get_score(self):
        return self.score

    def set_score(self, ajout):
        self.score += ajout

# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= #
###################################################################################

Application().mainloop()