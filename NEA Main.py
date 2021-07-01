import pygame, sys, random, os
pygame.init()


#since i cant put multiple text lines at once with indentations, i'll instead use images and put texts on it


White = (255,255,255)
Black = (0,0,0)
screenx = 1280
screeny = 1024



print(pygame.font.match_font('impact'))
#print(pygame.font.get_fonts())

textfont = pygame.font.Font(r'C:\Windows\Fonts\georgia.ttf', 16 )
 
click = False
test = textfont.render("test", True, White)
screen = pygame.display.set_mode((screenx,screeny))
running = True

spawnamount_easy = random.randint(0,4)
spawnamount_medium = random.randint(5,8)
spawnamount_hard = random.randint(9,12)
sprites = pygame.sprite.Group()

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
#for testing purposes, amount spawned will be based on run time of game
#the way how rooms will be generated with have some sort of grid to it, where it will spawn in built in objects that will be implemented, structure is always random
#the current issue is that enemies do spawn when the player moves to the next room, but it only lasts for 1 frame and they are isntantly removed

class Attack:
    def __init__(self):
        self.Projectile 
        


class Enemy:
    def __init__(self,enemy,enemylist):
        self.enemy = enemy
        #self.screen = screen
        #self.posx = playerx
        #self.posy = playery

        
        self.enemylist = enemylist
        
        #lets make the enemy spawn a list 
        
    def SpawnEnemy(self,difficulty):
        if difficulty == 0:
            return None
        if difficulty == 1:
            for i in range(0,5):
                self.enemyposition = (random.randint(20,1000), random.randint(20,1000))
                self.enemylist.append(self.enemyposition)
                #self.enemylist.append(self.enemyposition()#[(100,200), (300,1000)]
            for position in self.enemylist:
                    #screen.fill(White)
                screen.blit(textfont.render(self.enemy, True, Black), (position[0],position[1]))

        #def Move(self):

    #if difficulty == 2:
    #    for i in range( pawnamount_medium):
    #        screen.blit(textfont.render(enemy, True, Black ), (random.randint(0,1280),random.randint(0,1080)))
    #else:
     #   for i in range(spawnamount_hard): 
      #      screen.blit(textfont.render(enemy, True, Black ), (random.randint(0,1280),random.randint(0,1080)))



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
        

#TODO
#Room to room movement - when the player goes to the border limit, it puts them into a new room 
class Player(pygame.sprite.Sprite):
    player_image = pygame.image.load("test sprite.jpg").convert()
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = Player.player_image
            self.rect = self.image.get_rect()
            self.rect.center = (1280/2, 1024/2)
            self.spawnx = 200
            self.spawny = 200
            self.border = 2
            
    # def update(self):
    #     keypressed = pygame.key.get_pressed()
    #     if keypressed[pygame.K_s] and self.rect.y < screeny:
    #         self.rect.y += self.border
    #     if keypressed[pygame.K_a] and self.rect.x > self.border:
    #         self.rect.x -= self.border
    #     if keypressed[pygame.K_d] and self.rect.x <  screenx :
    #         self.rect.x += self.border
    #     if keypressed[pygame.K_w] and self.rect.y > self.border:
    #         self.rect.y -= self.border
    def moveright(self):
        self.rect.x += self.border
    def moveleft(self):
        self.rect.x -= self.border
    def moveup(self):
        self.rect.y -= self.border
    def movedown(self):
        self.rect.y += self.border
        
#def enemystate(collide)
# if collide is true:
#      enemystate is True
#      while enemystate is True:
#           colliding into walls will not teleport the player to the other side of the wall until enemystate becomes false again
#           the only way to do that is when the enemy count (or contents in the enemy list) is o
#           if enemycount == 0
#               enemystate = False


def game():
    
    
    enemylist = []
    enemy = Enemy("#",enemylist)
  
    #nextroom = False
    #power_level = 0 #to indicated the player's power level 
    running = True
    enemystate = True
    spawnx = 200
    spawny = 200
    border_gap = 0
    player = Player()
    sprites.add(player)
    while running:
        
         #its getting constnatly updated therefore the spawns are getting hidden by the 
        
        
        screen.fill(White)
        
  
        #if i dont fill the screen, then the circle will just keep going, but if i keep filling the screen, enemies wont show, so I'll need to make some changes with the player
        #player = pygame.draw.circle(screen, Black, (spawnx,spawny) ,34)
        #keypressed = pygame.key.get_pressed()
        # if keypressed[pygame.K_s] and spawny < screeny:
        #     spawny += border
        # if keypressed[pygame.K_a] and spawnx > border:
        #     spawnx -= border
        # if keypressed[pygame.K_d] and spawnx <  screenx :
        #     spawnx += border
        # if keypressed[pygame.K_w] and spawny > border:
        #     spawny -= border
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_s] and player.rect.y < screeny - border_gap :
            #self.rect.y += self.border
            player.movedown()
        if keypressed[pygame.K_a] and player.rect.x > border_gap :
            player.moveleft()
        if keypressed[pygame.K_d] and player.rect.x <  screenx -border_gap:
            player.moveright()
        if keypressed[pygame.K_w] and player.rect.y > border_gap:
            player.moveup()
        ##################################
        #                                #
        #                                #
        #                                #
        ##################################  
        
        sprites.update()
        
        sprites.draw(screen)
        left_top_to_right = pygame.draw.rect(screen, Black, (0,0,1280,10))
        left_top_to_bot = pygame.draw.rect(screen, Black, (0,0, 10,1280))
        right_top_to_bot = pygame.draw.rect(screen, Black, (1270,0,10,1280))
        left_bot_to_right = pygame.draw.rect(screen, Black, (0,1014, 1280,10))
        #def function (enemystate)
        #if enemystate = true:
        #player rect x and rect y will constantly be forced in the room
        #speed becomes 0 when bumped into a wall or some sort
        if enemystate == False:    
        
            if left_bot_to_right.collidepoint(player.rect.x, player.rect.y): 
                
                player.rect.x = screenx/2 - 100
                player.rect.y = 50
                #spawn enemy algorithm here
                #print(player.rect.x)
                enemy.SpawnEnemy(1) 
                #be in a state where when the player goes through a room, it is not allowed to leave until the enemy count is 0.
                #if player goes into room
                #  exit room will not be allowed, false no matter what
                #  exit room statement will always be false while there are still enemies in the room
                #  once enemy count is down to 0 (maybe using a list, and if the list is empty), exit room statement can be converted into true
                #  repeat the process and roll a random number to determine if the room will contain enemies or not
            
            
            if left_top_to_right.collidepoint(spawnx, spawny): 
            
                spawnx = screenx/2
                spawny = screeny-50
                enemy.SpawnEnemy(1)
            #spawn enemy algorithm here
            
            if right_top_to_bot.collidepoint(spawnx, spawny):
            
                spawnx = 50
                spawny = screeny/2
                enemy.SpawnEnemy(1)
            #spawn enemy algorithm here
                
            if left_top_to_bot.collidepoint(spawnx, spawny):
            
                spawnx = screenx-50
                spawny = screeny/2
                enemy.SpawnEnemy(1)
            #spawn enemy algorithm here
        elif enemystate == True:
            border_gap = 200
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Did the user click the window close button?
                running = False
                sys.exit()
            
                    
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_DOWN:
            #         spawny += border                      #if ever the free movement doesnt seem to work, this is an example code that only allows one short movement with one click 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
        
        pygame.display.update()
        

while running:
    screen.fill(White) #the colour
    button1 = pygame.draw.rect(screen, Black,(50,50,50,50))
    
    screen.blit(textfont.render("Play", True, White), (50,50))
    mousex, mousey = pygame.mouse.get_pos()
    if button1.collidepoint(mousex,mousey):
        if click == True:
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
