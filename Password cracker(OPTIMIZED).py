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
        print(f'The password is: {guess}')
        print(f'The password was guessed in {tries} tries!')
        exit()
    else:
        usedPasswords.append(guess)
    if tries%interval:
        print('|')
    if tries==tryLimit:
        print(f'Could not find the password in {tryLimit} tries')

#Runtime 100,000 tries 6 digit(unoptimized): 1:50
#RUntime 100,000 tries 6 digit(optimized):