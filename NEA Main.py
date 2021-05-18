import pygame, sys, random
pygame.init()


#since i cant put multiple text lines at once with indentations, i'll instead use images and put texts on it


White = (255,255,255)
Black = (0,0,0)
screenx = 1280
screeny = 1024

randomspawnx = random.randint(20, 1280)
randomspawny = random.randint(20,1024)


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


#procedural generation

#when the player goes to a new room so some kind of condition that acknowledges that the player has moved into a new room or region
#spawn enemies and enemy types accordingly 


#room generation
#based on the player's power level or such
#put obstacles/secrets accordingly


#a lot of random generated types will be used here




class Enemy:
    def __init__(self,enemy,playerx,playery):
        self.enemy = enemy
        self.posx = playerx
        self.posy = playery
        enemyx, enemyy = (random.randint(20,1000), random.randint(20,1000))
        enemylist = []
        #lets make the enemy spawn a list 
        def Spawn(self,difficulty):
            if difficulty == 0:
               return None
            if difficulty == 1:
                
                    
                
        #def Move(self):
            
            
        
    
     #will have to implement this in the main one i think, it needs its own separate screen

    #if difficulty == 2:
    #    for i in range( pawnamount_medium):
    #        screen.blit(textfont.render(enemy, True, Black ), (random.randint(0,1280),random.randint(0,1080)))
    #else:
     #   for i in range(spawnamount_hard): 
      #      screen.blit(textfont.render(enemy, True, Black ), (random.randint(0,1280),random.randint(0,1080)))
    


#when the user goes to another room (edge of border), EnterRoom gets called as its True
#EnterRoom then checks if the parameter is true, if it is, then spawn in that current screen
#for testing purposes, amount spawned will be based on run time of game
#the way how rooms will be generated with have some sort of grid to it, where it will spawn in built in objects that will be implemented, structure is always ranodm
#the current issue is that enemies do spawn when the player moves to the next room, but it only lasts for 1 frame and they are isntantly removed


def EnterRoom(RoomEnter):
    runtime = pygame.time.get_ticks()
    #if RoomEnter == True:
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
def game():
    
    
    #enemy = Enemy("#")
    nextroom = False
    power_level = 0 #to indicated the player's power level 
    running = True
    spawnx = 200
    spawny = 200
    border = 2
    while running:
        screen.fill(White) #its getting constnatly updated therefore the spawns are getting hidden by the 
        
        left_top_to_right = pygame.draw.rect(screen, Black, (0,0,1280,10))
        left_top_to_bot = pygame.draw.rect(screen, Black, (0,0, 10,1280))
        right_top_to_bot = pygame.draw.rect(screen, Black, (1270,0,10,1280))
        left_bot_to_right = pygame.draw.rect(screen, Black, (0,1014, 1280,10))
        
        player = pygame.draw.circle(screen, Black, (spawnx,spawny) ,34)
        
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_DOWN] and spawny < screeny:
            spawny += border
        if keypressed[pygame.K_LEFT] and spawnx > border:
            spawnx -= border
        if keypressed[pygame.K_RIGHT] and spawnx <  screenx :
            spawnx += border
        if keypressed[pygame.K_UP] and spawny > border:
            spawny -= border
        
        
        
        #Spawn(1)
        
        
        ##################################
        #                                #
        #                                #
        #                                #
        ##################################  
        
        if left_bot_to_right.collidepoint(spawnx, spawny): 
            nextroom = True
            spawnx = screenx/2
            spawny = 50
            #EnterRoom(nextroom)
            
            
        if left_top_to_right.collidepoint(spawnx, spawny): 
            nextroom = True
            spawnx = screenx/2
            spawny = screeny-50
            
            #EnterRoom(nextroom)
        
        if right_top_to_bot.collidepoint(spawnx, spawny):
            nextroom = True
            spawnx = 50
            spawny = screeny/2
            
            #EnterRoom(nextroom)
            
        if left_top_to_bot.collidepoint(spawnx, spawny):
            nextroom = True
            spawnx = screenx-50
            spawny = screeny/2
         
            #EnterRoom(nextroom)
            
            
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
