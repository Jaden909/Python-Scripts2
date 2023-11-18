import random
import tkinter
from tkinter import *
from tkinter import simpledialog
numbers = list(range(0, 26))
def split(word):
    return list(word)

#Changelog
#v0.1.1 Spaces are no longer included in the cipher

#UI
input=Tk()
word=simpledialog.askstring(title='Random Cipher', prompt="What is the word or words you want deciphered?")
input.destroy()
input.mainloop()

letters = split(word)

#Main code
for pairs in range((len(split(word)))):
    # Letter Stuff
    letter=letters.__getitem__(0)
    letters.remove(letter)
    
    # Number Stuff
    number=random.choice(numbers)
    numbers.remove(number)
    
    # Pair Stuff
    strNumber=str(number)
    pair=letter+strNumber
    if letter==' ':
        pair=' '
    print (pair)

   

#planned feature: ability to decipher chiphered text
#basic ui to perform the above