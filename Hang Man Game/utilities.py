import random
import os

def intValidate(txtInput):
    while True:
        result = input(txtInput).strip()
        try:
            if result == ''.strip(): return ''
            int(result)
            return int(result)

        except ValueError:
            print('Not a valid number. Try again:')


def floatValidate(txtInput):
    while True:
        result = input(txtInput).strip()
        try:
            if result == ''.strip(): return ''
            float(result)
            return float(result)

        except ValueError:
            print('Not a valid number. Try again:')


def strValidate(txtInput):
    while True:
        result = input(txtInput).strip()
        if result == '': return ''
        if result.isdigit():
            print('Did not input a string. Try again:')

        else:
            return result


def intWithCommas(x):
    if type(x) not in [type(0), type(0)]:
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)


def randWord():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, "wordList10000.txt"), "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))

        # print random string
        return random.choice(words)


# after you import utilities use f'{uu.colors.(the color that you want on the list)}(Your Text){uu.colors.end}' to change the color of the text
# ex: f'{uu.colors.red}Wrong!{uu.colors.end}'
# or you could import colorama: from colorama import Fore, Back, Style
# Commands in colorama are Fore, Back, and Style
class colors:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    gray = '\033[90m'
    brightGray = '\033[37m'
    brightRed = '\033[91m'
    brightGreen = '\033[92m'
    brightYellow = '\033[93m'
    brightBlue = '\033[94m'
    brightMagenta = '\033[95m'
    brightCyan = '\033[96m'
    white = '\033[97m'
    end = '\033[0m'
