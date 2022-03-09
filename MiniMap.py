import pygame

#the screen has to be passed in through the main function and not a separate variable in this class
class MiniMap():
    def __init__(self,screen,maplist,traversed=None):   #the screen itself and the map list
        self.map = maplist  
        self.image = pygame.Surface((300,150))
        
        self.width = 1
        self.white = (200,200,200)
        self.Black = (0,0,0)
        self.xval = self.image.get_width()//len(self.map[0])
        self.yval = self.image.get_height()//len(self.map)
        self.green = (0,255,0)
        
        self.gray = (220,220,220)
        self.yellow =(255,255,0)
        self.red = (255,0,0)
        self.screen = screen
        self.image.fill(self.white)
        if traversed == None:
            self.traversedlist = self.traversed()
        else:
            self.traversedlist = traversed
        
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
    def isBorder(self,i, i_length, j, j_length): #checks if the list element is on the border
        if i == 0 or i == i_length or j== 0 or j == j_length:
            return True

    def isCorner(self,i, i_length, j, j_length):
        if i == 0 and j == 0 or i == 0 and j == j_length or i == i_length and j == 0 or i == i_length and j == j_length: #checks if the list element is on the corner
            return True 
    def traversed(self):
        traversedlist = []
        for i in range(0,len(self.map)):
            traversedlist.append([])
            for _ in range(0,len(self.map[0])):
                traversedlist[i].append(0)
        return traversedlist
       
    def drawgrid(self,posx,posy):
        distancei=0
        distancej=0
        new = {}
        indexing =0 
        mapi_length = len(self.map)
        mapj_length = len(self.map[0])
        Directionlist = [(0,1),(0,-1),(1,0),(-1,0)]
        #(1,0), (-1,0),  (0,1), (0,-1)
        for y, row in enumerate(self.map):  #element, value
            for x , col in enumerate(row):
                
                #for every direction
                xval = x*self.xval
                yval = y*self.yval
                if y == posx and x == posy:

                    self.traversedlist[y][x] = 1
                    
                
                #take a place in this 2d grid
                #make everything surrounding the room black and the room that the player is in green
                #make neighbouring available rooms to traverse to grey to indicate that it can be reached, but will not show the entire layout of the level
                
                

                # Directionlist = [(0,1),(0,-1),(1,0),(-1,0)]
                # if self.isBorder(currenti,len(NewLayout)-1,currentj,len(NewLayout[0])-1):
                #     if self.isCorner(currenti,len(NewLayout)-1,currentj,len(NewLayout[0])-1):
                #         if currenti == 0 and currentj == 0: #remove left and up
                #             Directionlist.pop(1) 
                #             Directionlist.pop(2)
                #         elif currenti == 0 and currentj == len(NewLayout[0])-1: #remove right and up
                #             Directionlist.pop(0) 
                #             Directionlist.pop(2)
                #         elif currenti == len(NewLayout)-1 and currentj == len(NewLayout[0])-1: #remove down and right
                #             Directionlist.pop(0) 
                #             Directionlist.pop(1)
                #         elif currenti == len(NewLayout)-1 and currentj == 0: #remove left and down
                #             Directionlist.pop(1) 
                #             Directionlist.pop(1)
                #     else:
                #         if currenti == 0: 
                #             Directionlist.pop(3)
                #         elif currenti == len(NewLayout)-1:
                #             Directionlist.pop(2)  
                #         elif currentj == 0:
                #             Directionlist.pop(1)
                #         else:
                #             Directionlist.pop(0)   
                #rect = pygame.Rect(1582.5+xval,39+yval,self.xval-4,self.yval-4)
                # pygame.draw.rect(self.screen,self.Black,rect) #          
                rect = pygame.Rect(1582.5+xval,39+yval,self.xval-4,self.yval-4)
                pygame.draw.rect(self.screen,self.Black,rect) 
               
                # distancei = posy - y
                # distancej = posx - x
                
                #     if self.map[y][x+1] !=' ':
                #        # print('reach')
                #         rect = pygame.Rect(1582.5+((x+1)*self.xval),39+yval,self.xval-4,self.yval-4)
                #         pygame.draw.rect(self.screen,self.gray,rect)
                # if self.map[y][x] == ' ' :
                #     pygame.draw.rect(self.screen,self.Black,rect)
                
                
                if self.map[y][x] == '#':
                    pygame.draw.rect(self.screen,self.green,rect)
                # elif self.map[y][x] == 'B':
                elif self.map[y][x] == 'R' or self.map[y][x] == 'E' or self.map[y][x] == 'B':
                    for i in Directionlist:
                        if self.map[y+i[0]][x+i[1]] == '#':
                            pygame.draw.rect(self.screen,self.gray,rect)
                    
                # #     pygame.draw.rect(self.screen,self.red,rect)
                # if self.map[y][x] == '#':
                #     pygame.draw.rect(self.screen,self.green,rect)
                #     for i in Directionlist:
                #         if self.map[y+i[0]][x+i[1]] == 'R' or self.map[y+i[0]][x+i[1]] == 'E' or self.map[y+i[0]][x+i[1]] == 'B' and self.traversedlist[y+i[0]][x+i[1]] <0:
                #             rect = pygame.Rect(1582.5+((x+i[1])*self.xval),39+((y+i[0])*self.yval),self.xval-4,self.yval-4)
                #             pygame.draw.rect(self.screen,self.gray,rect)
                        
                            
                # else:
                    if self.traversedlist[y][x] >0:
                        
                        pygame.draw.rect(self.screen,self.gray,rect)
                # # else:
                #     pygame.draw.rect(self.screen,self.Black,rect)
                
              
                    
                
                    
                
                    #if the distance between the list indexes is one
                    #show room on map
                    #other wise,treat as if no room (black)
        #print(new)            
    # def drawgrid(self,posx,posy):
        
    #     for y, row in enumerate(self.map):
    #         for x , col in enumerate(row):
                
    #             xval = x*self.xval
    #             yval = y*self.yval
    #             if y == posx and x == posy:
    #                 self.traversedlist[y][x] = 1
    #             #print(xval,yval)
                
    #             rect = pygame.Rect(1582.5+xval,39+yval,self.xval-4,self.yval-4)
    #             if self.map[y][x] == ' ':
    #                 pygame.draw.rect(self.screen,self.Black,rect)
    #             elif self.map[y][x] == '#':
                    
    #                     pygame.draw.rect(self.screen,self.green,rect)
    #             elif self.map[y][x] == 'B':
                    
    #                     pygame.draw.rect(self.screen,self.red,rect)
                    
    #             else:
    #                 if self.traversedlist[y][x] >0:
    #                     pygame.draw.rect(self.screen,self.yellow,rect)
                    
    #                 else:
    #                     pygame.draw.rect(self.screen,self.gray,rect)
        
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
        
        
    
    
        

