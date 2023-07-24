#Both required to blit anything to the computer screen
import Computer,pygame
#Useful for loading meta data
import PyEngine
#Load and print meta data
meta=PyEngine.load('Apps\\ExampleMod\\meta.json')
#Load any images you want to use like this
cn4=pygame.image.load('Apps\\ExampleMod\\media\\clocknum04.png')
#The loop() function is automatically called by the main computer during its main loop. Put anything you want the mod to constantly do like screen blits if you want them to last more than a frame.
def loop():
    #This accesses the computer's main screen
    Computer.screen.blit(cn4,(278,241))
#Called when the app is opened (not implemented yet)
def init():
    pass