from ast import Delete
from tkinter import Tk, Canvas, Button
from math import cos, sin, radians
from random import randrange
class Balle :

    def __init__(self, zone, d, couleur, angle, vitesse, x=0, y=0, tag="balle"):
        self.zoneJ = zone
        self.balle = self.zoneJ.create_oval(x, y, x+d, y+d, fill=couleur, tag=tag)
        self.hauteurzoneJ = self.zoneJ.winfo_reqheight()
        self.largeurzoneJ = self.zoneJ.winfo_reqwidth()
        #print(self.hauteurzoneJ, self.largeurzoneJ)
        self.angle = angle
        self.v = vitesse
        self.x = cos(radians(self.angle))
        self.y = sin(radians(self.angle))
        self.zoneJ.move(self.balle, self.largeurzoneJ/2, self.hauteurzoneJ/2)

        self.zoneJ.nbr_balle += 1

    def deplacer(self) :
        self.pos = self.zoneJ.coords(self.balle)
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


class ZoneDeJeu(Canvas) :
    
    def __init__(self, largeur, hauteur):
        Canvas.__init__(self, width = largeur, height = hauteur, bg='white')
        self.pack()
        self.balle = [None]
        self.nbr_balle = 0
        self.creerBalle()
        self.bind('<Button-1>', self.autreBalle)
        self.afficher_balle()

    def rafraichir(self) :
        self.update()
   
    def creerBalle(self, size=16, couleur="red"):
        self.balle[0] = Balle(self, size, couleur, randrange(20,360,30), 5) #zone, diamètre, couleur, vitesse

    def autreBalle(self, event):
        #self.delete('autre')
        couleur = ['red', 'green', 'blue', 'black', 'yellow', 'pink', 'purple'][randrange(0,7)]
        x = event.x-(self.winfo_reqwidth())/2-15
        y = event.y-(self.winfo_reqheight())/2-15
        #print(x, y)
        self.balle.append(Balle(self, randrange(16,30,4), couleur, randrange(20,360,30), 5, x,y, tag='autre')) #zone, diamètre, couleur, vitesse
        
    def afficher_balle(self):
        for i in range(self.nbr_balle):
            self.balle[i].deplacer()
        self.rafraichir()
        self.after(10, self.afficher_balle)
        

class Application(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Jeu de balles")
        self.zoneJ = ZoneDeJeu(300, 300)
        #self.zoneJ2 = ZoneDeJeu(100, 300)
        self.btn = Button(self, text = "Quitter", command = self.quitter)
        self.btn.pack(padx=5, pady=5)
         
    def quitter(self):
        self.destroy()
        
Application().mainloop()