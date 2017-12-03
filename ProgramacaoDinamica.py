#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import numpy as n
import matplotlib.pyplot as plt
import random

toggle = True #variavel para controlar os cliques
G = nx.Graph() #G é um grafo 
H = {} #H é um dicionário que armazena o passo a passo do algoritmo
j = 0 #j é um contador para contar a quantidade de cliques

#funcao que retorna o menor valor dentro de uma linha da matriz de pesos, 
#desconsiderando os valores iguas a -1            
def buscarMenor(lst):
   i = float("inf")
   for nr in lst:
       if nr < i and nr != -1:
           i = nr
   return i       

#funcao que gera a MST do grafo dado
def MST(G = nx.Graph()):
    i = 0 #contador para o passo a passo da geracao da MST
    Q  = [] #matriz adjacencia que contem os pesos do grafo

    MST = nx.create_empty_copy(G) #cria uma copia vazia (somente os vertices) do grafo dado
    
    #inicializa a matriz com valores infinitos
    for k in range(0, nx.number_of_nodes(G)):
         linha = []
         for l in range(0, nx.number_of_nodes(G)):
               linha.append(n.inf)
         Q.append(linha)
    
    #insere na matriz os pesos das arestas
    for v1, v2, data in G.edges(data = True):
         Q[int(v1)].pop(int(v2))
         Q[int(v1)].insert(int(v2) ,data['weight'])
         
     
    #verifica se existem ciclos e os retira    
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
	
    #varre a matriz e adiciona na MST as arestas seguras e que possuem menor peso		
    for k in range(0, nx.number_of_nodes(G) -1):
      #inicializa as variaves com valores que nao sao possiveis
      menor_peso = n.inf 
      indice_menor = -1
      indice = -1
      #varre cada linha procurando o menor valor
      for j in range (0, nx.number_of_nodes(G)):
       aux = buscarMenor(Q[j]) #variavel que armazena o possivel menor peso
       if menor_peso > aux and aux != n.inf: #caso o valor encontrado seja o menor, armazena ele na variavel menor_peso
            menor_peso = aux #armazena o menor peso
            indice = Q[j].index(menor_peso) #armazena a coluna do menor peso
            indice_menor = j #armazena a linha do menor peso
      MST.add_edge(indice_menor, indice, weight = menor_peso) #adiciona a aresta com menor peso no grafo
      H[i] = MST.copy() #faz uma copia do passo i para a lista de grafos
      i = i + 1 #incrementa i
      Q[indice_menor].pop(indice) #retira da matriz o peso que acabou de ser adicionado
      Q[indice_menor].insert(indice, -1) #insere -1 na posicao do peso colocado
      Q[indice].pop(indice_menor) #retira da matriz o peso que acabou de ser adicionado (nao é digrafo, por isso essa verificaçao é necessaria)
      Q[indice].insert(indice_menor, -1) #insere -1 na posicao do peso colocado
      #varre a cada linha da matriz
      for k in range (0, nx.number_of_nodes(G)):
	  #antes de marcar o vertice como visitado, passa os valores dele na matriz de adjacencia para o vertice com que
	  #ele tem uma aresta. no entanto, isso so acontece se o peso for menor.
          if Q[indice_menor][k] != -1 and Q[indice_menor][k] < Q[k][indice_menor]: 
              Q[k].pop(indice_menor)
              Q[k].insert(indice_menor, Q[indice_menor][k])
          Q[indice_menor].pop(k) #marca o no como "visitado" colocando -1 em sua linha na matriz de adjacencia
          Q[indice_menor].insert(k, -1)
       
#funcao que mostra os grafos na tela a cada clique
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

#inicializa um grafo aleatorio
G = nx.gnm_random_graph(4, 5)

#adiciona pesos aleatorios ao grafo
for (u, v) in G.edges():
    G[u][v]['weight'] = random.randint(1,10)

#gera a MST
MST(G)

#chama a funcao que mostra os grafos a cada clique
pos = nx.spring_layout(G)
fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', onclick)

#printa na tela os grafos
plt.show()

