# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:40:26 2020

@author: Takwa Aldroe
"""
import numpy as np


""" On a essayer avec l'algo de Prism
    Mais on s'est ensuite rendu compte que ça ne permettait pas d'obtenir le résultat souhaité
    En effet, le Prism algo comme celui de Kruskal, permettent d'avoir les chemin
    les plus rapide sans faire de cycle. 
    Alors que nous, nous voulons parcourir toutes les salles que une fois.
    Pour répondre à notre problèmatique, l'algo qui nous a semblait le plus logique
    d'utlisier est celui d'Hamilton
"""
   
def hamilton(G, pt, path):
    size = len(G)
    if pt not in set(path):
        path.append(pt)
        if len(path)==size:
            return path
        for pt_next in G.get(pt, []):
            res_path = [i for i in path]
            candidate = hamilton(G, pt_next, res_path)
            if candidate is not None:  
                return candidate

INF=np.inf
CrewMates = [[0, 4,INF, INF, INF, INF, 5.5, 6, INF, INF, 7, INF, INF, 5.5],
     [4, 0, 3.5, 5.5, 8, INF, INF, INF, INF, INF, INF, INF, INF, INF],
     [INF, 3.5, 0, 5, 7.5, INF, INF, INF, INF, INF, INF, INF, INF, INF],
     [INF, 5.5, 5, 0, 6, INF, INF, INF,INF, INF, INF, INF, INF,INF],
     [INF, 8, 7.5, 6, 0, 3,INF,5, INF, INF, INF, INF, INF, INF],
     [INF, INF, INF, INF, 3, 0, INF, 4.5, INF, INF, INF, INF, INF, INF],
     [5.5,INF, INF, INF, INF, INF, 0, 4.5, INF, INF, INF, INF, INF, INF],
     [6, INF, INF, INF, 5, 4.5, 4.5, 0, 5, 9, INF, INF, INF, INF],
     [INF,INF, INF, INF, INF, INF, INF, 5, 0, 7, INF, INF, INF, INF],
     [INF, INF, INF, INF, INF, INF, INF, 7, 7, 0, 5, 4.5, 4, INF],
     [7, INF, INF, INF, INF, INF, INF, INF, INF, 5, 0, 4.5, 4, 5.5],
     [INF, INF, INF, INF, INF, INF, INF, INF, INF, 4.5, 4.5, 0, 3.5, INF],
     [INF, INF, INF, INF, INF, INF, INF, INF, INF, 4, 4, 3.5, 0, INF],
     [5.5, INF, INF, INF, INF, INF, INF, INF, INF, INF, 5.5, INF, INF,0]]
G1={}
for i in range(14):
    liste=[]
    for j in range(14):
        if(CrewMates[i][j]!=np.inf and CrewMates[i][j]!=0):
            liste.append(j)
    G1[i]=liste
    #print(i)
    #print(liste)
#hamilton(G1,12,[])  
    
listeimpossible=[0,4,7,9,10,11,12]
listepossible=[1,2,3,5,6,8,13]

if __name__ == "__main__":   
   print("0 : Cafetaria\n1 : Weapons\n2 : O2\n3 : Navigation\n4 : Shield\n5 : Communication")
   print("6 : Admin\n7 : Storage\n8 : Electrical\n9 : Lower E\n10 : Upper E\n11 : Reactor\n12 : Security\n13 : Medbay\n")
   room=(input("Choose  a number of room : "))
   room2=int(room)
   print("-----------------------------------------------------")
   if room2 in listeimpossible:
       print("It is impossible to visit all the rooms if you begin in this room: ")
   if room2 in listepossible:
       print("There is the path to follow if you want to visit all the rooms ")
       print("-----------------------------------------------------")
       print(hamilton(G1,room2,[]) )
   if room2 not in listeimpossible and room2 not in listepossible:
       print("You tap a wrong number")
