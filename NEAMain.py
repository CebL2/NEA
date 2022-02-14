#TO DO
#Implement Projectiles #DONE 
#Room traversal with restrictiosn #DONE
#Enemy spawn DONE
#Room modifications (obstacles)         
#Character creation with built in speical abilities for different classes    #PROGRESS
#Spells 
#Create self.Map 


import pygame, sys, random
from Enemy import *
from GridGenerator import *
from Stats import *
from Obstacles import *
from Player import *
from MiniMap import*
import pickle


pygame.init()




#json to save files
#write is save
#read is load 
#in order to save, we need to dump or write binary data with binary write 
#with open("filename.txt",'wb') as file 
#file.dump(data) with the pickle module?
# with open ('test.txt', 'w') as file:
#     file.write("this is a test")
#     file.close()

def Main():  #main function to call 
    while 1:
        
  
        #print(ab)
        MainGame = Game()
        MainGame.MainMenu()
        del MainGame

class Hud:  #WIP
    def __init__(self):
        pass
        
    def Health(self):
        pass

    def Inventory(self):
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
class Paladin:
    def __init__(self):
        pass
class Rogue:
    def __init__(self):
        pass


#         M = pygame.surf
class Game(): 
    def __init__(self):
        self._screen = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
        self._White = (255,255,255) #preset values for colour and resolution
        self._Black = (0,0,0)
        self._screenx = 1920
        self._screeny = 1080
        self._textfont = pygame.font.Font(r'C:\Windows\Fonts\georgia.ttf', 50 ) 
        self.clock = pygame.time.Clock()

        self.enemies = pygame.sprite.Group()   #preset sprite groups to be used for colllision purposes
        self.playersp = pygame.sprite.Group()
        self.charclass = 0  #other features that are yet to be implemented
        
        self.luck = 0  
        self.badluck = 0 
        self.enemystate = 0
        self.Map = self.GenerateMap()
        self.globalpos = None
        self.border_gap = 0
        #adds the player sprite to the the group 

        
    def checkifRoom(self,room,i,j): #checks whether if a element in the self.Map/list is a room
        roomstate = room[i][j]
        new_i = random.randint(0,len(room)-1)
        new_j = random.randint(0,len(room[0])-1)
        if roomstate != 'R': #if the roomstate isn't R (i.e its E or B)
            return self.checkifRoom(room,new_i,new_j) #recurssive call the function to check again
        else:
            return i,j 
        
    def GenerateMap(self):  #calls a class imported from a separate file to generate grid
        Grid = GridGenerator() #calls the class 
        Rooms = Grid.Layout() #generates the room, outputs a list
        Map = Grid.GenerateEnemyRoom(Rooms) #input is a list, the output is a modified version of the list
        return Map
            
    def Save(self):
        with open("file1", "wb") as file:
            pickle.dump(self.Map,file)
            pickle.dump(self.globalpos,file)
            
            
    def Load(self):
        with open("file1","rb") as file:
            map = pickle.load(file)
            position = pickle.load(file)
        return map,position
    def RunGame(self,File=None):  #runs the game 
        player = Player(self._screenx,self._screeny) #calls the player class
        self.playersp.add(player) 
       
        Load = File
        if Load != None:
            print('reach?')
            self.Map = Load[0]
            playerpos = Load[1]
            currentpos = playerpos
            ma = MiniMap(self._screen,self.Map)
        else:
            print("or did it reach here")
            Roomi = random.randint(0,len(self.Map)-1) 
            Roomj = random.randint(0,len(self.Map[0])-1)
            roompos = self.checkifRoom(self.Map,Roomi,Roomj) #and pass it through a function to check whether if its a valid room with no enemies 
            
            #m = pygame.Surface((800,300))
            #m.fill((0,222,0))
            ma = MiniMap(self._screen,self.Map)
        
            self.Map[roompos[0]][roompos[1]] = "#"  #player symbol
            playerpos = (roompos[0],roompos[1])  #a tuple to represent the player position on the self.Map
             #by default, there are no enemies in the room 
            currentpos = playerpos
            self.globalpos = (playerpos[0],playerpos[1])
             #preset values to check how many times has the enemy spaned
           #a separate group to draw obstacles, the idea is to have a group of obstacles ready to be added to another group to ONLY draw
            #specific obstacles in each room, as each room has a set obstacle assigned to it     
        # print("is this reaching multiple times?") 
        ObstacleGroup = pygame.sprite.Group() #obstacle group to be used to draw obstacles in every room 
        for i,value in enumerate(self.Map):  #iterates the entire self.Map to add a separate obstacle, still improving
            for j,val in enumerate(value):  
                for _ in range(0,3):
                    obs = RoomObstacles(i,j)
                    ObstacleGroup.add(obs)
        ObstacleToDraw = pygame.sprite.Group()  
        TimesSpawned = 0 
        EnemyInRoom = 0
        running = 1
        while running:
            self.clock.tick(120)
            pygame.mouse.set_visible(0)
            self._screen.fill(self._White) 
            TopLeft = pygame.draw.rect(self._screen,self._Black,(0,0,700,40))    #walls/borders, there are variants of wall as the 'exit' to different rooms will be a separate wall
            TopRight = pygame.draw.rect(self._screen,self._Black,(1220,0,700,40))
            DownLeft = pygame.draw.rect(self._screen, self._Black, (0,1040, 700,40))
            DownRight = pygame.draw.rect(self._screen, self._Black, (1220,1040, 700,40))
            LeftUp = pygame.draw.rect(self._screen, self._Black, (0,0, 40,350))
            LeftDown = pygame.draw.rect(self._screen, self._Black, (0,730, 40,350))
            RightUp = pygame.draw.rect(self._screen, self._Black, (1880,0,40,350))
            RightDown = pygame.draw.rect(self._screen, self._Black, (1880,730,40,350))
            #check which position is it currently
            if currentpos != playerpos:
                ObstacleToDraw.empty()
                for obstacle in ObstacleGroup:
                    if obstacle.i == playerpos[0] and obstacle.j == playerpos[1]:
                        ObstacleToDraw.add(obstacle)
            else:
                for obstacle in ObstacleGroup:
                    if obstacle.i == playerpos[0] and obstacle.j == playerpos[1]:
                        ObstacleToDraw.add(obstacle)  #simple check to see if obstacles are being drawn    
            
            
             #draws th*e obstacle
            
            #rect = pygame.Rect(50,500,300,300)
            #pygame.draw.rect(self._screen,self._Black, rect)
            #self._screen.blit()*
            if LeftUp.colliderect(player.rect) or LeftDown.colliderect(player.rect):    #these statements make sure that the player does not go through the borders
                player.rect.x = 40
            if RightUp.colliderect(player.rect) or RightDown.colliderect(player.rect):
                player.rect.x = 1830  
            if DownLeft.colliderect(player.rect) or DownRight.colliderect(player.rect):
                player.rect.y = 990
            if TopLeft.colliderect(player.rect) or TopRight.colliderect(player.rect):
                player.rect.y = 40
            
            if EnemyInRoom == 0:  #if there are no enemies in the room, then check the player position on the self.Map and see if the adjacent rooms are passable or not.
                                      #if the adjacent room/element is empty (not P, E or B), then a self._Black wall will replace the self._White wall in that corresponding place
                if playerpos[0] != len(self.Map)-1: #checks if the player is at a border
                    if self.Map[playerpos[0]+1][playerpos[1]] == 'R' or self.Map[playerpos[0]+1][playerpos[1]] == 'E' or self.Map[playerpos[0]+1][playerpos[1]] == 'B':
                        DownExit= pygame.draw.rect(self._screen,self._White,(700,1040,520,40))
                        if self.Map[playerpos[0]+1][playerpos[1]] == 'E':  #if the corresponding room has an enemy
                            if DownExit.colliderect(player.rect):  #and the player has collided the exit rect/exited the room
                                player.rect.x = self._screenx/2  #set values to put them at where they would appear when going through a room from a certain side
                                player.rect.y = 100
                                EnemyInRoom = 1 #set to 1, certain conditions will be applied 
                                self.Map[playerpos[0]][playerpos[1]] = 'R'  #as the player position hasnt been changed, the value gets changed to R as 'Room'
                                self.Map[playerpos[0]+1][playerpos[1]] = '#' #the adjacent room gets changed into the player symbol
                                currentpos = playerpos
                                playerpos = (playerpos[0]+1,playerpos[1]) #then, the player position gets changed accordingly
                                #print(playerpos)
                                self.globalpos = (playerpos[0],playerpos[1])
                                for i in self.Map:  #for convenience, every time the player has moved to a different room the self.Map will be printed out in the terminal, 
                                                #planning to add a self.Map overlay in the main game 
                                    print(i)                  
                        else: 
                            if DownExit.colliderect(player.rect): #if the adjacent room has no enemies, 
                                player.rect.x = self._screenx/2 #then similar operations occur apart from the EnemInRoom being modified.
                                player.rect.y = 100
                                self.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.Map[playerpos[0]+1][playerpos[1]] = '#'
                                currentpos = playerpos
                                playerpos = (playerpos[0]+1,playerpos[1])
                                self.globalpos = (playerpos[0],playerpos[1])
                                #print(playerpos)
                                for i in self.Map:
                                    print(i)#for convenience, every time the player has moved to a different room the self.Map will be printed out in the terminal, 
                                                #planning to add a self.Map overlay in the main game             
                    else:
                        DownExit= pygame.draw.rect(self._screen,self._Black,(700,1040,520,40)) #if there is no room available, then draw a self._Black rectangle
                        if DownExit.colliderect(player.rect): #if the player collides into it: 
                            player.rect.y = 990        #the player will stay in place 
                else:
                    DownExit= pygame.draw.rect(self._screen,self._Black,(700,1040,520,40)) #this is to check whether if the player is at a border or not
                    if DownExit.colliderect(player.rect): 
                        player.rect.y = 990    
                        #rest of the code are relatively similar to this one as its just a different side          
                if playerpos[0] != 0:
                    if self.Map[playerpos[0]-1][playerpos[1]] == 'R' or self.Map[playerpos[0]-1][playerpos[1]] == 'E'or self.Map[playerpos[0]-1][playerpos[1]] == 'B':
                        TopExit = pygame.draw.rect(self._screen,self._White,(700,0,520,40))
                        if self.Map[playerpos[0]-1][playerpos[1]] == 'E':
                            if TopExit.colliderect(player.rect) :
                                player.rect.x = self._screenx/2
                                player.rect.y = self._screeny-100
                                EnemyInRoom = 1        
                                self.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.Map[playerpos[0]-1][playerpos[1]] = '#'
                                currentpos = playerpos
                                playerpos = (playerpos[0]-1,playerpos[1])
                                self.globalpos = (playerpos[0],playerpos[1])
                                for i in self.Map:
                                    print(i)  
                        else: 
                            if TopExit.colliderect(player.rect): 
                                player.rect.x = self._screenx/2
                                player.rect.y = self._screeny-100
                                self.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.Map[playerpos[0]-1][playerpos[1]] = '#'
                                currentpos = playerpos
                                playerpos = (playerpos[0]-1,playerpos[1])
                                self.globalpos = (playerpos[0],playerpos[1])
                                for i in self.Map:
                                    print(i)
                    else:
                        TopExit= pygame.draw.rect(self._screen,self._Black,(700,0,520,40))
                        if TopExit.colliderect(player.rect):
                            player.rect.y = 40
                else:
                    TopExit= pygame.draw.rect(self._screen,self._Black,(700,0,520,40))
                    if TopExit.colliderect(player.rect):
                        player.rect.y = 40
                if playerpos[1] != len(self.Map[0]) -1:
                    if self.Map[playerpos[0]][playerpos[1]+1] == 'R' or self.Map[playerpos[0]][playerpos[1]+1] == 'E' or self.Map[playerpos[0]][playerpos[1]+1] == 'B':
                        RightExit =  pygame.draw.rect(self._screen, self._White,(1880,350,40,380))
                        if self.Map[playerpos[0]][playerpos[1]+1] == 'E':
                            if RightExit.colliderect(player.rect): 
                                player.rect.x = 100
                                player.rect.y = self._screeny/2
                                self.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.Map[playerpos[0]][playerpos[1]+1] = '#'
                                EnemyInRoom = 1
                                currentpos = playerpos
                                playerpos = (playerpos[0],playerpos[1]+1)
                                self.globalpos = (playerpos[0],playerpos[1])
                                print(playerpos)
                                for i in self.Map:
                                    print(i)     
                        else:
                            if RightExit.colliderect(player.rect): 
                                player.rect.x = 100
                                player.rect.y = self._screeny/2
                                self.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.Map[playerpos[0]][playerpos[1]+1] = '#'
                                currentpos = playerpos
                                playerpos = (playerpos[0],playerpos[1]+1)
                                self.globalpos = (playerpos[0],playerpos[1])
                                print(playerpos)
                                for i in self.Map:
                                    print(i)
                    else:
                        RightExit =  pygame.draw.rect(self._screen, self._Black,(1880,350,40,380))
                        if RightExit.colliderect(player.rect):
                            player.rect.x = 1830
                else:
                    RightExit =  pygame.draw.rect(self._screen, self._Black,(1880,350,40,380))
                    if RightExit.colliderect(player.rect):
                        player.rect.x = 1830
                if playerpos[1] != 0:
                    if self.Map[playerpos[0]][playerpos[1]-1] == 'R'or self.Map[playerpos[0]][playerpos[1]-1] == 'E'or self.Map[playerpos[0]][playerpos[1]-1] == 'B':
                        LeftExit = pygame.draw.rect(self._screen, self._White, (0,350,40,380))
                        if self.Map[playerpos[0]][playerpos[1]-1] == 'E':
                            if LeftExit.colliderect(player.rect):
                                '''testing
                                '''
                                player.rect.x = self._screenx-100
                                player.rect.y = self._screeny/2 
                                EnemyInRoom = 1
                                self.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.Map[playerpos[0]][playerpos[1]-1] = '#' 
                                currentpos = playerpos
                                playerpos = (playerpos[0],playerpos[1]-1) 
                                self.globalpos = (playerpos[0],playerpos[1])
                                print(playerpos)
                                for i in self.Map:
                                    print(i)
                        else:
                            if LeftExit.colliderect(player.rect):
                                player.rect.x = self._screenx-100
                                player.rect.y = self._screeny/2 
                                self.Map[playerpos[0]][playerpos[1]] = 'R'
                                self.Map[playerpos[0]][playerpos[1]-1] = '#'
                                currentpos = playerpos  
                                playerpos = (playerpos[0],playerpos[1]-1) 
                                self.globalpos = (playerpos[0],playerpos[1])
                                print(playerpos)
                                for i in self.Map:
                                    print(i)
                    else:
                        LeftExit =  pygame.draw.rect(self._screen, self._Black,(0,350,40,380))
                        if LeftExit.colliderect(player.rect):
                            player.rect.x = 40
                else:
                    LeftExit =  pygame.draw.rect(self._screen, self._Black,(0,350,40,380))
                    if LeftExit.colliderect(player.rect):
                        player.rect.x = 40
            else: #if EnemyInRoom is 1:
                if TimesSpawned < 1:
                    #for i in range(0,3):
                    enemy = Enemy()
                    self.enemies.add(enemy)
                    TimesSpawned +=1 
                DownExit= pygame.draw.rect(self._screen,self._Black,(700,1040,520,40)) #seal all walls shut
                if DownExit.colliderect(player.rect):
                    player.rect.y = 990
                TopExit= pygame.draw.rect(self._screen,self._Black,(700,0,520,40))
                if TopExit.colliderect(player.rect):
                    player.rect.y = 40
                RightExit =  pygame.draw.rect(self._screen, self._Black,(1880,350,40,380))
                if RightExit.colliderect(player.rect):
                    player.rect.x = 1830
                LeftExit =  pygame.draw.rect(self._screen, self._Black,(0,350,40,380))  
                if LeftExit.colliderect(player.rect):
                    player.rect.x = 40
                    
                for projectile in player.projectilegroup:  #checks if player attack projectiles has collided with the enemy
                    collision = pygame.sprite.spritecollide(projectile, self.enemies, 0) #checks within the sprite group whether if 'projectile' has collided with any sprites the sprite group self.enemies
                    for enemy in collision:
                        if enemy.health == 0:  #if enemy health is 0:
                            enemy.kill()     #delete the enemy from the group
                            projectile.kill()
                        elif collision and enemy.health != 0: #if the attack projectile collides, -1 to enemy health 
                            enemy.health -=1
                            projectile.kill()   
                playercol = pygame.sprite.spritecollide(player, self.enemies, 0)
                if len(playercol) != 0:
                    running = 0
                    break
                    
                if len(self.enemies) == 0: #if the sprite group is enpty, return to normal state 
                    print("No more enemies")
                    TimesSpawned = 0
                    EnemyInRoom = 0 
                self.enemies.draw(self._screen)
                self.enemies.update(player.rect.x,player.rect.y) #player positions are passed into the update function for the enemy to move towards the player
            player.projectilegroup.draw(self._screen)
            player.projectilegroup.update()
            self.playersp.draw(self._screen)
            self.playersp.update()
            ObstacleToDraw.draw(self._screen)
            ObstacleToDraw.update()
            ma.update()            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Did the user click the window close button?
                    running = 0
                    sys.exit()  
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_ESCAPE: #one time events
                        #running = 0
                        running = self.Pause()     #pause menu         
                    if event.key == pygame.K_DOWN:  #attack projectiles
                        player.Attackdown()
                    if event.key == pygame.K_UP:
                        player.Attackup()
                    if event.key == pygame.K_RIGHT:
                        player.Attackright()
                    if event.key == pygame.K_LEFT:
                        player.Attackleft()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click = 1   
            pygame.display.update()    
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
            mousex, mousey = pygame.mouse.get_pos()
            if SaveGame.collidepoint(mousex,mousey) and click == 1:
                print('reach')
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
     
    def option(self):
        running = 1
        while running: 
            self._screen.fill(self._Black)
            self._screen.blit(self._textfont.render("options",1, self._Black), (200,50))
            #button3 = pygame.draw.rect(self._screen, self._Black,(100,100,50,50))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Did the user click the window close button?
                    running = 0
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click = 1
            pygame.display.update()
            
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
                return charclass[i],stats

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
    def save():
        pass                
           
if __name__ == "__main__":
    Main()