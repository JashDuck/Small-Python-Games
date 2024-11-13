from threading import Thread
from threading import Timer

import sys
from tkinter.messagebox import askretrycancel

import pygame as gg
import time
import random as rr
import math as mm

gg.init()

screen_width = 500
screen_height = 480

win = gg.display.set_mode((screen_width, screen_height))
gg.display.set_caption("Goblin Slayer")
backgroundColor = 255, 0, 0

healthAni = [gg.image.load('heart0.png'), gg.image.load('heart1.png'), gg.image.load('heart2.png'),
             gg.image.load('heart3.png')]

walkRight = [gg.image.load('R1.png'), gg.image.load('R2.png'), gg.image.load('R3.png'),
             gg.image.load('R4.png'), gg.image.load('R5.png'), gg.image.load('R6.png'),
             gg.image.load('R7.png'), gg.image.load('R8.png'), gg.image.load('R9.png')]
walkLeft = [gg.image.load('L1.png'), gg.image.load('L2.png'), gg.image.load('L3.png'),
            gg.image.load('L4.png'), gg.image.load('L5.png'), gg.image.load('L6.png'),
            gg.image.load('L7.png'), gg.image.load('L8.png'), gg.image.load('L9.png')]

bg = gg.image.load('bg.jpg')
char = gg.image.load('standing.png')
clock = gg.time.Clock()

bulletSound = gg.mixer.Sound('bullet.mp3')
hitSound = gg.mixer.Sound('hit.mp3')

gg.mixer.music.load('music.mp3')
gg.mixer.music.play(-1)

bulletSound.set_volume(.3)
hitSound.set_volume(.3)
gg.mixer.music.set_volume(.1)

# Starting Score
score = 0

# Starting number of lives
lives = 3

# Length of invincibility after death
immune_length = 5

# Amount of rounds
round_count = 1

# Speed of the Goblin
speed = 1.5

# Other Variables
invincible = True
died_txt_visible = False
round_txt_visible = False
off_screen = False
player_flashing = True


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 8
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, window):
        if self.walkCount >= 26:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                if invincible:
                    walkLeft[self.walkCount // 3].set_alpha(100)
                else:
                    walkLeft[self.walkCount // 3].set_alpha(1000)
                self.walkCount += 1
            elif self.right:
                window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                if invincible:
                    walkRight[self.walkCount // 3].set_alpha(100)
                else:
                    walkRight[self.walkCount // 3].set_alpha(1000)
                self.walkCount += 1
        else:
            if self.right:
                window.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                window.blit(walkLeft[0], (self.x, self.y))
            else:
                window.blit(char, (self.x, self.y))
                if invincible:
                    char.set_alpha(100)
                else:
                    char.set_alpha(1000)

        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def hit(self):
        self.isJump = False
        self.jumpCount = 8
        self.y = 410
        self.walkCount = 0
        gg.display.update()
        i = 0
        while i < 200:
            i += 1
            for events in gg.event.get():
                if events.type == gg.QUIT:
                    i = 201
                    gg.quit()


class projectile(object):
    def __init__(self, x, y, radius, color, dir_facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = dir_facing
        self.vel = 10 * dir_facing

    def draw(self, window):
        gg.draw.circle(window, self.color, (self.x, self.y), self.radius)


class enemy(object):
    walkRight = [gg.image.load('R1E.png'), gg.image.load('R2E.png'), gg.image.load('R3E.png'),
                 gg.image.load('R4E.png'), gg.image.load('R5E.png'), gg.image.load('R6E.png'),
                 gg.image.load('R7E.png'), gg.image.load('R8E.png'), gg.image.load('R9E.png'),
                 gg.image.load('R10E.png'), gg.image.load('R11E.png')]
    walkLeft = [gg.image.load('L1E.png'), gg.image.load('L2E.png'), gg.image.load('L3E.png'),
                gg.image.load('L4E.png'), gg.image.load('L5E.png'), gg.image.load('L6E.png'),
                gg.image.load('L7E.png'), gg.image.load('L8E.png'), gg.image.load('L9E.png'),
                gg.image.load('L10E.png'), gg.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [0, self.end]
        self.walkCount = 0
        self.vel = speed
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = health
        self.startHealth = health
        self.visible = True

    def draw(self, window, boss):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                window.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                window.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            if boss:
                gg.draw.rect(window, (218, 165, 32), (17, 67, 466, 26))
                gg.draw.rect(window, (88, 88, 88), (20, 70, 460, 20))
                gg.draw.rect(window, (208, 18, 229), (20, 70, (self.health / self.startHealth) * 460, 20))
            else:
                gg.draw.rect(window, (105, 105, 105), (self.hitbox[0] - 21, self.hitbox[1] - 22, 79, 14))
                gg.draw.rect(window, (88, 88, 88), (self.hitbox[0] - 19, self.hitbox[1] - 20, 75, 10))
                gg.draw.rect(window, (255, 0, 0), (self.hitbox[0] - 19, self.hitbox[1] - 20,
                                                   (self.health / self.startHealth) * 75, 10))
            self.hitbox = (self.x + 15, self.y + 2, 31, 57)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0

    def hit(self):
        global round_count
        global score
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
            round_txt = Thread(target=roundTextOnScreen)
            round_txt.start()
            round_count += 1
            score += 1


def redrawGameWindow():
    global off_screen
    win.blit(gg.transform.scale(bg, (500, 480)), (0, 0))
    man.draw(win)
    if round_count % 10 == 0:
        goblin.draw(win, True)
    else:
        goblin.draw(win, False)
    win.blit(gg.transform.scale(healthAni[lives], (108, 34)), (10, 10))

    for draw_bullet in bullets:
        if goblin.visible:
            draw_bullet.draw(win)

    if man.x > 470 or man.x < -35:
        off_screen = True

    # print the score on the screen
    txtScore = font1.render('Score: ' + str(score), True, (0, 0, 0))
    win.blit(txtScore, (340, 40))

    # print the high score on the screen
    txtScore = font1.render('High Score: ' + str(highscore[0]), True, (0, 0, 0))
    win.blit(txtScore, (260, 10))

    if round_count % 10 == 0 and round_txt_visible:
        txtRound = 'Boss Round'
        round_txt = font3.render(txtRound, True, (0, 0, 0))
        text_width, text_height = font3.size(txtRound)
        win.blit(round_txt, (screen_width / 2 - text_width / 2, screen_height / 2 - 180))

    elif round_txt_visible:
        txtRound = 'Round ' + str(round_count)
        round_txt = font3.render(txtRound, True, (0, 0, 0))
        text_width, text_height = font3.size(txtRound)
        win.blit(round_txt, (screen_width / 2 - text_width / 2, screen_height / 2 - 180))

    if died_txt_visible and done:
        txtLife = '-1 Life'
        lost_Life = font2.render(txtLife, True, (0, 0, 0))
        text_width, text_height = font2.size(txtLife)
        win.blit(lost_Life, (screen_width / 2 - text_width / 2, screen_height / 2 + text_height / 2))

    gg.display.update()


def waitInvisible():
    global invincible
    global done
    invincible = False
    done = True
    time.sleep(immune_length)


def detectLeftRight():
    global invincible
    global done
    t_end = time.time() + 60 * immune_length
    while time.time() < t_end:
        if man.left or man.right:
            if invincible:
                invincible = False
                done = True
                break


def textOnScreen():
    global died_txt_visible
    died_txt_visible = True
    time.sleep(immune_length - 1)
    died_txt_visible = False


def roundTextOnScreen():
    global round_txt_visible
    round_txt_visible = True
    time.sleep(3)
    round_txt_visible = False


def goblinRespawn():
    global goblin
    global varX
    global speed

    if round_count % 10 == 0:
        goblin = enemy(varX, 410, 64, 64, 450, mm.log(round_count) * 50)
    else:
        goblin = enemy(varX, 410, 64, 64, 450, mm.log(round_count) * 20)

    speed = round_count * .2 + 1

    goblin.visible = True
    gg.time.delay(3000)


def readFile(fileName):
    listFileData = []
    try:
        with open(fileName, 'r') as fileRdr:
            listFileData = fileRdr.read().splitlines()

    except FileNotFoundError:
        print(fileName, 'not found. Program will terminate.')
        exit()

    return listFileData


def writeFile(fileName):
    listFileData = []
    try:
        with open(fileName, 'w') as fileRdr:
            fileRdr.write(str(score))

    except FileNotFoundError:
        print(fileName, 'not found. Program will terminate.')
        exit()

    return listFileData


font1 = gg.font.SysFont('-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*', 40, True)
font2 = gg.font.SysFont('-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*', 60, True)
font3 = gg.font.SysFont('-*-lucidatypewriter-medium-r-*-*-*-140-*-*-*-*-*-*', 80, True)
man = player(440, 410, 64, 64)
goblin = enemy(0, 410, 64, 64, 450, 7.5)
shootLoop = 0
bullets = []
run = True
loopCount = 1
done = False

highscore = readFile('High Score.txt')

# mainloop
while run:
    clock.tick(40)

    if loopCount == 1:
        detect = Thread(target=detectLeftRight)
        detect.start()
        immune = Timer(immune_length, waitInvisible)
        immune.start()
        loopCount += 1

    if lives == 0:
        if score > int(highscore[0]):
            writeFile('High Score.txt')
        answer = askretrycancel('Game Over', 'Game Over\nYou Lose')
        if answer:
            score = 0
            round_count = 1
            lives = 3
            man = player(440, 410, 64, 64)
            goblin = enemy(0, 410, 64, 64, 450, 7.5)
        else:
            sys.exit()

    if not goblin.visible:
        varX = rr.randrange(0, 411)
        spawn_goblin = Timer(0.5, goblinRespawn)
        spawn_goblin.start()

    if not invincible:
        if goblin.visible:
            if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + \
                        goblin.hitbox[2]:
                    man.hit()
                    lives -= 1
                    invincible = True
                    died_txt_visible = True
                    if done:
                        immune = Timer(immune_length, waitInvisible)
                        immune.start()
                    died_txt = Thread(target=textOnScreen)
                    died_txt.start()

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 8:
        shootLoop = 0

    for event in gg.event.get():
        if event.type == gg.QUIT:
            run = False

    for bullet in bullets:
        if goblin.visible:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > \
                    goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + \
                        goblin.hitbox[2]:
                    hitSound.play()
                    goblin.hit()
                    bullets.pop(bullets.index(bullet))

        if 500 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = gg.key.get_pressed()

    if keys[gg.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 3:
            bullets.append(
                projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

        shootLoop = 1

    if keys[gg.K_LEFT] or keys[gg.K_a]:
        if off_screen:
            man.x = 470
            if man.x == 470:
                off_screen = False
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[gg.K_RIGHT] or keys[gg.K_d]:
        if off_screen:
            man.x = -35
            if man.x == -35:
                off_screen = False
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not man.isJump:
        if keys[gg.K_UP] or keys[gg.K_w]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -8:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.4 * neg
            man.jumpCount -= 0.5
        else:
            man.isJump = False
            man.jumpCount = 8

    redrawGameWindow()
gg.quit()


