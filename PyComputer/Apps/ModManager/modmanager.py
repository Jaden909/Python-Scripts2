import Computer,pygame,PyEngine,os,importlib,sys,threading
windowOpen=False
window=pygame.image.load('Apps\\ModManager\\media\\screen1.png')
missingIcon=pygame.image.load('Apps\\ModManager\\media\\noIcon.png')
windowX,windowY=0,0
installedApps=[]
logList=[]
log={}
i=1
modSelected=False
titleFont=pygame.font.SysFont('monospace',20)
descFont=pygame.font.SysFont('monospace',15)
class App:
    def __init__(self,name,title,description,version,id,author,modified,script,icon,position):
        self.name=name
        self.title=title
        self.description=description
        self.version=version
        self.id=id
        self.author=author
        self.modified=modified
        self.script=script
        self.icon=icon
        self.position=position
    def loop(self):
        self.script.loop()
    def init(self):
        self.script.init()
    def config(self):
        self.script.config() 
def loadMods(modDir,loadingScreen,screen):
    global installedAppsGlobal,i   
    for root, dirs, files in os.walk(f'{Computer.path}\\Apps'):
        for name in dirs:
            if name[0].isupper():
                try:
                    meta=PyEngine.load(f'{Computer.path}\\Apps\\{name}\\meta.json') 
                except:
                    print(f'ERROR LOADING {name}:')
                    print(f'The mod "{name}" doesn\'t seem to have a meta.json file. Unable to retrieve meta data. The Mod might still work.')
                    logList.append(f'ERROR LOADING {name}:')
                    logList.append(f'The mod "{name}" doesn\'t seem to have a meta.json file. Unable to retrieve meta data. The Mod might still work.')
                    sys.path.insert(1,f'{modDir}\\{name}')
                    print(f'Folder named {name} successfully added to sys.path.')
                    logList.append(f'Folder named {name} successfully added to sys.path.')
                    app=App(name,'MISSING TITLE','MISSING DESCRIPTION','vX.X','unknown','MISSING AUTHOR','WHENEVER',importlib.import_module(name.lower()),None,i)
                    print(f'Mod named {name} sucessfully loaded but meta is missing.')
                    logList.append(f'Mod named {name} sucessfully loaded but meta is missing.')
                    if loadingScreen is not None:
                        screen.blit(loadingScreen,(0,0))
                    installedApps.append(app)
                    i+=1
                    continue
                print('________________________________________________________________________________________')
                logList.append('________________________________________________________________________________________')
                print(f'Mod named {name} found.')
                logList.append(f'Mod named {name} found.')
                sys.path.insert(1,f'{modDir}\\{name}')
                print(f'Folder named {name} successfully added to sys.path.')
                logList.append(f'Folder named {name} successfully added to sys.path.')
                meta=PyEngine.load(f'{modDir}\\{name}\\meta.json')
                print(f'meta data of {name} successfully loaded.')
                logList.append(f'meta data of {name} successfully loaded.')
                try:
                    app=App(name,meta.get('title'),meta.get('description'),meta.get('version'),meta.get('id'),meta.get('author'),meta.get('modified'),importlib.import_module(name.lower()),meta.get('icon'),i)
                except:
                    try:
                        app=App(name,meta.get('title'),meta.get('description'),meta.get('version'),meta.get('id'),meta.get('author'),meta.get('modified'),importlib.import_module(name.lower()),None,i)
                    except:
                        print('Loading mod meta data failed. Aborting mod loading.')
                        continue
                print(f'Mod object successfully created using the meta data of {name}.')
                logList.append(f'Mod object successfully created using the meta data of {name}.')
                installedApps.append(app)
                print(f'{name}\'s mod object succesfully added to list of mods.')
                print(f'Mod named {name} successfully loaded.')
                logList.append(f'{name}\'s mod object succesfully added to list of mods.')
                logList.append(f'Mod named {name} successfully loaded.')
                if loadingScreen is not None:
                    screen.blit(loadingScreen,(0,0))
                i+=1
                #print(f'App {i}:')
                #print(meta.get('title'))
                #print(meta.get('description'))
                #print(meta.get('version'))
                #print(meta.get('id'))
                #print(meta.get('author'))
                #print(meta.get('modified'))
    installedAppsGlobal=installedApps
    print(f'{i-1} apps installed.')
    return installedApps
def configMod():
    global currentPosition
    for mod in installedAppsGlobal:
        if mod.position==currentPosition:
            try:
                threading.Thread(target=mod.config).start()
            except AttributeError:
                print('The mod doesn\'t have a config function defined')
def runMod():
    global currentPosition
    for mod in installedAppsGlobal:
        if mod.position==currentPosition:
            try:
                threading.Thread(target=mod.init).start()
            except AttributeError:
                print('The mod doesn\'t have a init function defined')            
def selection(position):
    global modtitle,moddesc,modversion,modid,modauthor,modmodified,modSelected,modicon,currentPosition
    for mod in installedAppsGlobal:
        if mod.position==position:
            modtitle=titleFont.render(f'{mod.title}',True,'black')
            #print(len(mod.description))
            if len(mod.description)<=35:
                moddesc=descFont.render(f'{mod.description}',True,'black')
            else:
                #Blit multiple Lines
                moddesc=descFont.render(f'{mod.description}',True,'black')
            modversion=descFont.render(f'{mod.version}',True,'black')
            modid=descFont.render(f'ID: {mod.id}',True,'black')
            modauthor=descFont.render(f'Made By: {mod.author}',True,'black')
            modmodified=descFont.render(f'Last Updated: {mod.modified}',True,'black')
            if mod.icon is None or mod.icon=='none':
                modicon=missingIcon
            else:
                modicon=pygame.image.load(mod.icon)
            currentPosition=position
            modSelected=True
            #blit mod info
def loop():
    if windowOpen:
        Computer.screen.blit(window,(0,0))
        
        exitButton.listen()
        selectionButt1.listen()
        selectionButt2.listen()
        selectionButt3.listen()
        selectionButt4.listen()
        selectionButt5.listen()
        selectionButt6.listen()

        for mod in installedAppsGlobal:
            if mod.position>=7:
                break
            title=titleFont.render(mod.title,True,'black')
            Computer.screen.blit(title,(60,mod.position*50+mod.position*1))
            if mod.icon is None or mod.icon=='none':
                Computer.screen.blit(missingIcon,(12,mod.position*52+4))
            else:
                icon=pygame.image.load(mod.icon)
                Computer.screen.blit(icon,(12,mod.position*52+4))
        if modSelected:
            Computer.screen.blit(modtitle,(325,50))
            Computer.screen.blit(moddesc,(325,80))
            Computer.screen.blit(modversion,(325,100))
            Computer.screen.blit(modid,(325,125))
            Computer.screen.blit(modauthor,(325,150))
            Computer.screen.blit(modmodified,(325,175))
            Computer.screen.blit(modicon,(600,50))
            configButton.listen()
            configButton.show(screen=Computer.screen)
            runButton.listen()
            runButton.show(screen=Computer.screen)
        else:
            Computer.screen.blit(modTip,(350,50))
            Computer.screen.blit(modTip2,(350,70))
def init():
    global windowOpen,exitButton,selectionButt1,selectionButt2,selectionButt3,selectionButt4,selectionButt5,selectionButt6,descFont,modTip,modTip2,configButton,runButton
    def closeWindow():
        global windowOpen
        windowOpen=False
    if windowOpen==False:
        windowOpen=True
    exitButton=PyEngine.GameButton(x=windowX+580,y=windowY,imageResX=60,imageResY=40,image=None,function=closeWindow,hover=True,hoverSprite=Computer.linkcursorImg,notHoverSprite=Computer.cursorImg)
    configButton=PyEngine.GameButton(x=windowX+400,y=windowY+200,image='Apps\\ModManager\\media\\configButton.png',imageResX=128,imageResY=64,function=configMod,hover=True,hoverSprite=Computer.linkcursorImg,notHoverSprite=Computer.cursorImg)
    runButton=PyEngine.GameButton(x=windowX+400,y=windowY+275,image='Apps\\ModManager\\media\\runButton.png',imageResX=128,imageResY=64,function=runMod,hover=True,hoverSprite=Computer.linkcursorImg,notHoverSprite=Computer.cursorImg)
    selectionButt1=PyEngine.GameButton(x=0,y=50,imageResX=320,imageResY=52,image=None,function=lambda:selection(1),hover=True,hoverSprite=Computer.linkcursorImg,notHoverSprite=Computer.cursorImg)
    selectionButt2=PyEngine.GameButton(x=0,y=100,imageResX=320,imageResY=52,image=None,function=lambda:selection(2),hover=True,hoverSprite=Computer.linkcursorImg,notHoverSprite=Computer.cursorImg)
    selectionButt3=PyEngine.GameButton(x=0,y=150,imageResX=320,imageResY=52,image=None,function=lambda:selection(3),hover=True,hoverSprite=Computer.linkcursorImg,notHoverSprite=Computer.cursorImg)
    selectionButt4=PyEngine.GameButton(x=0,y=200,imageResX=320,imageResY=52,image=None,function=lambda:selection(4),hover=True,hoverSprite=Computer.linkcursorImg,notHoverSprite=Computer.cursorImg)
    selectionButt5=PyEngine.GameButton(x=0,y=250,imageResX=320,imageResY=52,image=None,function=lambda:selection(5),hover=True,hoverSprite=Computer.linkcursorImg,notHoverSprite=Computer.cursorImg)
    selectionButt6=PyEngine.GameButton(x=0,y=300,imageResX=320,imageResY=52,image=None,function=lambda:selection(6),hover=True,hoverSprite=Computer.linkcursorImg,notHoverSprite=Computer.cursorImg) 
    modTip=descFont.render('Click on a mod to view',True,'black')
    modTip2=descFont.render('more information about it.',True,'black')
def config():
    pass