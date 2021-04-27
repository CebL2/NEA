import pygame, sys
pygame.init()


#since i cant put multiple text lines at once, i'll instead use images and put texts on it instead


white = (255,255,255)
Black = (0,0,0)

print(pygame.font.match_font('impact'))

textfont = pygame.font.Font(r'C:\Users\user\Desktop\Computer Science\impact.ttf',32 )
 
click = False
test = textfont.render("test", True, white)
screen = pygame.display.set_mode((1280,1024 ))
running = True





def anothermenu():
    running = True
    while running:
        
        screen.fill(white)
        
        screen.blit(textfont.render("options",True, Black), (200,50))
        button3 = pygame.draw.rect(screen, Black,(100,100,50,50))
        screen.blit(test, (50,50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Did the user click the window close button?
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
        pygame.display.update()
        


def testMenu():
    running = True
   
    
    while running:
        screen.fill(white)
        button3 = pygame.draw.rect(screen, Black,(100,100,50,50))
        screen.blit(test, (50,50))
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
    button1 = pygame.draw.rect(screen, Black,(200,500,20,500))
    mousex, mousey = pygame.mouse.get_pos()
    if button1.collidepoint(mousex,mousey):
        if click == True:
            testMenu()
            click = False
    button2 = pygame.draw.rect(screen, Black,(200,50,500,500))
    if button2.collidepoint(mousex,mousey):
        if click == True:
            anothermenu()
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
