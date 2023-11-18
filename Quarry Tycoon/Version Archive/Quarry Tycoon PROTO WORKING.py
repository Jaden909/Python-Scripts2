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
newLevel=[0]*324


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
print(len(levelTest))
def loadLevel():
    #for i in range(3600):
        #if levelTest[i]==0:
        #    pass
        #else: 
        
        for i in range(18):    
            for gridy in range(18):
                tile=draw.Rect(i,gridy,32,32)
                print(gridy*i)
                if levelTest[0]==1:
                    screen.blit(mineImg,tile)
                    levelTest.pop(0)
                    newLevel.pop(i*gridy)
                    newLevel.insert(i*gridy,1)
                    print(newLevel)
                else:
                    levelTest.pop(0)
                
            pygame.display.update()    
            
            #print(f'{i}: object added')
            #level.pop(i)
            #level.insert(i,1)
            #print(level)
PyEngine.save('Saves\\PySave.json',levelTest)
print(f'Saved: {levelTest[:50]}(Shortened to save memory)')
newnewLevel=[0]*324
def hoverEffect():
    global mineImg2
    mouseX,mouseY=pygame.mouse.get_pos()
    
    screen.blit(mineImg2,(round(mouseX,-1),round(mouseY,-1)))
def saveLevel():
    for i in range(18):
        for ii in range(18):    
            color=screen.get_at((i*32+16,ii*32+16))
            print(color)
            screen.set_at((i*32+16,ii*32+16),(0,0,0,255))
            if color!=(14,209,69,255) and color!=(126, 255, 14, 255):
                newnewLevel.pop(i*ii)
                newnewLevel.insert(i*ii,1)
    print (newnewLevel)
screen.blit(bg,(0,0))
loadLevel()
saveLevel()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    PyEngine.checkHover(200,400,200,400,hoverEffect)
    pygame.display.update()
    