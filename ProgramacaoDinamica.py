#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import numpy as n
import matplotlib.pyplot as plt
import random

toggle = True
G = nx.Graph()
H = {}
j = 0
             
def buscarMenor(lst):
   i = float("inf")
   for nr in lst:
       if nr < i and nr != -1:
           i = nr
   return i       

def MST(G = nx.Graph()):
    i = 0
    Q  = []
    pred = {}

    MST = nx.create_empty_copy(G)
    
    for k in range(0, nx.number_of_nodes(G)):
         linha = []
         for l in range(0, nx.number_of_nodes(G)):
               linha.append(n.inf)
         Q.append(linha)
    
    for v1, v2, data in G.edges(data = True):
         Q[int(v1)].pop(int(v2))
         Q[int(v1)].insert(int(v2) ,data['weight'])
         
         
    for  v3 in G.nodes():
         for  v1 in G.nodes():
              for  v2 in G.nodes():
                 if Q[int(v1)][int(v3)] != n.inf and Q[int(v1)][int(v2)] != n.inf and Q[int(v3)][int(v2)] != n.inf:
                      if Q[int(v1)][int(v3)] + Q[int(v3)][int(v2)] <= Q[int(v1)][int(v2)]:
                           Q[int(v1)].pop(int(v2))
                           Q[int(v1)].insert(int(v2), n.inf)
		      elif Q[int(v1)][int(v3)] >= Q[int(v3)][int(v2)]:
			   Q[int(v2)].pop(int(v3))
                           Q[int(v2)].insert(int(v3), n.inf)
		      elif Q[int(v1)][int(v3)] <= Q[int(v3)][int(v2)]:
			   Q[int(v3)].pop(int(v2))
                           Q[int(v3)].insert(int(v2), n.inf)
			
    for k in range(0, nx.number_of_nodes(G) -1):
              menor_peso = n.inf
              indice_menor = -1
	      indice = -1
              for j in range (0, nx.number_of_nodes(G)):
               aux = buscarMenor(Q[j])
               if menor_peso > aux and aux != -n.inf and aux != n.inf:
                    menor_peso = aux
                    indice = Q[j].index(menor_peso)
                    indice_menor = j
              MST.add_edge(indice_menor, indice, weight = menor_peso)
              H[i] = MST.copy()
              i = i + 1
              Q[indice_menor].pop(indice)
              Q[indice_menor].insert(indice, -1)
              Q[indice].pop(indice_menor)
              Q[indice].insert(indice_menor, -1)
              for k in range (0, nx.number_of_nodes(G)):
                  if Q[indice_menor][k] != -1 and Q[indice_menor][k] < Q[k][indice_menor]  :
                      Q[k].pop(indice_menor)
                      Q[k].insert(indice_menor, Q[indice_menor][k])
                  Q[indice_menor].pop(k)
                  Q[indice_menor].insert(k, -1)
               

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

G = nx.gnm_random_graph(8, 12)

for (u, v) in G.edges():
    G[u][v]['weight'] = random.randint(1,10)

MST(G)

pos = nx.spring_layout(G)
fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
