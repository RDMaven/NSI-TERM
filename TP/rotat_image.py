# Pour que les images soient affichées à la même dimenssion
from IPython.display import HTML

HTML("""
<style>
    .output_area img {
        width: 20%;
    }
</style>""")

from PIL import Image
import numpy as np

def AfficherPix(image):
    largeur, hauteur = image.size
    for y in range(hauteur): 
        for x in range(largeur): 
            rvb = image.getpixel((x,y)) 
            print(rvb)

filein = "./TP/pixel.png"
img = Image.open(filein)
#img.show()
#print(img.format, img.size, img.mode)

#img.show()
#AfficherPix(img)

"""
Combien de paramètres retourne la méthode getpixel((x,y)) ?
- 3
Que représentent ces paramètres ?
- la couleur du pixel en rvb
"""


def filtreR(img):
    """
    Permet d'obtenir une image filtrée Rouge

    Parameters
    ----------
    img : image couleur

    Returns
    -------
    img_out : image couleur

       """
    
    # A compléter !
    L, H = img.size
    img_out = Image.new("RGB", (L,H))
    for y in range(H): 
        for x in range(L): 
            rvb = img.getpixel((x,y)) 
            img_out.putpixel((x,y), (rvb[0],0,0)) 
    
    
    return img_out


imgR = filtreR(img)
#imgR.show()

def filtre(img, f):
    """
    Permet d'obtenir une image filtrée f

    Parameters
    ----------
    img : image couleur
    f : caractère R, V ou B

    Returns
    -------
    img_out : image couleur

   """
    
    L, H = img.size
    img_out = Image.new("RGB", (L,H))

    if f == 'R': f = "(rvb[0],0,0)"
    elif f=='V': f = "(0, rvb[1],0)"
    else : f = "(0,0,rvb[2])"

    for y in range(H): 
        for x in range(L): 
            rvb = img.getpixel((x,y)) 
            img_out.putpixel((x,y), eval(f)) 
    
    
    return img_out


"""f = "V"
imgF = filtre(img, f)
imgF.show()
"""

def imageNG(img):
    """
    Permet d'obtenir une image en niveau de gris

    Parameters
    ----------
    img : image couleur

    Returns
    -------
    img_out : image en niveau de gris

    """
    return img.convert('L')


"""imgNG = imageNG(img)
imgNG.show()
"""

def imageNB(img):
    """
    Permet d'obtenir une image en noir et blanc
    Parameters
    ----------
    img : image en couleur
    Returns
    -------
    img_out : image en noir et blanc
    """

    img = imageNG(img)
    L, H = img.size
    img_out = Image.new("RGB", (L,H))

    
    for y in range(H): 
        for x in range(L): 
            rvb = img.getpixel((x,y))
            if rvb > float(255)/2:
                img_out.putpixel((x,y), (255,255,255))
            else:
                img_out.putpixel((x,y), (0,0,0))
    
    
    return img_out

    
imgNB = imageNB(img)
#imgNB.show()


def retourne(img:Image):
    """
    permet d'obtenir une image tournée d'un quart
    de tour
    Parameters
    ----------
    img : image couleur
    Returns
    -------
    img_out : image couleur
    """

    L, H = img.size
    img_out = Image.new("RGB", (L,H))

    for y in range(H): 
        for x in range(L): 
            rvb = img.getpixel((x,y))
            img_out.putpixel((y,L-1-x), rvb)    
    
    #Q = len(img_colors)//4

    return img_out


"""imgRot1 = retourne(img)
imgRot1.show()
"""


def echange_pix(img, x0, y0, x1, y1):
    """
    Echange deux pixels d'une image (x0, y0) avec (x1, y1)
    Parameters
    ----------
    img : image couleur
    x0, y0, x1, y1 : int
    Returns
    -------
    None.
    """

    rvb0 = img.getpixel((x0,y0))
    rvb1 = img.getpixel((x1,y1))

    img.putpixel((x1,y1), rvb0)        
    img.putpixel((x0,y0), rvb1)
    return img

"""img2 = echange_pix(img, 6, 2, 11, 1)
img2.show()
"""



def echange_quadrant(img, x0, y0, x1, y1, largeur):
    """
    Echange deux carrés de <<largeur>> d'une image. Le premier commence en
    x0, y0 et le second en x1, y1.
    Parameters
    ----------
    img : image couleur
    x0, y0, x1, y1 : int
    largeur : int
    Returns
    -------
    None.
    """
    for x in range(largeur): 
        for y in range(largeur):

            echange_pix(img, x+x0,y+y0, x+x1, y+y1)

    return img


largeur, hauteur = img.size
#img3 = echange_quadrant(img, 0, 0, largeur//2, largeur//2, largeur//2)
img3 = echange_quadrant(img, 0, 0, largeur//2, 0, largeur//2)
#img3.show()



def rotation(img, xa=0, ya=0, dim=0):
    """
    Effectue la rotation de 90° dans le sens horaire
    d'une image

    Parameters
    ----------
    img : image couleur
    xa, ya : int
    largeur : int
    
    Returns
    -------
    None.

    """

    if dim >= 1:
        rotation(img, xa=0,      ya=0,       dim=dim//2)
        rotation(img, xa=0,      ya=dim//2,  dim=dim//2)
        rotation(img, xa=dim//2, ya=0,       dim=dim//2)
        rotation(img, xa=dim//2, ya=dim//2,  dim=dim//2)
    
    echange_quadrant(img, x0=xa, y0=ya, x1=xa+dim//2, y1=ya, largeur=dim//2)
    echange_quadrant(img, x0=xa+dim//2, y0=ya, x1=xa+dim//2, y1=ya+dim//2, largeur=dim//2)
    echange_quadrant(img, x0=xa+dim//2, y0=ya+dim//2, x1=xa, y1=ya+dim//2, largeur=dim//2)

    
    return img

largeur, hauteur = img.size
img_out = rotation(img, dim=largeur)
img_out.show()


