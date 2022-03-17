import pygame

class MiniMap():
    def __init__(self,screen,maplist,traversed=None):   
        self.map = maplist  #a passed in map or array 
        self.image = pygame.Surface((300,150)) #the background of the minimap
        self.background = (200,200,200)
        self.Black = (0,0,0)
        self.xval = self.image.get_width()//len(self.map[0]) #takes the width and height of the image and divided by the width and height of the map respectively
        self.yval = self.image.get_height()//len(self.map) #this would give us the size of each room in the minimap
        self.green = (0,255,0)
        
        self.gray = (220,220,220)
        self.yellow =(255,255,0)
        self.red = (255,0,0)
        self.screen = screen
        self.image.fill(self.background)
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
        traversedlist = []  #makes an empty array if there isn't a array passed in from the class to begin with
        for i in range(0,len(self.map)):
            traversedlist.append([])
            for _ in range(0,len(self.map[0])):
                traversedlist[i].append(0)
        return traversedlist
       
    def drawgrid(self,posx,posy):
        for y, row in enumerate(self.map):  #element, value
            for x , col in enumerate(row):
                

                xval = x*self.xval
                yval = y*self.yval
                if y == posx and x == posy:
                    self.traversedlist[y][x] = 1 
                    
                
               
                Directionlist = [(0,1),(0,-1),(1,0),(-1,0)] #similar operations with how the layout of the map was generated, but instead it is used to determine which room has been traversed
                if self.isBorder(y,len(self.map)-1,x,len(self.map[0])-1):
                    if self.isCorner(y,len(self.map)-1,x,len(self.map[0])-1):
                        if y == 0 and x == 0: 
                            Directionlist.pop(1) 
                            Directionlist.pop(2)
                        elif y == 0 and x == len(self.map[0])-1:
                            Directionlist.pop(0) 
                            Directionlist.pop(2)
                        elif y == len(self.map)-1 and x == len(self.map[0])-1:
                            Directionlist.pop(0) 
                            Directionlist.pop(1)
                        elif y == len(self.map)-1 and x == 0: 
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
            
                             
                rect = pygame.Rect(1582.5+xval,39+yval,self.xval-4,self.yval-4) #preset rect to be drawn
                pygame.draw.rect(self.screen,self.Black,rect)  #by default, all rooms are black

                if self.map[y][x] == 'R' or self.map[y][x] == 'E' or self.map[y][x] == 'B': #if the current position of the map is NOT where the player is currently
                    for direction in Directionlist:
                        if self.map[y+direction[0]][x+direction[1]] == '#': #and the neighbouring room is where the player is 
                            self.traversedlist[y][x] = 1 #then make that position in the traversedlist equal to 1
                if self.traversedlist[y][x] >0: #if the current position of the traversedlist is greater than 0, then the rectangle drawn in that specific location will be gray instead of black
                    pygame.draw.rect(self.screen,self.gray,rect)
                if self.map[y][x] == '#':
                    pygame.draw.rect(self.screen,self.green,rect) #otherwise, if the position is where the player is, then colour the rectangle green
           
    def update(self,x,y):
        self.drawgrid(x,y)
        self.screen.blit(self.image,(1580,39)) #projects the background of the minimap
       
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_m]:
        
            self.image.set_alpha(100) #minimap by default would be slightly less visible if a key is not pressed, in this case, while the key 'M' is pressed down, the minimap will be 
        else:                         #a bit more visible by making the background of the minimap more transparent
            
            self.image.set_alpha(200)