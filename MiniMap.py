import pygame

#the screen has to be passed in through the main function and not a separate variable in this class
class MiniMap():
    def __init__(self,screen,maplist):   #the screen itself and the map list
        self.map = maplist  
        self.image = pygame.Surface((300,150))
        
        self.width = 1
        self.white = (200,200,200)
        self.Black = (0,0,0)
        self.xval = self.image.get_width()//len(self.map[0])
        self.yval = self.image.get_height()//len(self.map)
        self.green = (0,255,0)
        
        self.gray = (220,220,220)
        self.blue = (0,0,255)
       
        self.screen = screen
        self.image.fill(self.white)
        self.traversedlist = self.traversed()
        
        #self.rect = pygame.Rect(1400,50,300,300)
        
        #self.inner.fill((255,255,255))
        
        #self.rect1 = self.image.get_rect()
        #self.rect1.center = (1420,0)
        
       # self.rect2 = self.inner.get_rect()
        #print(self.rect1.center, self.rect2.center)
       # img = pygame.Rect(1420,0,700,300)
        #create a grid within the 
        # for x, row in enumerate(self.map):
        #     for y, col in enumerate(row):
        #         #rect
    def traversed(self):
        traversedlist = []
        for i in range(0,len(self.map)):
            traversedlist.append([])
            for _ in range(0,len(self.map[0])):
                traversedlist[i].append(0)
        return traversedlist
       
    def drawgrid(self,posx,posy):
        
        for y, row in enumerate(self.map):
            for x , col in enumerate(row):
                
                xval = x*self.xval
                yval = y*self.yval
                if y == posx and x == posy:
                    self.traversedlist[y][x] = 1
                #print(xval,yval)
                
                rect = pygame.Rect(1582.5+xval,39+yval,self.xval-4,self.yval-4)
                if self.map[y][x] == ' ':
                    pygame.draw.rect(self.screen,self.Black,rect)
                elif self.map[y][x] == '#':
                    
                        pygame.draw.rect(self.screen,self.green,rect)
                    
                else:
                    if self.traversedlist[y][x] >0:
                        pygame.draw.rect(self.screen,self.blue,rect)
                    
                    else:
                        pygame.draw.rect(self.screen,self.gray,rect)
        
    def update(self,x,y):
        
        self.drawgrid(x,y)
        self.screen.blit(self.image,(1580,39))
       
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_m]:
            #self.inner.set_alpha(200)
            
            self.image.set_alpha(100)
        else:
            #self.inner.set_alpha(255)
            self.image.set_alpha(200)
 
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
        
        
    
    
        

