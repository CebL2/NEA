import pygame

class MiniMap():
    def __init__(self,Grid): 
        self.image = Grid
        self.rect = self.image.get_rect()
        
        pygame.draw.rect(self.image,(255,255,255),(1420,-300,400,400))
        print(self.rect.center)
        
    
    def update(self):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_m]:
            self.image.set_alpha(200)
        else:
            self.image.set_alpha(100)
            
    def MapGrid(self):
        pass
#         M = pygame.surface(500,300)
#         rows = len(self.Map)-1
#         cols = len(self.Map[0])-1
#         TopLeft = pygame.Rect((0,0,500,500))    #walls/borders, there are variants of wall as the 'exit' to different rooms will be a separate wall
#         # TopRight = pygame.draw.rect(screen,Black,(1220,0,700,40))
#         # DownLeft = pygame.draw.rect(screen, Black, (0,1040, 700,40))
#         # DownRight = pygame.draw.rect(screen, Black, (1220,1040, 700,40))
#         # LeftUp = pygame.draw.rect(screen, Black, (0,0, 40,350))
#         # LeftDown = pygame.draw.rect(screen, Black, (0,730, 40,350))
#         # RightUp = pygame.draw.rect(screen, Black, (1880,0,40,350))
#         # RightDown = pygame.draw.rect(screen, Black, (1880,730,40,350))
        
#         #must be in scale with the 
        
        
        
#         ''' ['E', 'E', 'R', 'E', 'R', 'E', ' ']
#             ['B', 'R', 'E', ' ', ' ', 'E', 'E']
#             [' ', 'R', 'E', ' ', 'R', ' ', 'E']
#             [' ', ' ', 'E', 'E', 'E', 'E', 'R']
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ']
# '''
        
        
    
    
        

