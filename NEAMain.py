import os
import pygame, sys, random
from GridGenerator import *
from Obstacles import *
from Units import *
from Hud import*
import pickle
#custom and built in libraries imported


pygame.init() #initialises the library

def Main():  
    '''
    Main function
    '''
    while 1:
        MainGame = Game() 
        MainGame.MainMenu()
        del MainGame  
        #the purpose of this is as long as the user does not quit the program, a new instance of the class can be made again in the event the user dies in the game

class GameStats:
    def __init__(self,boss=None, Map = None, pos = None, traversed = None, health = None, Level = 0):
        self.BossPos = boss
        
        self.Map = Map
        self.globalpos = pos
        
        self.traversed = traversed
        self.Health = health
        self.Level = Level
        
class Game:  
    '''
    Main game class
    '''
    def __init__(self):
        
        self.stats = GameStats()
        self.player = None
        
        self._screen = pygame.display.set_mode((1920,1080))
        self._White = (255,255,255) #preset values for colour and resolution
        self._Black = (0,0,0)
        self._Red = (255,0,0)
        self._Gray = (220,220,220)
        self._Green = (0,255,0)
        self._screenx = 1920
        self._screeny = 1080 #protected variables
        #self._texfont= pygame.font.Font(r'..\')
        self._textfont = pygame.font.Font(r'fonts\georgia.ttf', 50 ) #fonts for text
        self._bigtextfont= pygame.font.Font(r'fonts\georgia.ttf', 70 )
        self._symbol = pygame.font.Font(r'fonts\seguisym.ttf', 50)
        self._clock = pygame.time.Clock()
        
        self.cooldowntime = 1000
        self.cooldowncap = 500

        self.enemies = pygame.sprite.Group()   #preset sprite groups to be used for collision purposes
        self.playersp = pygame.sprite.Group()
        self.ObstacleGroup = pygame.sprite.Group()
        self.AmountOfRooms = 20
        self.health = 3
        self.AmountOfEnemyRooms = 12
        self.upperbound = 3
        self.MaxRooms = 40
        self.MaxEnemy = 30
        
    def checkifRoom(self,room,i,j,limit): 
        '''
        checks whether if a element in the list is a room
        '''
        limit+=1
        if limit <100: #since this is a recursive function, to prevent overflow, on the 100th attempt, it will find the next available suitable element rather than randomly choosing one
            for row in range(0,len(room)-1):
                for col in range(0,len(room[0])):
                    if room[row][col] == 'R':
                        return row,col
        roomstate = room[i][j]
        new_i = random.randint(0,len(room)-1)
        new_j = random.randint(0,len(room[0])-1)
        if roomstate != 'R': #if the roomstate isn't R (i.e its E or B)
            return self.checkifRoom(room,new_i,new_j,limit) #recurssive call the function to check again
        else:
            return i,j 
    def GenerateMap(self):  
        '''
        Calls a class imported from a separate file to generate grid
        '''
        BossPos = None
        Grid = GridGenerator(self.AmountOfRooms,self.AmountOfEnemyRooms) #calls the class 
        Rooms = Grid.GenerateLayout() #generates the room, outputs a list #no issues
        Map = Grid.GenerateEnemyRoom(Rooms) #input is a list, the output is a modified version of the list
        for i in range(0,len(Map)-1):
            for j in range(0,len(Map[0])):
                if Map[i][j] == 'B':
                    BossPos = i,j
        return Map,BossPos
            
    def Save(self): 
        '''
        save function to save player progress
        '''
        obslist=[]
        with open("file1", "wb") as file1:
            pickle.dump(self.stats,file1)
            pickle.dump(self.player.rect.center,file1)
        with open("file2","wb") as file2: #in this file, it saves every single obstacle's information 
            for obstacle in self.ObstacleGroup:
                newdict = {}
                newdict['i'] = obstacle.i
                newdict['j'] = obstacle.j
                newdict['xsize'] = obstacle.xsize
                newdict['ysize'] = obstacle.ysize
                newdict['xcenter'] = obstacle.xcenter
                newdict['ycenter'] = obstacle.ycenter
                obslist.append(newdict)
            pickle.dump(obslist,file2)
            
    def Load(self):
        '''
        Load function to load save file
        '''
        try: #error handle in case if the file does not exist
            with open("file1","rb") as file1:
                statsobj = pickle.load(file1)  
                playercenter = pickle.load(file1)
            with open("file2","rb") as file2:
                obstacles = pickle.load(file2)
        except:
            return False
        return statsobj,playercenter,obstacles
    def RunGame(self,File=None,health=3,enemyHealthInc=0): 
        '''
        runs the game, there are preset values incase changes occur during the game
        '''
        #bstacleGroup = pygame.sprite.Group() #initialises a sprite group for obstacles
        if File != None:  #if the file is not empty
            NewStats = File[0]
            self.stats = GameStats(NewStats.BossPos,NewStats.Map,NewStats.globalpos,NewStats.traversed,NewStats.Health,NewStats.Level)
            playercenter = File[1]
            obstaclelist = File[2]
            if self.cooldowntime > self.cooldowncap:
                self.cooldowntime -= 10*self.stats.Level
            GameHud = Hud(self._screen,self.stats.Health) #Hud to display health
            self.player = Player(self._screenx,self._screeny,(50,50),self._Green,playercenter[0],playercenter[1]) #player information to be passed on
            for obstacle in obstaclelist: #from the saved list of obstacles
                obs = RoomObstacles(obstacle['i'],obstacle['j'],obstacle['xsize'],obstacle['ysize'],obstacle['xcenter'],obstacle['ycenter'])
                self.ObstacleGroup.add(obs) #assign the values of the previous obstacles, and add them to the sprite group
            playerpos = self.stats.globalpos
            currentpos = playerpos
            Map = MiniMap(self._screen,self.stats.Map,self.stats.traversed) 
        else: #if the file is empty 
            GameHud = Hud(self._screen,health)
            self.player = Player(self._screenx,self._screeny,(50,50),self._Green)
            self.stats.Map,BossPos = self.GenerateMap() #generates a map and the position of the boss room within the map
            self.stats.BossPos = BossPos
            Roomi = random.randint(0,len(self.stats.Map)-1) 
            Roomj = random.randint(0,len(self.stats.Map[0])-1)
            roompos = self.checkifRoom(self.stats.Map,Roomi,Roomj,0) #and pass it through a function to check whether if its a valid room with no enemies 
            self.stats.Map[roompos[0]][roompos[1]] = "#"  #player symbol
            playerpos = (roompos[0],roompos[1])  #a tuple to represent the player position on the self.stats.Map
            #by default, there are no enemies in the room 
            currentpos = playerpos
            Map = MiniMap(self._screen,self.stats.Map)
            self.stats.globalpos = (playerpos[0],playerpos[1])
            self.stats.Health = 3
        
            
            for i,value in enumerate(self.stats.Map):  #iterates the entire self.stats.Map to add a separate obstacle,
                for j,val in enumerate(value):  
                    if (i,j) == playerpos: #if the position is the starting room, there will be no obstacles added
                        continue
                    randomobs = random.randint(1,4) #otherwise, create a random number of 1-4 obstacles
                    for _ in range(0,randomobs):
                        obs = RoomObstacles(i,j)
                        if (i,j) == BossPos: #if the position is the boss room
                            self.randomxcenter1 = random.randint(300,500) #manipulate where the obstacles and be put to make sure it does not cover the exit to the next level
                            self.randomxcenter2 = random.randint(1500,1700)
                            self.randomycenter1 = random.randint(300,400)
                            self.randomycenter2 = random.randint(800,900)
                        self.ObstacleGroup.add(obs) #adds the obstacle to the spirte group
        ObstacleToDraw = pygame.sprite.Group()  #ObstacleToDraw is a separate group where it contains the obstacles to be drawn, ObstacleGroup has all the details of each obstacle,
                                                #this sprite group is so that it can be drawn onto the surface of the game                             
        alphaset = 0  #preset values for further use
        TimesSpawned = 0  
        EnemyInRoom = 0
        running = 1
        BossDefeated = 0
      
        
        IsBoss = False
        Invincibility_time = pygame.USEREVENT+0  #short for Invincibility Frames, this is a custom event id.
        Invincibility= pygame.event.Event(Invincibility_time) #a custom event to be used later on
        
        attackevent = pygame.USEREVENT+1
        enemyAttack = pygame.event.Event(attackevent)
        
        check = 0 
        enemycheck = 0
        
        NextLevel = pygame.Surface((150,150))  #exit to the next level
        NextLevel.set_alpha(0) 
        NextLevel.fill((50,50,50))
        
        
        self.playersp.add(self.player)
     
        while running:  
            self._clock.tick(60) #caps the frame rate at 60 frames per second
            self.stats.traversed = Map.traversedlist
            runningtime = pygame.time.get_ticks() #used for certain events
            pygame.mouse.set_visible(0) #hides the cursor
            self._screen.fill(self._White) 
            TopLeft = pygame.draw.rect(self._screen,self._Black,(0,0,700,40))    #walls/borders, there are variants of wall as the 'exit' to different rooms will be a separate wall
            TopRight = pygame.draw.rect(self._screen,self._Black,(1220,0,700,40))
            DownLeft = pygame.draw.rect(self._screen, self._Black, (0,1040, 700,40))
            DownRight = pygame.draw.rect(self._screen, self._Black, (1220,1040, 700,40))
            LeftUp = pygame.draw.rect(self._screen, self._Black, (0,0, 40,350))
            LeftDown = pygame.draw.rect(self._screen, self._Black, (0,730, 40,350))
            RightUp = pygame.draw.rect(self._screen, self._Black, (1880,0,40,350))
            RightDown = pygame.draw.rect(self._screen, self._Black,  (1880,730,40,350))
            
            #obstacles
            if currentpos != playerpos:#check which position is it currently
                ObstacleToDraw.empty() #empties the group if the player position is not the same as the current position stored
            for obstacle in self.ObstacleGroup:
                if obstacle.i == playerpos[0] and obstacle.j == playerpos[1]: #checks if the position of the player is the same as the information in each obstacle
                    ObstacleToDraw.add(obstacle) #adds the obstacle to be drawn into the group    

            #obstacle collision
            if LeftUp.colliderect(self.player.rect) or LeftDown.colliderect(self.player.rect):    #these statements make sure that the player does not go through the borders
                self.player.rect.x = 40
            if RightUp.colliderect(self.player.rect) or RightDown.colliderect(self.player.rect):  #tried to use elif statements, but if the player inputs two directions when already agianst a while, the player goes through the wall
                self.player.rect.x = 1830  
            if DownLeft.colliderect(self.player.rect) or DownRight.colliderect(self.player.rect):
                self.player.rect.y = 990
            if TopLeft.colliderect(self.player.rect) or TopRight.colliderect(self.player.rect):
                self.player.rect.y = 40
            
            if EnemyInRoom == 0:  #if there are no enemies in the room, then check the player position on the self.stats.Map and see if the adjacent rooms are passable or not.
                                      #if the adjacent room/element is empty (not P, E or B), then a self._Black wall will replace the self._White wall in that corresponding place
                if playerpos[0] != len(self.stats.Map)-1: #checks if the player is at a border
                    if self.stats.Map[playerpos[0]+1][playerpos[1]] == 'R' or self.stats.Map[playerpos[0]+1][playerpos[1]] == 'E' or self.stats.Map[playerpos[0]+1][playerpos[1]] == 'B':
                        DownExit= pygame.draw.rect(self._screen,self._White,(700,1040,520,40))
                        if self.stats.Map[playerpos[0]+1][playerpos[1]] == 'E' or self.stats.Map[playerpos[0]+1][playerpos[1]] == 'B':  #if the corresponding room has an enemy
                            if DownExit.colliderect(self.player.rect):  #and the player has collided the exit rect/exited the room
                                self.player.projectilegroup.empty()
                                IsBoss = self.BossOrNot(self.stats.Map[playerpos[0]+1][playerpos[1]])
                                self.player.rect.x = self._screenx/2  #set values to put them at where they would appear when going through a room from a certain side
                                self.player.rect.y = 100
                                EnemyInRoom = 1 #set to 1, certain conditions will be applied 
                                self.stats.Map[playerpos[0]][playerpos[1]] = 'R'  #as the player position hasnt been changed, the value gets changed to R as 'Room'
                                self.stats.Map[playerpos[0]+1][playerpos[1]] = '#' #the adjacent room gets changed into the player symbol
                                currentpos = playerpos
                                playerpos = (playerpos[0]+1,playerpos[1]) #then, the player position gets changed accordingly
                                self.stats.globalpos = (playerpos[0],playerpos[1])
                        else: 
                            if DownExit.colliderect(self.player.rect): #if the adjacent room has no enemies,
                                self.player.projectilegroup.empty() 
                                self.player.rect.x = self._screenx/2 #then similar operations occur apart from the EnemInRoom being modified.
                                self.player.rect.y = 100
                                self.stats.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.stats.Map[playerpos[0]+1][playerpos[1]] = '#'
                                currentpos = playerpos
                                playerpos = (playerpos[0]+1,playerpos[1])
                                self.stats.globalpos = (playerpos[0],playerpos[1])   
                                      
                    else:
                        DownExit= pygame.draw.rect(self._screen,self._Black,(700,1040,520,40)) #if there is no room available, then draw a self._Black rectangle
                        if DownExit.colliderect(self.player.rect): #if the player collides into it: 
                            self.player.rect.y = 990        #the player will stay in place 
                else:
                    DownExit= pygame.draw.rect(self._screen,self._Black,(700,1040,520,40)) #this is to check whether if the player is at a border or not
                    if DownExit.colliderect(self.player.rect): 
                        self.player.rect.y = 990    
                        
                        #the code above handles when the player goes to a exit downwards
                        #rest of the code are relatively similar to this one as its just a different side   
                               
                if playerpos[0] != 0:
                    
                    #Top exit
                    if self.stats.Map[playerpos[0]-1][playerpos[1]] == 'R' or self.stats.Map[playerpos[0]-1][playerpos[1]] == 'E'or self.stats.Map[playerpos[0]-1][playerpos[1]] == 'B':
                        TopExit = pygame.draw.rect(self._screen,self._White,(700,0,520,40))
                        if self.stats.Map[playerpos[0]-1][playerpos[1]] == 'E' or self.stats.Map[playerpos[0]-1][playerpos[1]] == 'B':
                            if TopExit.colliderect(self.player.rect) :
                                self.player.projectilegroup.empty()
                                IsBoss = self.BossOrNot(self.stats.Map[playerpos[0]-1][playerpos[1]])
                                self.player.rect.x = self._screenx/2
                                self.player.rect.y = self._screeny-100
                                EnemyInRoom = 1        
                                self.stats.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.stats.Map[playerpos[0]-1][playerpos[1]] = '#'
                                currentpos = playerpos
                                playerpos = (playerpos[0]-1,playerpos[1])
                                self.stats.globalpos = (playerpos[0],playerpos[1])
                              
                              
                        else :
                            if TopExit.colliderect(self.player.rect): 
                                self.player.projectilegroup.empty()
                                self.player.rect.x = self._screenx/2
                                self.player.rect.y = self._screeny-100
                                self.stats.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.stats.Map[playerpos[0]-1][playerpos[1]] = '#'
                                currentpos = playerpos
                                playerpos = (playerpos[0]-1,playerpos[1])
                                self.stats.globalpos = (playerpos[0],playerpos[1])
                                
                    else:
                        TopExit= pygame.draw.rect(self._screen,self._Black,(700,0,520,40))
                        if TopExit.colliderect(self.player.rect):
                            self.player.rect.y = 40
                else:
                    TopExit= pygame.draw.rect(self._screen,self._Black,(700,0,520,40))
                    if TopExit.colliderect(self.player.rect):
                        self.player.rect.y = 40
                if playerpos[1] != len(self.stats.Map[0]) -1:
                    
                    #Right exit
                    if self.stats.Map[playerpos[0]][playerpos[1]+1] == 'R' or self.stats.Map[playerpos[0]][playerpos[1]+1] == 'E' or self.stats.Map[playerpos[0]][playerpos[1]+1] == 'B':
                        RightExit =  pygame.draw.rect(self._screen, self._White,(1880,350,40,380))
                        if self.stats.Map[playerpos[0]][playerpos[1]+1] == 'E' or self.stats.Map[playerpos[0]][playerpos[1]+1] == 'B':
                            if RightExit.colliderect(self.player.rect): 
                                self.player.projectilegroup.empty()
                                IsBoss = self.BossOrNot(self.stats.Map[playerpos[0]][playerpos[1]+1])
                                self.player.rect.x = 100
                                self.player.rect.y = self._screeny/2
                                self.stats.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.stats.Map[playerpos[0]][playerpos[1]+1] = '#'
                                EnemyInRoom = 1
                                currentpos = playerpos
                                playerpos = (playerpos[0],playerpos[1]+1)
                                self.stats.globalpos = (playerpos[0],playerpos[1])
                               
                                   
                        else:
                            if RightExit.colliderect(self.player.rect): 
                                self.player.projectilegroup.empty()
                                self.player.rect.x = 100
                                self.player.rect.y = self._screeny/2
                                self.stats.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.stats.Map[playerpos[0]][playerpos[1]+1] = '#'
                                currentpos = playerpos
                                playerpos = (playerpos[0],playerpos[1]+1)
                                self.stats.globalpos = (playerpos[0],playerpos[1])
                                
                    else:
                        RightExit =  pygame.draw.rect(self._screen, self._Black,(1880,350,40,380))
                        if RightExit.colliderect(self.player.rect):
                            self.player.rect.x = 1830
                else:
                    RightExit =  pygame.draw.rect(self._screen, self._Black,(1880,350,40,380))
                    if RightExit.colliderect(self.player.rect):
                        self.player.rect.x = 1830
                if playerpos[1] != 0:
                    
                    #Left Exit
                    if self.stats.Map[playerpos[0]][playerpos[1]-1] == 'R'or self.stats.Map[playerpos[0]][playerpos[1]-1] == 'E'or self.stats.Map[playerpos[0]][playerpos[1]-1] == 'B':
                        LeftExit = pygame.draw.rect(self._screen, self._White, (0,350,40,380))
                        if self.stats.Map[playerpos[0]][playerpos[1]-1] == 'E' or self.stats.Map[playerpos[0]][playerpos[1]-1] == 'B':
                            if LeftExit.colliderect(self.player.rect):
                                self.player.projectilegroup.empty()
                                IsBoss = self.BossOrNot(self.stats.Map[playerpos[0]][playerpos[1]-1])
                                self.player.rect.x = self._screenx-100
                                self.player.rect.y = self._screeny/2 
                                EnemyInRoom = 1
                                self.stats.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.stats.Map[playerpos[0]][playerpos[1]-1] = '#' 
                                currentpos = playerpos
                                playerpos = (playerpos[0],playerpos[1]-1) 
                                self.stats.globalpos = (playerpos[0],playerpos[1])
                              
                        else:
                            if LeftExit.colliderect(self.player.rect):
                                self.player.projectilegroup.empty()
                                self.player.rect.x = self._screenx-100
                                self.player.rect.y = self._screeny/2 
                                self.stats.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.stats.Map[playerpos[0]][playerpos[1]-1] = '#'
                                currentpos = playerpos  
                                playerpos = (playerpos[0],playerpos[1]-1) 
                                self.stats.globalpos = (playerpos[0],playerpos[1])
                                
                    else:
                        LeftExit =  pygame.draw.rect(self._screen, self._Black,(0,350,40,380))
                        if LeftExit.colliderect(self.player.rect):
                            self.player.rect.x = 40
                else:
                    LeftExit =  pygame.draw.rect(self._screen, self._Black,(0,350,40,380))
                    if LeftExit.colliderect(self.player.rect):
                        self.player.rect.x = 40
                
                if check == 1 and newtime< runningtime: #the end of invincibility frames for the player
                    self.player.image.fill((0,255,0))
                    self.player.state = 1
            
                if BossDefeated != 0: #if the boss is defeaeted on this floor
                    if (playerpos[0],playerpos[1]) == self.stats.BossPos: #and if the current position of the player is indeed the boss room
                        self._screen.blit(NextLevel,(880,700))   #draw a exit, but the alpha or transparency is currently 0, as there is a condition to ensure that              
                        alphaset+=5                              #the exit is completely opaque before the player could move on to the next level
                        NextLevel.set_alpha(alphaset)     #periodically sets the alpha every time the game loops
                    
                    
     
                    
                    
                    else: #if the current position of the player isn't the boss room
                        alphaset = 0 
                        NextLevel.set_alpha(0) #set the transparency to 0 
                NextAlpha = NextLevel.get_alpha()
                if NextAlpha == 255: #if the alpha of the exit is 255 (the maximum value)
                    nextRect = pygame.draw.rect(self._screen,(50,50,50),((880,700,150,150))) #then draw a rectangle on this position
                    if nextRect.colliderect(self.player.rect): #and if the player collides with the rect or exit
                        running = 0 #the RunGame() function stops and runs LevelBetween() with the player's current health as a parameter
                        self.LevelBetween(GameHud.health,runningtime)
                    
                    

            else: #if the player goes into an enemy room 
            
                if IsBoss: #if the enemy room is a boss room
                    if TimesSpawned < 1:
                        boss = Boss(self._screenx,self._screeny,(100,100),(165,42,42)) #create a boss class
                        self.enemies.add(boss) #and add to the sprite group of enemies
                        TimesSpawned +=1  #this counter is to ensure that the spawning cycle only goes through once
                else:
                    if TimesSpawned < 1:
                        randomNum = random.randint(1,self.upperbound) #spawn a random amount of enemies per enemy room
                        for i in range(0,randomNum):
                            decision = random.randint(1,2) #decision whether to put a melee enemy or ranged enemy
                            if decision == 1: 
                                enemy = MeleeEnemy(self._screenx,self._screeny,(100,100),(0,0,0))
                                enemy.health += enemyHealthInc #add any health increases
                                self.enemies.add(enemy) 
                            else:
                                ranged = RangedEnemy(self._screenx,self._screeny,(100,100),(255,0,0))
                                ranged.health += enemyHealthInc
                                self.enemies.add(ranged)
                        TimesSpawned +=1 
                DownExit= pygame.draw.rect(self._screen,self._Black,(700,1040,520,40)) #seal all walls shut
                if DownExit.colliderect(self.player.rect):
                    self.player.rect.y = 990
                TopExit= pygame.draw.rect(self._screen,self._Black,(700,0,520,40))
                if TopExit.colliderect(self.player.rect):
                    self.player.rect.y = 40
                RightExit =  pygame.draw.rect(self._screen, self._Black,(1880,350,40,380))
                if RightExit.colliderect(self.player.rect):
                    self.player.rect.x = 1830
                LeftExit =  pygame.draw.rect(self._screen, self._Black,(0,350,40,380))  
                if LeftExit.colliderect(self.player.rect):
                    self.player.rect.x = 40
                
                for enemy in self.enemies: 
                    if enemy.state == 1: #for ranged enemies, as they can also attack using projectiles in intervals of one second 
                        if enemy.cooldown == 0: #if the cooldown is 0
                            intervals = runningtime + self.cooldowntime #set the interval time to 1 second ahead of the current running time (time is measured in milliseconds)
                            pygame.event.post(enemyAttack) #force a event in the event queue
                            enemycheck = 1
                #print(enemy/coold)
                for enemy in self.enemies:
                    if enemycheck == 1 and intervals< runningtime: #if the running time is greater than the interval
                        if enemy.state == 1:
                            enemy.cooldown = 0 #set the cooldown to 0
                
                for enemy in self.enemies:
                    for enemprojectile in enemy.projectilegroup:
                        if pygame.sprite.spritecollideany(enemprojectile,ObstacleToDraw): #destroy any projectiles that collide with the obstacles
                            enemprojectile.kill()
            
                for projectile in self.player.projectilegroup:  #checks if player attack projectiles has collided with the enemy
                    collision = pygame.sprite.spritecollide(projectile, self.enemies, 0) #checks within the sprite group whether if 'projectile' has collided with any sprites the sprite group self.enemies
                    for enemy in collision:
                        if enemy.health == 0:  #if enemy health is 0:
                            enemy.kill()     #delete the enemy from the group
                            projectile.kill()
                        elif collision and enemy.health != 0: #if the attack projectile collides, -1 to enemy health 
                            enemy.health -= 1#self.playerdamage
                            projectile.kill()   
                
                for enemy in self.enemies:
                    for enemyprojectile in enemy.projectilegroup:
                        collision = pygame.sprite.spritecollide(enemyprojectile, self.playersp, 0) #checks within the sprite group whether if 'projectile' has collided with any sprites the sprite group self.enemies
                        if len(collision)!=0 and self.player.state == 1: #if the attack projectile collides, -1 to enemy health 
                            GameHud.health -=1 #decrease one 
                            enemyprojectile.kill() #destroys the enemy projectile as it hits the player
                            if GameHud.health >0: #if the player's health is greater than 0,
                                self.stats.Health = GameHud.health #set the health value 
                                newtime = runningtime +1500 #add 1.5 seconds to the current running time
                                pygame.event.post(Invincibility) #and force a event to the event queue
                                check = 1 
                            else: #if player health is 0
                                running = 0 #RunGame() stops running
                                self.GameOver() #runs the game over screen
                                break    
                playercol = pygame.sprite.spritecollide(self.player, self.enemies, 0) #if the player collides with the enemy
                if len(playercol)!=0 and self.player.state == 1:
                   GameHud.health -=1 #similar operations happen just like the code above
                   if GameHud.health >0:
                        self.stats.Health = GameHud.health
                        newtime = runningtime +1500
                        pygame.event.post(Invincibility)
                        check = 1 
                   else:
                       running = 0
                       self.GameOver()
                       break               

                if check == 1 and newtime< runningtime:
                    self.player.image.fill((0,255,0))
                    self.player.state = 1

                if len(self.enemies) == 0 and not IsBoss: #if the sprite group is enpty, return to normal state 
                    TimesSpawned = 0
                    EnemyInRoom = 0 
                elif len(self.enemies) == 0 and  IsBoss:
                    TimesSpawned = 0
                    EnemyInRoom =0
                    BossDefeated = 1
                    
                self.enemies.draw(self._screen) #draws the sprites
                self.enemies.update(self.player.rect.centerx,self.player.rect.centery,ObstacleToDraw) #player positions in the room are passed into the update function for the enemy to move towards the player
                for enemy in self.enemies:
                    enemy.projectilegroup.draw(self._screen) #draws the projectiles
                    enemy.projectilegroup.update()
            self.player.projectilegroup.draw(self._screen)   #draws each respective sprite and updates it with each game loop
            self.player.projectilegroup.update()
            self.playersp.draw(self._screen)
            self.playersp.update(ObstacleToDraw)
            ObstacleToDraw.draw(self._screen)
            ObstacleToDraw.update()
            Map.update(playerpos[0],playerpos[1])  #the current position of the player is passed in for the minimap
            GameHud.update()
            
            for event in pygame.event.get(): #gets the event
                if event.type == pygame.QUIT: # Did the user click the window close button?
                    running = 0
                    sys.exit()  
                if event == Invincibility:  #if the player gets hit by the enemy
                    if newtime > runningtime: #as long as the newtime is greater than the current running time
                        self.player.image.fill((0,0,255)) #change the player's colour
                        self.player.state = 0 #and set the state to 0, which the player is invulnerable when the state is 0
                if event == enemyAttack: 
                    if intervals > runningtime: #similar operations, except it chooses a random direction to fire projectiles
                        decision = random.randint(1,4)
                        for enemy in self.enemies:
                            if enemy.state == 1: 
                                if decision == 1:
                                    enemy.Attack(1)
                                    enemy.cooldown = 1
                                elif decision == 2:
                                    enemy.Attack(2)
                                    enemy.cooldown = 1
                                elif decision == 3:
                                    enemy.Attack(3)
                                    enemy.cooldown = 1
                                else:
                                    enemy.Attack(4)
                                    enemy.cooldown = 1
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE:  
                        running = self.Pause()    #Pause() returns either 0 or 1, based on what the user does, either returning to the game or returning to the main menu
                    if event.key == pygame.K_UP: #attack projectiles 
                        self.player.Attack(1)    #whenever it detects that either of the arrow keys are pressed
                    if event.key == pygame.K_RIGHT: #then the Attack function is called
                        self.player.Attack(2)
                    if event.key == pygame.K_LEFT:
                        self.player.Attack(3)
                    if event.key == pygame.K_DOWN:
                        self.player.Attack(4)
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click = 1   
                
            pygame.display.update()    
        
    def GameOver(self):
        '''
        Game over screen when the user dies
        '''
        running = 1
        while running:
            pygame.mouse.set_visible(1)
            mousex, mousey = pygame.mouse.get_pos()
            self._screen.fill(self._Black)
            self._screen.blit(self._textfont.render('Game Over' ,1, self._White),(870,200)) #game over text
            BackToMain = self._screen.blit(self._textfont.render('Click here to return to main menu', 1,self._White),(670,900))
            if BackToMain.collidepoint(mousex,mousey) and click == 1:
                running = 0 #sends the user back to the main menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = 1
                else:
                    click =0 
            pygame.display.update() 
            
    def LevelBetween(self,Health=3,runningtime=0): 
        '''
        the intermission betweeen levels, with the default parameter of the health being 3
        '''
        self.stats.Level+=1                #will be passed through and carried on to the next level
        if self.cooldowntime > self.cooldowncap and self.stats.Level != 1: #reduces cooldown between attacks for ranged enemies to a cap
            self.cooldowntime -= 10*self.stats.Level
        if self.AmountOfRooms < self.MaxRooms and self.AmountOfEnemyRooms < self.MaxEnemy and self.AmountOfEnemyRooms < self.AmountOfRooms: #there is limit to how many rooms can exist as the algorithm to generate rooms may reach the recursive depth if too many rooms are added
            if runningtime < 1000*60*2:
                self.AmountOfRooms+=random.randint(1,3)
                self.AmountOfEnemyRooms+= random.randint(1,2)
            else:
                self.AmountOfRooms+=random.randint(3,5)
                self.AmountOfEnemyRooms+=random.randint(2,3)
        leveltext = "Level "+str(self.stats.Level)
        running = 1
        click = 0
        self.playersp.empty() #empties the player sprite group to prevent more than one player sprite existing
        while running:
            pygame.mouse.set_visible(1)
            self._screen.fill(self._Black) 
            mousex, mousey = pygame.mouse.get_pos()
            self._screen.blit(self._textfont.render(leveltext ,1, self._White),(870,200))
            Play = self._screen.blit(self._textfont.render("Play",1, self._White), (900,700)) 
            if self.stats.Level == 1: #if the level is currently 1
                if Play.collidepoint(mousex,mousey) and click == 1:
                    running = 0 
                    self.RunGame(None,Health) #no extra rooms will be added
            else:
                if Play.collidepoint(mousex,mousey) and click == 1:
                    running = 0
                    self.AmountOfRooms += random.randint(1,5) #otherwise, a random amount of rooms will be added
                    self.AmountOfEnemyRooms+= random.randint(0,3)
                    self.RunGame(None,Health,random.randint(1,2))
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Did the user click thei window close button?
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = 1 
                else:
                    click = 0 
            pygame.display.update()
    def Pause(self): 
        '''
        Pause menu
        '''
        running = 1
        click = 0
        while running:
            pygame.mouse.set_visible(1)
            self._screen.fill(self._White)
            BackToGame = pygame.draw.rect(self._screen, self._Black,(860,200,200,200))
            self._screen.blit(self._textfont.render("Back",1, self._White),(880,250))
            SaveGame =  pygame.draw.rect(self._screen, self._Black,(860,500,200,200))
            self._screen.blit(self._textfont.render("save",1, self._White),(880,550))
            ExittoMenu = pygame.draw.rect(self._screen, self._Black,(820,800,300,200))
            self._screen.blit(self._textfont.render("Main menu",1, self._White),(830,830))
            
            mousex, mousey = pygame.mouse.get_pos()
            if SaveGame.collidepoint(mousex,mousey) and click == 1: #if either buttons are pressed
                click = 0  #instantly change click to 0, as if click is unchanged, this statement will keep calling if the mouse button is held down
                self.Save()
            if BackToGame.collidepoint(mousex,mousey) and click == 1:
                    running = 0 
                    click = 0  
                    return 1
            if ExittoMenu.collidepoint(mousex,mousey) and click == 1:
                    running = 0
                    click = 0
                    return 0  
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Did the user click the window close button?
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = 0
                        return 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = 1
                    
                else:
                    click =0 
            pygame.display.update()
   
        
    def BossOrNot(self,input):
        '''
        simple function to check whether if a room is a boss or not
        '''
        if input == 'B':
            return True
        return False       
    
    def Controls(self): 
        '''
        control page for the player to know the controls
        ''' 
        running = 1
        click = 0
        while running:
            self._screen.fill(self._Black)
            mousex, mousey = pygame.mouse.get_pos()
            self._screen.blit(self._textfont.render("Controls", 1, self._White), (865,100)) 
            
            
            self._screen.blit(self._textfont.render("Movement", 1, self._White), (380,300))
            
            self._screen.blit(self._textfont.render("Attack", 1, self._White), (1330,300))
            
            W = pygame.draw.rect(self._screen, self._White,(450,400,100,100))
            A= pygame.draw.rect(self._screen, self._White,(300,550,100,100))
            S= pygame.draw.rect(self._screen, self._White,(450,550,100,100))
            D= pygame.draw.rect(self._screen, self._White,(600,550,100,100))
            
            self._screen.blit(self._textfont.render("W", 1, self._Black), (473,410))
            self._screen.blit(self._textfont.render("A", 1, self._Black), (323,560))
            self._screen.blit(self._textfont.render("S", 1, self._Black), (473,560))
            self._screen.blit(self._textfont.render("D", 1, self._Black), (623,560))
            
            #rectangles a drawn in a way to represent the keyboard layout
            up= pygame.draw.rect(self._screen, self._White,(1350,400,100,100))
            left= pygame.draw.rect(self._screen, self._White,(1200,550,100,100))
            down= pygame.draw.rect(self._screen, self._White,(1350,550,100,100))
            right= pygame.draw.rect(self._screen, self._White,(1500,550,100,100))
            
            arrowup = self._screen.blit(self._symbol.render("↑",1,self._Black), (1390,400))
            arrowleft = self._screen.blit(self._symbol.render("←",1,self._Black), (1230,550))
            arrowdown = self._screen.blit(self._symbol.render("↓",1,self._Black), (1390,550))
            arrowright = self._screen.blit(self._symbol.render("→",1,self._Black), (1530,550))
            
            back =  pygame.draw.rect(self._screen, self._White,(100,900,110,100))
            self._screen.blit(self._textfont.render("Back",1,self._Black),(100,900))
            cont = self._screen.blit(self._textfont.render("Continue", 1, self._White), (850,900))
            if cont.collidepoint(mousex,mousey) and click == 1: #if the mouse position collides at the text and the user presses the mouse button
                running = 0 #stops the function
                return 1
            
            elif back.collidepoint(mousex,mousey) and click == 1:
                running = 0
                return 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Did the user click the window close button?
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = 0
                        return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = 1
                else:
                    click = 0
            pygame.display.update()  
    def Erase(self):
        '''
        Erase the current save file from the system
        '''
        try: #error handle to try and remove certain files
            os.remove("file1") 
            os.remove("file2")
            return 1
        except:
            return 2
            
    def MainMenu(self):
        '''
        Main menu for the game
        '''
        running = 1
        click = 0
        Fail = False
        Remove = False
        while running:
            
            
            pygame.mouse.set_visible(1)
            self._screen.fill(self._Black) #the colour
            Title = self._screen.blit(self._bigtextfont.render("Dungeon Crawl NEA",1, self._White), (630,100)) #texts and boxes
            Play = pygame.draw.rect(self._screen, self._White,(900,300,100,100))
            self._screen.blit(self._textfont.render("Play",1, self._Black), (900,300))
            Exit = pygame.draw.rect(self._screen, self._White,(900,900,100,100))
            self._screen.blit(self._textfont.render("Exit",1, self._Black), (900,900))
            Load = pygame.draw.rect(self._screen, self._White,(900,500,110,100))
            self._screen.blit(self._textfont.render("Load",1, self._Black), (900,500))
            Erase = pygame.draw.rect(self._screen, self._White,(840,700,240,100))
            self._screen.blit(self._textfont.render("Erase Save",1, self._Black), (840,700))
            
            mousex, mousey = pygame.mouse.get_pos()
            if Fail: #if the program fails to load a save file
                self._screen.blit(self._textfont.render("No save file detected",1, self._White), (740,1000)) #then it means there are no save files
                
            if Play.collidepoint(mousex,mousey) and click  == 1:
                check = self.Controls()
                if check == 1:
                    self.LevelBetween()
                    running = 0
                    return 0
                
                
            
            if Load.collidepoint(mousex,mousey) and click == 1 and Remove!=1:
                data = self.Load()
                if not data:
                    Fail = True
                else:
                    self.RunGame(data)
                    running =0
                    return 0
            if Erase.collidepoint(mousex,mousey) and click == 1:
                Remove =self.Erase()
                click  =0 
                
            if Remove == 2:
                self._screen.blit(self._textfont.render("No save file detected",1, self._White), (740,1000))
            elif Remove == 1:
                self._screen.blit(self._textfont.render("Save file deleted",1, self._White), (770,1000))
                
            if Exit.collidepoint(mousex,mousey) and click == 1:
                exit()   #exits the program if the user presses the exit button
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Did the user click the window close button?
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = 1
                else:
                    click = 0
            pygame.display.update()              
           
if __name__ == "__main__":
    Main() #main function