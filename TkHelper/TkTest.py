from tkinter import *
import TkHelper
TkHelper.defaultSize='300x300'
t=Tk()
t.geometry('300x300')
#tt=Canvas(t,height=300,width=300,background='grey75')
#tt.pack()
#g=TkHelper.button(t,'yeet',print('urmom'))
#TkHelper.quickCanvas(300)
j=TkHelper.quickImage(t,"C:\\Users\\ejh\\Documents\\Main Scripts\\slash4.png")
j.pack()
t.mainloop()
