
from typing import OrderedDict


def occurenceLettre(phrase):
    return dict(zip(set(phrase), [phrase.count(c) for c in set(phrase)]))

def ordonne(d:dict[str, int]) -> list[tuple[str, int]] :
    return sorted(d.items(), key=lambda i: i[1])

def huffman(listeF):
    listeF = [[k,v, [k, None, None]] for k,v in listeF]

    while len(listeF) > 1:
        noeud = listeF[0][1] + listeF[1][1]
        #arbreH = arbre noeud
        arbreH = [str(noeud), listeF[0][2], listeF[1][2]]
        #Effacer les deux premiers éléments
        listeF = listeF[2:]
        #liste = liste + [valeur noeud, poids noeud, arbre noeud]
        listeF.append([str(noeud), noeud, arbreH])
        #Trier listeF par ordre croissant
        listeF.sort(key=lambda a: a[1])
    return arbreH

def encode(arbreH, code='', dicoHuf={}):
    if not arbreH:
        return []
    else:
        if not arbreH[1] and not arbreH[2]:
            dicoHuf[arbreH[0]] = code
        else:
            encode(arbreH[1], code+'0', dicoHuf)
            encode(arbreH[2], code+'1', dicoHuf)
        return dicoHuf
    

def compresse(phrase):
    dicoComp = encode(huffman(ordonne(occurenceLettre(phrase))))
    t_comp = 1- (sum([len(dicoComp[char]) for char in phrase]) / (len(phrase)*8))
    
    return ''.join([dicoComp[char] for char in phrase]), t_comp, huffman(ordonne(occurenceLettre(phrase)))
    
def decompresse(phraseComp:str, arbreH:list):
    #dicoHuf = {v :k for k,v in dicoHuf.items()}
    rep = ''
    # tant que le noeud n'est pas une feuille
    for i in range(int(arbreH[0])):
        sub_arbreH = arbreH.copy()

        while sub_arbreH[1] and sub_arbreH[2]:
            # si le prochain charactère est un 0:
            if phraseComp[0] == '0':
                # concerver la liste gauche
                sub_arbreH = sub_arbreH[1]
            # sinon 
            else:
                # concerver la liste droite
                sub_arbreH = sub_arbreH[2]
            phraseComp = phraseComp[1:]
        rep += sub_arbreH[0]
    return rep


"""
dicoF = occurenceLettre("CODE DE MORSE")
print(f'dicoF : {dicoF}')
listeF = ordonne(dicoF)
print(f'listeF : {listeF}')
arbreH = huffman(listeF)
print(f'arbreH : {arbreH}')
dicoHuf = encode(arbreH)
print(f'dicoHuf : {dicoHuf}')
print()"""

phraseComp, taux_compression, arbreH = compresse("Par ces paroles, Stubb, sans doute, suggérait indirectement que l'homme a beau aimer son semblable, néanmoins l'homme est un animal fait pour gagner de l'argent et que ce dernier penchant peut souvent empêcher sa bonté naturelle.")

print(phraseComp)
print(f'Le taux de compression est de : {round(taux_compression*100, 2)}%')
pharse_decomp = decompresse(phraseComp, arbreH)
print(pharse_decomp)