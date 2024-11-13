import pygame as gg
import math
# Initializing Pygame
gg.init()

# Screen
width = 500
Height = 650
rows = 3
win = gg.display.set_mode((width, Height))
gg.display.set_caption("TicTacToe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Images
X_IMAGE = gg.transform.scale(gg.image.load("x_modified.png"), (150, 150))
O_IMAGE = gg.transform.scale(gg.image.load("o_modified.png"), (150, 150))

# Fonts
END_FONT = gg.font.SysFont('courier', 40)


def draw_grid():
    gap = width // rows

    # Starting points
    x = 0
    y = 0

    for i in range(2):
        y = i * width

        gg.draw.line(win, GRAY, (0, 0), (x, width), 3)

    for i in range(rows):
        x = i * gap

        gg.draw.line(win, GRAY, (x, 0), (x, width), 3)
        gg.draw.line(win, GRAY, (0, x), (width, x), 3)


def initialize_grid():
    dis_to_cen = width // rows // 2

    # Initializing the array
    game_array = [[None, None, None], [None, None, None], [None, None, None]]

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x = dis_to_cen * (2 * j + 1)
            y = dis_to_cen * (2 * i + 1)

            # Adding centre coordinates
            game_array[i][j] = (x, y, "", True)

    return game_array


def click(game_array):
    global x_turn, o_turn, images

    # Mouse position
    m_x, m_y = gg.mouse.get_pos()

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x, y, char, can_play = game_array[i][j]

            # Distance between mouse and the centre of the square
            dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)

            # If it's inside the square
            if dis < width // rows // 2 and can_play:
                if x_turn:  # If it's X's turn
                    images.append((x, y, X_IMAGE))
                    x_turn = False
                    o_turn = True
                    game_array[i][j] = (x, y, 'x', False)

                elif o_turn:  # If it's O's turn
                    images.append((x, y, O_IMAGE))
                    x_turn = True
                    o_turn = False
                    game_array[i][j] = (x, y, 'o', False)


# Checking if someone has won
def has_won(game_array):
    # Checking rows
    for row in range(len(game_array)):
        if (game_array[0][2] == game_array[1][2] == game_array[2][2]) and game_array[0][2] != "":
            display_message(game_array[0][2].upper() + " has won!")
            return True

    # Checking columns
    for col in range(len(game_array)):
        if (game_array[0][2] == game_array[1][2] == game_array[2][2]) and game_array[0][2] != "":
            display_message(game_array[0][2].upper() + " has won!")
            return True

    # Checking main diagonal
    if (game_array[0][0][2] == game_array[1][1][2] == game_array[2][2][2]) and game_array[0][0][2] != "":
        display_message(game_array[0][0][2].upper() + " has won!")
        return True

    # Checking reverse diagonal
    if (game_array[0][2][2] == game_array[1][1][2] == game_array[2][0][2]) and game_array[0][2][2] != "":
        display_message(game_array[0][2][2].upper() + " has won!")
        return True

    return False


def has_drawn(game_array):
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            if game_array[i][j][2] == "":
                return False

    display_message("It's a draw!")
    return True


def display_message(content):
    gg.time.delay(500)
    win.fill(WHITE)
    end_text = END_FONT.render(content, 1, BLACK)
    win.blit(end_text, ((width - end_text.get_width()) // 2, (width - end_text.get_height()) // 2))
    gg.display.update()
    gg.time.delay(3000)


def render():
    win.fill(WHITE)
    draw_grid()

    # Drawing X's and O's
    for image in images:
        x, y, IMAGE = image
        win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

    gg.display.update()


def main():
    global x_turn, o_turn, images, draw
    images = []
    draw = False

    run = True

    x_turn = True
    o_turn = False

    game_array = initialize_grid()

    while run:
        for event in gg.event.get():
            if event.type == gg.QUIT:
                gg.quit()
            if event.type == gg.MOUSEBUTTONDOWN:
                click(game_array)

        render()

        if has_won(game_array) or has_drawn(game_array):
            run = False


while True:
    if __name__ == '__main__':
        main()