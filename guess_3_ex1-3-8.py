'''
***  Guess Three Program  ***
***  Guess Three Program  ***
***  Guess Three Program  ***

This program:
    - Generates a three digit number at random (called the secret number).
        - Each digit in the secret number must be unique (880 is invalid since the 8 is repeated).
    - Asks the player to guess the secret number.
    - After each guess, the computer tells the player:
        - If they they win (guessed the secret number)
        - If they don't win, it tells them:
            - how many digits from their guess are in the secret number.
            - How many of the digits from their guess are in the correct position.
    - The player gets 10 guesses.
    - They win if they guess all three digits in the correct sequence.
    - Win or lose, the player is asked whether or not they want to play again.
    - The number of guesses and the number of digits in the secret number are flexible:
        - Set in the MAXGUESSES and NUMDIGITS constants.
'''

import random

NUMDIGITS = 3
MAXGUESS = 10

# Use lists and random.randint() to create the secret number.
def getSecretNum(numDigits):
    # Returns a string that is numDigits long, made up of unique random digits.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum

# Allow the player to enter a guess
def getClues(guess, secretNum):
    # Returns a string with the # correct and # correct and in correct place clues to the user.
    if guess == secretNum:
        return      # Exit this function if they got it right.

    # These variables store the number of numbers guessed that are in the secretNum
    #       and how many are in the correct position.
    inTheList = 0
    correctPosition = 0

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            inTheList += 1
            correctPosition +=1
        elif guess[i] in secretNum:
            inTheList +=1
    # This 2 character string is returned indicating the number in the
            #  list and, of those numbers, the ones in the correct position.
    return str(inTheList) + str(correctPosition)

# Asks the player to play again.
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    return input('Do you want to play again? (y/n)').lower().startswith('y')


print('I am thinking of a %s-digit number. Each digit is unique. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')

# Was the guess valid
def validGuess(guess):
    # Check for hint request

    # Skip validation on initial loop
    if len(guess) == 0:
        return False

    # Validate Number of digits
    if len(guess) != NUMDIGITS:
        print('Invalid Number of Digits Entered: Please enter ' + str(NUMDIGITS) + ' unique numbers from 0-9)')
        return False

    # Numeric Validation
    if not guess.isdigit():
        print('Non-numeric data entered: Please enter ' + str(NUMDIGITS) + ' unique numbers from 0-9)')
        return False

    # Unique Number Validation
    testedDigit = ''
    for digit in guess:
        if digit in testedDigit:
            print('Duplicate digit entered: Please enter ' + str(NUMDIGITS) + ' unique numbers from 0-9')
            return False
        else:
            testedDigit += digit
    return True


# Game Loop
# Game Loop
while True:
    secretNum = getSecretNum(NUMDIGITS)
    #print(' DEBUGGING PURPOSES ONLY - Secret Number: ' + str(secretNum))

    print('I have thought of a ' + str(NUMDIGITS) + ' digit a number. You have %s guesses to get it.' % (MAXGUESS))

    numGuesses = 1
    while numGuesses <= MAXGUESS:
        guess = ''
        #while len(guess) != NUMDIGITS or not guess.isdigit() or not validGuess(guess):
        # Keep looping until they enter a valid guess
        while not validGuess(guess):
            guess = input('Guess #%s: ' % (numGuesses))

        clue = getClues(guess, secretNum)
        if guess == secretNum:
            print('You have won...Great Job!')
            break

        # They didn't guess correctly.
        print('Your guess was: ' + str(guess) + '. You got ' + clue[0] + ' correct an	d ' + clue[1] + ' is/are in the correct place.')
        numGuesses += 1

        if numGuesses > MAXGUESS:
            print('You ran out of guesses. The answer was %s.' % (secretNum))

    if not playAgain():
        break