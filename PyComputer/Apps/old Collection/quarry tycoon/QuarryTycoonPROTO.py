import PyEngine,pygame,threading,sys,time
debugMode=True
buildMode=False
coalMines=0
coalMultiplier=1
coalIncrement=1
version='v0.0 PREVIEW DEVELOPMENT BUILD'
#Temp value for coal until save is loaded
coal=0
if debugMode:
    print('Debug: Setting up pygame window...')
pygame.init()
pygame.display.set_caption('Quarry Tycoon')
ico=pygame.image.load('Assets\\icoTemp.png')
pygame.display.set_icon(ico)
screen=pygame.display.set_mode((600,600),pygame.RESIZABLE)
if debugMode:
    print('Debug: pygame window sucessfully created')
    print('Debug: loading assets...')
font=pygame.font.Font('Assets\\vgaoem.fon',4) 
loading=font.render('Loading...',True,'white')
coalCount=font.render(f'Coal: {coal}',True,'white')
versionText=font.render(f'Quarry Tycoon {version}',True,'white')
screen.blit(loading,(250,300))
pygame.display.flip()
bg=pygame.image.load('Assets\\grassBig.png').convert()
mineImg=pygame.image.load('Assets\\Buildings\\mine.png').convert()
mineImg.set_colorkey('white')
mineImg2=pygame.image.load('Assets\\Buildings\\mine.png').convert()
mineImg2.set_colorkey('white')
mineImg2.set_alpha(125)
cursorImg=pygame.image.load('Assets\\Cursor\\cursor2.png').convert()
cursorImg.set_colorkey((235, 52, 52))
cursorHoverImg=pygame.image.load('Assets\\Cursor\\cursor2Hover.png').convert()
cursorHoverImg.set_colorkey((235, 52, 52))
uiBase=pygame.image.load('Assets\\UI\\uiNormal.png').convert()
upgradeButtonImg=pygame.image.load('Assets\\UI\\upgradeButton3.png').convert()
upgradeTabImg=pygame.image.load('Assets\\UI\\upgradeFrame.png').convert()
if debugMode:
    print('Debug: assets sucessfully loaded')
    print('Debug: loading save...')
#TODO: add version number in game
save:dict=PyEngine.load('Saves\\PySave.json')
coal=save.get('coal')
_buildingData:list=save.get('buildingData')
#used to reset save
defaultSave={"buildingData": [], "coal": 50}
if debugMode:
    print('Debug: save sucessfully loaded')
    print('Debug: loading ui...')
Ui=[{'sprite':uiBase,'pos':(0,500)},{'sprite':upgradeButtonImg,'pos':(10,550)}]
tabOpen=False
def blitUi(elementList):
    for i in elementList:
        screen.blit(i.get('sprite'),i.get('pos'))
if debugMode:
    print('Debug: ui sucessfully created')
    print('Debug: loading general stuff like functions...')

customCursor=pygame.Cursor((2,24),cursorImg)
pygame.mouse.set_cursor(customCursor)

def produceMineral():
        global coal
        while True:    
            coal+=coalIncrement
            time.sleep(1)

def closeTab():
    global tabOpen
    tabOpen=False
def upgradeCoal():
    global coalMultiplier,coal
    if coal>=100:
        coalMultiplier+=1
        coal-=100
    else:
        pass
def openUpgradeTab():
    global tabOpen
    screen.blit(upgradeTabImg,(150,150))
    exitButton=PyEngine.GameButton(x=425,y=160,imageRes=11,function=closeTab,hover=True,hoverSprite=cursorHoverImg,notHoverSprite=cursorImg,image=None)
    upgradeButton1=PyEngine.GameButton(x=140,y=200,imageResX=150,imageResY=32,image=None,hover=True,hoverSprite=cursorHoverImg,notHoverSprite=cursorImg,function=upgradeCoal)
    #exitButton.show(screen=screen)
    tabOpen=True
    exitButton.listen()
    upgradeButton1.listen()
def customRound(x, base=32):
    return base * round(x/base)
Exit=False
threading.Thread(target=produceMineral,daemon=True).start()
if debugMode:
    print('Debug: produceMineral thread sucessfully created')
def loadLevel():
    global coalMines
    screen.blit(bg,(0,0))
    for i in _buildingData:
        screen.blit(mineImg,i.get('pos'))
        coalMines+=1
    pygame.display.update()    

def hoverEffect():
    global coal,coalMines
    if not {'id':1,'pos':(customRound(mouseX),customRound(mouseY))} in _buildingData:
        screen.blit(mineImg2,(customRound(mouseX),customRound(mouseY)))
        mI=pygame.mouse.get_pressed()
        if mI[0] and coal>=50:    
            newBuildingData={'id':1,'pos':(customRound(mouseX),customRound(mouseY))}
            coalMines+=1
            _buildingData.append(newBuildingData)
            coal-=50
            save.update(buildingData=_buildingData)
    pygame.display.flip()        
def saveLevel():
    PyEngine.save('Saves\\PySave.json',save)
upgradeButton=PyEngine.GameButton(x=10,y=550,imageResX=100,imageResY=40,hoverSprite=cursorHoverImg,notHoverSprite=cursorImg,hover=True,image=None,function=openUpgradeTab)

#def produceCoal():
#    global coal
#    while True:
#        coal+=1
#        pygame.time.wait(1000)
clock=pygame.time.Clock()
#matThread=threading.Thread(target=produceMaterial)
loadLevel()
saveLevel()
if debugMode:
    print('Debug: pregame loading sucessfully finished (any crashes after this message incdicate a problem with the gameloop and not the loading)')
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            PyEngine.save('Saves\\PySave.json',save)
            print('Game Saved')
            Exit=True
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:    
                if buildMode==False:
                    buildMode=True
                else:
                    buildMode=False 
            if debugMode:    
                if event.key==pygame.K_F2:
                    print(f'Mouse coordinates: {mouseX,mouseY}')
                if event.key==pygame.K_F3:
                    coal+=1000
                    print('Added 1000 coal')
                if event.key==pygame.K_F1:
                    PyEngine.save('Saves\\PySave.json',defaultSave)
                    print('Cleared save') 
    mouseX,mouseY=pygame.mouse.get_pos()
    mouseX-=16
    mouseY-=16
    
    coalCount=font.render(f'Coal: {coal}',True,'white')
    screen.blit(bg,(0.5,0))
    blitUi(Ui)
    #upgradeButton.show(screen=screen)
    upgradeButton.listen()
    for i in _buildingData:
        screen.blit(mineImg,i.get('pos'))
    screen.blit(coalCount,(20,520))
    screen.blit(versionText,(0,0))
    if tabOpen:
        openUpgradeTab()
    if buildMode:     
        PyEngine.checkHover(0,600,0,500,hoverEffect)
    if mouseY>=500:
        pygame.display.flip()
    else:
        pygame.display.flip()
    coalIncrement=coalMines*coalMultiplier
    save.update(coal=coal)
    clock.tick(60)