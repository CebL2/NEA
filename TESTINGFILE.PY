import random

import numpy as np

#we have the map of the room, now we need to focus on the contents of it

def isBorder(i, i_length, j, j_length):
    if i == 0 or i == i_length or j== 0 or j == j_length:
        return True

def Room(Rooms):
    #Rooms = []
   # directions = [(1,0),(0,1)]
    for i in range(4):
        Rooms.append([])
        for _ in range(4):
            Rooms[i].append(" ")
    RoomsToAdd = random.randint(6,(len(Rooms)*len(Rooms[0])-3))
    #print(RoomCount)
    direction = random.randint(0,3)
    randi = random.randint(0, len(Rooms)-1)
    randj = random.randint(0, len(Rooms[0])-1)
    Rooms[randi][randj] = "P"
    #print(i,j)
    #list = ['up','down','left','right']
    #print(np.random.choice(list,p=[1/4,1/4,]))
    i = randi
    j = randj
    while RoomsToAdd > 0:
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
        
        
        directions = ['up','down','left','right']
        RoomDirection = np.random.choice(directions,p=[0.25,0.25,0.25,0.25])
        
        if not isBorder(i, len(Rooms)-1,j,len(Rooms[0])-1):
            
         #picks a direction from the list with equal probability
            if RoomDirection == 'up' and Rooms[i-1][j] != "P":   #checks the dircection given and whether if there is already a P inside the grid
                Rooms[i-1][j] = "P"
                i-= 1
            #statements with i/j have to be kept in here, as it will add the "P" regardless of what hte value of i and j is
            elif RoomDirection == 'down' and Rooms[i+1][j] != "P":
                Rooms[i+1][j] = "P"
                i+=1
                RoomsToAdd -= 1
            elif RoomDirection == 'right' and Rooms[i][j+1] != "P" :
                Rooms[i][j+1] = "P"
                j+= 1
                RoomsToAdd -= 1
            elif RoomDirection == 'left' and Rooms[i][j-1] == "P":
                Rooms[i][j-1] = "P"
                j-=1
                RoomsToAdd -= 1
        else: #is border
            if i == 0 and RoomDirection == 'up':
                RoomDirection = np.random.choice(directions,p=[0,1/3,1/3,1/3])
                if RoomDirection == 'down' and Rooms[i+1][j] != "P":
                        Rooms[i+1][j] = "P"
                        i+=1
                        RoomsToAdd -= 1
                elif j == len(Rooms[0])-1 and RoomDirection == 'right' and Rooms[i][j+1] != "P":
                    Rooms[i][j+1] = "P"
                    j+=1
                    RoomsToAdd -= 1
                elif j == 0 and RoomDirection == 'left' and Rooms[i][j+1] != "P":
                    #RoomDirection == 'left' and Rooms[i][j-1] != "P" :
                    Rooms[i][j-1] = "P"
                    j-= 1
                    RoomsToAdd -= 1
                    
            elif i == len(Rooms)-1 and RoomDirection == 'down':
                RoomDirection = np.random.choice(directions,p=[0,1/3,1/3,1/3])
                if RoomDirection == 'down' and Rooms[i+1][j] != "P":
                        Rooms[i+1][j] = "P"
                        i+=1
                        RoomsToAdd -= 1
                elif j == len(Rooms[0])-1 and RoomDirection == 'right' and Rooms[i][j+1] != "P":
                    Rooms[i][j+1] = "P"
                    j+=1
                    RoomsToAdd -= 1
                elif j == 0 and RoomDirection == 'left' and Rooms[i][j+1] != "P":
                    #RoomDirection == 'left' and Rooms[i][j-1] != "P" :
                    Rooms[i][j-1] = "P"
                    j-= 1
                    RoomsToAdd -= 1
            elif j == 0 and RoomDirection == 'left':
                RoomDirection = np.random.choice(directions,p=[0,1/3,1/3,1/3])
                if RoomDirection == 'down' and Rooms[i+1][j] != "P":
                    Rooms[i+1][j] = "P"
                    i+=1
                    RoomsToAdd -= 1
                elif j == len(Rooms[0])-1 and RoomDirection == 'right' and Rooms[i][j+1] != "P":
                    Rooms[i][j+1] = "P"
                    j+=1
                    RoomsToAdd -= 1
                elif j == 0 and RoomDirection == 'left' and Rooms[i][j+1] != "P":
                    #RoomDirection == 'left' and Rooms[i][j-1] != "P" :
                    Rooms[i][j-1] = "P"
                    j-= 1
                    RoomsToAdd -= 1
            elif j == 0 and RoomDirection == 'left':
                RoomDirection = np.random.choice(directions,p=[0,1/3,1/3,1/3])
                if RoomDirection == 'down' and Rooms[i+1][j] != "P":
                    Rooms[i+1][j] = "P"
                    i+=1
                    RoomsToAdd -= 1
                elif j == len(Rooms[0])-1 and RoomDirection == 'right' and Rooms[i][j+1] != "P":
                    Rooms[i][j+1] = "P"
                    j+=1
                    RoomsToAdd -= 1
                elif j == 0 and RoomDirection == 'left' and Rooms[i][j+1] != "P":
                    #RoomDirection == 'left' and Rooms[i][j-1] != "P" :
                    Rooms[i][j-1] = "P"
                    j-= 1
                    RoomsToAdd -= 1
                
            else:
                randomi = random.randint(0,1)  #(1,1)
                randomj = random.randint(-1,1)  (1,-1)
                if randomi == 0 and randomj == -1: 
                    j -= 1
                elif randomi == 0 and randomj == 1:
                    j += 1
                else:
                    i +=1
                
            #if i == len(Rooms)-1 
                        

            # elif i == len(Rooms)-1 and RoomDirection == 'right':
            #         RoomDirection = np.random.choice(directions,p=[0,1/3,1/3,1/3])
            #         if j != 0:
            #             Rooms[i][j-1] = "P"
            #             j-=1

            #     else:
            #         RoomDirection = np.random.choice(directions,p=[0,0.5,0,0.5])
            #         if RoomDirection == 'down' and Rooms[i+1][j] != "P":
            #             Rooms[i+1][j] = "P"
            #             i+=1
            #         elif RoomDirection == 'right' and Rooms[i][j+1] != "P" :
            #             Rooms[i][j+1] = "P"
            #             j+= 1
            # elif RoomDirection == 'right' and  Rooms[i][j+1] != "P":
            #     if j != 0:
            #         Rooms[i][j+1] = "P"
            #         j+=1

            #     else:
            #         RoomDirection = np.random.choice(directions,p=[0,0.5,0,0.5])
            #         if RoomDirection == 'down' and Rooms[i+1][j] != "P":
            #             Rooms[i+1][j] = "P"
            #             i+=1
            #         elif RoomDirection == 'left' and Rooms[i][j-1] != "P" :
            #             Rooms[i][j+1] = "P"
            #             j+= 1
            # elif j != 0:
            #     if RoomDirection == 'up' and Rooms[i-1][j] != "P":
            #         if j != 0:
            #             Rooms[i-1][j] = "P"
            #             i-= 1
            #         else:
            #             RoomDirection = np.random.choice(directions,p=[0,0.5,0,0.5])
            #             if RoomDirection == 'down' and Rooms[i+1][j] != "P":
            #                 Rooms[i+1][j] = "P"
            #                 i+=1
            #             elif RoomDirection == 'right' and Rooms[i][j+1] != "P" :
            #                 Rooms[i][j+1] = "P"
            #                 j+= 1


            # elif RoomDirection == 'left' and Rooms[i][j-1] != "P":
            #     if j != 0:
            #         Rooms[i][j-1] = "P"
            #         j-=1

            #     else:
            #         RoomDirection = np.random.choice(directions,p=[0,0.5,0,0.5])
            #         if RoomDirection == 'down' and Rooms[i+1][j] != "P":
            #             Rooms[i+1][j] = "P"
            #             i+=1
            #         elif RoomDirection == 'right' and Rooms[i][j+1] != "P" :
            #             Rooms[i][j+1] = "P"
            #             j+= 1


            #     #RoomDirection = np.random.choice(directions,p[0,1/3,1/3,1/3])

            # elif RoomDirection == 'right' and  Rooms[i][j+1] != "P":
            #     if j != 0:
            #         Rooms[i][j+1] = "P"
            #         j+=1

            #     else:
            #         RoomDirection = np.random.choice(directions,p=[0,0.5,0,0.5])
            #         if RoomDirection == 'down' and Rooms[i+1][j] != "P":
            #             Rooms[i+1][j] = "P"
            #             i+=1
            #         elif RoomDirection == 'left' and Rooms[i][j-1] != "P" :
            #             Rooms[i][j+1] = "P"
            #             j+= 1

            #     Rooms[i+1][j] == "P"
            #     i+=1

        # if RoomDirection == 'right':
        #     if j == len(Rooms[0])-1:
        #         if i == len(Rooms[0])-1:
        #             RoomDirection = np.random.choice(directions,p=[0,0.5,0,0.5])
        #             if RoomDirection == 'down':
        #                 Rooms[i+1][j] = "P"
        #                 i+=1
        #             else:
        #                 Rooms[i][j-1] = "P"
        #                 j-= 1

                #and i == 0 and j == 0: #and we want to add left but we're at the edge
        #     RoomDirection = np.random.choice(directions,p=[0,0.5,0,0.5])
        #     if RoomDirection == 'down':
        #         Rooms[i+1][j] = "P"
        #         i+=1
        #     else:
        #         Rooms[i][j+1] = "P"
        #         j+= 1
        # elif RoomDirection == 'right' or RoomDirection == 'up' and i ==0 and j == len(Rooms[0]) -1:
        #     RoomDirection = np.random.choice(directions,p=[0,0.5,0.5,0])
        #     if RoomDirection == 'down':
        #         Rooms[i+1][j] = "P"
        #         i+=1
        #     else:
        #         Rooms[i][j-1] = "P"
        #         j-= 1
        # elif RoomDirection == 'down' or RoomDirection == 'right' and i == len(Rooms)-1 and j == len(Rooms[0]) -1:
        #     RoomDirection = np.random.choice(directions, p =[0.5,0,0.5,0])
        #     if RoomDirection == 'up':
        #         Rooms[i-1][j] = "P"
        #         i-=1
        #     else:
        #         Rooms[i][j+1] = "P"
        #         j+= 1
        # elif RoomDirection == 'down' or RoomDirection == 'left' and i == len(Rooms)-1 and j == 0:
        #     RoomDirection = np.random.choice(directions, p =[0.5,0,0,0.5])
        #     if RoomDirection == 'up':
        #         Rooms[i-1][j] = "P"
        #         i-=1
        #     else:
        #         Rooms[i][j+1] = "P"
        #         j+= 1



            RoomsToAdd -= 1
    return Rooms

#print(1)
#Rooms = []

one = 1
two = 2
three = 3
loop = 0
while loop < 5:
    print(loop)
    if one == 1:
        loop+=1
    
    # if one == 1:
    #     loop+=1



#print('test')
#index = random.randint(0,len(Rooms))
#for i in Rooms:






#if room = p
#no enemy spawn
#if room = e
#enemy spawn
#if room = b
#boss




#room generator
#choose a index to append P based on condition
#if you meet a wall, go back one step or add a room adjacently depending on probability
#
#print()


#print(len(Rooms)*len(Rooms[0]))

#if corners are popped, then the adjacent ones CANNOT be popped
#



# def checkifAdja(Rooms):
#     print(len(Rooms))
#     convertcount = 0
#     for i in range(len(Rooms)-1):
#         for j in range(len(Rooms[0])-1):
#             if i == 0 and j == 0:
#                 if Rooms[i][j] == "N" and Rooms[i+1][j] == "P"  and Rooms[i][j+1] == "P":
#                     #passable = random.randint(1,2)
#                     #if passable == 1:
#                         Rooms[i][j] = "P"
#                         convertcount += 1
#                     #else:
#                        # Rooms[i][j+1] = "P"
#             if i == 0:
#                 if Rooms[i][j] == "P" and Rooms[i+1][j] == "N":

#             if i == 0 and j == len(Rooms[0])-1:
#                 if Rooms[i][j] == "N" and Rooms[i+1][j] == "P"  and Rooms[i][j-1] == "P":
#                    # passable = random.randint(1,2)
#                    # if passable == 1:
#                         Rooms[i][j] = "P"
#                    # else:
#                       #  Rooms[i][j-1] = "P"
#             if i == len(Rooms)-1 and j == 0:
#                 if Rooms[i][j] == "N" and Rooms[i-1][j] == "P"  and Rooms[i][j+1] == "P":
#                     #passable = random.randint(1,2)
#                     #if passable == 1:
#                         Rooms[i][j] = "P"
#                    # else:
#                        # Rooms[i][j-1] = "P"
#             if i == len(Rooms)-1 and j == len(Rooms[0])-1:
#                 if Rooms[i][j] == "N" and Rooms[i-1][j] == "P"  and Rooms[i][j-1] == "P":
#                     #passable = random.randint(1,2)
#                     #if passable == 1:
#                         Rooms[i][j] = "P"
#                    # else:
#                     #    Rooms[i][j-1] = "P"

#                     #passable = random.randint(1,4)


#                     if Rooms[i][j-1] == "N":

#                     if Rooms[i+1][j] == "N":

#                     if   Rooms[i][j+1] == "N":

#                             Rooms[i+1][j] = "P"

#                             Rooms[i][j-1] = "P"

#                             Rooms[i-1][j] = "P"

#                             Rooms[i][j] = "P"

 #print(i,j)

#Rooms = []


#for i in new:
 #   print(i)
i = 0
j = 1
    #from the position of hte current P, get position of adjacent N and compare it to the (i+1,j+1), (i-1,j+1), (i-1,j-1), (i+1,j-1) position in the listq

    #if current position is P AND there isn't at least one P in 4 directions:
#choose a random adjacent N and make it P

def checkifN(room,i,j):
    #what if i = 1 and j =2?
        roomstate = room[i][j]
        new_i = random.randint(0,len(room)-1)
        new_j = random.randint(0,len(room[0])-1)
        if roomstate == 'N':
            return checkifN(room,new_i,new_j)
        else:
            return roomstate,i,j
#IF player is in room[i][j]
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