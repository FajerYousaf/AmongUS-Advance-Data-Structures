# -*- coding: utf-8 -*-
import random
import string
import statistics

#Function that randomize player name 
def random_player_name(length = 6):
    first_letter = string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    last_number = string.digits # 0123456789
    temp_name = first_letter + last_number
    name = "".join(random.choice(temp_name) for _ in range(length))
    return name

class Player :
    def __init__(self):
        self.name = random_player_name()
        self.score = 0
        self.liste=[]
    
    def __str__ (self):
        return ("Name :{}  Score :{}".format(self.name,self.score))
    
    def __lt__(self,player):
        return self.score < player.score

    def __gt__(self,player):
        return self.score > player.score

    def __ge__(self,player):
        return self.score >= player.score

    def __le__(self,player):
        return self.score <= player.score
    
    def scoreMoyen(self):
        return statistics.mean(self.score)


def voisins(lis):
    for i in lis:#On parcours la liste de tous les jours de la partie
         b=[] #on initialise une liste qu'on va remplir des valeurs de voisins possibles
         #print(b)
         for k in lis:
             if (len(k.liste)==0 and k!=i):
                 b.append(lis.index(k))
                 
         #print(b) 
         if(len(b)<(3-len(i.liste)) ):
             for k in lis:
                if (len(k.liste)==1 and k!=i):
                    b.append(lis.index(k)) 
                    
         #print(b)   
         if(len(b)<(3-len(i.liste))):
            for k in lis:
                if (len(k.liste)==2 and k!=i):
                    b.append(lis.index(k))
                    
         while(len(lis[lis.index(i)].liste)<3):
            if( len(b)>2 and len(lis[b[0]].liste)< len(lis[b[1]].liste)) :
                a=b[0]
            else :
                a=random.choice(b)
            b.remove(a)    
            #print(b)
            if (lis[a] not in lis[lis.index(i)].liste) and lis[a]!=lis[lis.index(i)] and len(lis[a].liste)<3:
                lis[lis.index(i)].liste.append(lis[a])
                lis[a].liste.append(lis[lis.index(i)])
                

def mortPlayer(liste,p):
    Probable_impostors=set()
    #liste.remove(p)
    print("The player "+p.name+" was killed")
    for i in p.liste:
        #print(i)
        Probable_impostors.add(i)
    for i in liste:
        test=False
        for j in p.liste:
            if(j in i.liste and test==False):
                test=True
        if(test==False):
            Probable_impostors.add(i)
    print("Here is the list of possible impostors")
    for i in Probable_impostors:
        print(i)
    return Probable_impostors



if __name__ == "__main__":
    print(" We begin a new game with 10 new players ")
    print("-----------------------------------------------------")
    print("There is the list of the 10 players : ")
    n=0   
    lis=[] 
    while n!=10:
        p = Player()
        print(p)
        lis.append(p)
        n=n+1  
    
    print("You have to choose a player to kill between the list bellow : ")
    for i in lis:
        print("Number :{}  Name :{}".format(lis.index(i),i.name))
    print("-----------------------")
    choix=int(input("Choose a number between 0 to 9 : \n"))
    print("You chose to kill the player {}".format(lis[choix].name))
    p=lis[choix]
    print("-----------------------------------------------------")
    voisins(lis)
    print("Here is the list of all the player and the index of the players they have met : ")
    for i in lis:
        print("Number :{}  Name :{}".format(lis.index(i),i.name))
        temp=[]
        for j in i.liste:
            temp.append(lis.index(j))
        print("List of the players seen")
        print(temp)
        print("\n")
    print("-----------------------------------------------------")
    print("The player who was killed crosses paths with the following players : ")
    for i in p.liste:
        print("Number :{}  Name :{}".format(lis.index(i),i.name))
    print("-----------------------------------------------------")

    Probable_impostors=mortPlayer(lis,p)
