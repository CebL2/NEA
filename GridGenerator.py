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
            #print('row iter')
            for j in range(0,len(layout[0])):
                #print('inside iter')
                if layout[i][j] == 'R':
                    chance = [0,1]
                    decision = np.random.choice(chance,p=[0.3,0.7])
                    print(decision)
                    if decision == 1:
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
        for i in range(10):
            Rooms.append([])
            for _ in range(10):
                Rooms[i].append(" ")
       
        RoomsToAdd =  random.randint(20,60)
        randi = random.randint(0, len(Rooms)-1)
        randj = random.randint(0, len(Rooms[0])-1)
        Rooms[randi][randj] = "R"
        i = randi
        j = randj
        RoomsToAdd -=1
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
                    if RoomDirection == 'up':
                        if i ==0:
                            upcount+=1
                            continue
                        else:
                            if  Rooms[i-1][j] == "R":
                                i-= 1
                                upcount+=1
                                continue
                            else:
                                Rooms[i-1][j] = "R"
                                i-= 1
                                upcount =0
                    elif RoomDirection == 'down':
                        if i == len(Rooms)-1:
                            downcount+=1
                            continue
                        else:
                            if Rooms[i+1][j] == "R":
                                i+=1
                                downcount+=1
                                continue
                            else:
                                Rooms[i+1][j] = "R"
                                i+=1
                                downcount =0
                                    
                            
                    elif RoomDirection == 'left':
                        if j == 0:
                            leftcount+=1
                            continue
                        else:
                            if Rooms[i][j-1] == "R":
                                j-=1
                                leftcount+=1
                                continue
                            else:
                                Rooms[i][j-1] = "R"
                                j-=1
                                leftcount=0
                    elif RoomDirection == 'right':
                        if j == len(Rooms[0])-1:
                            rightcount+=1
                            continue
                        else:
                            if Rooms[i][j+1] == "R":
                                j+=1
                                rightcount+=1
                                continue
                            else:
                                Rooms[i][j+1] = "R"
                                j+= 1
                                rightcount = 0
                else:
                    #is corner       
                    if i == 0 and j == 0: #top left
                        if RoomDirection == 'left':# directions = ['up','down','left','right']
                            leftcount+=1
                            continue
                        elif RoomDirection == 'up':
                            upcount+=1
                            continue
                            #statements with i/j have to be kept in here, as it will add the "R" regardless of what hte value of i and j is
                        elif RoomDirection == 'down' :
                            if Rooms[i+1][j] == "R":
                                i+=1
                                downcount +=1
                                continue
                            else:
                                Rooms[i+1][j] = "R"
                                i+=1
                                downcount = 0
                        elif RoomDirection == 'right' : 
                            if Rooms[i][j+1] == "R" :
                                j+= 1
                                rightcount +=1
                                continue
                            else:
                                Rooms[i][j+1] == "R"
                                j+=1
                                rightcount=0
                    elif i == 0 and j == len(Rooms[0])-1 : #top right
                        if RoomDirection == 'right':
                            rightcount+=1
                            continue
                        elif RoomDirection == 'up':   # directions = ['up','down','left','right']
                            upcount+=1
                            continue
                        
                        elif RoomDirection == 'down' :
                            if Rooms[i+1][j] == "R":
                                i+=1
                                downcount +=1
                                continue
                            else:
                                Rooms[i+1][j] = "R"
                                i+=1
                                downcount = 0
                                
                        elif RoomDirection == 'left':
                            if Rooms[i][j-1] == "R":
                                j-= 1
                                leftcount+=1
                                continue
                            else:
                                Rooms[i][j-1] = "R"
                                j-=1
                                leftcount =0
                
                        
                    elif i == len(Rooms)-1 and j == 0 : #bottom left
                        if  RoomDirection == 'left' :
                            leftcount+=1
                            continue
                        elif RoomDirection == 'down':   # directions = ['up','down','left','right']
                            downcount+=1
                            continue
                        
                        elif RoomDirection == 'up':
                            if Rooms[i-1][j] == "R":
                                i-=1
                                upcount+=1
                                continue
                            else:
                                Rooms[i-1][j] = "R"
                                i-=1
                                upcount=0
                        elif RoomDirection == 'right' : 
                            if Rooms[i][j+1] == "R" :
                                j+= 1
                                rightcount +=1
                                continue
                            else:
                                Rooms[i][j+1] == "R"
                                j+=1
                                rightcount=0          
                    elif i == len(Rooms)-1 and j == len(Rooms[0])-1 : #bottom right
                        if RoomDirection == 'right' :
                            rightcount+=1
                            continue
                        elif RoomDirection == 'down':   # directions = ['up','down','left','right']
                            downcount+=1
                            continue
                        elif RoomDirection == 'up':
                            if Rooms[i-1][j] == "R":
                                i-=1
                                upcount+=1
                                continue
                            else:
                                Rooms[i-1][j] = "R"
                                i-=1
                                upcount=0
                                
                        elif RoomDirection == 'left':
                            if Rooms[i][j-1] == "R":
                                j-= 1
                                leftcount+=1
                                continue
                            else:
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