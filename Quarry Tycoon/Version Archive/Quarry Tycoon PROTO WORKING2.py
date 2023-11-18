import PyEngine,pygame,threading
pygame.init()
screen=pygame.display.set_mode((600,600),pygame.RESIZABLE)
pygame.display.set_caption('Quarry Tycoon')
ico=pygame.image.load('Assets\\icoTemp.png')
pygame.display.set_icon(ico)
bg=pygame.image.load('Saves\\Image.png').convert()
mineImg=pygame.image.load('Assets\\mine.png').convert()
mineImg.set_colorkey('white')
mineImg2=pygame.image.load('Assets\\mine.png').convert()
mineImg2.set_colorkey('white')
mineImg2.set_alpha(125)
cursorImg=pygame.image.load('Assets\\cursor2.png').convert()
cursorImg.set_colorkey((235, 52, 52))
save:dict=PyEngine.load('Saves\\PySave.json')
coal=0
buildMode=False
#used to reset save
defaultSave={"buildingData": []}

_buildingData:list=save.get('buildingData')
font=pygame.font.Font('Assets\\vgaoem.fon',60)    
coalCount=font.render(f'Coal: {coal}',True,'white')

customCursor=pygame.Cursor((2,24),cursorImg)
pygame.mouse.set_cursor(customCursor)

def customRound(x, base=32):
    return base * round(x/base)

def loadLevel():
    screen.blit(bg,(0,0))
    for i in _buildingData:
        screen.blit(mineImg,i.get('pos'))
        threading.Thread(target=produceCoal).start()
        pygame.time.wait(10)
    pygame.display.update()    

def hoverEffect():
    if not {'id':1,'pos':(customRound(mouseX),customRound(mouseY))} in _buildingData:
        screen.blit(mineImg2,(customRound(mouseX),customRound(mouseY)))
        pygame.display.flip()
        mI=pygame.mouse.get_pressed()
        if mI[0]:    
            newBuilding={'id':1,'pos':(customRound(mouseX),customRound(mouseY))}
            _buildingData.append(newBuilding)
            threading.Thread(target=produceCoal).start()
            print(_buildingData)
            save.update(buildingData=_buildingData)
coal=0
def saveLevel():
    PyEngine.save('Saves\\PySave.json',save)
def produceCoal():
    global coal
    while True:
        coal+=1
        pygame.time.wait(1000)
clock=pygame.time.Clock()
#matThread=threading.Thread(target=produceMaterial)
loadLevel()
saveLevel()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            PyEngine.save('Saves\\PySave.json',save)
            print('Game Saved')
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:    
                if buildMode==False:
                    buildMode=True
                else:
                    buildMode=False  
    mouseX,mouseY=pygame.mouse.get_pos()
    mouseX-=16
    mouseY-=16
    
    coalCount=font.render(f'Coal: {coal}',True,'white')
    screen.blit(bg,(0,0))
    
    for i in _buildingData:
        screen.blit(mineImg,i.get('pos'))
    screen.blit(coalCount,(100,500))
    if buildMode:     
        PyEngine.checkHover(0,594,0,594,hoverEffect)
    else:
        pygame.display.flip()
    clock.tick(60)