
# -*- coding: utf-8 -*-

#Importando as bibliotexas do Python.
import networkx as nx
import numpy as n
import matplotlib.pyplot as plt

#Inicializando variáveis globais.
toggle = True
G = nx.Graph()
H = {}
j = 0

#Função que realiza o algoritmo de Prim no grafo passado por parâmetro.
def Prim(G = nx.Graph(), R = None):
    i = 0
    Q  = {}
    predecessor = {}

    #Para todos os vértices do grafo, inicializamos seus pesos como infinito e seus     predecessores como nulos.
    for v,data in G.nodes(data=True):
        Q[v] = n.inf
        predecessor[v] = 'null'
    
    #Para todas as arestas do grafo, se não houver um peso definido seta-o como 1.
    for e,x in G.edges():
        if ('weight' not in G[e][x]):
            G[e][x]['weight'] = 1.0

    Q[R] = 0.0 #Raiz inicia com custo 0 pois é a primeira a sair da fila.
    MST  = nx.create_empty_copy(G) #Cria uma cópia do grafo inicial.

    #Enquanto houver elementos na fila Q:
    while Q:

        #Remove da fila o vértice de menor prioridade (peso).
        u = min(Q,key = Q.get)
        del Q[u]
        
        #Para todo v vizinho de u
        for vizinho in G[u]:
            if vizinho in Q:
 		#Se o peso da aresta de u até seu vizinho for menor do que o peso de v então
                if G[u][vizinho]['weight'] < Q[vizinho]:
                    predecessor[vizinho] = u #Muda o predecessor de vizinho para u já que encontramos uma entrada melhor.
                    Q[vizinho] = G[u][vizinho]['weight'] #Peso de vizinho recebe o peso da aresta de u até vizinho, atualizando o custo para o menor valor.

        if predecessor[u] is not 'null':
 	    
	    #Para a aresta formada por v1 e v2 com valor "peso".
            for v1,v2,data in G.edges(data=True):

 		#Se v1 é predecessor de v2.
                if (v1 is predecessor[u] and v2 is u):
                    MST.add_edge(v1,v2, weight=data['weight']) #Adiciona a aresta formada por esses vértices assim como seu peso no novo grafo MST.
                    H[i] = MST.copy() #Cria uma cópia do grafo MST para H que é um "vetor" de grafos para mostrar o passo a passo da função.
                    i = i + 1
                elif ((v1 is u and v2 is predecessor[u]) and (not nx.is_directed(G))):#Se acontecer ao contrário
                    MST.add_edge(v2,v1, weight=data['weight'])
                    H[i] = MST.copy()
                    i = i + 1

#Função onClick que define o clique na tela do programa.
def onclick(event):
    global toggle
    global j
   
    event.canvas.figure.clear()

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
import random
for (u, v) in G.edges():
    G[u][v]['weight'] = random.randint(1,10)

#Chama a função Prim.
Prim(G, 0)

#Imprime as imagens na tela.
pos = nx.spring_layout(G)
fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
