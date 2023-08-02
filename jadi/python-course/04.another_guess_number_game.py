from random import randint

down_limiter = 1
up_limiter = 100
guess_number = randint(down_limiter, up_limiter)

print('\nChoose a number between 1 to 100 in your mind! computer trying to guess that ;)')

while True:
    print(f'\nLOG: randint({down_limiter}, {up_limiter})  -->  computer guess is {guess_number}')
    user_input = input(f'>> my choosen number is (Lower, Greather, Equal) than {guess_number}: ').lower()
    if user_input == ('e' or 'equal'):
        print(f'\n{guess_number} is correct, computer find it :)))')
        break
    elif user_input == ('l' or 'lower'):
        up_limiter = guess_number - 1
    elif user_input == ('g' or 'greather'):
        down_limiter = guess_number + 1
    elif user_input == 'q':
        break
    else:
        print("WARNING: Wrong input, 'l' or 'lower', 'g' or 'greather', 'e' or 'equal' and 'q' are the only valid characters in this program.")
        continue
    guess_number = randint(down_limiter, up_limiter)
