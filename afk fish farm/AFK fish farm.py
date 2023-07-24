import time
import pyautogui
x1=961
y1=363
x2=963
y2=365
x3=959
y3=361

def get_pixel_colour(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[i_x, i_y]
time.sleep(5)
for urmom in range(100000): 
    yeet1=get_pixel_colour(x1,y1)
    yeet2=get_pixel_colour(x2,y2)
    yeet3=get_pixel_colour(x3,y3)
    print(yeet1)
    mx,my=pyautogui.position()
    print(x1,y1)
    if yeet1!=(252,252,252):
        if yeet2!=(252,252,252):
            if yeet3!=(252,252,252):
                pyautogui.click(x=mx,y=my,button='right') 
    else:pass
    time.sleep(0.6)