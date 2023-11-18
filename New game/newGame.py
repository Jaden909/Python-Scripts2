#Elevator Panic?
import pygame,PyEngine
x,y=300,500
screen=pygame.display.set_mode((600,600))
bg=pygame.image.load('bg.png').convert()
playerImg=pygame.image.load('player.png').convert()
screen.blit(bg,(0,0))
screen.blit(playerImg,(x,y))
pygame.display.update()
clock=pygame.time.Clock()
speed=1
playerCollider=pygame.Rect((x,y),(32,32))

def left():
    global x,speed
    if x>229:    
        x-=speed
    else:
        x=229
def right():
    global x,speed
    if x<361:    
        x+=speed
    else:
        x=361
def up():
    global y,speed
    if y>339:    
        y-=speed
    else:
        y=339
def down():
    global y,speed
    if y<557:    
        y+=speed
    else:
        y=557
while True:    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    PyEngine.wasdInput(up,left,down,right)
    playerCollider.update((x,y),(32,32))
    screen.blit(bg,(0,0))
    screen.blit(playerImg,(x,y))
    print(playerCollider)
    #playerCollider.colliderect()
    pygame.display.update()
    #print(pygame.mouse.get_pos())
    clock.tick(120)