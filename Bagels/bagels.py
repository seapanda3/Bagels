import random


NUM_DIGITS = 3
MAX_GUESS = 10


def main():

   print('''
 
  I am thinking of a {}-digit number with no repeated digits.
  Try to guess what it is. Here are some clues:
  When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
  
  For example, if the secret number was 248 and your guess was 843, the
  clues would be Fermi Pico.'''.format(NUM_DIGITS))
    while True:
        secretNum = getSecretNum()
        
        print('I have thought of a number!')
        print(f'You have #{MAX_GUESS} guesses to get it.')
        
        num_guess = 1
        while num_guess <= MAX_GUESS:
            
            guess = ''
            
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}'.format(num_guess))
                guess = input('> ')
                
            clues = getClues(guess, secretNum)
            print(clues)
            num_guess += 1
            
            if secretNum == guess:
                break
            if num_guess > MAX_GUESS:
                print('You ran out of guesses!')
                print('The secret number was {}.'.format(secretNum))
                
                
        print('Do you want to play again? (yes/no)')
        if not input("> ").lower().startswith('y'):
            break
    print('Goodbye!')


def getClues(guess, secretNum):
    if secretNum == guess:
        print('You got it!')
        
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
            
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
    
    
def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
        
    return secretNum

if __name__ == '__main__':
    main()
