#TO DO
#Implement Projectiles
#Room traversal with restrictiosn
#Enemy spawn
#Room modifications (obstacles)
#Character creation with built in speical abilities for different classes

import pygame, sys, random, os
#from Player import Player
from Enemy import Enemy
from Attack import Attack
from AttackDown import AttackDown
from TESTINGFILE import Room
#import pickle

#json to save files
pygame.init()
#write is save
#read is load 
#in order to save, we need to dump or write binary data with binary write 
#with open("filename.txt",'wb') as file 
#file.dump(data) with the pickle module?
# with open ('test.txt', 'w') as file:
#     file.write("this is a test")
#     file.close()
    
clock = pygame.time.Clock()
White = (255,255,255) #preset values for colour and resolution
Black = (0,0,0)
screenx = 1280
screeny = 1024

clock.tick()
display = pygame.display.set_mode((300,200))
#print(pygame.font.get_fonts())

textfont = pygame.font.Font(r'C:\Windows\Fonts\georgia.ttf', 16 ) 
 
click = False
test = textfont.render("test", True, White)
screen = pygame.display.set_mode((screenx,screeny))
running = True

spawnamount_easy = random.randint(0,4)
spawnamount_medium = random.randint(5,8)
spawnamount_hard = random.randint(9,12)
projectilegroup = pygame.sprite.Group()
enemies = pygame.sprite.Group()
playersp = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

#delay = pygame.time()

#when d

class Player(pygame.sprite.Sprite):
    player_image = pygame.Surface((100,200))
    def __init__(self,screenx,screeny,border_gap):
        super().__init__()
        self.image = Player.player_image
        self.rect = self.image.get_rect()
        self.rect.center = (1280/2, 1024/2)
        self.border = 2
        self.x = screenx
        self.y = screeny
        self.gap = border_gap
    
    def update(self):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_s] and self.rect.y < self.y - self.gap :
            self.rect.y += self.border
        if keypressed[pygame.K_a] and self.rect.x > self.gap :
            self.rect.x -= self.border
        if keypressed[pygame.K_d] and self.rect.x <  self.x -self.gap:
            self.rect.x += self.border
        if keypressed[pygame.K_w] and self.rect.y > self.gap:
            self.rect.y -= self.border

    def shootdown(self):
        projectileup = Attack(self.rect.x,self.rect.y)
        projectilegroup.add(projectileup)
        allsprites.add(projectileup)
    def shootup(self):
        projectiledown = AttackDown(self.rect.x,self.rect.y)
        projectilegroup.add(projectiledown)
        allsprites.add(projectiledown)
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
    def __init__(self, Menu1,Menu2):
        self.Player = Menu1
        self.Options = Menu2    

class Spells:
    def __init__(self,Fire, Water, Earth):
        self.Fire = Fire
        self.Water = Water
        self.Earth = Earth

# def EnterRoom(RoomEnter):
#     runtime = pygame.time.get_ticks()
#     #if RoomEnter == True:
      #  Spawn(1)
    #return None
   # enemy = "*"
    #runtime = pygame.time.get_ticks()
    #if runtime > 600000:
        
    #testspawn = "4"

# def EnemySpawn():
#     enemy = "*"
#     if runtime > 0:
#         screen.blit(textfont.render(enemy,True,Black))

#when the user goes to another room (edge of border), EnterRoom gets called as its True
#EnterRoom then checks if the parameter is true, if it is, then spawn in that current screen
#for testing purposes, amount spawnesd will be based on run time of game
#the way how rooms will be generated with have some sort of grid to it, where it will spawn in built in objects that will be implemented, structure is always random
#the current issue i
def option():
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
                click = True
        pygame.display.update()
        
def exitmenu():
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
    
def save():
    pass                
        #def Move(self):

#Room to room movement - when the player goes to the border limit, it puts them into a new room
def RoomLayout(Rooms):
    for i in range(3):
        Rooms.append([])
        for _ in range(3):
            passorno = random.randint(1,2)
            if passorno == 1:
                Rooms[i].append("P")
            else:
                Rooms[i].append("N")
    return Rooms
def checkifN(room,i,j):  
#what if i = 1 and j =2?
    roomstate = room[i][j]
    new_i = random.randint(0,len(room)-1)
    new_j = random.randint(0,len(room[0])-1)
    if roomstate == 'N':
        return checkifN(room,new_i,new_j)
    else:
        return roomstate,i,j 
def game():
    #if charclass = warrior
    #give special skill1
    #if charclass = mage
    #give special skill2d
    luck = 0 
    badluck = 0 
    #nextroom = False
    #power_level = 0 #to indicated the player's power level 
    running = True
    enemystate = False
    border_gap = 0
    player = Player(screenx,screeny,border_gap)
    playersp.add(player)
    allsprites.add(player)
    #Rooms = []
    for i in range(0,3):
        #enemy = Enemy() #put coords as a input see if it works 
        e = Enemy()
        enemies.add(e)
        allsprites.add(e)

    #Rooms = RoomLayout(Rooms)
   

    #i = random.randint(0,len(Rooms)-1)
   # j = random.randint(0,len(Rooms[0])-1) 
    #    
    #roomstates = checkifN(Rooms,i,j)
    #i_value = roomstates[1]
    #j_value = roomstates[2]
    i = 0
    j = 1
    #playerpos = (i_value,j_value)
    playerpos = (i,j)
    Rooms = [['N','P','N'],
             ['N','P','P'],
             ['P','P','N']]
    
    #playerpos = (i_value,j_value)
    #for i in Rooms:
     #   print(i)
    print(playerpos[0])
    print(playerpos[1])
    #print(Rooms[playerpos[0]-1][playerpos[1]])
    print(len(Rooms)-1)
    
    
    while running:
        screen.fill(White)
        ##################################
        #                                #
        #                                #
        #                                #
        ##################################
        
        #Rooms 
        for projectile in projectilegroup:
            pygame.sprite.spritecollide(projectile, enemies, True, None)
                #enemy.kill()
                   #    
        
        Top = pygame.draw.rect(screen, Black, (0,0,1280,10))
        Left = pygame.draw.rect(screen, Black, (0,0, 10,1280))
        Right = pygame.draw.rect(screen, Black, (1270,0,10,1280))
        Down = pygame.draw.rect(screen, Black, (0,1014, 1280,10))
        #def function (enemystate)
        #if enemystate = true:
        #player rect x and rect y will constantly be forced in the room
        #speed becomes 0 when bumped into a wall 
        if Down.collidepoint(player.rect.x, player.rect.y) and playerpos[0] != len(Rooms)-1:   #problem is the second statement
            if Rooms[playerpos[0]+1][playerpos[1]] == 'P' :
                player.rect.x = screenx/2 - 100
                player.rect.y = 50
                playerpos = (playerpos[0]+1,playerpos[1])
                print(playerpos)
                #spawn enemy algorithm here
                #print(player.rect.x)
        if Top.collidepoint(player.rect.x, player.rect.y)  and playerpos[0] != 0: 
            if Rooms[playerpos[0]-1][playerpos[1]] == 'P':
                player.rect.x = screenx/2
                player.rect.y = screeny-50
                playerpos = (playerpos[0]-1,playerpos[1])
                print(playerpos)
        if Right.collidepoint(player.rect.x, player.rect.y)and Rooms[playerpos[0]][playerpos[1]+1] == 'P' and playerpos[1] != len(Rooms[0]) -1: 
            player.rect.x = 50
            player.rect.y = screeny/2
            playerpos = (playerpos[0],playerpos[1]+1)
            print(playerpos)
        if Left.collidepoint(player.rect.x, player.rect.y)and Rooms[playerpos[0]][playerpos[1]-1] == 'P' and playerpos[1] != 0: 
            player.rect.x = screenx-50
            player.rect.y = screeny/2   
            playerpos = (playerpos[0],playerpos[1]-1) 
            print(playerpos)
        enemies.draw(screen)
        enemies.update()
        projectilegroup.draw(screen)
        projectilegroup.update()
        playersp.update()
        playersp.draw(screen)
       
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
                    exitmenu()               
                if event.key == pygame.K_DOWN:
                    player.shootdown()
                if event.key == pygame.K_UP:
                    player.shootup()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                
        pygame.display.update()        
  
keypressed = pygame.key.get_pressed()     

while running:
    screen.fill(White) #the colour
    button1 = pygame.draw.rect(screen, Black,(50,50,50,50))
    screen.blit(textfont.render("Play", True, White), (50,50))
    mousex, mousey = pygame.mouse.get_pos()
    if button1.collidepoint(mousex,mousey):
        if click == True:
            #characterCreation()
            game()
            click = False             
    button2 = pygame.draw.rect(screen, Black,(100,100,100,50))
    screen.blit(textfont.render("Options", True, White), (100,100))
    if button2.collidepoint(mousex,mousey):
        if click == True:
            option()
            click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Did the user click the window close button?
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
    pygame.display.update()