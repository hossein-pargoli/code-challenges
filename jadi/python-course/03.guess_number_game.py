import random

number = random.randint(1, 100)

print('This is the number guess game. Guess the number between 1 and 100. Have fun :))')

while True:
    guess_number = int(input('>> '))
    if guess_number == number:
        print('Find it :))))')
        break
    elif guess_number > number:
        print('too big')
    else:
        print('too small')

print(guess_number)
