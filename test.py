import pygame
pygame.init()


#since i cant put multiple text lines at once, i'll instead use images and put texts on it instead


white = (255,255,255)
Black = (0,0,0)

print(pygame.font.match_font('impact'))

    
    
#textfont = pygame.font.Font(r'C:\Users\user\Desktop\Computer Science\impact.ttf',32)
#top_input_text = textfont


#top_text = textfont.render(top_input_text, True, Black) 
    
    
    
screen = pygame.display.set_mode((1000,1000 ))
running = True
while running:
    screen.fill(white) #the colour
    #screen.blit(top_text, (250, 250))
    pygame.draw.rect(screen, Black,(200,500,20,500))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Did the user click the window close button?
            running = False
    pygame.display.update()
#Menu

    
    
def test():
    thing = 1
    if thing == 0:
        print("No")
    else:
        print("Yes")
    
#print(test())
        

