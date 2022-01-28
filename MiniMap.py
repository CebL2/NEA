import pygame

screenx = 1920
screeny = 1080

screen = pygame.display.set_mode((screenx,screeny),pygame.FULLSCREEN)
class MiniMap():
    def __init__(self,Grid): 
        self.image = Grid
        self.inner = pygame.Surface((600,200))
        #self.inner.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (1420,0)
       # img = pygame.Rect(1420,0,700,300)
        #create a grid within the 
        
    
    def update(self):
        screen.blit(self.inner,(1400,50))
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_m]:
            self.inner.set_alpha(200)
            self.image.set_alpha(200)
        else:
            self.inner.set_alpha(255)
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
        
        
    
    
        

