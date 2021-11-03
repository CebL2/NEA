import pygame, sys, random, os
#from Player import Player
from Enemy import Enemy
from Attack import Attack
#import pickle


#json to save files
pygame.init()
#write is save
#read is load 
#in order to save, we need to dump or write binary data with binary write 
#with open("filename.txt",'wb') as file 
#file.dump(data) with the pickle module?


projectilegroup = pygame.sprite.Group()



White = (255,255,255) #preset values for colour and resolution
Black = (0,0,0)
screenx = 1280
screeny = 1024

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
enemies = pygame.sprite.Group()
playersp = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

        
class Player(pygame.sprite.Sprite):
    player_image = pygame.image.load("spritegroup//test sprite.jpg").convert()
    def __init__(self,screenx,screeny,border_gap):
        pygame.sprite.Sprite.__init__(self)
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

    def shoot(self):
        projectile = Attack(self.rect.x,self.rect.y)
        projectilegroup.add(projectile)
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
    running = True
    while running:
        click = False
        screen.fill(Black)
        exitbutton = pygame.draw.rect(screen, Black,(50,50,50,50))
        mousex, mousey = pygame.mouse.get_pos()
        if exitbutton.collidepoint(mousex,mousey):
            if click == True:
                running = False
                return False
            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Did the user click the window close button?
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
      
    
    
 
def save():
    pass
                
        #def Move(self):

#Room to room movement - when the player goes to the border limit, it puts them into a new room 


def RoomLayout():
    Rooms = []
    for i in range(3):
        Rooms.append([])
        for j in range(3):
            passorno = random.randint(1,2)
            print(passorno)
            if passorno == 1:
                Rooms[i].append("P")
            else:
                Rooms[i].append("N")
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
    
    

def collision(player,enemies): #player is player, enemies is the spritegroup
    hit = pygame.sprite.spritecollideany(player,enemies, True )
    hitx = pygame.sprite.spritecollideany()
    if hit:
        return True  #checks collision between the sprite group enemies and the sprite player, which is in another sprite group

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
    for i in range(0,3):
        #enemy = Enemy() #put coords as a input see if it works 
        e = Enemy()
        enemies.add(e)
        allsprites.add(e)
    
    
    while running:
        
        screen.fill(White)
        keypressed = pygame.key.get_pressed()
      
        if keypressed[pygame.K_DOWN]:
            player.shoot()
            
            
        
        ##################################
        #                                #
        #                                #
        #                                #
        ##################################
        
        projectilegroup.draw(screen)
        projectilegroup.update()
        
        playersp.update()
        playersp.draw(screen)
        #enemies.draw(screen)
        
        #for enemy in enemies(sprite group)
        #if collision(playerbullet, enemy, True, False)
        #remove enemy (.kill())

        
        
       
        left_top_to_right = pygame.draw.rect(screen, Black, (0,0,1280,10))
        left_top_to_bot = pygame.draw.rect(screen, Black, (0,0, 10,1280))
        right_top_to_bot = pygame.draw.rect(screen, Black, (1270,0,10,1280))
        left_bot_to_right = pygame.draw.rect(screen, Black, (0,1014, 1280,10))
        #def function (enemystate)
        #if enemystate = true:
        #player rect x and rect y will constantly be forced in the room
        #speed becomes 0 when bumped into a wall or some sort
           
        
        if left_bot_to_right.collidepoint(player.rect.x, player.rect.y): 
                
            player.rect.x = screenx/2 - 100
            player.rect.y = 50
                #spawn enemy algorithm here
                #print(player.rect.x)
            
            #for i in range(2):
                #enemies.add(enemy)
            
                
                #if collision(player,enemies) == True:
                    
                #be in a state where when the player goes through a room, it is not allowed to leave until the enemy count is 0.
                #if player goes into r oom
                #  exit room will not be allowed, false no matter what
                #  exit room statement will always be false while there are still enemies in the room
                #  once enemy count is down to 0 (maybe using a list, and if the list is empty), exit room statement can be converted into true
                #  repeat the process and roll a random number to determine if the room will contain enemies or not
            
        if left_top_to_right.collidepoint(player.rect.x, player.rect.y): 
        
            player.rect.x = screenx/2
            player.rect.y = screeny-50
           
        #spawn enemy algorithm here
        
        if right_top_to_bot.collidepoint(player.rect.x, player.rect.y):
        
            player.rect.x = 50
            player.rect.y = screeny/2
        
        #spawn enemy algorithm here
            
        if left_top_to_bot.collidepoint(player.rect.x, player.rect.y):
        
            player.rect.x = screenx-50
            player.rect.y = screeny/2
           
        #spawn enemy algorithm here
        #elif enemystate == True:
        #    border_gap = 200
        enemies.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Did the user click the window close button?
                running = False
                sys.exit()       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exitmenu()
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
        
        pygame.display.flip()
        
        

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