#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

n = 5 #numero maximo de vertices
toggle = True
G = nx.Graph()
peso = {}
H = {}
C = {}
j = 0

def forca_bruta(G = nx.Graph()):
    i = 0
    
    for e,x in G.edges():
        peso[i] = G[e][x]['weight']
        i+=1

    for j in range(n-1):
        C[j] = 0

    C[0] = 1
    peso[0] = 0
    tamanho_c = 0

    while(tamanho_c < n):
        w = np.inf

        for j in range(n-1):
            if (C[j] == 0) and (w > peso[j]):
                w = peso[j]
                posicao_w = j

        C[posicao_w] = 1

        for j in range(n-1):
            for e,x in G.edges():
                if (C[j] == 0) and (peso[j] > (w + G[e][x]['weight'])):
                    peso[j] = w + G[e][x]['weight']
        tamanho_c += 1

def onclick(event):
    global toggle
    global j
   
    event.canvas.figure.clear()
    
    if toggle:
        labels = {}
        for v1,v2,data in G.edges(data=True):
            labels[(v1,v2)] = data['weight']
        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, labels)
        toggle = not toggle

    else:
        labels = {}
        for v1,v2,data in H[j].edges(data=True):
            labels[(v1,v2)] = data['weight']
        nx.draw(H[j], pos, with_labels=True)
        nx.draw_networkx_edge_labels(H[j], pos, labels)
        j = j + 1

    event.canvas.draw()

G = nx.gnm_random_graph(n, 5)

for (u, v) in G.edges():
    G[u][v]['weight'] = random.randint(1,10)

forca_bruta(G)

pos = nx.spring_layout(G)
fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

                    
                            

    
