import random
import time

usedPasswords=list()
password=random.sample('1234567890', k=6)
tries=0
tryLimit=100000
interval=10
idk=0
print('Guessing...')
time.sleep(3)

for truePassword in range(tryLimit):
    guess=random.sample('1234567890', k=6)
    tries=tries+1
    if guess in usedPasswords:
        pass
    elif guess==password:
        strPassword=''.join(guess)
        print('The password is: '+strPassword)
        tries=str(tries)
        print('The password was guessed in '+tries+' tries!')
        exit()
    else:
        usedPasswords.append(guess)
    if tries%interval:
        print('|')
    if tries==tryLimit:
        tryLimit=str(tryLimit)
        print('Could not find the password in '+tryLimit+' tries')