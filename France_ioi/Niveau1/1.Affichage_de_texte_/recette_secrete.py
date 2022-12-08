from robot import *

def remplir(i):pass
def transferer(a,b): pass
def vider(a): pass


remplir(3)          # 0 | 3
transferer(3, 5)    # 3 | 0
remplir(3)          # 3 | 3
transferer(3, 5)    # 5 | 1
vider(5)            # 0 | 1
transferer(3, 5)    # 1 | 0
remplir(3)          # 1 | 3
transferer(3, 5)    # 4 | 0