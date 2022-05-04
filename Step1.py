# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:31:41 2020

@author: Admin
"""

import random
import string
import sys
import statistics

#Function that randomize player name 
def random_player_name(length = 6):
    first_letter = string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    last_number = string.digits # 0123456789
    temp_name = first_letter + last_number
    name = "".join(random.choice(temp_name) for _ in range(length))
    return name
#random_player_name()

   
#Function that randomize player score at each game (between 0 point to 12 points)
def random_player_score() :
    score = random.randint(0,12)
    return score
#random_player_score()


class Player :
    def __init__(self):
        self.name = random_player_name()
        self.score = random_player_score()
    
    def __str__ (self):
        return ("Name :{},Score :{}".format(self.name,self.score))
    
    def __lt__(self,player):
        return self.score < player.score

    def __gt__(self,player):
        return self.score > player.score

    def __ge__(self,player):
        return self.score >= player.score

    def __le__(self,player):
        return self.score <= player.score
    
class Node(object): 
    def __init__(self,val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
        
        
class AVLTree(object):
    
    def insert_node(self, root, key): 
      
        # Step 1 - Perform normal BST 
        if not root: 
            return Node(key) 
        elif key < root.val: 
            root.left = self.insert_node(root.left, key) 
        else: 
            root.right = self.insert_node(root.right, key) 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if (balance) > 1 and (key <= root.left.val): 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if (balance < -1) and (key >= root.right.val): 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if (balance > 1) and (key > root.left.val): 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if (balance < -1) and (key < root.right.val): 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.val
            root.right = self.delete_node(root.right,
                                          temp.val)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balance = self.getBalance(root)

        # Balance the tree
        if balance > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balance < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
     

    # Function to perform left rotation
    def leftRotate(self, a):
        b = a.right
        T2 = b.left
        b.left = a
        a.right = T2
        a.height = 1 + max(self.getHeight(a.left),
                           self.getHeight(a.right))
        b.height = 1 + max(self.getHeight(b.left),
                           self.getHeight(b.right))
        return b

    # Function to perform right rotation
    def rightRotate(self, a):
        b = a.left
        T3 = b.right
        b.right = a
        a.left = T3
        a.height = 1 + max(self.getHeight(a.left),
                           self.getHeight(a.right))
        b.height = 1 + max(self.getHeight(b.left),
                           self.getHeight(b.right))
        return b

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)
    
    def getMaxValueNode(self, root):
        if root is None or root.right is None:
            return root
        return self.getMaxValueNode(root.right)
    

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.val)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)
    
    def InOrder(self,root, liste=[]):
        if root:
            self.InOrder(root.left, liste) 
            liste.append(root.val)
            self.InOrder(root.right, liste)

def nodes_count(node):
    if not node:
        return 0
    return 1 + nodes_count(node.right) + nodes_count(node.left) 

#Create the AVL tree with the players inside
def Creation_Tree():
    myTree = AVLTree()
    root = None
    
    while nodes_count(root)!=100:
        p = Player()
        root = myTree.insert_node(root, p)
    return root   

def update_player_score (myTree,root):
    li=[]
    myTree.InOrder(root,li)
    root=None
    for i in li:
        i.score = round(statistics.mean([random_player_score(),random_player_score(),random_player_score()]),2)
        root = myTree.insert_node(root,i)
    return root

def delete_last_ten_players(myTree,root):
    for i in range(10):
        root= myTree.delete_node(root,myTree.getMinValueNode(root).val)
    return root
            
def reinitiate_last_ten_players_score(myTree,root):
    li=[]
    myTree.InOrder(root,li)
    root=None
    for i in li:
        i.score = 0 #reinitiating score at 0
        root=myTree.insert_node(root,i)
    return root

def update_last_ten_players_score(myTree,root):
    li=[]
    myTree.InOrder(root,li)
    root=None
    for i in li:
        i.score = i.score = round(statistics.mean([random_player_score(),random_player_score(),random_player_score(),
                            random_player_score(),random_player_score()]),2)
        root=myTree.insert_node(root,i)
    return root
    
def Tournament():
    myTree = AVLTree()
    root = Creation_Tree()
    total_nb_players = nodes_count(root)
    print ("Here are the" + " " + str(total_nb_players) + " " + "players")
    print("________________________________________________________")
    myTree.printHelper(root, "", True) #print_in_RankingOrder(root)
    print ( str(total_nb_players) + " " + "players in total\n")
    
    while nodes_count(root)!=10:
        
        root = update_player_score(myTree,root)
        root = delete_last_ten_players(myTree,root)
    
    myTree.printHelper(root, "", True) #print_in_RankingOrder(root)
    print("\n")
    print ("Here are the last" + " " + str(nodes_count(root)) + " " + "players left\n")
    
    #Here start the final game between the last ten players left
    #We reinitiate the scire at 0
    print ("The score has been reinitiated for the last" + " " + str(nodes_count(root)) + " " + "players")
    print("________________________________________________________")
    root = reinitiate_last_ten_players_score(myTree,root)  
    myTree.printHelper(root, "", True) #print_in_RankingOrder(root)
    
    #After playing 5 games
    print("________________________________________________________")
    print("The score of the last" + " " + str(nodes_count(root)) + " " + "players :" )
    root = update_last_ten_players_score(myTree,root) 
    myTree.printHelper(root, "", True) #print_in_RankingOrder(root)
    winner = str(myTree.getMaxValueNode(root).val)
    winner_name = winner[6:12]
    winner_score = winner [20:23]
    print("\n")
    print("The winner is" + " " + winner_name + " " + "with the score of" + " " + winner_score)
    
    
    
if __name__ == "__main__":
    Tournament()  

