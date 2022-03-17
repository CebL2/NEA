
import random

import numpy as np

#loops=0
class GridGenerator: 
    def __init__(self, rooms,enemyrooms):
        self.rooms = rooms
        self.enemyrooms = enemyrooms
    def isBorder(self,i, i_length, j, j_length): #checks if the list element is on the border
        if i == 0 or i == i_length or j== 0 or j == j_length:
            return True
    def isCorner(self,i, i_length, j, j_length):
        if i == 0 and j == 0 or i == 0 and j == j_length or i == i_length and j == 0 or i == i_length and j == j_length: #checks if the list element is on the corner
            return True 
    def GenerateEnemyRoom(self,layout):
        BossToAdd = 1
     
        while self.enemyrooms > 0:
            for i in range(0,len(layout)-1):
                for j in range(0,len(layout[0])):
                    if self.enemyrooms == 0:
                        break
                    elif layout[i][j] == 'R':
                        chance = [0,1]
                        decision = np.random.choice(chance,p=[0.3,0.7])
                        if decision == 1:
                            layout[i][j] = 'E'
                            
                            self.enemyrooms -=1
        while BossToAdd>0:#heuristic approach
            for i in range(0,len(layout)-1):
                for j in range(0,len(layout[0])): 
                    if layout[i][j] == 'E':
                        chance = [0,1]
                        decision = np.random.choice(chance,p=[0.3,0.7])
                        if decision == 1:
                            layout[i][j] = 'B'
                            BossToAdd -= 1
                            return layout    
    def RecursiveAdd(self,currenti,currentj,NewLayout,RoomsLeft):
        RoomsToAdd = RoomsLeft 
        if RoomsToAdd == 0: #if there are no more rooms to add
            return NewLayout #return the layout or the array with the completed rooms
        Directionlist = [(0,1),(0,-1),(1,0),(-1,0)] 
        if self.isBorder(currenti,len(NewLayout)-1,currentj,len(NewLayout[0])-1): 
            if self.isCorner(currenti,len(NewLayout)-1,currentj,len(NewLayout[0])-1):
                if currenti == 0 and currentj == 0: #remove certain directions based on the conditions from the list
                    Directionlist.pop(1) #remove left and up
                    Directionlist.pop(2)
                elif currenti == 0 and currentj == len(NewLayout[0])-1:
                    Directionlist.pop(0)  #remove right and up
                    Directionlist.pop(2)
                elif currenti == len(NewLayout)-1 and currentj == len(NewLayout[0])-1: 
                    Directionlist.pop(0) #remove down and right
                    Directionlist.pop(1)
                elif currenti == len(NewLayout)-1 and currentj == 0: 
                    Directionlist.pop(1) #remove left and down
                    Directionlist.pop(1)
            else:
                if currenti == 0: 
                    Directionlist.pop(3)
                elif currenti == len(NewLayout)-1:
                    Directionlist.pop(2)  
                elif currentj == 0:
                    Directionlist.pop(1)
                else:
                    Directionlist.pop(0)             
        RandomDirection = Directionlist[random.randint(0,len(Directionlist)-1)] #takes a random direction based on how long the Directionlist is
        if NewLayout[currenti+RandomDirection[0]][currentj+RandomDirection[1]] == 'R': #it then adds that value of the chosen direction to each of the elements and checks if it's a available room
            currenti+=RandomDirection[0] #if the current position does contain 'R'
            currentj+=RandomDirection[1] #then add the current directions to the positions and start from there again
        else:
            NewLayout[currenti+RandomDirection[0]][currentj+RandomDirection[1]] = 'R' #otherwise, assign that position with 'R'
            RoomsToAdd-=1 #and decrease the roomstoadd by 1
        return self.RecursiveAdd(currenti,currentj,NewLayout,RoomsToAdd) #recursively call the function again until there are no more rooms to add
    def GenerateLayout(self): #generates the whole map
        Rooms = []
        for i in range(10): #first it creates a empty 10x10 array 
            Rooms.append([])
            for _ in range(10):
                Rooms[i].append(" ")
        RoomsToAdd =  self.rooms #then assigns the amount of rooms to RoomsToAdd
        randi = random.randint(0, len(Rooms)-1) #takes a random number based on the length of the room layout
        randj = random.randint(0, len(Rooms[0])-1)
        Rooms[randi][randj] = "R" #and assigns the element in that specific position "R"
        RoomsToAdd -=1  #and decrements the rooms to add by 1
        Rooms = self.RecursiveAdd(randi,randj,Rooms,RoomsToAdd) #the array is then passed through a recursive function to add rooms
        return Rooms