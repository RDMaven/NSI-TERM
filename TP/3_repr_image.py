
# +-----+ Partie 1 : Init +-----+ #
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
filein = "./TP/dino.jpg"
img_origin = mpimg.imread(filein)
larg = len(img_origin)
haut = len(img_origin[0])
print(f"l'image est de largeur {larg} et de hauteur {haut}")

"""
print(img_origin)
fig1 = plt.figure()
ax = fig1.add_subplot(1, 1, 1)
ax.imshow(img_origin)
plt.show()
"""
# +-----------------------------+ #
# +-----------------------------+ #



# +-----+ Partie 2 : découpe4 +-----+ #
def decoupe4(img_origin):
    dimg = np.array_split(img_origin, 2)
    nord = np.hsplit(dimg[0], 2)
    sud = np.hsplit(dimg[1], 2)

    return nord[0], nord[1], sud[0], sud[1]

print("=================")

"""
img_no, img_ne, img_so, img_se = decoupe4(img_origin)
print(img_no[0])


fig2 = plt.figure()
ax1 = fig2.add_subplot(2, 2, 1)
ax2 = fig2.add_subplot(2, 2, 2)
ax4 = fig2.add_subplot(2, 2, 4)
ax3 = fig2.add_subplot(2, 2, 3)

ax1.imshow(img_no)
ax2.imshow(img_ne)
ax3.imshow(img_se)
ax4.imshow(img_so)

plt.show()
"""
# +-----------------------------+ #
# +-----------------------------+ #



# +-----+ Partie 3 : assemble4 +-----+ #
def assemble4(img_no, img_ne, img_so, img_se):
    nord = np.concatenate((img_no, img_ne), axis=1)
    sud = np.concatenate((img_so,img_se), axis=1)
    return np.concatenate((nord, sud), axis=0)
    
"""
img = assemble4(img_no, img_ne, img_so, img_se)

print(img)
fig3 = plt.figure()
ax = fig3.add_subplot(1, 1, 1)
ax.imshow(img)
plt.show()
"""
# +-----------------------------+ #
# +-----------------------------+ #



# +-----+ Partie 4 : moy_pix +-----+ #
def moy_pix(img):
    return [round(c) for c in np.mean(img, axis=(0,1))]
    # return np.mean(img, axis=(0,1), dtype=int)

#print(moy_pix(img_no))
#print(moy_pix(img_ne))
#print(moy_pix(img_se))
#print(moy_pix(img_so))

"""
imgh = np.concatenate(([moy_pix(img_no)], [moy_pix(img_ne)]), axis=0)
imgb = np.concatenate(([moy_pix(img_so)], [moy_pix(img_se)]), axis=0)
img = np.concatenate(([imgh], [imgb]), axis=0)
fig4 = plt.figure()
ax = fig4.add_subplot(1, 1, 1)
ax.imshow(img)
plt.show()
"""

# +-----------------------------+ #
# +-----------------------------+ #



# +-----+ Partie 5 : qarbre +-----+ #
class Qarbre():
    id=0
    def __init__(self, img, prof=0):
        self.val = img
        
        self.no = None
        self.ne = None
        self.so = None
        self.se = None
        
        self.prof = prof      
        self.construire()
        self.couleur = moy_pix(img)
        Qarbre.id += 1
        self.id = Qarbre.id
        
    def __str__(self):
        """Renvoie une chaine de caractère d'un tuple récursif représentant 
            l'arbre"""
        return f'({self.id},{self.couleur[0]},{self.couleur[1]},{self.couleur[2]},{self.no},{self.ne},{self.so},{self.se})'
    
    #Complété#
    def insert_no(self, valeur, prof=1):
        self.no = Qarbre(valeur, prof)
        
    def insert_ne(self, valeur, prof=1):
        self.ne = Qarbre(valeur, prof)
    
    def insert_so(self, valeur, prof=1):
        self.so = Qarbre(valeur, prof)
    
    def insert_se(self, valeur, prof=1):
        self.se = Qarbre(valeur, prof)
    
    def hauteur(self):
        """Obtenir la hauteur de l'arbre.
        """
        if not self:
            return -1
        return 1 + max(Qarbre.hauteur(self.no), Qarbre.hauteur(self.ne),Qarbre.hauteur(self.so), Qarbre.hauteur(self.se))

    
    def est_feuille(self):
        """Déterminer si le noeud est une feuille.
        Returns:
            bool : est-ce une feuille ?
        """
        #Si c'est une feuille
        return not (self.no or self.ne or self.so or self.se)
    #Fin complété#
    
    def conv2tuple(self):
        arbre = self.__str__()
        return eval(arbre)
       
    def trace_arbre(self):
        dim = 10
        plt.figure(figsize=(dim, dim))
        dl = dim*80
        dh = dim*80
        pad = dim*0
        plt.axis([0, dl, 0, dh])
        #plt.axis('off')
        abr = self.conv2tuple()
        self.affiche(abr, dl-pad, dh-pad, pad, pad)
        plt.show()

    def noeud(self, x0, y0, r, txt, coul):
        x = np.linspace(0, 2*np.pi, 100)
        x1 = r*np.cos(x)
        x2 = r*np.sin(x)
        coul = [c/255 for c in coul]
        plt.fill(x0+x1, y0+x2, facecolor=coul, edgecolor='purple', linewidth=2)
        plt.text(x0, y0, str(txt), fontsize=8, ha='center', va='center')

    def branche(self, x0, y0, x1, y1):
        plt.plot([x0,x1], [y0,y1], color='pink')

    def affiche(self, abr, dl, dh, x0, y0):
        if abr == None:
            return
        ida, r, v, b, no, ne, so, se = abr  #INVERSER SE ET SO POUR AVOIR LE BON ORDRE
        coul = [r, v, b]
        rn = 20 # rayon du noeud
        dx = dl / 4
        y = (self.hauteur()+1)
        dy = dh/y
        self.noeud(x0+2*dx, dh-y0-dy/2, rn, ida, coul)
        if no != None:
            self.branche(x0+2*dx, dh-y0-dy/2, x0+dx/2, dh-y0-3*dy/2)
        if ne != None:
            self.branche(x0+2*dx, dh-y0-dy/2, x0+3*dx/2, dh-y0-3*dy/2)
        if so != None:
            self.branche(x0+2*dx, dh-y0-dy/2, x0+5*dx/2, dh-y0-3*dy/2)
        if se != None:
            self.branche(x0+2*dx, dh-y0-dy/2, x0+7*dx/2, dh-y0-3*dy/2)
        Qarbre.affiche(self, no, dl/4, dh, x0, dy+y0)
        Qarbre.affiche(self, ne, dl/4, dh, x0+dx, dy+y0 )
        Qarbre.affiche(self, so, dl/4, dh, x0+2*dx, dy+y0)
        Qarbre.affiche(self, se, dl/4, dh, x0+3*dx, dy+y0)    

# P 7 : génération de l'arbre image

    def construire(self):   
        if uni_pix(self.val) == False: # Si la couleur est unique (deux couleurs sont différentes)
            for i in ["ne", "no", "so", "se"]:
                no, ne, so, se = decoupe4(self.val)
                eval(f"self.insert_{i}({i}, self.prof+1)")
                eval(f"Qarbre.construire(self.{i})")
        else: # Si la couleur est répétée pour tout les pixels,
            return self.val


    def get_image(self):
        if self.est_feuille():
            return np.tile(self.couleur, [len(self.val), len(self.val[0]), 1])       
        else:
            return assemble4(Qarbre.get_image(self.no), Qarbre.get_image(self.ne), Qarbre.get_image(self.so), Qarbre.get_image(self.se))

"""
mat_img = [[[0, 255, 0], [0, 0, 255]], [[255, 0, 0], [255, 255, 255]]]
mat_no, mat_ne, mat_so, mat_se = decoupe4(mat_img)
qt = Qarbre(mat_img)
qt.insert_no(mat_no, 1)
qt.insert_ne(mat_ne, 1)
qt.insert_so(mat_so, 1)
qt.insert_se(mat_se, 1)
print(qt)
print(qt.no)
print(qt.val)
print(qt.est_feuille())
print(qt.no.est_feuille())
print(qt.hauteur())
print(qt.no.prof)
print(qt)
qt.trace_arbre()
"""
# +-----------------------------+ #
# +-----------------------------+ #



# +-----+ Partie 6 : pixels identiques +-----+ #
def uni_pix(valeur):
    main_color= valeur[0]
    reste_couleurs = valeur[1:]
    return np.allclose(main_color, reste_couleurs, atol=5)
    
"""
qt_img = Qarbre(img_origin)
qt_img.insert_no(img_no, 1)
qt_img.insert_ne(img_ne, 1)
qt_img.insert_so(img_so, 1)
qt_img.insert_se(img_se, 1)
print(uni_pix(qt_img.val))
larg, haut = len(img_no), len(img_no[0])
print(uni_pix(qt_img.no.val))
print(uni_pix(qt_img.ne.val))
print(uni_pix(qt_img.so.val))
print(uni_pix(qt_img.se.val))"""


# +-----------------------------+ #
# +-----------------------------+ #



# +-----+ Partie 5 : qarbre +-----+ #


abr_quat = Qarbre(img_origin)
"""print(abr_quat)
abr_quat.trace_arbre()
"""

imageqt = abr_quat.get_image()
#print(imageqt[0])
fig6 = plt.figure()
ax = fig6.add_subplot(1, 1, 1)
ax.imshow(imageqt)
plt.show()
