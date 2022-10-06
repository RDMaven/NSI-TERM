# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 18:18:38 2021
@author: ljosse
Les fonctions suivantes permettent de tracer un arbre binaire instancié
avec la classe "classe_arbre_binaire".
Il suffit d'écrire : repr_graph(arbre, (6,4),True)
(6,4) est la taille de la fenêtre, True pour voir les noueds "None"
"""
import networkx as nx
import matplotlib.pyplot as plt

def parcours(arbre, noeuds, branches, labels, positions, profondeur, 
             pos_courante, pos_parent, null_node):
    if arbre is not None:
        noeuds[0].append(pos_courante)
        positions[pos_courante] = (pos_courante, profondeur)
        profondeur -= 1
        labels[pos_courante] = str(arbre.get_valeur())
        branches[0].append((pos_courante, pos_parent))
        pos_gauche = pos_courante - 2**profondeur
        parcours(arbre.get_gauche(), noeuds, branches, labels, 
                 positions, profondeur, pos_gauche, pos_courante, 
                 null_node)
        pos_droit = pos_courante + 2**profondeur
        parcours(arbre.get_droit(), noeuds, branches, labels, 
                 positions, profondeur, pos_droit, pos_courante, 
                 null_node)
    elif null_node:
        noeuds[1].append(pos_courante)
        positions[pos_courante] = (pos_courante, profondeur)
        branches[1].append((pos_courante, pos_parent))

def repr_graph(arbre, size=(8,8), null_node=False):
    """
    size : tuple de 2 entiers. Si size est int -> (size, size)
    null_node : si True, trace les liaisons vers les sous-arbres vides
    """
    if arbre is None:
        return
    branches = [[]]
    profondeur = arbre.hauteur()
    pos_courante = 2**profondeur
    noeuds = [[pos_courante]]
    positions = {pos_courante: (pos_courante, profondeur)} 
    labels = {pos_courante: str(arbre.get_valeur())}
    if null_node:
        branches.append([])
        noeuds.append([])
    profondeur -= 1
    parcours(arbre.get_gauche(), noeuds, branches, labels, positions, 
             profondeur, pos_courante - 2**profondeur, pos_courante, 
             null_node)
    parcours(arbre.get_droit(), noeuds, branches, labels, positions, 
             profondeur, pos_courante + 2**profondeur, pos_courante, 
             null_node) 
    mon_arbre = nx.Graph()
    if type(size) == int:
        size = (size, size)    
    plt.figure(figsize=size)
    ax = plt.gca()
    ax.margins(0.1)
    #plt.axis("off")
    nx.draw_networkx_nodes(mon_arbre, positions, nodelist=noeuds[0], 
                           node_color="pink", node_size=500, 
                           edgecolors="blue")
    nx.draw_networkx_edges(mon_arbre, positions, edgelist=branches[0], 
                           edge_color="black", width=2)
    nx.draw_networkx_labels(mon_arbre, positions, labels)
    if null_node:
        nx.draw_networkx_nodes(mon_arbre, positions, nodelist=noeuds[1], 
                               node_color="white", node_size=50, 
                               edgecolors="grey")
        nx.draw_networkx_edges(mon_arbre, positions, edgelist=branches[1], 
                               edge_color="grey", width=1)
    plt.show()