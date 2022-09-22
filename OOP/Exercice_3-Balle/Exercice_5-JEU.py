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
        self.balle = self.zoneJ.create_oval(x, y, x+d, y+d, fill=couleur)
        self.zoneJ.move(self.balle, self.largeurzoneJ/2, self.hauteurzoneJ/2)
        # +--------------------+ #


    def deplacer(self) :
        self.rebondir() # Pour les paroies (haut, gauche, droite) et raquette.
        self.zoneJ.detec_colision() # paroie du bas.

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
            self.y *= -1
            self.zoneJ.set_score()
        """if meme_hauteur and (dans_cote_droite or dans_cote_gauche):
            self.zoneJ.detec_colision(True)"""

        # +-------------+ #

    def get_position(self):
        return self.zoneJ.coords(self.balle)

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
        largeur, hauteur : ...de la zone de jeu.
        """

        # +-- Initialisation Canvas --+ #
        Canvas.__init__(self, width = largeur, height = hauteur, bg='white')
        # +---------------------------+ #
        
        self.debuter_partie()

        # +-- Création du jeu --+ #
        self.Game = True
        self.pack()
        self.score = IntVar()
        # +---------------------+ #
    
    def creerBalle(self, size=16, couleur='red'):
        angle = randrange(45,135,30)
        vitesse = 2
        self.balle = Balle(self, size, couleur, angle, vitesse)
    
    def creerRaquette(self):
        x = self.winfo_reqwidth()/2 - 50
        y = self.winfo_reqheight() - 20
        self.raquette = Raquette(self, x, y, 100)

    def afficher_balle(self):
        self.balle.deplacer()
        self.update()
        self.after(10, self.afficher_balle)

    def detec_colision(self, hack=False):
        if not hack :
            p_balle = self.balle.get_position()
            if p_balle[3] >= self.winfo_reqheight():
                print("Décès.")
                self.effacer()
                self.unbind("<Motion>")
        """else :
            print("ACKER.")
            self.effacer()
            self.unbind("<Motion>")"""
        
    def debuter_partie(self):
        self.creerBalle()
        self.creerRaquette()
        self.jouer()

    def effacer(self):
        self.delete(self.balle.balle)
        del self.balle

    def jouer(self):
        self.effacer()
        self.creerBalle()
        self.afficher_balle()
        self.bind('<Motion>', self.raquette.deplacer)

    def get_score(self):
        return self.score.get()

    def set_score(self):
        self.score.set(self.get_score()+1)

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
        self.score = Label(self, textvariable=self.zoneJ.score)

        self.btn_Q.pack(padx=0, pady=0)
        self.btn_P.pack(padx=5, pady=5)
        self.score.pack()
        
    def quitter(self):
        self.destroy()
    
# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= #
###################################################################################

Application().mainloop()