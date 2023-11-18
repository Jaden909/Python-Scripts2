import random

numbers = list(range(0, 26))
letters = list(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])

for pairs in range(26):
    # Letter Stuff
    letter=random.choice(letters)
    letters.remove(letter)
    
    # Number Stuff
    number=random.choice(numbers)
    numbers.remove(number)
    
    # Pair Stuff
    strNumber=str(number)
    pair=letter+strNumber
    print (pair)