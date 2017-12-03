#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Importando as bibliotexas do Python.
import networkx as nx
import numpy as n
import matplotlib.pyplot as plt
import random

#Inicializando variáveis globais.
toggle = True
G = nx.Graph()
H = {}
j = 0

#Inicialmente cada vértice é colocado num grupo distinto e cada vez que uma aresta é
#inserida, os dois vértices extremidades passam a fazer parte do mesmo grupo. Assim, arestas que
#ligam vértices do mesmo grupo, formam ciclos e devem ser evitadas.

#Função que retorna o grupo a que o vértice pertence.
def make_set(lista, vertice):
    i = 0
    for grupo in lista:
        if (vertice in grupo):
            return i
        i = i+1

#Função que realiza o algoritmo de Kruskal no grafo passado por parâmetro.
def Kruskal(G = nx.Graph()):
    i = 0
    
    MST = nx.create_empty_copy(G)
    
    #Ordenando as arestas por pesos.
    E = sorted(G.edges(data=True), key=lambda k: k[2]['weight']) 
   
    vertices = []

    #Cria uma lista de grupos distintos com apenas um vértice cada, inicialmente.
    for v in G.nodes():
        vertices.append({v})

    #Para cada aresta em E, cria dois grupos contendo vertices distintos.
    #Vértices extremidades de uma mesma aresta fazem parte do mesmo grupo.
    for aresta in E:
        Grupo1 = make_set(vertices, aresta[0])
        Grupo2 = make_set(vertices, aresta[1])

        #Se os grupos dos vértices forem iguais não podemos uni-los pois isso fecharia um ciclo.
        #Se os grupos forem diferentes,
        if Grupo1 != Grupo2:
            
            #Adicionamos as arestas ao novo grafo formado.
            peso = aresta[2]['weight']
            MST.add_edge(aresta[0], aresta[1], weight = peso)
            H[i] = MST.copy()
            i = i + 1

            #Removendo os dois grupos de vértices do vetor "vertices".
            if Grupo1 > Grupo2:
                conj1 = vertices.pop(Grupo1)
                conj2 = vertices.pop(Grupo2)
            else:
                conj2 = vertices.pop(Grupo2)
                conj1 = vertices.pop(Grupo1)

            #Inserindo um novo grupo a partir da união dos dois.
            vertices.append(conj1.union(conj2))
            
#Função onClick que define o clique na tela do programa.
def onclick(event):
    global toggle
    global j
   
    event.canvas.figure.
    
    #Se foi identificado o clique, imprime o grafo inicial na tela
    if toggle:
        labels = {}
        for v1,v2,data in G.edges(data=True):
            labels[(v1,v2)] = data['weight']
        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, labels)
        toggle = not toggle

    #Senão, imprime o passo a passo do novo grafo encontrado.
    else:
        labels = {}
        for v1,v2,data in H[j].edges(data=True):
            labels[(v1,v2)] = data['weight']
        nx.draw(H[j], pos, with_labels=True)
        nx.draw_networkx_edge_labels(H[j], pos, labels)
        j = j + 1

    event.canvas.draw()

#Main
    
#Cria um grafo aleatório com 10 vértices e 15 arestas.
G = nx.gnm_random_graph(10, 15)

#Da pesos aleatórios de 1 a 10 às arestas do grafo.
for (u, v) in G.edges():
    G[u][v]['weight'] = random.randint(1,10)

#Chama a função Kruskal
Kruskal(G)

#Imprime as imagens na tela.
pos = nx.spring_layout(G)
fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
