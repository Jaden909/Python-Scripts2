import pygame
import random
import sys
import sdl2.ext as sdl
import time
import sdl2

sdl.init()
window=sdl.Window('2D adventure... Coming Soon!', size=(600,600))
window.show()
def onclick(x,y):
    print('it works!')
    
running=True
factory=sdl.SpriteFactory(sdl.SOFTWARE)
sprite=factory.from_image("C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\2D Adventure\\LOGO.png")
renderer=factory.create_sprite_render_system(window)
renderer.render(sprite)
uifactory=sdl.UIFactory(factory)
button=uifactory.from_image(sdl.BUTTON,"C:\\Users\\ejh\\Documents\\Main Scripts\\Python\\2D Adventure\\buttTest.png")
button.position=(300,300)
renderer.render(button)
button.click +=onclick
uiprocessor=sdl.UIProcessor()
while running:
    events=sdl.get_events()
    for event in events:
        if event.type==sdl2.SDL_QUIT:
            running=False
            break
        uiprocessor.dispatch(button,event)

processor=sdl.TestEventProcessor()
processor.run(window)
sdl.quit()