"""

In Bagels, a deductive logic game, you

must guess a secret three-digit number

based on clues. The game offers one of

the following hints in response to your guess:

“Pico” when your guess has a correct digit in the

wrong place, “Fermi” when your guess has a correct

digit in the correct place, and “Bagels” if your guess

has no correct digits. You have 10 tries to guess the

secret number.

Tags: short,game,puzzle

"""
import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(f'''
        Bagels, a deductive logic game.
    ---------------------------------------
    By Emmanuel Munyite (emunyite@gmail.com)
    
    I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
    Try to guess the number. Here are some clues:

    When I say:     That means:
    Pico             One digit is correct, but in the wrong place
    Fermi            One digit is correct and in the right place
    Bagels           No digits are correct

    For example, if the secret number was 248 and your guess was 843,
    the clues would be Fermi Pico.
    '''
    )

    #   Main loop for running the game
    while True:
        #   This stores the secret number we will generate(player needs to guess this number)
        secretNum = getSecretNum()
        print('I have thought up a secret number')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''  #   So that the player always gets a clean slate to feed the guesses
            #   Keep looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}:')
                guess = input('> ')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1


            if guess == secretNum:
                break   #   They are correct so break out of main the loop

            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f"The answer was {secretNum}")
                

        #   Ask player if they want to play again
        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing')



def getSecretNum():
    """ Returns a string made up of NUM_DIGITS unique random digits. """
    numbers = list('123456789')
    random.shuffle(numbers) # Shuffle the numbers list into random order

    #   Get the first NUM_DIGITS digits in the list for the secret number

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    
    return secretNum


def getClues(guess, secretNum):
    """ Returns a string with the Pico, Fermi, bagels clues for a guess 
    and secret number pair """
    if guess == secretNum:
        return 'You got it!'
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            #   A correct digit in the right plae
            clues.append('Fermi')
        elif guess[i] in secretNum:
            #   A correct digit in an incorrect place.
            clues.append('Pico')

            
    if len(clues) == 0:
        return 'Bagels' # There are no correct digits

    else:
        #   Sort the clues into alphabetical order so their original order
        #   does not give information away
        clues.sort()
        #   Make a single  string from the list of string clues.
        return ' '.join(clues)


#   If the program is run directly (instead of imported), run the game
if __name__ == '__main__':
    main()


