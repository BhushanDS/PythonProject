

import random

def guess(x):  #for user guess
    random_number = random.randint(1,x)
    guess = 0
    while guess!= random_number:
        guess = int(input("Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("I/P Number is low")
        elif guess>random_number:
            print("I/P Number is To high")
    print(f'Yay you have guess the number {random_number}')

def computer_guess(x):  # for Computer guess
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else :
            guess = low
        feedback = input(f'Is {guess} too high (H), or too low (L) or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess +1
        
    print(f'Yay , computer gues your umer {guess}')
    
computer_guess(100)