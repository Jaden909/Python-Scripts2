import PyEngine,pygame,sys,os,importlib,time,ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(0)
pygame.init() 
screen=pygame.display.set_mode((1280,720))
pygame.display.set_caption('PyComputer')
icon=pygame.image.load('icon3.png')
pygame.display.set_icon(icon)
path=sys.path[0]
mods=True
booting=False
cursorImg=pygame.image.load('Assets\\Cursors\\arrow.png')
linkcursorImg=pygame.image.load('Assets\\Cursors\\link2.png')
loadingScreen=pygame.image.load('Assets\\Screens\\loadingScreen.png').convert()
begin=0
ctrl=False
try:
    controller=pygame.joystick.Joystick(0)
    controller.init()
    ctrl=True
except:
    print('No controller detected')
#Change Log
#Improved Handling of mods with missing meta files
if __name__=='__main__':
    print(sys.path[0])
    computerScreen=pygame.image.load('Assets\\Screens\\computerScreen6.png').convert()
    def power():
        exit()
    def modConfig():
        if mods:
            for app in installedApps:
                if app.id=='modlist':
                    app.init()
                    pygame.mouse.set_cursor(cursor)
                    break
        else:
            print('Mods Disabled. How are you going to manage nothing?')
    def ide():
        if mods:
            for app in installedApps:
                if app.id=='ide':
                    app.init()
                    pygame.mouse.set_cursor(cursor)
                    break
        else:
            print('IDE Disabled. How are you going to code with nothing?')
    powerButton=PyEngine.GameButton(x=0,y=600,function=power,imageResX=114,imageResY=120,hover=True,image=None,hoverSprite=linkcursorImg,notHoverSprite=cursorImg)
    modConfigButton=PyEngine.GameButton(x=0,y=0,function=modConfig,imageResX=114,imageResY=120,hover=True,image=None,hoverSprite=linkcursorImg,notHoverSprite=cursorImg)
    IDEButton=PyEngine.GameButton(x=0,y=100,function=ide,imageResX=114,imageResY=100,hover=True,image=None,hoverSprite=linkcursorImg,notHoverSprite=cursorImg)
    cursor=pygame.cursors.Cursor((0,0),cursorImg)
    linkcursor=pygame.cursors.Cursor((0,0),linkcursorImg)
    try:
        import PyBIOS
        mods=PyBIOS.mods
    except ImportError:
        print('PyBIOS missing or damaged. Booting in safe mode...')
        mods=False
        booting=True
    if mods:    
        try:
            sys.path.insert(1,f'{path}\\Apps\\ModManager')
            modmanager=importlib.import_module('modmanager')
        except:
            print('Mod manager missing. Mod support disabled.')
            mods=False
    if mods:
        begin=time.time()
        installedApps=modmanager.loadMods(f'{path}\\Apps',loadingScreen,screen)
        timeTaken=time.time()-begin
        print(f'Mods loaded in {timeTaken} seconds.') 
    pygame.mouse.set_cursor(cursor) 
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if ctrl:
                if event.type==pygame.JOYAXISMOTION:
                    #Axis 1: UP/Down on left joystick
                    mouseX,mouseY=pygame.mouse.get_pos()
                    
                    pygame.mouse.set_pos(mouseX+round(controller.get_axis(0)),mouseY+round((controller.get_axis(1))),)
                    print(f'Axis 1:{controller.get_axis(1)}, Axis 0:{controller.get_axis(0)}')
                if event.type==pygame.JOYBUTTONDOWN:
                    if controller.get_button(0):
                        mouseX,mouseY=pygame.mouse.get_pos()
                        print(mouseX,mouseY)
                        #PyEngine.listenAll()
                        PyEngine.listenPulseAll()
        screen.blit(computerScreen,(0,0))
        if mods:
            for app in installedApps:
                app.loop()
                if app.id=='modlist':
                    if not app.script.windowOpen:
                        modConfigButton.listen()
                elif app.id=='ide':
                    if not app.script.windowOpen:
                        IDEButton.listen()
        powerButton.listen()
        pygame.display.update()      