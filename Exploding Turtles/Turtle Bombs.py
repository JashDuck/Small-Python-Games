from tkinter import *
from tkinter import messagebox
import turtle as tt
import random as rr

win = Tk()
win.geometry('1200x1080')
win.resizable(False, False)

isPressed = {'Up': False, 'Down': False, 'Left': False, 'Right': False}

w = 1080
h = 1080

can = Canvas(master=win, width=w, height=h, bg='white')
can.pack()
tt.tracer(0, 0)

t = tt.RawTurtle(can)
b = tt.RawTurtle(can)
c = tt.RawTurtle(can)
t.pu()
t.shape('turtle')

xCoords = []
yCoords = []
radii = []

tarY = 0
tarX = 0
tarD = 0

points = 0
count = 1


def update():
    print('\r', 'You have', points, 'point(s)!', end='')
    win.after(10, update)


def bombs():
    b.speed(0)
    b.ht()

    run = True

    while run:
        x = rr.randint(int(-w / 2), int(w / 2))
        y = rr.randint(int(-w / 2), int(w / 2))
        d = rr.randint(50, 100)
        if t.distance(x, y) < d:
            x = rr.randint(int(-w / 2), int(w / 2))
            y = rr.randint(int(-w / 2), int(w / 2))
            d = rr.randint(50, 100)
        if t.distance(x, y) > d:
            run = False

    xCoords.append(x)
    yCoords.append(y)
    radii.append(d / 2)

    b.pu()
    b.goto(x, y)
    b.pd()
    b.dot(d, 'black')


def targets():
    c.speed(0)
    c.ht()

    run = True

    while run:
        x = rr.randint(int(-w / 2), int(w / 2))
        y = rr.randint(int(-w / 2), int(w / 2))
        d = rr.randint(50, 100)
        if t.distance(x, y) < d:
            x = rr.randint(int(-w / 2), int(w / 2))
            y = rr.randint(int(-w / 2), int(w / 2))
            d = rr.randint(50, 100)
        if t.distance(x, y) > d:
            run = False

    c.pu()
    c.goto(x, y)
    c.pd()
    c.dot(d // 2, 'red')

    return x, y, d // 2


def pressed(event):
    isPressed[event.keysym] = True


def released(event):
    isPressed[event.keysym] = False


def bindings():
    for i in ['Up', 'Down', 'Left', 'Right']:
        win.bind('<KeyPress-%s>' % i, pressed)
        win.bind('<KeyRelease-%s>' % i, released)


def close():
    win.withdraw()
    messagebox.showinfo('Game Over', 'Game Over\nYou Lose!')
    exit(0)
    win.destroy()


def anime(cleared=None):
    global tarX, tarY, tarD, points, count

    if isPressed['Up']: t.fd(7)
    if isPressed['Down']: t.bk(7)
    if isPressed['Left']: t.lt(5)
    if isPressed['Right']: t.rt(5)

    for i in range(len(xCoords)):
        if t.distance(xCoords[i], yCoords[i]) < radii[i]:
            close()

    if t.distance(tarX, tarY) < tarD:
        c.clear()
        cleared = True
        points += 1

    if cleared:
        tarX, tarY, tarD = targets()
        count += 1

    if count % 5 == 0:
        for k in range(2):
            bombs()
            count += 1

    can.update()
    win.after(10, anime)


if __name__ == '__main__':
    for i in range(20):
        bombs()

    tarX, tarY, tarD = targets()

    update()

    bindings()
    anime()

    win.mainloop()
