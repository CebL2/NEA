#TO DO
#Implement Projectiles
#Room traversal with restrictiosn
#Enemy spawn
#Room modifications (obstacles)
#Character creation with built in speical abilities for different classes

import numpy as np
import pygame, sys, random, os
from Enemy import Enemy
from Attack import Attack
from AttackDown import AttackDown
from AttackLeft import AttackLeft
from AttackRight import AttackRight
from GridGenerator import GridGenerator
pygame.init()

#import pickle

clock = pygame.time.Clock()
White = (255,255,255) #preset values for colour and resolution
Black = (0,0,0)
screenx = 1280
screeny = 1024

clock.tick()
display = pygame.display.set_mode((300,200))
textfont = pygame.font.Font(r'C:\Windows\Fonts\georgia.ttf', 16 ) 
 
click = False
test = textfont.render("test", True, White)
screen = pygame.display.set_mode((screenx,screeny))
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



#delay = pygame.time()

#when d


#procedural generation

#when the player goes to a new room so some kind of condition that acknowledges that the player has moved into a new room or region
#spawn enemies and enemy types accordingly 


#room generation
#based on the player's power level or such
#put obstacles/secrets accordingly
#a lot of random generated types will be used here


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
    player_image = pygame.Surface((100,200)) 
    def __init__(self,screenx,screeny):      
        super().__init__() 
        self.image = Player.player_image
        self.rect = self.image.get_rect()
        self.rect.center = (1280/2, 1024/2)
        self.speed = 1
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
        if keypressed[pygame.K_s] and self.rect.y < self.screeny > self.gap :
            self.rect.y += self.speed
        if keypressed[pygame.K_a] and self.rect.x > self.gap :
            self.rect.x -= self.speed
        if keypressed[pygame.K_d] and self.rect.x <  self.screenx -self.gap:
            self.rect.x += self.speed
        if keypressed[pygame.K_w] and self.rect.y > self.gap:
            self.rect.y -= self.speed

    def shootdown(self):
        projectileup = Attack(self.rect.centerx,self.rect.centery+100)
        self.projectilegroup.add(projectileup)
       
    def shootup(self):
        projectiledown = AttackDown(self.rect.centerx,self.rect.centery-100)
        self.projectilegroup.add(projectiledown)
        
    def shootright(self):
        projectiledown = AttackRight(self.rect.centerx+50,self.rect.centery)
        self.projectilegroup.add(projectiledown)
        
    def shootleft(self):
        projectiledown = AttackLeft(self.rect.centerx-50,self.rect.centery)
        self.projectilegroup.add(projectiledown)
        
      
        
        
class Game():
    
    def __init__(self,screenx,screeny):
        self.enemies = pygame.sprite.Group()
        self.playersp = pygame.sprite.Group()
        self.allsprites = pygame.sprite.Group()
        self.charclass = 0
        self.Grid = []
#def game(charclass):
    #if charclass = warrior
    #give special skill1
    #if charclass = mage
    #give special skill2d
        self.luck = 0 
        self.badluck = 0 
    #nextroom = False
    #power_level = 0 #to indicated the player's power level 
        self.enemystate = False
        self.border_gap = 0
       # print(charclass)
        self.player = Player(screenx,screeny)
        self.playersp.add(self.player)
        self.allsprites.add(self.player)
        #Rooms = []
        for i in range(0,3):
        #enemy = Enemy() #put coords as a input see if it works 
            enemy= Enemy()
            self.enemies.add(enemy)
            self.allsprites.add(enemy)

    #Rooms = RoomLayout(Rooms)
   

    #i = random.randint(0,len(Rooms)-1)
   # j = random.randint(0,len(Rooms[0])-1) 
    #    
    def GenerateGrid(self):
        self.Grid = GridGenerator()
        return self.Grid.Layout()
    
          


   
    def GenerateWalls(self,Rooms):
        for i in len(Rooms)-1:
            for j in len(i):
                print(j)
            
    def RunGame(self):
        Grid = self.GenerateGrid()
       
        Roomi = random.randint(0,len(Grid)-1)
        Roomj = random.randint(0,len(Grid[0])-1)
        print("above")
        roompos = self.checkifRoom(Grid,Roomi,Roomj)
        print("below")
        
        
        Grid[roompos[0]][roompos[1]] = "#"
        playerpos = (roompos[0],roompos[1])
        print(playerpos)
        
        for i in Grid:
            print(i)
    
        running = True
        while running:
            screen.fill(White)
            ##############      ##############
            #                                #
        
                                        
            #                                #
            ##############      ##############
            
            for projectile in self.player.projectilegroup:
                if pygame.sprite.spritecollide(projectile, self.enemies, True, None):
                    projectile.kill()
                    #enemy.kill()
                    #    
        
            # Topleft 
            # Topright
            
            Top = pygame.draw.rect(screen, Black, (0,0,1280,10))
            Left = pygame.draw.rect(screen, Black, (0,0, 10,1280))
            Right = pygame.draw.rect(screen, Black, (1270,0,10,1280))
            Down = pygame.draw.rect(screen, Black, (0,1014, 1280,10))
            #def function (enemystate)
            #if enemystate = true:
            #player rect x and rect y will constantly be forced in the room
            #speed becomes 0 when bumped into a wall 
            if Down.collidepoint(self.player.rect.x, self.player.rect.y) and playerpos[0] != len(Grid)-1:   #problem is the second statement
                if Grid[playerpos[0]+1][playerpos[1]] == 'R' :
                    
                    self.player.rect.x = screenx/2 - 100
                    self.player.rect.y = 50
                    Grid[playerpos[0]][playerpos[1]] = 'R'
                    Grid[playerpos[0]+1][playerpos[1]] = '#'
                    playerpos = (playerpos[0]+1,playerpos[1])
                    print(playerpos)
                    for i in Grid:
                        print(i)
                    #spawn enemy algorithm here
                    #print(player.rect.x)
            if Top.collidepoint(self.player.rect.x, self.player.rect.y)  and playerpos[0] != 0: 
                if Grid[playerpos[0]-1][playerpos[1]] == 'R':
                    self.player.rect.x = screenx/2
                    self.player.rect.y = screeny-50
                    Grid[playerpos[0]][playerpos[1]] = 'R'
                    Grid[playerpos[0]-1][playerpos[1]] = '#'
                    playerpos = (playerpos[0]-1,playerpos[1])
                    print(playerpos)
                    for i in Grid:
                        print(i)    
            if Right.collidepoint(self.player.rect.x, self.player.rect.y)and  playerpos[1] != len(Grid[0]) -1: 
                if Grid[playerpos[0]][playerpos[1]+1] == 'R':
                    self.player.rect.x = 50
                    self.player.rect.y = screeny/2
                    Grid[playerpos[0]][playerpos[1]] = 'R'
                    Grid[playerpos[0]][playerpos[1]+1] = '#'
                    playerpos = (playerpos[0],playerpos[1]+1)
                    print(playerpos)
                    for i in Grid:
                        print(i)
            if Left.collidepoint(self.player.rect.x, self.player.rect.y)and playerpos[1] != 0: 
                if Grid[playerpos[0]][playerpos[1]-1] == 'R':
                    self.player.rect.x = screenx-50
                    self.player.rect.y = screeny/2 
                    Grid[playerpos[0]][playerpos[1]] = 'R'
                    Grid[playerpos[0]][playerpos[1]-1] = '#'  
                    playerpos = (playerpos[0],playerpos[1]-1) 
                    print(playerpos)
                    for i in Grid:
                        print(i)
            self.enemies.draw(screen)
            self.enemies.update()
            self.player.projectilegroup.draw(screen)
            self.player.projectilegroup.update()
            self.playersp.update()
            self.playersp.draw(screen)
        
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
                        self.Pause()               
                    if event.key == pygame.K_DOWN:
                        self.player.shootdown()
                    if event.key == pygame.K_UP:
                       self.player.shootup()
                    if event.key == pygame.K_RIGHT:
                        self.player.shootright()
                    if event.key == pygame.K_LEFT:
                        self.player.shootleft()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click = True       
            pygame.display.update()         

    def Pause(self):
        print("does this reach")
        running = True
        click = False
        while running:
            screen.fill(White)
            exitbutton = pygame.draw.rect(screen, Black,(100,200,200,200))
            mousex, mousey = pygame.mouse.get_pos()
            if exitbutton.collidepoint(mousex,mousey):
                if click == True:
                    print("reach?")
                    running = False 
                    click = False        
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Did the user click the window close button?
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
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
        stats = ['Speed','Damage','Spell damage','Health']
        
        i = 0
        click = False
       
        while running:
            
            #print(click)
            screen.fill(White)
            mousex, mousey = pygame.mouse.get_pos()
            next = pygame.draw.rect(screen, Black,(700,100,100,100))
            prev = pygame.draw.rect(screen, Black,(350,100,100,100))
            screen.blit(textfont.render("Choose your class", True, Black), (575,100))
            screen.blit(textfont.render("Next", True, White), (700,100))
            screen.blit(textfont.render("Prev", True, White), (350,100))
            screen.blit(textfont.render("Randomise", True, Black), (575,200))
            play = pygame.draw.rect(screen, Black,(375,900,100,100))
            
            
            
            # (pos),(size)
            pygame.draw.rect(screen, Black,(500,300,100,100))
            pygame.draw.rect(screen, Black,(500,400,100,100))
            pygame.draw.rect(screen, Black,(500,500,100,100))
            pygame.draw.rect(screen, Black,(500,600,100,100))
            screen.blit(textfont.render("Speed", True, White), (500,300))
            screen.blit(textfont.render("Damage", True, White), (500,400))
            screen.blit(textfont.render("Spell Damage", True, White), (500, 500))
            screen.blit(textfont.render("Health", True, White), (500,600))
         
            
            pygame.draw.rect(screen, Black,(375,500,100,100))
            screen.blit(textfont.render(charclass[i],True,White),(375,500))
            if i == len(charclass)-1:
                if next.collidepoint(mousex,mousey) and click == True:
                    pygame.draw.rect(screen, Black,(375,500,100,100))
                    screen.blit(textfont.render(charclass[0],True,White),(375,500))
                    i = 0
            if i < -len(charclass):
                if prev.collidepoint(mousex,mousey) and click == True:
                    pygame.draw.rect(screen, Black,(375,500,100,100))
                    screen.blit(textfont.render(charclass[i-1],True,Black),(375,500))
                    i = len(charclass) -1
                
            if next.collidepoint(mousex,mousey) and click == True:
               
                pygame.draw.rect(screen, Black,(375,500,100,100))
                screen.blit(textfont.render(charclass[i+1],True,Black),(375,500))
                i += 1
                #print(charclass[i])
                #click = False
            if prev.collidepoint(mousex,mousey) and click == True: #if click == true and false the moment the mouse button comes up 
                #print("reach 2")
                pygame.draw.rect(screen, Black,(375,500,100,100))
                screen.blit(textfont.render(charclass[i-1],True,Black),(375,500))
                i -= 1 
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
                
                    #click = False
                    
                #if event.type == pygame.MOUSEBUTTONUP:
                    #click = False
                   # continue
               
            pygame.display.update()   
    def MainMenu(self):
        click = False
        while running:
            
            screen.fill(White) #the colour
            button1 = pygame.draw.rect(screen, Black,(50,50,50,50))
            screen.blit(textfont.render("Play", True, White), (50,50))
            mousex, mousey = pygame.mouse.get_pos()
            if button1.collidepoint(mousex,mousey) and event.type == pygame.MOUSEBUTTONDOWN:
                print("click reach")
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
        #def Move(self):

#Room to room movement - when the player goes to the border limit, it puts them into a new room
    
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