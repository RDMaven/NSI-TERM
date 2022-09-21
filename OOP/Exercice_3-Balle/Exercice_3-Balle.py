from tkinter import Tk, Canvas, Button
from math import cos, sin, radians
from random import randrange
class Balle :

    def __init__(self, zone, d, couleur, angle, vitesse, x=0, y=0):
        self.zoneJ = zone
        self.balle = self.zoneJ.create_oval(x, y, x+d, y+d, fill=couleur)
        self.hauteurzoneJ = self.zoneJ.winfo_reqheight()
        self.largeurzoneJ = self.zoneJ.winfo_reqwidth()
        #print(self.hauteurzoneJ, self.largeurzoneJ)
        self.angle = angle
        self.v = vitesse
        self.x = cos(radians(self.angle))
        self.y = sin(radians(self.angle))
        self.zoneJ.move(self.balle, self.largeurzoneJ/2, self.hauteurzoneJ/2)

    def deplacer(self) :
        self.pos = self.zoneJ.coords(self.balle)
        if (self.pos[1] <= 0 or self.pos[3] >= self.hauteurzoneJ or self.pos[0] <= 0 or self.pos[2] >= self.largeurzoneJ):
            self.rebondir()
        self.zoneJ.move(self.balle, self.x*self.v, self.y*self.v) # deplacement

    def rebondir(self) :
        if self.pos[1] <= 0 or self.pos[3] >= self.hauteurzoneJ : # haut ou bas
            self.y = -self.y 
        if self.pos[0] <= 0 or self.pos[2] >= self.largeurzoneJ : #gauche ou droite
            self.x = -self.x
        #print(f'REBONDIR angle : {self.angle},\t position : {self.pos}')

    def get_position(self):
        return self.pos

class Raquette:
    
    def __init__(self, zone, x, y, longueur):
        self.zoneJ = zone
        self.raquette = self.zoneJ.create_rectangle(x, y, x+longueur, y+10)
        self.zoneJ.bind('<Motion>', self.deplacer)

        #print(self.hauteurzoneJ, self.largeurzoneJ)
        
    def deplacer(self, event):
        self.zoneJ.move(self.raquette, event.x-400, 0)

    def get_position(self):
        return self.zoneJ.coords(self.raquette)


class ZoneDeJeu(Canvas) :
    
    def __init__(self, largeur, hauteur):
        Canvas.__init__(self, width = largeur, height = hauteur, bg='white')
        self.pack()
        self.creerBalle()
        self.raquette = self.creerRaquette()
        self.bind('<Button-1>', self.autreBalle)
        self.afficher_balle()

    def rafraichir(self) :
        self.update()
    
    def creerBalle(self, size=16, couleur="red"):
        self.balle = Balle(self, size, couleur, randrange(20,360,30), 1) #zone, diamètre, couleur, vitesse
    
    def autreBalle(self, event):
        couleur = ['red', 'green', 'blue', 'black', 'yellow'][randrange(0,4)]
        x = event.x-(self.winfo_reqwidth())
        y = event.y-(self.winfo_reqheight())
        #print(x, y)
        self.balle2 = Balle(self, randrange(16,30,4), couleur, randrange(20,360,30), 1, x,2*y) #zone, diamètre, couleur, vitesse

    def creerRaquette(self):
        self.x = self.winfo_reqwidth()/2-50
        self.y = self.winfo_reqheight()-20

        self.raquette = Raquette(self, self.x, self.y, 100)

    def afficher_balle(self):
        self.balle.deplacer()
        try :self.balle2.deplacer()
        except: 
            #print("uwu maxinou")

            #print("aaaaaaaaaaaaaaaaaaaaaaa")
            pass
        self.rafraichir()
        self.after(1, self.afficher_balle)

    def detec_colision(self):
        print("aaa")
        pass

    def debuter_partie(self):
        pass

    def jouer(self):
        pass

class Application(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Jeu de balles")
        self.zoneJ = ZoneDeJeu(500, 400)
        #self.zoneJ2 = ZoneDeJeu(100, 300)
        self.btn = Button(self, text = "Quitter", command = self.quitter)
        self.btn.pack(padx=5, pady=5)

        self.score = 0
        
    def quitter(self):
        self.destroy()
    
    def get_score(self):
        return self.score/3

    def set_score(self, ajout):
        self.score += ajout


    
Application().mainloop()