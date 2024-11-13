import pygame as gg

gg.init()

width = 500
height = 650
rows = 3
win = gg.display.set_mode((width, height))
gg.display.set_caption("Tic Tac Toe")

gray = (88, 88, 88)
white = (255, 255, 255)


def draw_grid():
    gap = width // rows

    # Starting points
    x = 0
    y = 0

    for i in range(2):
        gg.draw.line(win, gray, (0, 0), (x, width), 3)
        gg.draw.line(win, gray, (0, width), (x, width), 3)
        gg.draw.line(win, gray, (0, 0), (width, x), 3)
        gg.draw.line(win, gray, (width, 0), (width, x), 3)

    for i in range(rows):
        x = i * gap

        gg.draw.line(win, gray, (x, 0), (x, width), 3)
        gg.draw.line(win, gray, (0, x), (width, x), 3)


def render():
    win.fill(white)
    draw_grid()

    # Drawing X's and O's
    for image in images:
        x, y, IMAGE = image
        win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

    gg.display.update()


def main():
    global x_turn, o_turn, images, draw
    run = True
    images = []

    while run:
        for event in gg.event.get():
            if event.type == gg.QUIT:
                gg.quit()

        render()


if __name__ == '__main__':
    main()
