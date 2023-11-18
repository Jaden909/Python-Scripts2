"""Module to simplify making UI with Tkinter. Obviously, It requires Tkinter."""
from tkinter import *
defaultSize='100x100'
"""default geometry of windows created by TkHelper functions"""
def quickButton(Title:str,Text:str,Command):
    """Creates a new Tkinter window and adds a button to it"""
    __=Tk()
    Tk.title(__,Title)
    __.geometry(defaultSize)
    _=Button(master=__,text=Text,command=Command)
    _.pack()
    __.mainloop()
def quickLabel(Title:str,Text:str):
    """Creates a new Tkinter window with a label"""
    __=Tk()
    Tk.title(__,Title)
    __.geometry(defaultSize)
    _=Label(master=__,text=Text)
    _.pack()
    __.mainloop()
def dynamicLabel(Master:Tk,string:str):
    """Creates a label that can change value dynamically. DOES NOT create its own window"""
    __=StringVar(value=string)
    _=Label(master=Master,textvariable=__)
    _.pack()
    return __
def button(Master:Tk,Text:str,Command):
    """Button with auto-pack. Requires a window. Returns a Tk button."""
    _=Button(Master,text=Text,command=Command)
    _.pack()
    return _
def label(Master:Tk,Text:str):
    """Label with auto-pack. Requires a window. Returns a Tk label."""
    _=Label(master=Master,text=Text)
    _.pack()
    return _
def QuickWin(Title:str,Geometry:str):
    """Creates a new Tkinter window with properties. Geometry is WidthxHeight format EX:('600x600'). Returns a Tk Window"""
    _=Tk()
    Tk.title(_,Title)
    _.geometry(Geometry)
    return _
def Wait(Window:Tk,Delay:int,function):  
    """Tk Friendly Wait command. Calls function after Delay time in ms"""
    Window.after(Delay,function)
def animation(frames:int,Delay:int,Window:Tk,File1:str,File2:str,File3:str,File4:str,File5:str,File6:str,File7:str,File8:str):
    """Plays an animation using provided Image frames. Amount of Files provided must match value of frames. Delay is time between each frame being shown"""    
    if frames>8:
        print("TkHelper doesn't support more than 8 frames currently." )
        return
    if frames>0:
        j1=PhotoImage(file=File1,master=Window)
        j00=Label(Window,image=j1)
        def call1():
            j00.pack()
            Window.update()
        Window.after(Delay,call1)
    if frames>1:
        j2=PhotoImage(file=File2,master=Window)
        j01=Label(Window,image=j2)
        j01.photo=j2
        def call2():
            j00.destroy()
            j01.pack()
            Window.update()
        Window.after(Delay*2,call2)
    if frames>2:
        j3=PhotoImage(file=File3,master=Window)
        j02=Label(Window,image=j3)
        j02.photo=j3
        def call3():
            j01.destroy()
            j02.pack()
            Window.update()
        Window.after(Delay*3,call3)
    if frames>3:
        j4=PhotoImage(file=File4,master=Window)
        j03=Label(Window,image=j4)
        j03.photo=j4
        def call4():
            j02.destroy()
            j03.pack()
            Window.update()
        Window.after(Delay*4,call4)
    if frames>4:
        j5=PhotoImage(file=File5,master=Window)
        j04=Label(Window,image=j5)
        j04.photo=j5
        def call5():
            j03.destroy()
            j04.pack()
            Window.update()
        Window.after(Delay*5,call5)
    if frames>5:
        j6=PhotoImage(file=File6,master=Window)
        j05=Label(Window,image=j6)
        j05.photo=j6
        def call6():
            j04.destroy()
            j05.pack()
            Window.update()
        Window.after(Delay*6,call6)
    if frames>6:
        j7=PhotoImage(file=File7,master=Window)
        j06=Label(Window,image=j7)
        j06.photo=j7
        def call7():
            j05.destroy()
            j06.pack()
            Window.update()
        Window.after(Delay*7,call7)
    if frames>7:
        j8=PhotoImage(file=File8,master=Window)
        j07=Label(Window,image=j8)
        j07.photo=j8
        def call8():
            j06.destroy()
            j07.pack()
            Window.update()
        Window.after(Delay*8,call8)
def canAnimation(frames:int,Delay:int,canvas:Canvas,File1:str,File2:str,File3:str,File4:str,File5:str,File6:str,File7:str,File8:str,x:int,y:int):
    """Plays an animation using provided Image frames. Amount of Files provided must match value of frames. Delay is ms between each frame being shown. Canvas Verison."""    
    if frames>8:
        print("animation() doesn't support more than 8 frame animations currently." )
        return
    if frames>0:
        j1=PhotoImage(file=File1,master=canvas)
        j00=Label(canvas,image=j1)
        def call1():
            canvas.create_window(x,y,window=j00,tags='_')
        canvas.after(Delay,call1)
        canvas.update()
    if frames>1:
        j2=PhotoImage(file=File2,master=canvas)
        j01=Label(canvas,image=j2)
        j01.photo=j2
        def call2():
            canvas.delete('_')
            canvas.create_window(x,y,window=j01,tags='_')
        canvas.after(Delay*2,call2)
        canvas.update()
    if frames>2:
        j3=PhotoImage(file=File3,master=canvas)
        j02=Label(canvas,image=j3)
        j02.photo=j3
        def call3():
            canvas.delete('_')
            canvas.create_window(x,y,window=j02,tags='_')
        canvas.after(Delay*3,call3)
        canvas.update()
    if frames>3:
        j4=PhotoImage(file=File4,master=canvas)
        j03=Label(canvas,image=j4)
        j03.photo=j4
        def call4():
            canvas.delete('_')
            canvas.create_window(x,y,window=j03,tags='_')
        canvas.after(Delay*4,call4)
        canvas.update()
    if frames>4:
        j5=PhotoImage(file=File5,master=canvas)
        j04=Label(canvas,image=j5)
        j04.photo=j5
        def call5():
            canvas.delete('_')
            canvas.create_window(x,y,window=j04,tags='_')
        canvas.after(Delay*5,call5)
        canvas.update()
    if frames>5:
        j6=PhotoImage(file=File6,master=canvas)
        j05=Label(canvas,image=j6)
        j05.photo=j6
        def call6():
            canvas.delete('_')
            canvas.create_window(x,y,window=j05,tags='_')
        canvas.after(Delay*6,call6)
        canvas.update()
    if frames>6:
        j7=PhotoImage(file=File7,master=canvas)
        j06=Label(canvas,image=j7)
        j06.photo=j7
        def call7():
            canvas.delete('_')
            canvas.create_window(x,y,window=j06,tags='_')
        canvas.after(Delay*7,call7)
        canvas.update()
    if frames>7:
        j8=PhotoImage(file=File8,master=canvas)
        j07=Label(canvas,image=j8)
        j07.photo=j8
        def call8():
            canvas.delete('_')
            canvas.create_window(x,y,window=j07,tags='_')
        canvas.after(Delay*8,call8)
        canvas.update()
def quickCanvas(size:int):
    """Create a canvas with a window."""
    _=Tk()
    _.geometry(defaultSize)
    __=Canvas(_,width=size,height=size)
    __.pack()
    _.mainloop()
def quickImage(Master:Misc,File:str):
    """Load an image and place it into a label"""
    _=PhotoImage(master=Master,file=File)
    __=Label(Master,image=_)
    __.photo=_
    return __

