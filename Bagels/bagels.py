"""
bagels is a deductive logic game. (deductive meaning: "the deriving of a conclusion by reasoning")
"""

import random
num_digit = 3
max_guess = 10

#How to play
how_to_play = (f"""welcome to Bagels is a deductive logic game by PAL.
In this game you must guess a secret {num_digit} digit number(with no repeated digit) based on clues.

The game offers one of the following hints in response to your guess: 
1: "Pico" when your guess has a (correct digit in the wrong place).
2: "Fermi" when your guess has a (correct digit in the correct place).
3: "Bagels" if your guess has (no correct digits). 
You have 10 tries to guess the secret number.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.
""")


def main():
    print(how_to_play)
    start = input("IF you are ready to play type start: ")

    if start.lower() !=  "start":
        print("you quited the game! start again")
    else:
        start.lower() == "start"
        
        while True:
            secret_num = get_secret_num()

            guess_count = 0
            while guess_count <= max_guess:
                guess = ''
                while len(guess) != num_digit or not guess.isdecimal:
                    guess = input(f"Guess #{guess_count}:\n> ")

                clues = get_clues(guess, secret_num)
                print(clues)
                guess_count += 1

                if guess == secret_num:
                    break       # They're correct, so break out of this loop.
                if guess_count == max_guess:
                    print('You ran out of guesses restart the game')
                    print(f'The answer was {secret_num}:')
            
            print('Do you want to play again? ')
            if not input('> ').lower().startswith('y'):
                break
        print('Thanks for playing!')


        



def get_secret_num():
    num = list('0123456789')
    random.shuffle(num)
    secret_num = ''
    for i in range(num_digit):
        secret_num += str(num[i])
    return secret_num

def get_clues(guess, secret_num):
    if guess == secret_num:
        return "you WON!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return ''.join(clues)
    


main()

            