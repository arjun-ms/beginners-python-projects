import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess any number from 1 to {x} : '))
        if guess < random_number:
            print(f'Guess is not correct, Too LOW!')
        elif guess > random_number:
            print(f'Guess is not correct, Too HIGH!')
    print('Hooray!!! , You have guessed correct')


guess(10)
