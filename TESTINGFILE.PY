import random

import numpy as np






# IF player is in room[i][j]
#check whether if the direction


#test = [1,2,3,4]





#j_value = roomstates.index(j)

#print(i_value,j_value)
      # if  i == len(room)-1 and j == len(room[0])-1 and room[row][col] == 'N': #if i = 1 and j =2
                    #     roomstate = room[row-x][col-y]
                    #     checkifN(room,i,j)
                    # elif i == 0 and j == 0 and room[row][col] == 'N':
                    #     roomstate = room[row+x][col+y]
#if i = 0, row can only add up
#if j = 0, col can only add up
#if i = length of list, row can only deduct
#if j = elnegth of sub list, col cna only deduct
#j = random.randint(0,len())
        # for x,y in directions:
        #     print(room[i+x])

 #room will be 3x3 for now
    #[['P', 'P', 'P'],
    # ['N', 'N', 'N'],
    # ['P', 'N', 'N']]
    #directions = [(0,0),(0,1),()]
    # player is put into one of the rooms
    # i = random.randint(0,2)
    # j = random.randint(0,2)
    #roomstate = Rooms[i][j]
    #if roomstate == "N"
    #check if any of the directions is a "P" and put the roomstate to that instead
    #else, i = random.randint(0,2)
    #    j = random.randint(0,2)
    #get random values again, then put roomstate into the new i and j values, roomstate = Rooms[i][j] (new i and j values)
    #for x,y in directions:
    #print(room[x][y])


#pygame.time
#if time is over 1000 ticks
#enemy difficulty will increase


#Player spawns
# roomstate = unlocked
# player goes into room
# does enemyspawn = true?
# if yes:
# roomstate = locked
# else:
# roomstate = unlocked
# if enemycount (or enemylist) is empty
# roomstate = unlocked


# does the player get hit?
# player dies
# exits to main menu
# (for the sake of simplicity, players can only take 1 hit for now.)
# asd = [3,4,5]  #we want [5,4,3]

# new = []
# #temphigh = 3
# print(len(asd))
# while len(new) <= len(asd)+1:
#     temphigh = asd[0]
#     for i in asd:
#         if temphigh  < i: #[3,4,5]
#             temphigh = i
#     new.append(i)
#     asd.remove(i)

# print(new)

def isBorder(i, i_length, j, j_length):
        if i == 0 or i == i_length or j== 0 or j == j_length:
            return True

def isCorner(i, i_length, j, j_length):
    if i == 0 and j == 0 or i == 0 and j == j_length or i == i_length and j == 0 or i == i_length and j == j_length:
        return True 
Room=[]

def Layout(Rooms):
    

    for i in range(10):
        Rooms.append([])
        for _ in range(10):
            Rooms[i].append(" ")
    print(len(Rooms))
    print(len(Rooms[0]))
    RoomsToAdd = 30# random.randint(20,60)
    
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
        print(i,j)
        for a in Rooms:
            print(a)
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
        print(RoomDirection)
        if not isBorder(i, len(Rooms)-1,j,len(Rooms[0])-1):
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
            if not isCorner(i,len(Rooms)-1, j,len(Rooms[0])-1):
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

new = Layout(Room)

for i in new:
    print(i)

