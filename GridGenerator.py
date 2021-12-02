import random

import numpy as np

class GridGenerator:
    def __init__(self):
        pass
    def isBorder(self,i, i_length, j, j_length):
        if i == 0 or i == i_length or j== 0 or j == j_length:
            return True

    def isCorner(self,i, i_length, j, j_length):
        if i == 0 and j == 0 or i == 0 and j == j_length or i == i_length and j == 0 or i == i_length and j == j_length:
            return True 
    def GenerateEnemyRoom(self,layout):
        BossToAdd = 1
        for i in range(0,len(layout)-1):
            for j in range(0,i):
               # print(j)
                if layout[i][j] == 'R':
                    chance = random.randint(0,1)
                    #print(chance)
                    if chance == 1:
                        layout[i][j] = 'E'
        
        for i in range(0,len(layout)-1):
            for j in range(0,i):
                if layout[i][j] == 'E':
                    layout[i][j] = 'B'
                    BossToAdd -= 1
                    break
            if BossToAdd ==0:
                break
        
        return layout
                    
    

    def Layout(self):
        Rooms = []

        for i in range(15):
            Rooms.append([])
            for _ in range(15):
                Rooms[i].append(" ")
        print(len(Rooms))
        print(len(Rooms[0]))
        RoomsToAdd = random.randint(25,75)
        
        #print(RoomCount)
        #direction = random.randint(0,3)
        randi = random.randint(0, len(Rooms)-1)
        randj = random.randint(0, len(Rooms[0])-1)
        
        Rooms[randi][randj] = "R"
        #print(i,j)
        #list = ['up','down','left','right']
        #print(np.random.choice(list,p=[1/4,1/4,]))
        i = randi
        j = randj
        #RoomsToAdd = 150
        print(RoomsToAdd,  'is the total number of rooms')
        RoomsToAdd -=1
        print(RoomsToAdd ,'is the amount of rooms to add')
        upcount = 0
        downcount = 0
        leftcount = 0
        rightcount = 0
        probup = 0.25
        probdown = 0.25
        probleft = 0.25
        probright = 0.25
        while RoomsToAdd > 0:
            if upcount >3:
                probup = 1/10
                probdown = 3/10
                probleft = 3/10
                probright = 3/10
                upcount = 0
            elif downcount >3:
                probup = 3/10
                probdown = 1/10
                probleft = 3/10
                probright = 3/10
                downcount = 0
            elif leftcount >3:
                probup = 3/10
                probdown = 3/10
                probleft = 1/10
                probright = 3/10
                leftcount = 0
            elif rightcount>3:
                probup = 3/10
                probdown = 3/10
                probleft = 3/10
                probright = 1/10
                rightcount = 0                 
            directions = ['up','down','left','right']
            RoomDirection = np.random.choice(directions,p=[probup,probdown,probleft,probright])
            
            if not self.isBorder(i, len(Rooms)-1,j,len(Rooms[0])-1):
                #not border
                if RoomDirection == 'up' and Rooms[i-1][j] == "R":  
                    i-= 1
                    upcount +=1
                    continue
                elif RoomDirection == 'up':  
                    Rooms[i-1][j] = "R"
                    i-= 1
                    upcount = 0
                #statements with i/j have to be kept in here, as it will add the "R" regardless of what hte value of i and j is
                elif RoomDirection == 'down' and Rooms[i+1][j] == "R":
                    i+=1
                    downcount +=1
                    continue
                elif RoomDirection == 'down':
                    Rooms[i+1][j] = "R"
                    i+=1
                    downcount = 0
                elif RoomDirection == 'right' and Rooms[i][j+1] == "R" :
                    j+= 1
                    rightcount +=1
                    continue
                    
                elif RoomDirection == 'right':
                    Rooms[i][j+1] = "R"
                    j+= 1
                    rightcount = 0
                elif RoomDirection == 'left' and Rooms[i][j-1] == "R":
                    j-=1
                    leftcount +=1
                    continue
                    
                elif RoomDirection == 'left':
                    Rooms[i][j-1] = "R"   
                    j-=1
                    leftcount = 0
                
            else: #is border
                if not self.isCorner(i,len(Rooms)-1, j,len(Rooms[0])-1):
                    #not corner
                    if i == 0 and RoomDirection == 'up': #top
                        RoomDirection = np.random.choice(directions,p=[0,1/3,1/3,1/3]) # directions = ['up','down','left','right']
                        if RoomDirection == 'down' and Rooms[i+1][j] == "R":
                            i+= 1
                            downcount +=1
                            continue
                        elif RoomDirection == 'down':
                            Rooms[i+1][j] = "R"
                            i+=1
                            downcount =0
                            
                        elif RoomDirection == 'right' and Rooms[i][j+1] == "R":
                            j+=1
                            rightcount +=1
                            continue
                        elif RoomDirection == 'right':
                            Rooms[i][j+1] = "R"
                            j+=1
                            rightcount = 0
                        elif RoomDirection == 'left' and Rooms[i][j-1] == "R":
                            j-= 1
                            leftcount += 1
                            continue
                        elif RoomDirection == 'left':
                            Rooms[i][j-1] = "R"
                            j-= 1
                            leftcount = 0
                            
                    elif i == len(Rooms)-1 and RoomDirection == 'down': #bot
                        RoomDirection = np.random.choice(directions,p=[1/3,0,1/3,1/3]) # directions = ['up','down','left','right']
                        if RoomDirection == 'up' and Rooms[i-1][j] == "R":
                            i-=1
                            upcount +=1
                            continue
                        elif RoomDirection == 'up':
                            Rooms[i-1][j] = "R"
                            i-=1
                            upcount = 0
                            
                        elif RoomDirection == 'right' and Rooms[i][j+1] == "R":
                            j+= 1
                            rightcount +=1
                            continue
                        elif RoomDirection == 'right':    
                            Rooms[i][j+1] = "R"
                            j+=1
                            rightcount = 0
                        elif RoomDirection == 'left' and Rooms[i][j-1] == "R":
                            j-= 1
                            leftcount +=1
                            continue
                            
                        elif RoomDirection == 'left':
                            Rooms[i][j-1] = "R"
                            j-= 1
                            leftcount = 0
                    elif j == 0 and RoomDirection == 'left':# left
                        RoomDirection = np.random.choice(directions,p=[1/3,1/3,0,1/3]) # directions = ['up','down','left','right']
                        if RoomDirection == 'down' and Rooms[i+1][j] == "R":
                            i+=1
                            downcount += 1
                            continue
                        elif RoomDirection == 'down':
                            Rooms[i+1][j] = "R"
                            i+=1
                            downcount = 0
                        elif RoomDirection == 'right' and Rooms[i][j+1] == "R":
                            j+=1
                            rightcount +=1
                            continue
                        elif RoomDirection == 'right':
                            Rooms[i][j+1] = "R"
                            j+=1
                            rightcount =0
                        elif RoomDirection == 'up' and Rooms[i-1][j] == "R":
                            i-=1
                            upcount +=1
                            continue
                        elif RoomDirection == 'up':
                            Rooms[i-1][j] = "R"
                            i-= 1
                            upcount = 0
                        
                    elif j == len(Rooms[0])-1 and RoomDirection == 'right':  #right
                        RoomDirection = np.random.choice(directions,p=[1/3,1/3,1/3,0]) 
                        if RoomDirection == 'down' and Rooms[i+1][j] == "R":
                            i+=1
                            downcount +=1
                            continue
                        elif RoomDirection == 'down':
                            Rooms[i+1][j] = "R"
                            i+=1
                            downcount =0
                        elif RoomDirection == 'up' and Rooms[i-1][j] == "R":
                            i-= 1
                            upcount +=1
                            continue
                        elif RoomDirection == 'up':
                            Rooms[i-1][j] = "R"
                            i-=1
                            upcount = 0
                        elif RoomDirection == 'left' and Rooms[i][j-1] == "R":
                            j-= 1
                            leftcount +=1
                            continue
                        elif RoomDirection == 'left':
                            Rooms[i][j-1] = "R"
                            j-= 1
                            leftcount =0 
                    else:  
                        if RoomDirection == 'up' and Rooms[i-1][j] == "R":   #checks the dircection given and whether if there is already a P inside the grid
                            i-= 1
                            upcount +=1
                            continue
                        elif RoomDirection == 'up':  
                            Rooms[i-1][j] = "R"
                            i-= 1
                            upcount =0
                        #statements with i/j have to be kept in here, as it will add the "R" regardless of what hte value of i and j is
                        elif RoomDirection == 'down' and Rooms[i+1][j] == "R":
                            i+=1
                            downcount +=1
                            continue
                        elif RoomDirection == 'down':
                            Rooms[i+1][j] = "R"
                            i+=1
                            downcount =0
                        elif RoomDirection == 'right' and Rooms[i][j+1] == "R" :
                            j+= 1
                            rightcount +=1
                            continue
                            
                        elif RoomDirection == 'right':
                            Rooms[i][j+1] = "R"
                            j+= 1
                            rightcount = 0
                        elif RoomDirection == 'left' and Rooms[i][j-1] == "R":
                            j-=1
                            leftcount +=1
                            continue
                            
                        elif RoomDirection == 'left':
                            Rooms[i][j-1] = "R"   
                            j-=1   
                            leftcount =0   
                else:
                    #is corner       
                    if i == 0 and j == 0: #top left
                        if RoomDirection == 'left' or RoomDirection == 'up':   # directions = ['up','down','left','right']
                            RoomDirection = np.random.choice(directions,p=[0,1/2,0,1/2])
                            if RoomDirection == 'down' and Rooms[i+1][j] == "R":
                                i+= 1
                                downcount +=1
                                continue
                            elif RoomDirection == 'down':
                                Rooms[i+1][j] = "R"
                                i+= 1
                                downcount = 0
                            elif RoomDirection == 'right' and Rooms[i][j+1] == "R":
                                j+= 1
                                rightcount +=1
                                continue
                            
                            elif RoomDirection == 'right':
                                Rooms[i][j+1] = "R"
                                j+= 1
                                rightcount =0
                        else:  
                        
                            #statements with i/j have to be kept in here, as it will add the "R" regardless of what hte value of i and j is
                            if RoomDirection == 'down' and Rooms[i+1][j] == "R":
                                i+=1
                                downcount +=1
                                continue
                            elif RoomDirection == 'down':
                                Rooms[i+1][j] = "R"
                                i+=1
                                downcount = 0
                            elif RoomDirection == 'right' and Rooms[i][j+1] == "R" :
                                j+= 1
                                rightcount +=1
                                continue
                                
                            elif RoomDirection == 'right':
                                Rooms[i][j+1] = "R"
                                j+= 1
                                rightcount = 0
                        
                    elif i == 0 and j == len(Rooms[0])-1 : #top right
                        if RoomDirection == 'right' or RoomDirection == 'up':   # directions = ['up','down','left','right']
                            RoomDirection = np.random.choice(directions,p=[0,1/2,1/2,0])
                            if RoomDirection == 'down' and Rooms[i+1][j]== "R":
                                i+= 1
                                downcount +=1
                                continue
                            elif RoomDirection == 'down':
                                Rooms[i+1][j] = "R"
                                i+= 1
                                downcount = 0
                            elif RoomDirection == 'left' and Rooms[i][j-1] == "R":
                                j-= 1
                                leftcount += 1
                                continue
                            elif RoomDirection == 'left':
                                Rooms[i][j-1] = "R"
                                j-= 1
                                leftcount = 0
                        else:  
                        
                            #statements with i/j have to be kept in here, as it will add the "R" regardless of what hte value of i and j is
                            if RoomDirection == 'down' and Rooms[i+1][j] == "R":
                                i+=1
                                downcount +=1
                                continue
                            elif RoomDirection == 'down':
                                Rooms[i+1][j] = "R"
                                i+=1
                                downcount = 0
                            elif RoomDirection == 'left' and Rooms[i][j-1] == "R":
                                j-=1
                                leftcount +=1
                                continue
                                
                            elif RoomDirection == 'left':
                                Rooms[i][j-1] = "R"   
                                j-=1 
                                leftcount =0
                    elif i == len(Rooms)-1 and j == 0 : #bottom left
                        if  RoomDirection == 'left' or RoomDirection == 'down':   # directions = ['up','down','left','right']
                            RoomDirection = np.random.choice(directions,p=[1/2,0,0,1/2])
                            if RoomDirection == 'up' and Rooms[i-1][j] == "R":
                                i-= 1
                                upcount +=1
                                continue
                            elif RoomDirection == 'up':
                                Rooms[i-1][j] = "R"
                                i-= 1
                                upcount =0
                            elif RoomDirection == 'right' and Rooms[i][j+1] == "R":
                                j+=1
                                rightcount +=1
                                continue
                            elif RoomDirection == 'right':
                                Rooms[i][j+1] = "R"
                                j+= 1
                                rightcount =0
                        else:  
                            if RoomDirection == 'up' and Rooms[i-1][j] == "R":   #checks the dircection given and whether if there is already a P inside the grid
                                i-= 1
                                upcount +=1
                                continue
                            elif RoomDirection == 'up':  
                                Rooms[i-1][j] = "R"
                                i-= 1
                                upcount =0
                            #statements with i/j have to be kept in here, as it will add the "R" regardless of what hte value of i and j is
                    
                                
                            elif RoomDirection == 'right' and Rooms[i][j+1] == "R" :
                                j+= 1
                                rightcount +=1
                                continue
                                
                            elif RoomDirection == 'right':
                                Rooms[i][j+1] = "R"
                                j+= 1
                                rightcount =0
                            
                    elif i == len(Rooms)-1 and j == len(Rooms[0])-1 : #bottom right
                        if RoomDirection == 'right' or RoomDirection == 'down':   # directions = ['up','down','left','right']
                            RoomDirection = np.random.choice(directions,p=[1/2,0,1/2,0])
                            if RoomDirection == 'up' and Rooms[i-1][j] == "R":
                                i-= 1
                                upcount +=1
                                continue
                            elif RoomDirection == 'up':
                                Rooms[i-1][j] = "R"
                                i-= 1
                                upcount =0 
                            elif RoomDirection == 'left' and Rooms[i][j-1] == "R":
                                j-= 1
                                leftcount +=1
                                continue
                            elif RoomDirection == 'left':

                                Rooms[i][j-1] = "R"
                                j-= 1
                                leftcount =0
                        else:  
                            if RoomDirection == 'up' and Rooms[i-1][j] == "R":   #checks the dircection given and whether if there is already a P inside the grid
                                i-= 1
                                upcount +=1
                                continue
                            elif RoomDirection == 'up':  
                                Rooms[i-1][j] = "R"
                                i-= 1
                                upcount = 0
                            #statements with i/j have to be kept in here, as it will add the "R" regardless of what hte value of i and j    
                            elif RoomDirection == 'left' and Rooms[i][j-1] == "R":
                                j-=1
                                leftcount +=1
                                continue
                            elif RoomDirection == 'left':
                                Rooms[i][j-1] = "R"   
                                j-=1 
                                leftcount =0                         
            RoomsToAdd -= 1
        return Rooms
    
    
Grid = GridGenerator()
layout = Grid.Layout()
newroom = Grid.GenerateEnemyRoom(layout)
for i in newroom:
    print(i)