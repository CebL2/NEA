import random



#we have the map of the room, now we need to focus on the contents of it
def Room(Rooms):
   # directions = [(1,0),(0,1)]
    for i in range(4):
        Rooms.append([])
        for _ in range(4):
            Rooms[i].append(" ")
    RoomCount = random.randint(6,(len(Rooms)*len(Rooms[0])-3)) 
    print(RoomCount)
    direction = random.randint(0,3)
    i = random.randint(0, len(Rooms)-1)
    j = random.randint(0, len(Rooms[0])-1)
    Rooms[i][j] = 'P'
    for i_index, i_val in enumerate(Rooms):
        for j_index, j_val in enumerate(i_val):
            while RoomCount > 0:
                if j_val == 'P' and i_index == 0:
                    RoomsToAdd = random.randint(0,4)
                    for _ in range(0,RoomsToAdd):
                        Rooms[i_index][j_index+1] = "P"
                        
                
                
            
            #if j_index == 0:
                
            
            
            
            #print(j_index)
           # current = Rooms[i][j]
    
    
    #if i == 0:
    
        
    return Rooms


Rooms = []
Rooms = Room(Rooms)

for i in Rooms:
    print(i)

#index = random.randint(0,len(Rooms)) 
#for i in Rooms:
    
        
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
   
Rooms = []


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