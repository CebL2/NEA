#TO DO
#Implement Projectiles #DONE 
#Room traversal with restrictiosn #DONE
#Enemy spawn
#Room modifications (obstacles)         
#Character creation with built in speical abilities for different classes    #PROGRESS
#Spells

import numpy as np
import pygame, sys, random, os

from pygame.constants import FULLSCREEN
from Enemy import *
from Attack import *
from AttackDown import *
from AttackLeft import *
from AttackRight import *
from GridGenerator import *
from Stats import *
from Obstacles import *
#import pickle

clock = pygame.time.Clock()
White = (255,255,255) #preset values for colour and resolution
Black = (0,0,0)
screenx = 1920
screeny = 1080
pygame.init()

#display = pygame.display.set_mode((300,200))
textfont = pygame.font.Font(r'C:\Windows\Fonts\georgia.ttf', 50 ) 
 
click = False
test = textfont.render("test", True, White)
screen = pygame.display.set_mode((screenx,screeny),pygame.FULLSCREEN)
running = True

spawnamount_easy = random.randint(0,4)
spawnamount_medium = random.randint(5,8)
spawnamount_hard = random.randint(9,12)
#json to save files
#write is save
#read is load 
#in order to save, we need to dump or write binary data with binary write 
#with open("filename.txt",'wb') as file 
#file.dump(data) with the pickle module?
# with open ('test.txt', 'w') as file:
#     file.write("this is a test")
#     file.close()
def Main():

    MainGame = Game(screenx,screeny)
    MainGame.MainMenu()

#procedural generation

#when the player goes to a new room so some kind of condition that acknowledges that the player has moved into a new room or region
#spawn enemies and enemy types accordingly 




#have multiple huds/menus and parse it through the class
#if a button is pressed, call the specific function 
class Hud:
    def __init__(self, screenx,screeny):
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
        

#if playerclass = warrior:
#


class Player(pygame.sprite.Sprite):
    player_image = pygame.Surface((50,50)) 
    player_image.fill((0,255,0))
    def __init__(self,screenx,screeny):      
        super().__init__() 
        self.image = Player.player_image
        self.rect = self.image.get_rect()
        self.rect.center = (1280/2, 1024/2)
        self.vectorposition = pygame.math.Vector2(self.rect.x,self.rect.y)
        self.speed = 3
        self.screenx = screenx
        self.screeny = screeny
        self.gap = 0 
        self.projectilegroup = pygame.sprite.Group()
        # self.charClass = charclass
        # self.statblock = statblock
        # self.charlist = charclasslist
        
    def PlayerClass(self):
        if self.charClass == self.charlist[0]:#warrior #charclass = ["Warrior","Mage","Paladin","Rogue"]
            bonuses = Warrior()
        elif self.charclass == self.charlist[1]:
            bonuses = Mage()
        elif self.charclass == self.charlist[2]:
            bonuses = Paladin()    
        else:
            bonuses = Rogue()     #add bonuses to statblock
            
    def Spell(self,charclass,charlist):
        thing = Spells()    
    def update(self):

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_s] and self.rect.y < self.screeny:
            self.rect.y += self.speed
        if keypressed[pygame.K_w] and self.rect.y > 0:
            self.rect.y  -= self.speed
        if keypressed[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keypressed[pygame.K_d] and self.rect.x <  self.screenx:
            self.rect.x += self.speed
      

    def Attackup(self):
        projectileup = Attack(self.rect.centerx,self.rect.centery-100)
        self.projectilegroup.add(projectileup)
        
        
    def Attackdown(self):
        projectiledown = AttackDown(self.rect.centerx,self.rect.centery+100)
        self.projectilegroup.add(projectiledown)
        
    def Attackright(self):
        projectiledown = AttackRight(self.rect.centerx+50,self.rect.centery)
        self.projectilegroup.add(projectiledown)
        
    def Attackleft(self):
        projectiledown = AttackLeft(self.rect.centerx-50,self.rect.centery)
        self.projectilegroup.add(projectiledown)
             
        
class Game():
    def __init__(self,screenx,screeny):
        self.enemies = pygame.sprite.Group()
        self.playersp = pygame.sprite.Group()
        self.obstaclegroup = pygame.sprite.Group()
        self.charclass = 0
        self.Map = []
        self.luck = 0 
        self.badluck = 0 
        self.enemystate = False
        self.border_gap = 0
        self.player = Player(screenx,screeny)
        self.playersp.add(self.player)
        #self.obstacle = RoomObstacles()
        #self.obstaclegroup.add(self.obstacle)
        #self.allsprites.add(self.player)
        
    def GenerateObstacles(self):
        pass

    def GenerateMap(self):
        Grid = GridGenerator()
        Rooms = Grid.Layout()
        Map = Grid.GenerateEnemyRoom(Rooms)
        return Map
    
          

    def GenerateWalls(self,Rooms):
        for i in len(Rooms)-1:
            for j in len(i):
                print(j)
            
    def RunGame(self):
        Map = self.GenerateMap()
        
        Roomi = random.randint(0,len(Map)-1)
        Roomj = random.randint(0,len(Map[0])-1)
        
        roompos = self.checkifRoom(Map,Roomi,Roomj)

        
        #enemy = Enemy()
        # Obstacles = RoomObstacles()
        # self.obstacles.add()
        Map[roompos[0]][roompos[1]] = "#"
        
       
        playerpos = (roompos[0],roompos[1])
        
        EnemyInRoom = False
        EnemyBattle = False
        
        
        TimesSpawned = 0 
        
        
        
        for i in Map:
            print(i)
            
       
        running = True
        while running:
            screen.fill(White)
            ##############      ##############
            #           #                    #
                    ##########
            #        ###                     #
            ##############      ##############
            TopLeft = pygame.draw.rect(screen,Black,(0,0,700,40))
            TopRight = pygame.draw.rect(screen,Black,(1220,0,700,40))
            DownLeft = pygame.draw.rect(screen, Black, (0,1040, 700,40))
            DownRight = pygame.draw.rect(screen, Black, (1220,1040, 700,40))
            LeftUp = pygame.draw.rect(screen, Black, (0,0, 40,350))
            LeftDown = pygame.draw.rect(screen, Black, (0,730, 40,350))
            RightUp = pygame.draw.rect(screen, Black, (1880,0,40,350))
            RightDown = pygame.draw.rect(screen, Black, (1880,730,40,350))
            
            if LeftUp.colliderect(self.player.rect) or LeftDown.colliderect(self.player.rect):
                self.player.rect.x = 40
            if RightUp.colliderect(self.player.rect) or RightDown.colliderect(self.player.rect):
                    self.player.rect.x = 1830
                
            if DownLeft.colliderect(self.player.rect) or DownRight.colliderect(self.player.rect):
                self.player.rect.y = 990
                
            if TopLeft.colliderect(self.player.rect) or TopRight.colliderect(self.player.rect):
                self.player.rect.y = 40
                
            #print(self.enemy.health)
          
                    
            if EnemyInRoom == False:
                
                if playerpos[0] != len(Map)-1:
                    if Map[playerpos[0]+1][playerpos[1]] == 'R' or Map[playerpos[0]+1][playerpos[1]] == 'E' or Map[playerpos[0]+1][playerpos[1]] == 'B':
                        

                        DownExit= pygame.draw.rect(screen,White,(700,1040,520,40))
                        if Map[playerpos[0]+1][playerpos[1]] == 'E':
                            if DownExit.colliderect(self.player.rect):
                                self.player.rect.x = screenx/2 
                                self.player.rect.y = 100
                                EnemyInRoom = True
                               
                                Map[playerpos[0]][playerpos[1]] = 'R'
                                Map[playerpos[0]+1][playerpos[1]] = '#'
                                playerpos = (playerpos[0]+1,playerpos[1])
                                print(playerpos)
                                for i in Map:
                                    print(i)
                                
                        else:
                            
                            if DownExit.colliderect(self.player.rect):
                                self.player.rect.x = screenx/2 
                                self.player.rect.y = 100
                                Map[playerpos[0]][playerpos[1]] = 'R'
                                Map[playerpos[0]+1][playerpos[1]] = '#'
                                playerpos = (playerpos[0]+1,playerpos[1])
                                print(playerpos)
                                for i in Map:
                                    print(i)
                                    
                    else:
                        DownExit= pygame.draw.rect(screen,Black,(700,1040,520,40))
                        if DownExit.colliderect(self.player.rect):
                            self.player.rect.y = 990
                else:
                    DownExit= pygame.draw.rect(screen,Black,(700,1040,520,40))
                    if DownExit.colliderect(self.player.rect):
                        self.player.rect.y = 990    
                            
                if playerpos[0] != 0:
                    if Map[playerpos[0]-1][playerpos[1]] == 'R' or Map[playerpos[0]-1][playerpos[1]] == 'E'or Map[playerpos[0]-1][playerpos[1]] == 'B':
                        TopExit = pygame.draw.rect(screen,White,(700,0,520,40))
                        if Map[playerpos[0]-1][playerpos[1]] == 'E':
                            if TopExit.colliderect(self.player.rect) :
                            
                                self.player.rect.x = screenx/2
                                self.player.rect.y = screeny-100
                                EnemyInRoom = True
                                
                                
                                Map[playerpos[0]][playerpos[1]] = 'R'
                                Map[playerpos[0]-1][playerpos[1]] = '#'
                                playerpos = (playerpos[0]-1,playerpos[1])
                                print(playerpos)
                                for i in Map:
                                    print(i)
                            
                        else:
                           
                            if TopExit.colliderect(self.player.rect) :
                        
                                self.player.rect.x = screenx/2
                                self.player.rect.y = screeny-100
                                Map[playerpos[0]][playerpos[1]] = 'R'
                                Map[playerpos[0]-1][playerpos[1]] = '#'
                                playerpos = (playerpos[0]-1,playerpos[1])
                                print(playerpos)
                                for i in Map:
                                    print(i)
                    else:
                        TopExit= pygame.draw.rect(screen,Black,(700,0,520,40))
                        if TopExit.colliderect(self.player.rect):
                            self.player.rect.y = 40
                else:
                    TopExit= pygame.draw.rect(screen,Black,(700,0,520,40))
                    if TopExit.colliderect(self.player.rect):
                        self.player.rect.y = 40
                if playerpos[1] != len(Map[0]) -1:
                    if Map[playerpos[0]][playerpos[1]+1] == 'R' or Map[playerpos[0]][playerpos[1]+1] == 'E' or Map[playerpos[0]][playerpos[1]+1] == 'B':
                        RightExit =  pygame.draw.rect(screen, White,(1880,350,40,380))
                        
                        if Map[playerpos[0]][playerpos[1]+1] == 'E':
                            if RightExit.colliderect(self.player.rect): 
                                self.player.rect.x = 100
                                self.player.rect.y = screeny/2
                                Map[playerpos[0]][playerpos[1]] = 'R'
                                Map[playerpos[0]][playerpos[1]+1] = '#'
                             
                                EnemyInRoom = True
                                RightExit =  pygame.draw.rect(screen, Black,(1880,350,40,380))
                                playerpos = (playerpos[0],playerpos[1]+1)
                                print(playerpos)
                                for i in Map:
                                    print(i)
                              
                                
                        else:
                            
                            if RightExit.colliderect(self.player.rect): 
                                self.player.rect.x = 100
                                self.player.rect.y = screeny/2
                                Map[playerpos[0]][playerpos[1]] = 'R'
                                Map[playerpos[0]][playerpos[1]+1] = '#'
                                playerpos = (playerpos[0],playerpos[1]+1)
                                print(playerpos)
                                for i in Map:
                                    print(i)
                    else:
                        RightExit =  pygame.draw.rect(screen, Black,(1880,350,40,380))
                        if RightExit.colliderect(self.player.rect):
                            self.player.rect.x = 1830
                else:
                    RightExit =  pygame.draw.rect(screen, Black,(1880,350,40,380))
                    if RightExit.colliderect(self.player.rect):
                        self.player.rect.x = 1830
                if playerpos[1] != 0:
                    if Map[playerpos[0]][playerpos[1]-1] == 'R'or Map[playerpos[0]][playerpos[1]-1] == 'E'or Map[playerpos[0]][playerpos[1]-1] == 'B':
                        
                        LeftExit = pygame.draw.rect(screen, White, (0,350,40,380))
                        if Map[playerpos[0]][playerpos[1]-1] == 'E':
                            if LeftExit.colliderect(self.player.rect):
                            
                                self.player.rect.x = screenx-100
                                self.player.rect.y = screeny/2 
                                EnemyInRoom = True
                                Map[playerpos[0]][playerpos[1]] = 'R'
                                Map[playerpos[0]][playerpos[1]-1] = '#' 
                                playerpos = (playerpos[0],playerpos[1]-1) 
                                print(playerpos)
                                for i in Map:
                                    print(i)
                        else:
                            
                            if LeftExit.colliderect(self.player.rect):
                                self.player.rect.x = screenx-100
                                self.player.rect.y = screeny/2 
                                Map[playerpos[0]][playerpos[1]] = 'R'
                                Map[playerpos[0]][playerpos[1]-1] = '#'  
                                playerpos = (playerpos[0],playerpos[1]-1) 
                                print(playerpos)
                                for i in Map:
                                    print(i)
                    else:
                        LeftExit =  pygame.draw.rect(screen, Black,(0,350,40,380))
                        if LeftExit.colliderect(self.player.rect):
                            self.player.rect.x = 40
                else:
                    LeftExit =  pygame.draw.rect(screen, Black,(0,350,40,380))
                    if LeftExit.colliderect(self.player.rect):
                        self.player.rect.x = 40
                
            else:
               
                
                if TimesSpawned < 1:
                    for i in range(0,3):
                        enemy= Enemy()
                        
                        self.enemies.add(enemy)
                    TimesSpawned +=1
            
                DownExit= pygame.draw.rect(screen,Black,(700,1040,520,40))
                if DownExit.colliderect(self.player.rect):
                    self.player.rect.y = 990
               
               
                TopExit= pygame.draw.rect(screen,Black,(700,0,520,40))
                if TopExit.colliderect(self.player.rect):
                    self.player.rect.y = 40
                
            
                RightExit =  pygame.draw.rect(screen, Black,(1880,350,40,380))
                if RightExit.colliderect(self.player.rect):
                    self.player.rect.x = 1830
               

                LeftExit =  pygame.draw.rect(screen, Black,(0,350,40,380))
                if LeftExit.colliderect(self.player.rect):
                    self.player.rect.x = 40
                    
                for projectile in self.player.projectilegroup:
                    collision = pygame.sprite.spritecollide(projectile, self.enemies, False)
                    for enemy in collision:
                        if enemy.health == 0:
                            enemy.kill()    
                            projectile.kill()
                        if pygame.sprite.spritecollide(projectile, self.enemies, False) and enemy.health != 0:
                            enemy.health -=1
                            projectile.kill()    
  

                
                if len(self.enemies) == 0:
                    print("No more enemies")
                    TimesSpawned = 0
                    EnemyInRoom = False 
                
            self.enemies.draw(screen)
            self.enemies.update()
            self.player.projectilegroup.draw(screen)
            self.player.projectilegroup.update()
            self.playersp.draw(screen)
            self.playersp.update()
            #self.obstaclegroup.draw(screen)
            #self.obstaclegroup.update()
            
                #consider usint pygame.event toget key presses?
                #keypressed is useful for continuous movement
                #events are useful for one time states
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Did the user click the window close button?
                    running = False
                    sys.exit()  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        #running = False
                        running = self.Pause()               
                    if event.key == pygame.K_DOWN:
                        self.player.Attackdown()
                    if event.key == pygame.K_UP:
                        self.player.Attackup()
                    if event.key == pygame.K_RIGHT:
                        self.player.Attackright()
                    if event.key == pygame.K_LEFT:
                        self.player.Attackleft()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click = True   
                    
            pygame.display.update()    
                    

    def Pause(self):
        print("does this reach")
        running = True
        click = False
        while running:
            screen.fill(White)
            BackToGame = pygame.draw.rect(screen, Black,(100,200,200,200))
            screen.blit(textfont.render("Back",True, White),(100,200))
            ExittoMenu = pygame.draw.rect(screen, Black,(100,500,200,200))
            mousex, mousey = pygame.mouse.get_pos()
            if BackToGame.collidepoint(mousex,mousey):
                if click == True:
                    running = False 
                    click = False  
                    return True
            if ExittoMenu.collidepoint(mousex,mousey):
                if click == True:
                    running = False
                    click = False
                    return False  
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Did the user click the window close button?
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        return True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
            pygame.display.update()
     
    def option(self):
        running = True
        while running: 
            screen.fill(Black)
            screen.blit(textfont.render("options",True, Black), (200,50))
            button3 = pygame.draw.rect(screen, Black,(100,100,50,50))
            screen.blit(test, (50,50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Did the user click the window close button?
                    running = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click = True
            pygame.display.update()
    def CharacterCreation(self):
        running = True
        charclass = ["Warrior","Mage","Paladin","Rogue"]
        ability = ["Melee","Magic","Heal"]
        stats = { 'Speed' : 0,
                  'Damage': 0,
                  'Spell Damage': 0,
                  'Health': 0
                }
        
        i = 0
        click = False
        statpoints = 20
        while running:
            
      
            #Class
            screen.fill(Black)
            mousex, mousey = pygame.mouse.get_pos()
            next = pygame.draw.rect(screen, White,(1000,300,100,100))
            prev = pygame.draw.rect(screen, White,(600,300,100,100))
            screen.blit(textfont.render("Choose your class", True, White), (800,50))
            screen.blit(textfont.render("Next", True, Black), (1000,300))
            screen.blit(textfont.render(charclass[i],True,White),(800,300))
            screen.blit(textfont.render("Prev", True,Black), (600,300))
            screen.blit(textfont.render("Randomise", True, White), (950,950))
            Randomise = pygame.draw.rect(screen, Black,(950,950,100,100))
            play = pygame.draw.rect(screen, Black,(900,900,100,100))
            screen.blit(textfont.render("Play", True, White), (900,900))
            pygame.draw.rect(screen, Black,(375,500,100,100))

            AddSpeed = pygame.draw.polygon(screen, White,[(600,600),(600,700),(550,500)])
            # RedSpeed = pygame.draw.rect(screen, Black,(900,900,100,100))
            # AddDamage =pygame.draw.rect(screen, Black,(900,900,100,100))
            # RedDamage=pygame.draw.rect(screen, Black,(900,900,100,100))
            # AddSpellD=pygame.draw.rect(screen, Black,(900,900,100,100))
            # RedSpellD=pygame.draw.rect(screen, Black,(900,900,100,100))
            # AddHealth=pygame.draw.rect(screen, Black,(900,900,100,100))
            # RedHealth=pygame.draw.rect(screen, Black,(900,900,100,100))
            # (pos),(size)
            #Stat 
            Speed = pygame.draw.rect(screen, White,(500,500,150,100))
            Damage =pygame.draw.rect(screen, White,(1500,800,150,100))
            SpellDmg =pygame.draw.rect(screen, White,(500,800,150,100))
            Health =pygame.draw.rect(screen, White,(1500,500,150,100))          
            screen.blit(textfont.render("Speed", True, White), (350,500))
            screen.blit(textfont.render("Damage", True, White), (850,800))
            screen.blit(textfont.render("Spell Damage", True, White), (350, 800))
            screen.blit(textfont.render("Health", True, White), (850,500))
          
            if Randomise.collidepoint(mousex,mousey) and click == True:
                pass
            #if button hit
            #respective stat block increases or decreases
            #return stat dictionary
            if next.collidepoint(mousex,mousey) and click == True:
               
                pygame.draw.rect(screen, Black,(375,500,100,100))
                
               
                if i == len(charclass)-1:
                    print("this should reach")
                    pygame.draw.rect(screen, Black,(375,500,100,100))
                    screen.blit(textfont.render(charclass[0],True,White),(800,300))
                    i = 0

                else:
                    
                    screen.blit(textfont.render(charclass[i+1],True,Black),(800,300))
                    i += 1
                #print(charclass[i])
                click = False
            if prev.collidepoint(mousex,mousey) and click == True: #if click == true and false the moment the mouse button comes up 
                #print("reach 2")
                pygame.draw.rect(screen, Black,(375,500,100,100))
               
                
                if i ==0:
                  
                        pygame.draw.rect(screen, Black,(375,500,100,100))
                        screen.blit(textfont.render(charclass[i-1],True,White),(800,300))
                        i = len(charclass) -1
                        
                else:
                    
                    screen.blit(textfont.render(charclass[i-1],True,Black),(800,300))
                    i -= 1 
                click = False
            if play.collidepoint(mousex,mousey) and click == True:
                running = False
               
                return charclass[i],stats
            
            
            
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Did the user click the window close button?
                    running = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = True
                
                    
               
            pygame.display.update()   
    def MainMenu(self):
        click = False
        while running:
            
            screen.fill(Black) #the colour
            button1 = pygame.draw.rect(screen, White,(900,300,100,100))
            screen.blit(textfont.render("Play", True, Black), (900,300))
            mousex, mousey = pygame.mouse.get_pos()
            if button1.collidepoint(mousex,mousey) and event.type == pygame.MOUSEBUTTONDOWN:
            
                #charac = CharacterCreation()
                self.CharacterCreation()
                self.RunGame()
                           
            button2 = pygame.draw.rect(screen, Black,(100,100,100,50))
            screen.blit(textfont.render("Options", True, White), (100,100))
            if button2.collidepoint(mousex,mousey) and event.type == pygame.MOUSEBUTTONDOWN:
                self.option()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Did the user click the window close button?
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     click = True
                #     print("click reach")
               
            pygame.display.update()
    def save():
        pass                
        

    
    def checkifRoom(self,room,i,j):  
    #what if i = 1 and j =2?
        roomstate = room[i][j]
        new_i = random.randint(0,len(room)-1)
        new_j = random.randint(0,len(room[0])-1)
        if roomstate != 'R':
            return self.checkifRoom(room,new_i,new_j)
        else:
            return i,j 
        
if __name__ == "__main__":
    Main()