import random

import numpy as np

   #if direction is up:
        #add a room upwards and decrease i by 1
        #but what if i is 0? i.e at the top
        #get a new direction with a probability of getting up to be 0
        #then add a room in the new direction and increment/decrease i/j accordingly
        
        #if direction is down:
        #add a room downwards and increase i by 1
        #if i is the length of the grid
        #new direction with the probability of getting down to be 0
        
        #if direction is right:
        #add a room to the right and increase j by 1
        #if j is length of sublist
        #new direction with the probability of getting right to be 0
        
        
        #if direction is left:
        #add a room to the left and decrease j by 1 
        #if j is 0
        #new direction with the probability of getting left to be 0
        #else
        
        #if direction is whatever
        #add a room in that direction 
        #this statement should be at the top to make things simpler and for code to run efficiently
        
#we have the map of the room, now we need to focus on the contents of it
class GridGenerator:
    def __init__(self):
        pass
    def isBorder(self,i, i_length, j, j_length):
        if i == 0 or i == i_length or j== 0 or j == j_length:
            return True

    def isCorner(self,i, i_length, j, j_length):
        if i == 0 and j == 0 or i == 0 and j == j_length or i == i_length and j == 0 or i == i_length and j == j_length:
            return True 


    def Layout(self):
        Rooms = []

        for i in range(40):
            Rooms.append([])
            for _ in range(39):
                Rooms[i].append(" ")
        print(len(Rooms))
        print(len(Rooms[0]))
        RoomsToAdd = random.randint(100,((len(Rooms))-30)*(len(Rooms[0])-19))
        
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
            #print(upcount,downcount,leftcount,rightcount)
            #print(RoomsToAdd)
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
           # print(probup,probdown,probleft,probright)
                        
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
for i in layout:
    print(i)