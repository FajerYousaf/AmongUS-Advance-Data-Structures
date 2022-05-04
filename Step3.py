# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:57:29 2020

@author: Takwa Aldroe
"""
import numpy as np
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

Impostors = [[0, 4, 4.5 , 4.5, 2.5, INF, 0, 6, INF, INF, 7, INF, INF, 5.5],
     [4, 0, 3.5, 0, 8, INF, 4.5, INF, INF, INF, INF, INF, INF, INF],
     [4.5, 3.5, 0, 5, 7.5, INF, 4.5, INF, INF, INF, INF, INF, INF, INF],
     [4.5, 0, 5, 0, 0, INF, 4.5, INF,INF, INF, INF, INF, INF,INF],
     [2.5, 8, 7.5, 0, 0, 3, 4.5, 5, INF, INF, INF, INF, INF, INF],
     [INF, INF, INF, INF, 3, 0, INF, 4.5, INF, INF, INF, INF, INF, INF],
     [0, 4.5, 4.5, 4.5, 4.5, INF, 0, 4.5, INF, INF, INF, INF, INF, INF],
     [6, INF, INF, INF, 5, 4.5, 4.5, 0, 5, 9, INF, INF, INF, INF],
     [INF,INF, INF, INF, INF, INF, INF, 5, 0, 7, INF, INF, 0, 0],
     [INF, INF, INF, INF, INF, INF, INF, 7, 7, 0, 5, 0, 4, INF],
     [7, INF, INF, INF, INF, INF, INF, INF, INF, 5, 0, 0, 4, 5.5],
     [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 0, 0, 3.5, INF],
     [INF, INF, INF, INF, INF, INF, INF, INF, 0, 4, 4, 3.5, 0, 0],
     [5.5, INF, INF, INF, INF, INF, INF, INF, 0, INF, 5.5, INF, 0,0]]


# Python Program for Floyd Warshall Algorithm
INF = np.inf
def floydWarshall(graph,n): 
    dist=graph
    for k in range(n):
        for i in range(n):
            for j in range(n): 
                dist[i][j] = min(dist[i][j] ,dist[i][k]+ dist[k][j])
    return dist

CheminCrewMates=floydWarshall(CrewMates,14)
CheminImpostors=floydWarshall(Impostors,14)

room0="Cafetaria"
room1="Weapons"
room2="O2"
room3="Navigation"
room4="Shield"
room5="Communication"
room6="Admin"
room7="Storage"
room8="Electrical"
room9="Lower E"
room10="Upper E"
room11="Reactor"
room12="Security"
room13="Medbay"

if __name__ == "__main__":
    #print(" Choose the map you want : \n1:Crewmates     2:Impostors ")
    carte=(input(" Choose the map you want : \n1:Crewmates     2:Impostors "))
    carte2=int(carte)
    print("-----------------------------------------------------")
    if carte2==1:
        print("There is the list of the 14 rooms: ")
        print("-----------------------------------------------------")
        print("0 : Cafetaria\n1 : Weapons\n2 : O2\n3 : Navigation\n4 : Shield\n5 : Communication")
        print("6 : Admin\n7 : Storage\n8 : Electrical\n9 : Lower E\n10 : Upper E\n11 : Reactor\n12 : Security\n13 : Medbay")
        print("-----------------------------------------------------")
        print("Choose the room of the departure between these 14 rooms")
        dep=int(input("Tap a number between 0 and 13\n"))
        print("Choose the room of the arrival between these 14 rooms")
        arr=int(input("Tap a number between 0 and 13\n"))
        time=CheminCrewMates[dep][arr]
        print("The time for a crewmate to go from the departure room to the arrival room is "+format(time)+" seconds")
    if carte2==2:
        print("There is the list of the 14 rooms: ")
        print("-----------------------------------------------------")
        print("0 : Cafetaria\n1 : Weapons\n2 : O2\n3 : Navigation\n4 : Shield\n5 : Communication")
        print("6 : Admin\n7 : Storage\n8 : Electrical\n9 : Lower E\n10 : Upper E\n11 : Reactor\n12 : Security\n13 : Medbay")
        print("-----------------------------------------------------")
        print("Choose the room of the departure between these 14 rooms")
        dep=int(input("Tap a number between 0 and 13\n"))
        print("Choose the room of the arrival between these 14 rooms")
        arr=int(input("Tap a number between 0 and 13\n"))
        time=CheminImpostors[dep][arr]
        print("The time for an impostor to go from the departure room to the arrival room is "+format(time)+" seconds")
    
    if carte!="1" and carte!="2":
        print("You tap a wrong number")
