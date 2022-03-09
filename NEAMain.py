#TO DO
#Implement Projectiles #DONE 
#Room traversal with restrictiosn #DONE
#Enemy spawn DONE
#Room modifications (obstacles)         
#Character creation with built in speical abilities for different classes    #PROGRESS
#Spells 
#Create self.Map 
from re import I
import time
import threading as thread
import pygame, sys, random
from Enemy import *
from GridGenerator import *
from Stats import *
from Obstacles import *
from Player import *
from MiniMap import*
from Hud import*
import pickle



pygame.init()
WIDTH, HEIGHT = 1920, 1080

def Main():  #main function to call 
    while 1:
        MainGame = Game()
        MainGame.MainMenu()
        del MainGame


class Items(pygame.sprite.Sprite):
    def __init__(self):
        
        #luck will affect this 
        pygame.sprite.Sprite.__init__(self)
        powerup = pygame.Surface((25,25)) 
        random
        pass
class Spells:
    def __init__(self):
        pass
class Warrior:
    def __init__(self):
        pass
class Mage:
    def __init__(self):
        pass
class Rogue:
    def __init__(self):
        pass

class Game(): 
    def __init__(self):
        self._screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self._White = (255,255,255) #preset values for colour and resolution
        self._Black = (0,0,0)
        self._Red = (255,0,0)
        self._screenx = 1920
        self._screeny = 1080
        self._textfont = pygame.font.Font(r'C:\Windows\Fonts\georgia.ttf', 50 ) 
        self._clock = pygame.time.Clock()

        self.enemies = pygame.sprite.Group()   #preset sprite groups to be used for colllision purposes
        self.playersp = pygame.sprite.Group()
        self.charclass = 0  #other features that are yet to be implemented
        self.rooms = 20
        self.health = 3
        self.enemyRooms = 12
        
        
        self.luck = 0
        self.badluck = 0 
        self.player = None
        self.Map = None
        self.globalpos = None
        self.border_gap = 0
        self.ObstacleGroup = None
        self.traversed = None
        

    def checkifRoom(self,room,i,j,limit): #checks whether if a element in the self.Map/list is a room
        limit+=1
        if limit >100:
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
    def GenerateMap(self):  #calls a class imported from a separate file to generate grid
        Grid = GridGenerator(self.rooms,self.enemyRooms) #calls the class 
        Rooms = Grid.Layout() #generates the room, outputs a list #no issues
        Map = Grid.GenerateEnemyRoom(Rooms) #input is a list, the output is a modified version of the list
        return Map
            
    def Save(self):
        obslist=[]
        with open("file1", "wb") as file1: #write the obstacles in as well
            #oblist = []

            pickle.dump(self.Map,file1)
            pickle.dump(self.globalpos,file1)
            pickle.dump(self.traversed,file1)
            pickle.dump(self.player.rect.center,file1)
        with open("file2","wb") as file2:
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
        try:
            with open("file1","rb") as file1:
            # oblist = []
                map = pickle.load(file1)
                position = pickle.load(file1)
                traversed = pickle.load(file1)
                playercenter = pickle.load(file1)
            with open("file2","rb") as file2:
                obstacles = pickle.load(file2)
        except:
            return False
       
            
        return map,position,obstacles,traversed,playercenter
    def RunGame(self,File=None):  #runs the game 
         #calls the player class
        self.ObstacleGroup = pygame.sprite.Group()
        Load = File
        if Load != None:
            self.Map = Load[0]
            playerpos = Load[1]
            obstaclelist = Load[2]
            traversedlist = Load[3]
            playercenter = Load[4]
            self.player = Player(self._screenx,self._screeny,playercenter[0],playercenter[1])
            for obstacle in obstaclelist:
                obs = RoomObstacles(obstacle['i'],obstacle['j'],obstacle['xsize'],obstacle['ysize'],obstacle['xcenter'],obstacle['ycenter'])
                self.ObstacleGroup.add(obs)
            currentpos = playerpos
            self.globalpos = playerpos
            Map = MiniMap(self._screen,self.Map,traversedlist)
            
            
        else:
            self.player = Player(self._screenx,self._screeny)
            self.Map = self.GenerateMap()
            Roomi = random.randint(0,len(self.Map)-1) 
            Roomj = random.randint(0,len(self.Map[0])-1)
            roompos = self.checkifRoom(self.Map,Roomi,Roomj,0) #and pass it through a function to check whether if its a valid room with no enemies 
            self.Map[roompos[0]][roompos[1]] = "#"  #player symbol
            playerpos = (roompos[0],roompos[1])  #a tuple to represent the player position on the self.Map
            #by default, there are no enemies in the room 
            currentpos = playerpos
           
            Map = MiniMap(self._screen,self.Map)
        
            self.globalpos = (playerpos[0],playerpos[1])
             #preset values to check how many times has the enemy spaned
           #a separate group to draw obstacles, the idea is to have a group of obstacles ready to be added to another group to ONLY draw
            #specific obstacles in each room, as each room has a set obstacle assigned to it     
        
            
             #obstacle group to be used to draw obstacles in every room 
            for i,value in enumerate(self.Map):  #iterates the entire self.Map to add a separate obstacle, still improving
                for j,val in enumerate(value):  
                    randomobs = random.randint(1,4)
                    for _ in range(0,randomobs):
                        obs = RoomObstacles(i,j)
                        self.ObstacleGroup.add(obs)
        ObstacleToDraw = pygame.sprite.Group()  
        TimesSpawned = 0 
        EnemyInRoom = 0
        running = 1
        BossDefeated = 0
        score = 0 
        speed = 5
        IsBoss = False
        iFrames_time = pygame.USEREVENT+0
        iFrames= pygame.event.Event(iFrames_time)
        check = 0
        GameHud = Hud(self._screen)
        self.playersp.add(self.player) 
        while running:  
            self._clock.tick(60)
            self.traversed = Map.traversedlist
            runningtime = pygame.time.get_ticks() #this will be logged to see how fast the player plays the game
       
            pygame.mouse.set_visible(0)
            self._screen.fill(self._White) 
            TopLeft = pygame.draw.rect(self._screen,self._Black,(0,0,700,40))    #walls/borders, there are variants of wall as the 'exit' to different rooms will be a separate wall
            TopRight = pygame.draw.rect(self._screen,self._Black,(1220,0,700,40))
            DownLeft = pygame.draw.rect(self._screen, self._Black, (0,1040, 700,40))
            DownRight = pygame.draw.rect(self._screen, self._Black, (1220,1040, 700,40))
            LeftUp = pygame.draw.rect(self._screen, self._Black, (0,0, 40,350))
            LeftDown = pygame.draw.rect(self._screen, self._Black, (0,730, 40,350))
            RightUp = pygame.draw.rect(self._screen, self._Black, (1880,0,40,350))
            RightDown = pygame.draw.rect(self._screen, self._Black,  (1880,730,40,350))
            
            
            #check which position is it currently
            if currentpos != playerpos:
                ObstacleToDraw.empty()
                for obstacle in self.ObstacleGroup:
                    if obstacle.i == playerpos[0] and obstacle.j == playerpos[1]:
                        ObstacleToDraw.add(obstacle)
            else:
                for obstacle in self.ObstacleGroup:
                    if obstacle.i == playerpos[0] and obstacle.j == playerpos[1]:
                        ObstacleToDraw.add(obstacle)  #simple check to see if obstacles are being drawn    


            #BOTTOM LEFT AND BOTTOM RIGHT STILL NOT WORKING
            
            #something to do with top rigth and top left edges
            
            for obs in ObstacleToDraw: 
                if self.player.rect.colliderect(obs.rect):  #colliderect  = true
                    if self.player.rect.y+45 > obs.rect.y and self.player.rect.y+10 < obs.rect.y+obs.ysize: 
                        if obs.rect.collidepoint(self.player.rect.x,self.player.rect.y) or obs.rect.collidepoint(self.player.rect.x,self.player.rect.y+50):
                            self.player.rect.x = obs.rect.x+obs.xsize
                        elif obs.rect.collidepoint(self.player.rect.x+50,self.player.rect.y) or obs.rect.collidepoint(self.player.rect.x+50,self.player.rect.y+50):
                            self.player.rect.x= obs.rect.x-50
                    else:
                        if obs.rect.collidepoint(self.player.rect.x,self.player.rect.y+50) or obs.rect.collidepoint(self.player.rect.x+50,self.player.rect.y+50):
                            self.player.rect.y = obs.rect.y-50
                        elif obs.rect.collidepoint(self.player.rect.x,self.player.rect.y) or obs.rect.collidepoint(self.player.rect.x+50,self.player.rect.y):
                            self.player.rect.y = obs.rect.y+obs.ysize
                for projec in self.player.projectilegroup:
                    if pygame.sprite.spritecollideany(obs,self.player.projectilegroup):
                        projec.kill()
                    
                   
        
            if LeftUp.colliderect(self.player.rect) or LeftDown.colliderect(self.player.rect):    #these statements make sure that the player does not go through the borders
                self.player.rect.x = 40
            if RightUp.colliderect(self.player.rect) or RightDown.colliderect(self.player.rect):  #tried to use elif statements, but if the player inputs two directions when already agianst a while, the player goes through the wall
                self.player.rect.x = 1830  
            if DownLeft.colliderect(self.player.rect) or DownRight.colliderect(self.player.rect):
                self.player.rect.y = 990
            if TopLeft.colliderect(self.player.rect) or TopRight.colliderect(self.player.rect):
                self.player.rect.y = 40
            
            if EnemyInRoom == 0:  #if there are no enemies in the room, then check the player position on the self.Map and see if the adjacent rooms are passable or not.
                                      #if the adjacent room/element is empty (not P, E or B), then a self._Black wall will replace the self._White wall in that corresponding place
                if playerpos[0] != len(self.Map)-1: #checks if the player is at a border
                    if self.Map[playerpos[0]+1][playerpos[1]] == 'R' or self.Map[playerpos[0]+1][playerpos[1]] == 'E' or self.Map[playerpos[0]+1][playerpos[1]] == 'B':
                        DownExit= pygame.draw.rect(self._screen,self._White,(700,1040,520,40))
                        if self.Map[playerpos[0]+1][playerpos[1]] == 'E' or self.Map[playerpos[0]+1][playerpos[1]] == 'B':  #if the corresponding room has an enemy
                            if DownExit.colliderect(self.player.rect):  #and the player has collided the exit rect/exited the room
                                self.player.projectilegroup.empty()
                                IsBoss = self.BossOrNot(self.Map[playerpos[0]+1][playerpos[1]])
                                self.player.rect.x = self._screenx/2  #set values to put them at where they would appear when going through a room from a certain side
                                self.player.rect.y = 100
                                EnemyInRoom = 1 #set to 1, certain conditions will be applied 
                                self.Map[playerpos[0]][playerpos[1]] = 'R'  #as the player position hasnt been changed, the value gets changed to R as 'Room'
                                self.Map[playerpos[0]+1][playerpos[1]] = '#' #the adjacent room gets changed into the player symbol
                                currentpos = playerpos
                                playerpos = (playerpos[0]+1,playerpos[1]) #then, the player position gets changed accordingly
                                self.globalpos = (playerpos[0],playerpos[1])
                        else: 
                            if DownExit.colliderect(self.player.rect): #if the adjacent room has no enemies,
                                self.player.projectilegroup.empty() 
                                self.player.rect.x = self._screenx/2 #then similar operations occur apart from the EnemInRoom being modified.
                                self.player.rect.y = 100
                                self.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.Map[playerpos[0]+1][playerpos[1]] = '#'
                                currentpos = playerpos
                                playerpos = (playerpos[0]+1,playerpos[1])
                                self.globalpos = (playerpos[0],playerpos[1])   
                                      
                    else:
                        DownExit= pygame.draw.rect(self._screen,self._Black,(700,1040,520,40)) #if there is no room available, then draw a self._Black rectangle
                        if DownExit.colliderect(self.player.rect): #if the player collides into it: 
                            self.player.rect.y = 990        #the player will stay in place 
                else:
                    DownExit= pygame.draw.rect(self._screen,self._Black,(700,1040,520,40)) #this is to check whether if the player is at a border or not
                    if DownExit.colliderect(self.player.rect): 
                        self.player.rect.y = 990    
                        #rest of the code are relatively similar to this one as its just a different side          
                if playerpos[0] != 0:
                    if self.Map[playerpos[0]-1][playerpos[1]] == 'R' or self.Map[playerpos[0]-1][playerpos[1]] == 'E'or self.Map[playerpos[0]-1][playerpos[1]] == 'B':
                        TopExit = pygame.draw.rect(self._screen,self._White,(700,0,520,40))
                        if self.Map[playerpos[0]-1][playerpos[1]] == 'E' or self.Map[playerpos[0]-1][playerpos[1]] == 'B':
                            if TopExit.colliderect(self.player.rect) :
                                self.player.projectilegroup.empty()
                                IsBoss = self.BossOrNot(self.Map[playerpos[0]-1][playerpos[1]])
                                self.player.rect.x = self._screenx/2
                                self.player.rect.y = self._screeny-100
                                EnemyInRoom = 1        
                                self.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.Map[playerpos[0]-1][playerpos[1]] = '#'
                                currentpos = playerpos
                                playerpos = (playerpos[0]-1,playerpos[1])
                                self.globalpos = (playerpos[0],playerpos[1])
                                for i in Map.traversedlist:
                                    print(i)
                              
                        else: 
                            
                            if TopExit.colliderect(self.player.rect): 
                                self.player.projectilegroup.empty()
                                self.player.rect.x = self._screenx/2
                                self.player.rect.y = self._screeny-100
                                self.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.Map[playerpos[0]-1][playerpos[1]] = '#'
                                currentpos = playerpos
                                playerpos = (playerpos[0]-1,playerpos[1])
                                self.globalpos = (playerpos[0],playerpos[1])
                                for i in Map.traversedlist:
                                    print(i)
                    else:
                        TopExit= pygame.draw.rect(self._screen,self._Black,(700,0,520,40))
                        if TopExit.colliderect(self.player.rect):
                            self.player.rect.y = 40
                else:
                    TopExit= pygame.draw.rect(self._screen,self._Black,(700,0,520,40))
                    if TopExit.colliderect(self.player.rect):
                        self.player.rect.y = 40
                if playerpos[1] != len(self.Map[0]) -1:
                    if self.Map[playerpos[0]][playerpos[1]+1] == 'R' or self.Map[playerpos[0]][playerpos[1]+1] == 'E' or self.Map[playerpos[0]][playerpos[1]+1] == 'B':
                        RightExit =  pygame.draw.rect(self._screen, self._White,(1880,350,40,380))
                        if self.Map[playerpos[0]][playerpos[1]+1] == 'E' or self.Map[playerpos[0]][playerpos[1]+1] == 'B':
                            if RightExit.colliderect(self.player.rect): 
                                self.player.projectilegroup.empty()
                                IsBoss = self.BossOrNot(self.Map[playerpos[0]][playerpos[1]+1])
                                self.player.rect.x = 100
                                self.player.rect.y = self._screeny/2
                                self.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.Map[playerpos[0]][playerpos[1]+1] = '#'
                                EnemyInRoom = 1
                                currentpos = playerpos
                                playerpos = (playerpos[0],playerpos[1]+1)
                                self.globalpos = (playerpos[0],playerpos[1])
                                for i in Map.traversedlist:
                                    print(i)
                                   
                        else:
                            if RightExit.colliderect(self.player.rect): 
                                self.player.projectilegroup.empty()
                                self.player.rect.x = 100
                                self.player.rect.y = self._screeny/2
                                self.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.Map[playerpos[0]][playerpos[1]+1] = '#'
                                currentpos = playerpos
                                playerpos = (playerpos[0],playerpos[1]+1)
                                self.globalpos = (playerpos[0],playerpos[1])
                                for i in Map.traversedlist:
                                    print(i)
                    else:
                        RightExit =  pygame.draw.rect(self._screen, self._Black,(1880,350,40,380))
                        if RightExit.colliderect(self.player.rect):
                            self.player.rect.x = 1830
                else:
                    RightExit =  pygame.draw.rect(self._screen, self._Black,(1880,350,40,380))
                    if RightExit.colliderect(self.player.rect):
                        self.player.rect.x = 1830
                if playerpos[1] != 0:
                    if self.Map[playerpos[0]][playerpos[1]-1] == 'R'or self.Map[playerpos[0]][playerpos[1]-1] == 'E'or self.Map[playerpos[0]][playerpos[1]-1] == 'B':
                        LeftExit = pygame.draw.rect(self._screen, self._White, (0,350,40,380))
                        if self.Map[playerpos[0]][playerpos[1]-1] == 'E' or self.Map[playerpos[0]][playerpos[1]-1] == 'B':
                            if LeftExit.colliderect(self.player.rect):
                                self.player.projectilegroup.empty()
                                IsBoss = self.BossOrNot(self.Map[playerpos[0]][playerpos[1]-1])
                                self.player.rect.x = self._screenx-100
                                self.player.rect.y = self._screeny/2 
                                EnemyInRoom = 1
                                self.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.Map[playerpos[0]][playerpos[1]-1] = '#' 
                                currentpos = playerpos
                                playerpos = (playerpos[0],playerpos[1]-1) 
                                self.globalpos = (playerpos[0],playerpos[1])
                                for i in Map.traversedlist:
                                    print(i)
                        else:
                            if LeftExit.colliderect(self.player.rect):
                                self.player.projectilegroup.empty()
                                self.player.rect.x = self._screenx-100
                                self.player.rect.y = self._screeny/2 
                                self.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.Map[playerpos[0]][playerpos[1]-1] = '#'
                                currentpos = playerpos  
                                playerpos = (playerpos[0],playerpos[1]-1) 
                                self.globalpos = (playerpos[0],playerpos[1])
                                for i in Map.traversedlist:
                                    print(i)
                    else:
                        LeftExit =  pygame.draw.rect(self._screen, self._Black,(0,350,40,380))
                        if LeftExit.colliderect(self.player.rect):
                            self.player.rect.x = 40
                else:
                    LeftExit =  pygame.draw.rect(self._screen, self._Black,(0,350,40,380))
                    if LeftExit.colliderect(self.player.rect):
                        self.player.rect.x = 40
                if check == 1 and newtime< runningtime:
                    self.player.player_image.fill((0,255,0))
                    self.player.state = 1
                    
                if BossDefeated != 0:
                    pass
            else: #if EnemyInRoom is 1:
                if not IsBoss:
                    if TimesSpawned < 1:
                        #for i in range(0,3):
                        enemy = Enemy()
                        self.enemies.add(enemy)
                        TimesSpawned +=1 
                else:
                    if TimesSpawned < 1:
                        #for i in range(0,3):
                        enemy = Enemy()
                        self.enemies.add(enemy)
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
                
                
                for obs in ObstacleToDraw: 
                    for enemies in self.enemies:
                        if enemies.rect.colliderect(obs.rect):  #colliderect  = true
                            if enemies.rect.y+45 > obs.rect.y and enemies.rect.y+10 < obs.rect.y+obs.ysize: 
                                if obs.rect.collidepoint(enemies.rect.x,enemies.rect.y) or obs.rect.collidepoint(enemies.rect.x,enemies.rect.y+100):
                                    enemies.rect.x = obs.rect.x+obs.xsize
                                elif obs.rect.collidepoint(enemies.rect.x+100,enemies.rect.y) or obs.rect.collidepoint(enemies.rect.x+100,enemies.rect.y+100):
                                    enemies.rect.x= obs.rect.x-100
                            else:
                                if obs.rect.collidepoint(enemies.rect.x,enemies.rect.y+100) or obs.rect.collidepoint(enemies.rect.x+100,enemies.rect.y+100):
                                    enemies.rect.y = obs.rect.y-100
                                elif  obs.rect.collidepoint(enemies.rect.x,enemies.rect.y) or obs.rect.collidepoint(enemies.rect.x+100,enemies.rect.y):
                                    enemies.rect.y = obs.rect.y+obs.ysize
                        #self.enemies.update()
                for projectile in self.player.projectilegroup:  #checks if player attack projectiles has collided with the enemy
                    collision = pygame.sprite.spritecollide(projectile, self.enemies, 0) #checks within the sprite group whether if 'projectile' has collided with any sprites the sprite group self.enemies
                    for enemy in collision:
                        if enemy.health == 0:  #if enemy health is 0:
                            enemy.kill()     #delete the enemy from the group
                            projectile.kill()
                        elif collision and enemy.health != 0: #if the attack projectile collides, -1 to enemy health 
                            enemy.health -=1
                            projectile.kill()   
                playercol = pygame.sprite.spritecollide(self.player, self.enemies, 0)
                #print(self.player.state)
                if len(playercol)!=0 and self.player.state == 1:
                   GameHud.health -=1
                   if GameHud.health >0:
                        
                        #print(GameHud.health)
                        newtime = runningtime +2000
                        pygame.event.post(iFrames)
                        check = 1
                          
                   else:
                       running = 0
                       break               
                    
                
                if check == 1 and newtime< runningtime:
                    self.player.player_image.fill((0,255,0))
                    self.player.state = 1
                    
                
                        
         
                if len(self.enemies) == 0 and not IsBoss: #if the sprite group is enpty, return to normal state 
                    TimesSpawned = 0
                    EnemyInRoom = 0 
                elif len(self.enemies) == 0 and  IsBoss:
                    TimesSpawned = 0
                    
                self.enemies.draw(self._screen)
                self.enemies.update(self.player.rect.x,self.player.rect.y) #player positions are passed into the update function for the enemy to move towards the player
            self.player.projectilegroup.draw(self._screen)
            self.player.projectilegroup.update()
            self.playersp.draw(self._screen)
            self.playersp.update()
            ObstacleToDraw.draw(self._screen)
            ObstacleToDraw.update()
            Map.update(playerpos[0],playerpos[1]) 
            GameHud.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Did the user click the window close button?
                    running = 0
                    sys.exit()  
                
                if event == iFrames: 
                    if newtime > runningtime:
                        self.player.player_image.fill((0,0,255))
                        self.player.state = 0
                    
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE: #one time events
                        #running = 0
                        running = self.Pause()     #pause menu         
                    if event.key == pygame.K_DOWN:  #attack projectiles
                        self.player.Attackdown()
                    if event.key == pygame.K_UP:
                        self.player.Attackup()
                    if event.key == pygame.K_RIGHT:
                        self.player.Attackright()
                    if event.key == pygame.K_LEFT:
                        self.player.Attackleft()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click = 1   
                
            pygame.display.update()    

    # def iFrames(self):
    #     print('reachreach')
    #     self.player.state == 1
    #     self.player.player_image.fill((0,255,0))
    # def GetTime(self):
        
    def GameOver(self):
        running = 1
        while running:
            pass
    
    def Pause(self): #pause menu
        running = 1
        click = 0
        while running:
            pygame.mouse.set_visible(1)
            self._screen.fill(self._White)
            BackToGame = pygame.draw.rect(self._screen, self._Black,(100,200,200,200))
            self._screen.blit(self._textfont.render("Back",1, self._White),(100,200))
            ExittoMenu = pygame.draw.rect(self._screen, self._Black,(100,500,200,200))
            SaveGame =  pygame.draw.rect(self._screen, self._Black,(900,900,200,200))
            self._screen.blit(self._textfont.render("save",1, self._White),(900,900))
            mousex, mousey = pygame.mouse.get_pos()
            if SaveGame.collidepoint(mousex,mousey) and click == 1:
                click = 0 
                self.Save()
                
            if BackToGame.collidepoint(mousex,mousey):
                if click == 1:
                    running = 0 
                    click = 0  
                    return 1
            if ExittoMenu.collidepoint(mousex,mousey):
                if click == 1:
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
        if input == 'B':
            return True
        return False       
    def CharacterCreation(self): #character creation section for the player to customise their character, still WIP
        running = 1
        charclass = ["Warrior","Mage","Paladin","Rogue"]
        ability = ["Melee","Magic","Heal"]
        stats = { 'Speed' : 0,
                  'Damage': 0,
                  'Spell Damage': 0,
                  'Health': 0
                }
        i = 0
        click = 0
        statpoints = 20
        while running:
            #Class
            self._screen.fill(self._Black)
            mousex, mousey = pygame.mouse.get_pos()
            next = pygame.draw.rect(self._screen, self._White,(1000,300,100,100))
            prev = pygame.draw.rect(self._screen, self._White,(600,300,100,100))
            self._screen.blit(self._textfont.render("Choose your class", 1, self._White), (800,50))
            self._screen.blit(self._textfont.render("Next", 1, self._Black), (1000,300))
            self._screen.blit(self._textfont.render(charclass[i],1,self._White),(800,300))
            self._screen.blit(self._textfont.render("Prev", 1,self._Black), (600,300))
            self._screen.blit(self._textfont.render("Randomise", 1, self._White), (950,950))
            Randomise = pygame.draw.rect(self._screen, self._Black,(950,950,100,100))
            play = pygame.draw.rect(self._screen, self._Black,(900,900,100,100))
            self._screen.blit(self._textfont.render("Play", 1, self._White), (900,900))
            pygame.draw.rect(self._screen, self._Black,(375,500,100,100))

            AddSpeed = pygame.draw.polygon(self._screen, self._White,[(600,600),(600,700),(550,500)])
            # RedSpeed = pygame.draw.rect(self._screen, self._Black,(900,900,100,100))
            # AddDamage =pygame.draw.rect(self._screen, self._Black,(900,900,100,100))
            # RedDamage=pygame.draw.rect(self._screen, self._Black,(900,900,100,100))
            # AddSpellD=pygame.draw.rect(self._screen, self._Black,(900,900,100,100))
            # RedSpellD=pygame.draw.rect(self._screen, self._Black,(900,900,100,100))
            # AddHealth=pygame.draw.rect(self._screen, self._Black,(900,900,100,100))
            # RedHealth=pygame.draw.rect(self._screen, self._Black,(900,900,100,100))
            # (pos),(size)
            #Stat 
            Speed = pygame.draw.rect(self._screen, self._White,(500,500,150,100))
            Damage =pygame.draw.rect(self._screen, self._White,(1500,800,150,100))
            SpellDmg =pygame.draw.rect(self._screen, self._White,(500,800,150,100))
            Health =pygame.draw.rect(self._screen, self._White,(1500,500,150,100))          
            self._screen.blit(self._textfont.render("Speed", 1, self._White), (350,500))
            self._screen.blit(self._textfont.render("Damage", 1, self._White), (850,800))
            self._screen.blit(self._textfont.render("Spell Damage", 1, self._White), (350, 800))
            self._screen.blit(self._textfont.render("Health", 1, self._White), (850,500))
          
            if Randomise.collidepoint(mousex,mousey) and click == 0:
                pass
            #if button hit
            #respective stat block increases or decreases
            #return stat dictionary
            if next.collidepoint(mousex,mousey):
                if click == 1:
                    pygame.draw.rect(self._screen, self._Black,(375,500,100,100))
                    if i == len(charclass)-1:
                        print("this should reach")
                        pygame.draw.rect(self._screen, self._Black,(375,500,100,100))
                        self._screen.blit(self._textfont.render(charclass[0],1,self._White),(800,300))
                        i = 0
                    else:
                        self._screen.blit(self._textfont.render(charclass[i+1],1,self._Black),(800,300))
                        i += 1
                #print(charclass[i])
                    click = 0
            if prev.collidepoint(mousex,mousey):
                if  click == 1: #if click == 1 and 0 the moment the mouse button comes up 
                #print("reach 2")
                    pygame.draw.rect(self._screen, self._Black,(375,500,100,100))
                    if i ==0:
                            pygame.draw.rect(self._screen, self._Black,(375,500,100,100))
                            self._screen.blit(self._textfont.render(charclass[i-1],1,self._White),(800,300))
                            i = len(charclass) -1       
                    else:
                        self._screen.blit(self._textfont.render(charclass[i-1],1,self._Black),(800,300))
                        i -= 1 
                    click = 0
            if play.collidepoint(mousex,mousey) and event.type == pygame.MOUSEBUTTONDOWN:
                running = 0
                #return charclass[i],stats

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Did the user click the window close button?
                    running = 0
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = 1
                else:
                    click = 0
            pygame.display.update()   
    def MainMenu(self):
        running = 1
        click = 0
        
        while running:
            pygame.mouse.set_visible(1)
            self._screen.fill(self._Black) #the colour
            Play = pygame.draw.rect(self._screen, self._White,(900,300,100,100))
            self._screen.blit(self._textfont.render("Play",1, self._Black), (900,300))
            button3 = pygame.draw.rect(self._screen, self._White,(900,900,100,100))
            self._screen.blit(self._textfont.render("Exit",1, self._Black), (900,900))
            Load = pygame.draw.rect(self._screen, self._White,(900,500,100,100))
            self._screen.blit(self._textfont.render("Load",1, self._Black), (900,500))
            mousex, mousey = pygame.mouse.get_pos()
            if Play.collidepoint(mousex,mousey) and click  == 1:
                self.CharacterCreation()
                self.RunGame()
                running = 0
                return 0
            if Load.collidepoint(mousex,mousey) and click == 1:
                data = self.Load()
                self.RunGame(data)
                running =0
                return 0
            if button3.collidepoint(mousex,mousey) and click == 1:
                exit()  
            button2 = pygame.draw.rect(self._screen, self._Black,(100,100,100,50))
            self._screen.blit(self._textfont.render("Options", 1, self._White), (100,100))
            if button2.collidepoint(mousex,mousey) and click == 1:
                self.option()
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
    Main()