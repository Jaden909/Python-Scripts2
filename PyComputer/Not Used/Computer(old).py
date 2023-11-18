import PyEngine,pygame,sys,os,importlib,time
pygame.init() 
installedApps=[]
screen=pygame.display.set_mode((640,360))
computerScreen=pygame.image.load('Assets\\Screens\\computerScreen3.png').convert()
loadingScreen=pygame.image.load('Assets\\Screens\\loadingScreen.png').convert()
def power():
    print('power')
cursorImg=pygame.image.load('Assets\\Cursors\\arrow.png')
linkcursorImg=pygame.image.load('Assets\\Cursors\\link.png')
cursor=pygame.cursors.Cursor((0,0),cursorImg)
linkcursor=pygame.cursors.Cursor((0,0),linkcursorImg)
powerButton=PyEngine.GameButton(x=0,y=300,function=power,imageResX=57,imageResY=60,hover=True,image=None,hoverSprite=linkcursorImg,notHoverSprite=cursorImg)
path=sys.path[0]
mods=True
booting=False
font=pygame.font.SysFont('Consolas',16)
titleFont=pygame.font.SysFont('Consolas',24)
bootTitle=titleFont.render('Boot Menu',False,'white')
bootOption1=font.render('Boot Normally',False,'white')
bootOption2=font.render('Boot in Safe Mode (no mods)',False,'white')
bootOption3=font.render('Test Single Mod',False,'white')
bootOption4=font.render('Custom Boot Mods',False,'white')#Would likely break current mods if implemented
selection=font.render('>',False,'white')
selectionNum,selectionMin,selectionMax=100,100,150
if __name__=='__main__':
    while True:
        if pygame.event.get(pygame.QUIT):
            exit()
        screen.fill((0,0,0))
        screen.blit(bootTitle,(220,50))  
        screen.blit(bootOption1,(220,100))
        screen.blit(bootOption2,(220,125))
        screen.blit(bootOption3,(220,150))
        screen.blit(selection,(200,selectionNum))
        
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                keys=pygame.key.get_pressed()
                if keys[pygame.K_DOWN]:
                    if selectionNum<selectionMax:
                        selectionNum+=25
                if keys[pygame.K_UP]:
                    if selectionNum>selectionMin:
                        selectionNum-=25
                if keys[pygame.K_RETURN]:
                    if selectionNum==100:
                        booting=True
                        break
                    if selectionNum==125:
                        mods=False
                        booting=True
                        break
                    if selectionNum==150:
                        print('not implemented yet')
                        #modTest()
        if booting:
            screen.blit(loadingScreen,(0,0))
            pygame.display.update()
            pygame.mouse.set_cursor(cursor)
            print('help me')
            start=time.time()
            break
        pygame.display.update()
    if mods:    
        try:
            sys.path.insert(1,f'{path}\\Apps\\ModManager')
            installedApps.append(importlib.import_module('modmanager'))
        except:
            print('Mod manager missing. Mod support disabled.')
            mods=False
    if mods:
        for root, dirs, files in os.walk(f'{path}\\Apps'):
            for name in dirs:
                if name[0].isupper():
                    sys.path.insert(0,f'{path}\\Apps\\{name}')
                    installedApps.append(importlib.import_module(name.lower()))
                    screen.blit(loadingScreen,(0,0))
                    pygame.display.update()
                    #pygame.time.wait(1000)
        timeTaken=time.time()-start
        print(f'Mods loaded in {timeTaken} seconds.')

    while True:
        if pygame.event.get(pygame.QUIT):
            exit()
        screen.blit(computerScreen,(0,0))
        for app in installedApps:
            app.loop()
        powerButton.listen()
        pygame.display.update()      