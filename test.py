import pygame, sys
pygame.init()


#since i cant put multiple text lines at once, i'll instead use images and put texts on it instead


white = (255,255,255)
Black = (0,0,0)

print(pygame.font.match_font('impact'))
    
 
MenuKey = pygame.key.get_pressed()
click = False

screen = pygame.display.set_mode((1280,1024 ))
running = True  
def testMenu():
    running = True
    while running:
        screen.fill(white)
        button2 = pygame.draw.rect(screen, Black,(100,100,50,50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Did the user click the window close button?
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
        pygame.display.update()
        


while running:
    screen.fill(white) #the colour
    #screen.blit(top_text, (250, 250))
    button1 = pygame.draw.rect(screen, Black,(200,500,20,500))
    mousex, mousey = pygame.mouse.get_pos()
    if button1.collidepoint(mousex,mousey):
        if click == True:
            testMenu()
            click = False
            
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Did the user click the window close button?
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
    pygame.display.update()





def test():
    thing = 1
    if thing == 0:
        print("No")
    else:
        print("Yes")
    
#print(test())
        

