import PyEngine,pygame,sys,os,importlib
installedApps=[]
screen=pygame.display.set_mode((640,360))
computerScreen=pygame.image.load('computerScreen2.png')
def power():
    print('power')
powerButton=PyEngine.GameButton(x=0,y=300,function=power,imageResX=40,imageResY=60,hover=True)
path=sys.path[0]
if __name__=='__main__':
    path=sys.path[0]
    sys.path.insert(1,f'{path}\\Apps\\ModManager')
    installedApps.append(importlib.import_module('modmanager'))
    for root, dirs, files in os.walk(f'{path}\\Apps'):
        for name in dirs:
            if name[0].isupper():
                sys.path.insert(0,f'{path}\\Apps\\{name}')
                installedApps.append(importlib.import_module(name.lower()))
    while True:
        if pygame.event.get(pygame.QUIT):
            exit()
        screen.blit(computerScreen,(0,0))
        for app in installedApps:
            app.loop()
        powerButton.listen()
        pygame.display.update()