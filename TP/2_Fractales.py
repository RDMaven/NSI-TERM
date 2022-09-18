####################################################################################################
# ====================================== # TP : Fractales # ====================================== #
####################################################################################################

# +------------------------------------------------------+ #
# +++++++++++++++ Premier exemple : turtle +++++++++++++++ #
# +------------------------------------------------------+ #
"""
import turtle as t

def segments(x, y, l):
    t1.penup()
    t1.goto(x+l,y)
    t1.pendown()
    t1.goto(x,y)
    t1.right(90)
    t1.goto(x,y+l)
    

def fractale(x, y, l, etape):

    # Pour la première étape
    if etape <= 0: return
    # Dessine la figure
    segments(x,y,l)
    fractale(x+l,y,l/2, etape-1)
    fractale(x,y+l,l/2, etape-1)


t1 = t.Turtle()
t1.speed(9)
fractale(0, 0, 100, 5)
t1.hideturtle()
t.done()
"""
# +------------------------------------------------------+ #
# +------------------------------------------------------+ #


# +------------------------------------------------------+ #
# ++++++++++++++ Premier exemple : matplot +++++++++++++++ #
# +------------------------------------------------------+ #
"""
import matplotlib.pyplot as plt 

def segments(x,y,l):    
    lx = []
    ly = []
    lx.append(x+l)
    lx.append(x)
    lx.append(x)
    ly.append(y)
    ly.append(y)
    ly.append(y+l)
    return lx,ly

def fractale(x,y,l,n):
     
    # Dessine la figure
    lx,ly = segments(x,y,l)
    plt.plot(lx,ly)
    # Pour la première étape
    if n <= 0: return
    
    # Pour les étapes intermédiaires
    else:
        n -= 1
        fractale(x+l,y,l/2, n)
        fractale(x,y+l,l/2, n)
    


fig = plt.figure(figsize=(4, 4))
c1 = fig.add_subplot(111) #ligne Colonne Numéro
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
fractale(0, 0, 100, 5)
plt.show()
"""
# +------------------------------------------------------+ #
# +------------------------------------------------------+ #


# +------------------------------------------------------+ #
# ++++++++++++++ Deuxième exemple : turtle +++++++++++++++ #
# +------------------------------------------------------+ #
"""
import turtle as t

def segment(long, angle):
    t2.forward(long)
    t2.left(angle)

def koch(n, long):

    if n<=0: 
        segment(long,60) 
        return
    
    n-=1
    koch(n,long/3)
    koch(n,long/3)
    t2.left(-180)
    koch(n,long/3)
    koch(n,long/3)

t2 = t.Turtle()
t2.speed(5)
koch(3, 300)
t.done()
"""

# +------------------------------------------------------+ #
# +------------------------------------------------------+ #


# +------------------------------------------------------+ #
# ++++++++++++++ Deuxième exemple : matplot ++++++++++++++ #
# +------------------------------------------------------+ #
"""
import matplotlib.pyplot as plt
from numpy import cos, sin, radians

def segment(x, y, angle, long):    
    lx = []
    ly = []
    lx.append(x)
    lx.append(x+long*cos(radians(angle)))
    ly.append(y)
    ly.append(y+long*sin(radians(angle)))
    return lx,ly

def koch(x, y, angle, n, long):
    
    if n<=0: 
        lx,ly = segment(x,y,angle,long) 
        plt.plot(lx,ly)
        return
    
    n-=1

    koch(x,y,angle,n-1,long/3)
    x += long/3*cos(radians(angle))
    y += long/3*sin(radians(angle))
    angle += 60
    koch(x,y,angle,n-1,long/3)
    x += long/3*cos(radians(angle))
    y += long/3*sin(radians(angle))
    angle -= 120
    koch(x,y,angle,n-1,long/3)
    x += long/3*cos(radians(angle))
    y += long/3*sin(radians(angle))
    angle += 60
    koch(x,y,angle,n-1,long/3)
    x += long/3*cos(radians(angle))
    y += long/3*sin(radians(angle))


fig = plt.figure(figsize=(6, 2))
c2 = fig.add_subplot(111) #ligne Colonne Numéro
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
koch(0, 0, 0, 3, 300)
plt.show()
"""
# +------------------------------------------------------+ #
# +------------------------------------------------------+ #


# +------------------------------------------------------+ #
# +++++++++++++++++++ flocons : turtle +++++++++++++++++++ #
# +------------------------------------------------------+ #
"""
import turtle as t

def segment(long, angle):
    t3.left(angle)
    t3.forward(long)

def koch(n, long):
   
    if n<=0: 
        segment(long,60) 
        return
    
    n-=1
    koch(n,long/3)
    koch(n,long/3)
    t3.left(-180)
    koch(n,long/3)
    koch(n,long/3)


def flocon(n, long):
    
    for i in range(3):
        koch(n,long)
        t3.right(180)
  
t3 = t.Turtle()
t3.speed(-1)
flocon(4, 200)
t.done()
"""
# +------------------------------------------------------+ #
# +------------------------------------------------------+ #


# +------------------------------------------------------+ #
# +++++++++++++++++ flocons : matplotlib +++++++++++++++++ #
# +------------------------------------------------------+ #
"""
import matplotlib.pyplot as plt
from numpy import cos, sin, radians

def segment(x, y, angle, long):    
    lx = []
    ly = []
    lx.append(x)
    lx.append(x+long*cos(radians(angle)))
    ly.append(y)
    ly.append(y+long*sin(radians(angle)))
    return lx,ly

def koch(x, y, angle, n, long):
    if n<=0: 
        lx,ly = segment(x,y,angle,long) 
        plt.plot(lx,ly)
        return
    
    n-=1
    koch(x,y,angle,n-1,long/3)
    x += long/3*cos(radians(angle))
    y += long/3*sin(radians(angle))
    angle += 60
    koch(x,y,angle,n-1,long/3)
    x += long/3*cos(radians(angle))
    y += long/3*sin(radians(angle))
    angle -= 120
    koch(x,y,angle,n-1,long/3)
    x += long/3*cos(radians(angle))
    y += long/3*sin(radians(angle))
    angle += 60
    koch(x,y,angle,n-1,long/3)
    x += long/3*cos(radians(angle))
    y += long/3*sin(radians(angle))
    return x,y


def flocon(x, y, angle, n, long):
    for i in range(3):
        x,y = koch(x,y,angle,n,long)
        angle -= 120
    

fig = plt.figure(figsize=(6, 6))
c3 = fig.add_subplot(111) #ligne Colonne Numéro
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
flocon(0, 0, 0, 3, 200)
plt.show()
"""
# +------------------------------------------------------+ #
# +------------------------------------------------------+ #


# +------------------------------------------------------+ #
# +++++++++++++++++++ arbres : turtle ++++++++++++++++++++ #
# +------------------------------------------------------+ #
"""
import random as rand
import turtle as t

def arbre(l,n):
    if l/8 < 1: t4.pencolor('green')
    else: t4.pencolor('brown')

    t4.pensize(l/8)
  
    if n <= 0: return
    
    coef = rand.randint(5,8)*0.1
    angle = rand.randint(30,50)

    t4.forward(l)
    t4.left(angle)

    arbre(coef * l, n-1)        
    
    t4.right(2*angle)

    arbre(coef * l, n-1)
    
    t4.penup()
    t4.left(angle)
    t4.forward(-l)
    t4.pendown()
        
t4 = t.Turtle()
t4.left(90)
t4.speed(0)
t4.pencolor('brown')
arbre(100,7)
t.done()
"""
# +------------------------------------------------------+ #
# +------------------------------------------------------+ #


# +------------------------------------------------------+ #
# ++++++++++++++++++ arbres : matplotlib +++++++++++++++++ #
# +------------------------------------------------------+ #

import matplotlib.pyplot as plt
from numpy import cos, sin, radians
import random as rand

def segment(x, y, angle, long):    
    lx = []
    ly = []
    lx.append(x)
    lx.append(x+long*cos(radians(angle)))
    ly.append(y)
    ly.append(y+long*sin(radians(angle)))
    return lx,ly

def arbre(x, y, angle, l):
    if l/8 < 1: color = ('green')
    else:  color = ('brown')
    
    thick = l/8
    
    
    if l <= 2: return
    
    coef_l = rand.randint(5,8)*0.1
    coef_a = rand.randint(30,50)
    
    lx,ly = segment(x,y,angle,l)
    plt.plot(lx,ly, linewidth=thick, color=color)
    x += l*cos(radians(angle))
    y += l*sin(radians(angle))

    angle += coef_a

    arbre(x,y,angle, coef_l*l)        
    
    angle-= 2*coef_a

    arbre(x,y,angle, coef_l*l)
    
    angle += coef_a

    lx,ly = segment(x,y,angle, -l)
    plt.plot(lx,ly,linewidth=thick, color=color)
    
fig = plt.figure(figsize=(5, 5))
c4 = fig.add_subplot(111) #ligne Colonne Numéro
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
arbre(0, 0, 90, 100)
plt.show()

# +------------------------------------------------------+ #
# +------------------------------------------------------+ #

