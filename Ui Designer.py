from customtkinter import *
from tkinter import *
import customtkinter
import tkinter
import json
mainWin=CTk()
mainWin.title('UI Designer')
layout={"widgets": []}
def newWindow():
    def update():
        tempX=inputX.get()
        tempY=inputY.get()
        newWidgetType=typeDropdown.get()
        widgets=layout.get('widgets')
        newWidget={'type':newWidgetType,'x':tempX,'y':tempY}
        widgets.append(newWidget)
        layout.update(widgets=widgets)
        print(layout)
        print(f'New Widget Created: {newWidgetType} at {tempX},{tempY}')
        if newWidgetType=='Label':
            _=CTkLabel()
            _.place(x=tempX,y=tempY)
        if newWidgetType=='Button':
            _=CTkButton()
            _.place(x=tempX,y=tempY)
    def click(_):
        global MouseX,MouseY
        inputX.delete(-1,999)
        inputY.delete(-1,999)
        inputX.insert(0,MouseX)
        inputY.insert(0,MouseY)
    newWidgetWin=CTk()
    newWidgetWin.title('Create New Widget')
    typeDropdown=CTkOptionMenu(master=newWidgetWin,values=['Label','Button','option 3'])
    typeDropdown.pack()
    inputX=CTkEntry(master=newWidgetWin,placeholder_text='X')
    inputX.pack()
    inputY=CTkEntry(master=newWidgetWin,placeholder_text='Y')
    inputY.pack()
    useMouseButt=CTkButton(text='Use Mouse')
    updateButton=CTkButton(text='Create',command=update,master=newWidgetWin)
    updateButton.pack()
    mainWin.bind("<Button-1>", click)
    newWidgetWin.mainloop()
def getMousePos(z):
    global MouseX,MouseY
    MouseX=z.x
    MouseY=z.y
def save(slot):
    if slot==1:
        with open('Layout1.json','w') as f:
            json.dump(layout,f)
    if slot==2:
        with open('Layout2.json','w') as f:
            json.dump(layout,f)
    if slot==3:
        with open('Layout3.json','w') as f:
            json.dump(layout,f)
def load(slot):
    global layout
    if slot==1:
        layout=json.load(open('Layout1.json'))
        loadLayout()
    if slot==2:
        layout=json.load(open('Layout2.json'))
        loadLayout()
    if slot==3:
        layout=json.load(open('Layout3.json'))
        loadLayout()
def loadLayout():
    global layout
    for widget in layout.get('widgets'):
        print(widget)
        if widget.get('type')=='Label':
            _=CTkLabel()
            _.place(x=widget.get('x'),y=widget.get('y'))
        if widget.get('type')=='Button':
            _=CTkButton()
            _.place(x=widget.get('x'),y=widget.get('y'))
def saveWindow():
    custom_font =("Times",25,'bold')
    saveWin=CTk()
    saveWin.title('Save Layout')
    saveWin.geometry('600x150')
    slot1Lab=CTkLabel(master=saveWin,text='Slot 1',text_font=custom_font)
    slot1Butt=CTkButton(master=saveWin,text='Save',command=lambda:save(1))
    slot2Lab=CTkLabel(master=saveWin,text='Slot 2',text_font=custom_font)
    slot2Butt=CTkButton(master=saveWin,text='Save',command=lambda:save(2))
    slot3Lab=CTkLabel(master=saveWin,text='Slot 3',text_font=custom_font)
    slot3Butt=CTkButton(master=saveWin,text='Save',command=lambda:save(3)) 
    slot1Lab.place(x=25,y=20)
    slot1Butt.place(x=25,y=70)
    slot2Lab.place(x=225,y=20)
    slot2Butt.place(x=225,y=70)   
    slot3Lab.place(x=450,y=20)
    slot3Butt.place(x=450,y=70)
    saveWin.mainloop()
def loadWindow():
    custom_font =("Times",25,'bold')
    loadWin=CTk()
    loadWin.title('Load Layout')
    loadWin.geometry('600x150')
    slot1Lab=CTkLabel(master=loadWin,text='Slot 1',text_font=custom_font)
    slot1Butt=CTkButton(master=loadWin,text='Load',command=lambda:load(1))
    slot2Lab=CTkLabel(master=loadWin,text='Slot 2',text_font=custom_font)
    slot2Butt=CTkButton(master=loadWin,text='Load',command=lambda:load(2))
    slot3Lab=CTkLabel(master=loadWin,text='Slot 3',text_font=custom_font)
    slot3Butt=CTkButton(master=loadWin,text='Load',command=lambda:load(3)) 
    slot1Lab.place(x=25,y=20)
    slot1Butt.place(x=25,y=70)
    slot2Lab.place(x=225,y=20)
    slot2Butt.place(x=225,y=70)   
    slot3Lab.place(x=450,y=20)
    slot3Butt.place(x=450,y=70)
    loadWin.mainloop()
def openControls():
    controlWin=CTk()
    controlWin.title('Control Panel')
    controlWin.geometry('150x100')
    newWidgetButton=CTkButton(master=controlWin,text='Create New Widget',command=newWindow)
    newWidgetButton.pack()
    saveButton=CTkButton(master=controlWin,text='Save Layout',command=saveWindow)
    saveButton.pack()
    loadButton=CTkButton(master=controlWin,text='Load Layout',command=loadWindow)
    loadButton.pack()
    controlWin.mainloop()
mainWin.bind('<Motion>',getMousePos)
mainWin.after(1,openControls)
mainWin.mainloop()