import PyEngine,pygame
from pygame_gridcalculator import GridCalculator
from pygame_gridcalculator import ShapeFactory
screen=pygame.display.set_mode((600,600))
bg=pygame.image.load('Assets\\grassBig.png').convert()
mineImg=pygame.image.load('Assets\\mine.png').convert()
mineImg.set_colorkey('white')
mineImg2=pygame.image.load('Assets\\mine.png').convert()
mineImg2.set_colorkey('white')
mineImg2.set_alpha(125)
#level Layout
#levelTest=[0]*324
#print(levelTest)
levelTest:list=PyEngine.load('Saves\\PySave.json')
grid=GridCalculator(600,600,18,18)
draw=ShapeFactory(grid)



def getGridPos(pos):
    #GridX Stuff
    if pos<61:
        gridx=50
    if pos==2 or pos==5 or pos==8:
        gridx=250
    if pos==3 or pos==6 or pos==9:
        gridx=450
    #GridY Stuff
    if pos<61:
        gridy=10
    if pos==4 or pos==5 or pos==6:
        gridy=250
    if pos==7 or pos==8 or pos==9:
        gridy=450
    return gridx,gridy
print(f'Loaded: {levelTest[:50]}(Shortened to save memory)')
def loadLevel():
    #for i in range(3600):
        #if levelTest[i]==0:
        #    pass
        #else: 
        gridy=1
        i=1
        for urmom in range(19):    
            for gridy in range(19):
                tile=draw.Rect(i,gridy,32,32)
                if levelTest[(gridy)*(i)]==1:
                    screen.blit(mineImg,tile)
                gridy+=1
            pygame.display.update()    
        i+=1
            #print(f'{i}: object added')
            #level.pop(i)
            #level.insert(i,1)
            #print(level)
PyEngine.save('Saves\\PySave.json',levelTest)
print(f'Saved: {levelTest[:50]}(Shortened to save memory)')
def hoverEffect():
    global mineImg2
    mouseX,mouseY=pygame.mouse.get_pos()
    
    screen.blit(mineImg2,(round(mouseX,-1),round(mouseY,-1)))
screen.blit(bg,(0,0))
loadLevel()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    PyEngine.checkHover(200,400,200,400,hoverEffect)
    pygame.display.update()
    