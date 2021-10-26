import random


#print(passorno)
#Rooms = ['P' and 'N' for i in range(10)]
Rooms = []

for i in range(3):
    Rooms.append([])
    for j in range(3):
        passorno = random.randint(1,2)
        #print(passorno)
        if passorno == 1:
            Rooms[i].append("P")
        else:
            Rooms[i].append("N")

room = [['P','P','N'],
        ['N','P','P']]
directions = [(0,0),(0,1),(1,0),(1,1)]
# for i in range(0,len(room)):
#     for j in range(0,len(room[i])):
#         for x,y in directions:
#             print(room[i+x])

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
for x,y in directions:
    print(room[x][y])
  

      
      
  
        
