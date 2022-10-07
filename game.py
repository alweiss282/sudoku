import pygame

WIDTH = 550
background_color = (251, 247, 245)


def main():
    """
    Window setup and main game loop.
    """
    grid = generate_grid()

    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)

    for i in range(10):
        line_width = 2
        if (i % 3 == 0):
            line_width = 4

        pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50),
                         (50 + 50*i, 500), line_width)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i),
                         (500, 50 + 50*i), line_width)
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


def generate_grid():
    """
    Generates valid and solvable sudoku grid.
    """


main()
