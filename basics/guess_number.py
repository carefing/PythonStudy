"""
Guess number between 1 and 100
"""

from random import randint

answer = randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('Guess a number: '))
    if number > answer:
        print('too big')
    elif number < answer:
        print('too small')
    elif number == answer:
        print('Bingo!')
        break
print('You have tried %d times.' % counter)