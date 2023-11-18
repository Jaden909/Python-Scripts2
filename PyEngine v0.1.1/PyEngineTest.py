import PyEngine
import pygame
screen=pygame.display.set_mode((600,600))

#Animation Test
slash0=pygame.image.load('slash0.png').convert()
slash1=pygame.image.load('slash1.png').convert()
slash2=pygame.image.load('slash2.png').convert()
slash3=pygame.image.load('slash3.png').convert()
slash4=pygame.image.load('slash4.png').convert()
slash5=pygame.image.load('slash5.png').convert()
slash6=pygame.image.load('slash6.png').convert()
slash7=pygame.image.load('slash7.png').convert()
slashList=[slash0,slash1,slash2,slash3,slash4,slash5,slash6,slash7]
def test():
    print('click')
    PyEngine.animation(slashList,16,8,screen,300,300)

#Button Test
button=PyEngine.GameButton(x=100,y=164,function=test,hover=True)

#What to save and then load
save={'y':'y'}
PyEngine.save('PySave.json',save)    
load=PyEngine.load('PySave.json')
print(f'Loaded: {load}')

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    button.show(screen=screen)
    button.listen()
    
    pygame.display.update()