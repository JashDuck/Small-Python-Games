import time

def intValidate(txtInput):
    while True:
        result = input(txtInput).strip()
        try:
            if result == ''.strip(): return 'endTask'
            int(result)
            return int(result)

        except ValueError:
            print('Not a valid number. Try again:')

def floatValidate(txtInput):
    while True:
        result = input(txtInput).strip()
        try:
            if result == ''.strip(): return 'endTask'
            float(result)
            return float(result)

        except ValueError:
            print('Not a valid number. Try again:')

def strValidate(txtInput):
    while True:
        result = input(txtInput).strip()
        if result == '': return 'endTask'
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


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1