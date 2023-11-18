from PyEngine import *
import pygame
screen=pygame.display.set_mode((600,600))

def test():
    print('click')
    animation(slashList,16,8,screen,300,300)
slash0=pygame.image.load('Slash\\slash0.png').convert()
slash1=pygame.image.load('Slash\\slash1.png').convert()
slash2=pygame.image.load('Slash\\slash2.png').convert()
slash3=pygame.image.load('Slash\\slash3.png').convert()
slash4=pygame.image.load('Slash\\slash4.png').convert()
slash5=pygame.image.load('Slash\\slash5.png').convert()
slash6=pygame.image.load('Slash\\slash6.png').convert()
slash7=pygame.image.load('Slash\\slash7.png').convert()
slashList=[slash0,slash1,slash2,slash3,slash4,slash5,slash6,slash7]

y=GameButton(x=100,y=164,function=test,hover=True)
u={'y':'y'}
save('Saves\\PySave.json',u)    
g=load('Saves\\PySave.json')
print(f'Loaded: {g}')
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    y.show(screen=screen)
    y.listen()
    
    #screen.blit(currentSprite,(300,300))
    pygame.display.update()