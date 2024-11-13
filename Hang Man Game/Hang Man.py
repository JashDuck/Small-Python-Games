import utilities as uu
from colorama import Fore, Back, Style


def drawWordBar(word, lives):
    guesses = ''
    while lives > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                failed += 1

        if failed == 0:
            print('\n')
            print(Fore.CYAN + Back.BLACK + 'You Won!' + Style.RESET_ALL)
            break

        print('')
        guess = uu.strValidate('Guess a character: ')
        while guess in guesses:
            if guess in guesses:
                print('You already guessed ' + guess + '. Try again:')
                guess = uu.strValidate('Guess a character: ')
        guesses += guess

        if guess not in word:
            lives -= 1
            print('\n' + Fore.RED + 'Wrong!' + Style.RESET_ALL)
            print('You have', lives, 'more guesses.')
        else:
            print('\n' + Fore.LIGHTGREEN_EX + 'Good job!' + Style.RESET_ALL)

        drawHangman(word, lives)


def drawHangman(word, lives):
    hangman = ('    ____  \n'
               '   |    | \n'
               '   |      \n'
               '   |      \n'
               '   |      \n'
               '   |      \n'
               '___|___   \n')

    if lives <= 5:
        hangman_temp = list(hangman)
        hangman_temp[30] = 'o'
        hangman = ''.join(hangman_temp)

    if lives <= 4:
        hangman_temp = list(hangman)
        hangman_temp[41] = '|'
        hangman = ''.join(hangman_temp)

    if lives <= 3:
        hangman_temp = list(hangman)
        hangman_temp[40] = '/'
        hangman = ''.join(hangman_temp)

    if lives <= 2:
        hangman_temp = list(hangman)
        hangman_temp[42] = '\\'
        hangman = ''.join(hangman_temp)

    if lives <= 1:
        hangman_temp = list(hangman)
        hangman_temp[51] = '/'
        hangman = ''.join(hangman_temp)

    if lives == 0:
        hangman_temp = list(hangman)
        hangman_temp[53] = '\\'
        hangman = ''.join(hangman_temp)
        print(hangman, '\n')
        print(Fore.CYAN + Back.BLACK + 'You Lose!' + Style.RESET_ALL + Fore.RED + '\nYour word was ' + Fore.MAGENTA + str(word) + Style.RESET_ALL + Fore.RED + '.' + Style.RESET_ALL)

    print(hangman)


def main():
    life = 6

    randWord = uu.randWord()
    print(randWord)
    print('Lets play some Hangman!')

    run = True

    while run:
        if len(randWord) <= 1:
            randWord = uu.randWord()

        else:
            run = False

    drawHangman(randWord, life)
    drawWordBar(randWord, life)
    playAgain = uu.strValidate('Do you want to play again? YES/NO ')
    if playAgain == 'yes':
        main()


if __name__ == '__main__':
    main()
