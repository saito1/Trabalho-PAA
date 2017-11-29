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

# Função auxiliar para encontrar o índice do conjunto em que o vértice se
# encontra
def encontrar_conjunto(lista, vertice):
    i = 0
    for conjunto in lista:
        if (vertice in conjunto):
            return i
        i = i+1

def Kruskal(G = nx.Graph()):
    i = 0
    
    MST = nx.create_empty_copy(G)

    E = sorted(G.edges(data=True), key=lambda k: k[2]['weight'])
   
    vertices_conexos = []

    # criamos uma lista de conjuntos disjuntos com apenas um vértice cada um, a
    # princípio, para depois fazermos as uniões
    for v in G.nodes():
        vertices_conexos.append({v})

    for aresta in E:
        indexConj1 = encontrar_conjunto(vertices_conexos, aresta[0])
        indexConj2 = encontrar_conjunto(vertices_conexos, aresta[1])

        # Se o conjunto encontrado para o vértice 0 é o mesmo do vértice 1,
        # então não podemos uni-los, já que isto fecharia um ciclo.
        if indexConj1 != indexConj2:

            # Se o grafo contém o peso, então adicionamos as três informações
            # da aresta (2 vértices e dados)
            peso = aresta[2]['weight']
            MST.add_edge(aresta[0], aresta[1], weight = peso)
            H[i] = MST.copy()
            i = i + 1

            # removemos os dois conjuntos de vértices do vetor vertices_conexos
            if indexConj1 > indexConj2:
                conj1 = vertices_conexos.pop(indexConj1)
                conj2 = vertices_conexos.pop(indexConj2)
            else:
                conj2 = vertices_conexos.pop(indexConj2)
                conj1 = vertices_conexos.pop(indexConj1)

            # e inserimos um novo conjunto a partir da união dos dois
            vertices_conexos.append(conj1.union(conj2))

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

G = nx.gnm_random_graph(10, 15)

for (u, v) in G.edges():
    G[u][v]['weight'] = random.randint(1,10)
    
Kruskal(G)

pos = nx.spring_layout(G)
fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
