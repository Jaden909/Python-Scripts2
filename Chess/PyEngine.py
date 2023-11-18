"""Game Engine for Python. Requires Pygame."""
import pygame,json
_mouseDown=False
def animation(moveList:list,fps:int,frames:int,screen,x,y):
    """Pygame animation."""
    for i in range(frames):    
        if i>len(moveList):
            i=0
        clock=pygame.time.Clock()
        clock.tick(fps)
        currentSprite=moveList[i]
        screen.blit(currentSprite,(x,y))
        pygame.display.update()
def wasdInput(WFunction,AFunction,SFunction,DFunction):
    """Simple WASD/arrow keys input listener. Also supports arrow keys. Args are functions to run when respective key is pressed(Tip: don't use () at the end of the functions. If you do, it will run them and try to use the return value as the arg instead of the function itself)"""
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]or keys[pygame.K_a]:
        AFunction()
    if keys[pygame.K_RIGHT]or keys[pygame.K_d]:
        DFunction()
    if keys[pygame.K_DOWN]or keys[pygame.K_s]:
        SFunction()
    if keys[pygame.K_UP]or keys[pygame.K_w]:
        WFunction()
class GameButton:
    """Create a button that can trigger a function if clicked on
    Required Args: x, y, imageRes(if image is used), use imageResX and imageResY for non-square buttons
    Optional Args: image,function,hoverSprite,notHoverSprite (if using custom cursor)
    """
    def __init__(self,**kwargs):
        #REQUIRED ARGS
        if 'x' in kwargs and 'y' in kwargs:  
            self.x=kwargs.get('x')
            self.y=kwargs.get('y')
        #Error raised if required args are not found
        else:
            raise ValueError('GameButton requires arguments x and y')
        #Optional arg check: if image not found default is used
        if 'image' in kwargs:    
            if kwargs.get('image')is None:
                self.image=None
            else:
                self.image=pygame.image.load(kwargs.get('image')).convert()
            if'imageRes' in kwargs:
                self.imageRes=kwargs.get('imageRes')
                self.square=True
            elif 'imageResX'in kwargs and 'imageResY' in kwargs:
                self.imageResX=kwargs.get('imageResX')
                self.imageResY=kwargs.get('imageResY')
                self.square=False
            else:
                raise ValueError('image requires either imageRes for square buttons or imageResX and imageResY for non-square buttons')
        else:
            self.image=pygame.image.load('Game Engine Stuff\\Defaults\\DEFAULTBUTTON.png').convert()
            self.imageRes=64
            self.square=True
        #Optional arg: default assinged if not found
        if'function' in kwargs:
            self.function=kwargs.get('function')
        else:
            self.function=lambda:print('This button doesn\'t have a function assigned to it. It currently does nothing.')
        #Optional arg: Default value is false
        if 'hover' in kwargs:
            self.hover=kwargs.get('hover')
        else:
            self.hover=False
        if 'hoverSprite' in kwargs:
            self.hoverSprite=kwargs.get('hoverSprite')
            self.hoverCursor=pygame.cursors.Cursor((2,24),self.hoverSprite)
        else:
            self.hoverCursor=pygame.SYSTEM_CURSOR_HAND
        if 'notHoverSprite' in kwargs:
            self.notHoverSprite=kwargs.get('notHoverSprite') 
            self.notHoverCursor=pygame.cursors.Cursor((2,24),self.notHoverSprite)   
        else:
            self.notHoverCursor=pygame.SYSTEM_CURSOR_ARROW     
    #Blits button to screen provided
    def show(self,**kwargs):
        'Blit button to screen. Screen to blit to required. Requires defined image'
        screen=kwargs.get('screen')
        screen.blit(self.image,(self.x,self.y-self.imageRes))
    #Listens for mouse clicks: should be in a loop to work properly
    def listen(self):    
        "Listens for clicks on the button. Should be in a loop."
        global _mouseDown
        left,middle,right=pygame.mouse.get_pressed()
        #Hover
        if self.hover:    
            if self.square:
                mouseX,mouseY=pygame.mouse.get_pos()
                if mouseX>self.x and mouseX<self.x+self.imageRes and mouseY>self.y and mouseY<self.y+self.imageRes:
                    pygame.mouse.set_cursor(self.hoverCursor)
                else:
                    pygame.mouse.set_cursor(self.notHoverCursor)
            else:
                mouseX,mouseY=pygame.mouse.get_pos()
                if mouseX>self.x and mouseX<self.x+self.imageResX and mouseY>self.y and mouseY<self.y+self.imageResY:
                    pygame.mouse.set_cursor(self.hoverCursor)
                else:
                    pygame.mouse.set_cursor(self.notHoverCursor)
        #CLick Event
        if left:
            if self.square:    
                mouseX,mouseY=pygame.mouse.get_pos()
                if mouseX>self.x and mouseX<self.x+self.imageRes and mouseY>self.y and mouseY<self.y+self.imageRes and _mouseDown==False:
                    self.function()
                    _mouseDown=True
            else:
                mouseX,mouseY=pygame.mouse.get_pos()
                if mouseX>self.x and mouseX<self.x+self.imageResX and mouseY>self.y and mouseY<self.y+self.imageResY and _mouseDown==False:
                    self.function()
                    _mouseDown=True
        else: _mouseDown=False
class Vector2:
    def __init__(self,x:int|float,y:int|float):
        self.value=(x,y)
          
class staticImage:
    "Static Graphic that doesn't move. Requires x,y and image"
    def __init__(self,**kwargs):
        if 'x' in kwargs and 'y' in kwargs and 'image' in kwargs:
            self.x=kwargs.get('x')
            self.y=kwargs.get('y')            
            self.image=pygame.image.load(kwargs.get('image')).convert()
        else:
            raise ValueError('staticImage requires args:x,y and image')
    def show(self,screen):
        screen.blit(self.image,(self.x,self.y))
#Save/Load system
def save(saveFile:str,save):
    "Save a dictionary of variables to a json file"
    _save=save
    with open(saveFile,'w') as f:
        json.dump(_save,f)
def load(saveFile:str):
    "Load a dictionary of variables from a json file and return it"
    _save=json.load(open(saveFile))
    return _save
def checkHover(x1:int,x2:int,y1:int,y2:int,function,inverseFuction=None):
    "Runs a function if mouse is in given area. Runs inverse function if mouse isn't in given area"
    mouseX,mouseY=pygame.mouse.get_pos()
    if mouseX>x1 and mouseX<x2 and mouseY>y1 and mouseY<y2:
        function()
    elif inverseFuction is not None:
        inverseFuction()



if __name__=='__main__':
    print('This script doesn\'t work on its own. Import it into a project to use the functions and classes defined here')
else:
    print('Using PyEngine v0.1 DEV') 