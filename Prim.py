#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import numpy as n
import matplotlib.pyplot as plt

toggle = True
G = nx.Graph()
H = {}
j = 0

def Prim(G = nx.Graph(), R = None):
    i = 0
    Q  = {}
    pred = {}

    for v,data in G.nodes(data=True):
        Q[v] = n.inf
        pred[v] = 'null'

    for e,x in G.edges():
        if ('weight' not in G[e][x]):
            G[e][x]['weight'] = 1.0

    Q[R] = 0.0
    MST  = nx.create_empty_copy(G)

    while Q:
        u = min(Q,key = Q.get)
        del Q[u]

        for vizinho in G[u]:
            if vizinho in Q:
                if G[u][vizinho]['weight'] < Q[vizinho]:
                    pred[vizinho] = u
                    Q[vizinho] = G[u][vizinho]['weight']

        if pred[u] is not 'null':
            for v1,v2,data in G.edges(data=True):
                if (v1 is pred[u] and v2 is u):
                    MST.add_edge(v1,v2, weight=data['weight'])
                    H[i] = MST.copy()
                    i = i + 1
                elif ((v1 is u and v2 is pred[u]) and (not nx.is_directed(G))):
                    MST.add_edge(v2,v1, weight=data['weight'])
                    H[i] = MST.copy()
                    i = i + 1

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

import random
#code creating G here
for (u, v) in G.edges():
    G[u][v]['weight'] = random.randint(1,10)

Prim(G, 0)

pos = nx.spring_layout(G)
fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
