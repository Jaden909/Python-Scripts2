import tkinter
from tkinter import *
from tkinter import simpledialog
# List of Classes
c000001=list(['Test 1', 1, 1,])
c000002=list(['Test 2', 2, 1,])
c000003=list(['Test 3', 3, 1,])
c000004=list(['Test 4', 4, 1,])
c000005=list(['Test 5', 1, 2,])
c000006=list(['Test 6', 2, 2,])
c000007=list(['Test 7', 3, 2,])
c000008=list(['Test 8', 4, 2,])
b1s1='none'
b2s1='none'
b3s1='none'
b4s1='none'
b1s2='none'
b2s2='none'
b3s2='none'
b4s2='none'


def query1():    
    mainWin=Tk()
    global answer
    answer=simpledialog.askstring(title='Class Scheduler', prompt="What class do you want to schedule for 1st Block 1st semester?")
    currentBlock=b1s1
def query2():    
    mainWin=Tk()
    global answer
    answer=simpledialog.askstring(title='Class Scheduler', prompt="What class do you want to schedule for 2nd Block 1st semester?")
    currentBlock=b2s1
def query3():    
    mainWin=Tk()
    global answer
    answer=simpledialog.askstring(title='Class Scheduler', prompt="What class do you want to schedule for 3rd Block 1st semester?")
    currentBlock=b3s1
def query4():    
    mainWin=Tk()
    global answer
    answer=simpledialog.askstring(title='Class Scheduler', prompt="What class do you want to schedule for 4th Block 1st semester?")
    currentBlock=b4s1
def query5():    
    mainWin=Tk()
    global answer
    answer=simpledialog.askstring(title='Class Scheduler', prompt="What class do you want to schedule for 1st Block 2nd semester?")
    currentBlock=b1s2
def query6():    
    mainWin=Tk()
    global answer
    answer=simpledialog.askstring(title='Class Scheduler', prompt="What class do you want to schedule for 2nd Block 2nd semester?")
    currentBlock=b2s2
def query7():    
    mainWin=Tk()
    global answer
    answer=simpledialog.askstring(title='Class Scheduler', prompt="What class do you want to schedule for 3rd Block 2nd semester?")
    currentBlock=b3s2
def query8():    
    mainWin=Tk()
    global answer
    answer=simpledialog.askstring(title='Class Scheduler', prompt="What class do you want to schedule for 4th Block 2nd semester?")
    currentBlock=b4s2
def checkAnswer():
    if answer=='c000001':
        print(c000001)
    if answer=='c000002':
        print(c000002)
    if answer=='c000003':
        print(c000003)
    if answer=='c000004':
        print(c000004)
    if answer=='c000005':
        print(c000005)
    if answer=='c000006':
        print(c000006)
    if answer=='c000007':
        print(c000007)
    if answer=='c000008':
        print(c000008)

query1()
checkAnswer()
query2()
checkAnswer()
query3()
checkAnswer()
query4()
checkAnswer()
query5()
checkAnswer()
query6()
checkAnswer()
query7()
checkAnswer()
query8()
checkAnswer()


        