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
clues would be Fermi Pico.""")
ex = """
for example:
Guess #1:           
> 123
Pico

Guess #2:
> 456
Bagels

Guess #3:
> 178
Pico Pico

Guess #4:
> 791
Fermi Fermi

Guess #5:
> 701
You got it!"""


def main():
    print(how_to_play)
    start = input("IF you are ready to play type start,\nOR For more examples to understand the game type examples: ")

    if start.lower() == "example":
        print(ex)
    elif start.lower() != "example" or "start":
        print("you quited the game! start again")
    else:
        start.lower() == "start"
        
        while True:
            secret_num = get_secret_num()

            guesses = 1
            score = 0
            while guesses <= max_guess:
                guess = ''
                while len(guess) != num_digit or not guess.isdecimal:
                    guess = input(f"Guess #{guesses}: \n >")
        


    print(start)



def get_secret_num():
    num = list('0123456789')
    random.shuffle(num)
    secret_num = ''
    for i in range(num_digit):
        secret_num += str(num[i])
    return secret_num

main()

            