from tkinter import Tk, Canvas, Button

class Balle :

    def __init__(self, zone, d, couleur):
        self.zoneJ = zone
        self.balle = self.zoneJ.create_oval(0, 0, d, d, fill=couleur)
        self.hauteurzoneJ = self.zoneJ.winfo_reqheight()
        self.largeurzoneJ = self.zoneJ.winfo_reqwidth()
        self.x = 0
        self.y = -1
        self.zoneJ.move(self.balle, self.largeurzoneJ/2,
        self.hauteurzoneJ/2)

    def deplacer(self) :
        self.pos = self.zoneJ.coords(self.balle)
        if (self.pos[1] <= 0 or self.pos[3] >= self.hauteurzoneJ or self.pos[0] <= 0 or self.pos[2] >= self.largeurzoneJ):
            self.rebondir()
        self.zoneJ.move(self.balle, self.x, self.y) # deplacement

    def rebondir(self) :
        if self.pos[1] <= 0 or self.pos[3] >= self.hauteurzoneJ : # haut ou bas
            self.y = -self.y
        if self.pos[0] <= 0 or self.pos[2] >= self.largeurzoneJ : #gauche ou droite
            self.x = -self.x


class ZoneDeJeu(Canvas) :
    
    def __init__(self, largeur, hauteur):
        Canvas.__init__(self, width = largeur, height = hauteur,
        bg='white')
        self.pack()
        self.creerBalle()
    
    def rafraichir(self) :
        self.update()
    
    def creerBalle(self):
        self.balle = Balle(self, 16, 'red') #zone, diamètre, couleur
        self.afficher_balle()
    
    def afficher_balle(self):
        self.balle.deplacer()
        self.rafraichir()
        self.after(10, self.afficher_balle)


class Application(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Jeu de balles")
        self.zoneJ = ZoneDeJeu(200, 300)
        #self.zoneJ2 = ZoneDeJeu(100, 300)
        self.btn = Button(self, text = "Quitter", command = self.quitter)
        self.btn.pack(padx=5, pady=5)
    
    def quitter(self):
        self.destroy()

Application().mainloop()