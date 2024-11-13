import random
import math as mm


def intValidate(txtInput):
    while True:
        result = input(txtInput).strip()
        try:
            if result == ''.strip(): return ''
            if result == 'quit'.strip().lower(): return ''
            int(result)
            return int(result)

        except ValueError:
            print('Not a valid number. Try again:')


def floatValidate(txtInput):
    while True:
        result = input(txtInput).strip()
        try:
            if result == ''.strip(): return ''
            if result == 'quit'.strip().lower(): return ''
            float(result)
            return float(result)

        except ValueError:
            print('Not a valid number. Try again:')


def strValidate(txtInput):
    while True:
        result = input(txtInput).strip()
        if result == 'quit'.strip().lower(): return ''
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
    with open("../Data Files/wordList10000.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))

        # print random string
        print(random.choice(words))


def readFile(fileName, heading):
    listFileData = []
    try:
        with open(fileName, 'r') as fileRdr:
            if not heading:
                fileRdr.readline()
            elif heading != 5:
                colHeadings = fileRdr.readline().split(',')
            listFileData = fileRdr.read().splitlines()

    except FileNotFoundError:
        print(fileName, 'not found. Program will terminate.')
        exit()

    if not heading:
        return listFileData
    elif heading != 5:
        return colHeadings, listFileData
    else:
        return listFileData


def extractNumbers(fileName, readLines):
    listNumbers = []
    try:
        with open(fileName) as fileRdr:
            for i in range(readLines - 1):
                fileRdr.readline()
            tempNumbers = fileRdr.readline()
            numbers = tempNumbers.split(',')
            for i in range(1, len(numbers)):
                listNumbers.append(int(numbers[i]))
    except FileNotFoundError:
        print(fileName, 'not found. Program will terminate.')
        exit()
    return listNumbers


def printList(theList):
    for i in range(len(theList) - 1):
        print(theList[i], end=', ')
    print(theList[len(theList) - 1])


def moneyPrint(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)


def round_nearest(x, a):
    return round(round(x / a) * a, -int(mm.floor(mm.log10(a))))


# after you import utilities use f'{uu.colors.(the color that you want on the list)}(Your Text){uu.colors.end}' to
# change the color of the text ex: f'{uu.colors.red}Wrong!{uu.colors.end}' or you could import colorama: from
# colorama import Fore, Back, Style Commands in colorama are Fore, Back, and Style
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
