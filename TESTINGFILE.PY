import random




Rooms = []

for i in range(4):
    Rooms.append([])
    for _ in range(5):
        passorno = random.randint(1,2)
        if passorno == 1:
            Rooms[i].append("P")
        else:
            Rooms[i].append("N")

#IF player is in room[i][j]
#check whether if the direction
for i in Rooms:
    print(i)
#directions = [(0,0),(0,1),(1,0),(1,1)]
i = random.randint(0,len(Rooms)-1)
j = random.randint(0,len(Rooms[0])-1)
#print(i,j)
def checkifN(room,i,j):  
#what if i = 1 and j =2?
    roomstate = room[i][j]
    new_i = random.randint(0,len(room)-1)
    new_j = random.randint(0,len(room[0])-1)
    if roomstate == 'N':
        return checkifN(room,new_i,new_j)
    else:
        return roomstate,i,j
        
    
print(checkifN(Rooms,i,j))  
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