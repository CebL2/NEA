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
                
                Directionlist = [(0,1),(0,-1),(1,0),(-1,0)]
                if self.isBorder(y,len(self.map)-1,x,len(self.map[0])-1):
                    if self.isCorner(y,len(self.map)-1,x,len(self.map[0])-1):
                        if y == 0 and x == 0: #remove left and up
                            Directionlist.pop(1) 
                            Directionlist.pop(2)
                        elif y == 0 and x == len(self.map[0])-1: #remove right and up
                            Directionlist.pop(0) 
                            Directionlist.pop(2)
                        elif y == len(self.map)-1 and x == len(self.map[0])-1: #remove down and right
                            Directionlist.pop(0) 
                            Directionlist.pop(1)
                        elif y == len(self.map)-1 and x == 0: #remove left and down
                            Directionlist.pop(1) 
                            Directionlist.pop(1)
                    else:
                        if y == 0: 
                            Directionlist.pop(3)
                        elif y == len(self.map)-1:
                            Directionlist.pop(2)  
                        elif x == 0:
                            Directionlist.pop(1)
                        else:
                            Directionlist.pop(0)       
                
                             
                rect = pygame.Rect(1582.5+xval,39+yval,self.xval-4,self.yval-4)
                pygame.draw.rect(self.screen,self.Black,rect) 
                
                
                # elif self.map[y][x] == 'B':
                if self.map[y][x] == 'R' or self.map[y][x] == 'E' or self.map[y][x] == 'B':
                    for i in Directionlist:
                        if self.map[y+i[0]][x+i[1]] == '#':
                            self.traversedlist[y][x] = 1
                            pygame.draw.rect(self.screen,self.gray,rect)
                if self.traversedlist[y][x] >0:
                    pygame.draw.rect(self.screen,self.gray,rect)
                if self.map[y][x] == '#':
                    pygame.draw.rect(self.screen,self.green,rect)
                            
                            

                
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