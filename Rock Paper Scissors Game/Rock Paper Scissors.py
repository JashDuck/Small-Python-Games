import utilities as uu
import random as rr


def computer():
    compChoices = ('rock', 'paper', 'scissors')
    comp = rr.randint(0, 2)

    return compChoices[comp]


def win(pla):
    comp = computer()

    print()
    print("Your guess: " + pla)
    print("Computer's guess: " + comp)
    print()

    if pla == 'rock':
        if comp == 'rock':
            print(f'{uu.colors.cyan}It was a Draw!{uu.colors.end}')
        if comp == 'paper':
            print(f'{uu.colors.red}You Lost!{uu.colors.end}')
        if comp == 'scissors':
            print(f'{uu.colors.green}You Win!{uu.colors.end}')

    if pla == 'paper':
        if comp == 'rock':
            print(f'{uu.colors.green}You Win!{uu.colors.end}')
        if comp == 'paper':
            print(f'{uu.colors.cyan}It was a Draw!{uu.colors.end}')
        if comp == 'scissors':
            print(f'{uu.colors.red}You Lost!{uu.colors.end}')

    if pla == 'scissors':
        if comp == 'rock':
            print(f'{uu.colors.red}You Lost!{uu.colors.end}')
        if comp == 'paper':
            print(f'{uu.colors.green}You Win!{uu.colors.end}')
        if comp == 'scissors':
            print(f'{uu.colors.cyan}It was a Draw!{uu.colors.end}')

    print()


def main():
    mainRun = True

    print('Welcome to rock papers scissors!')
    print("Enter 'Quit' to stop playing.")

    while mainRun:
        run = True

        while run:
            player = uu.strValidate("Enter 'Rock', 'Paper', or 'Scissors': ").lower()
            if player == 'rock' or player == 'paper' or player == 'scissors':
                win(player)
                run = False
            elif player == '':
                mainRun = False
                break
            else:
                print('Not a valid Input')

    print('Thanks for playing!')


if __name__ == '__main__':
    main()