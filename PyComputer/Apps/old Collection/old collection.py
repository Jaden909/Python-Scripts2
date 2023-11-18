from customtkinter import *
from tkinter import *
def init():    
    import importlib
    mainWin=CTk()
    mainWin.title('Old Collection')
    def run(script):
        importlib.import_module(script)
    title=Label(master=mainWin,text='Jaden909\'s Abandoned and Old Projects Collection',font=(50),background='grey14',foreground='white')
    desc=Label(master=mainWin,text='Click on a game\'s button to play',font=(50),background='grey14',foreground='white')
    iGameButt=CTkButton(master=mainWin,text='iGame',command=lambda:run('iGame'))
    cipherButt=CTkButton(master=mainWin,text='failed Random Cipher',command=lambda:run('failed Random Cipher'))
    pwordcrackerbutt=CTkButton(master=mainWin,text='Password cracker',command=lambda:run('password cracker'))
    turtTest2Butt=CTkButton(master=mainWin,text='TurtTest2',command=lambda:run('turtTest2'))
    importpygame2Butt=CTkButton(master=mainWin,text='import pygame2',command=lambda:run('import pygame2'))
    title.pack()
    desc.pack()
    iGameButt.pack()
    cipherButt.pack()
    pwordcrackerbutt.pack()
    turtTest2Butt.pack()
    importpygame2Butt.pack()
    mainWin.mainloop()
def loop():
    pass
def config():
    return 0