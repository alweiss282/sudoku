import pygame
import helpers

WIDTH = 550
BOX_SIZE = 3
background_color = (251, 247, 245)
original_grid_element_color = (52, 31, 151)
grid = [[0 for _ in range(BOX_SIZE**2)] for _ in range(BOX_SIZE**2)]
helpers.generate_grid(grid, BOX_SIZE)
helpers.remove_k_digits(grid, (BOX_SIZE**4)//2, BOX_SIZE)
grid_original = [row[:] for row in grid]
buffer = 5


def insert(win, position):
    i, j = position[1], position[0]
    myfont = pygame.font.SysFont('comicsansms', 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if grid_original[i-1][j-1] != 0:
                    return
                if event.key == 48:
                    grid[i-1][j-1] = 0
                    pygame.draw.rect(
                        win, background_color, (buffer + position[0]*50, buffer + position[1]*50, 50 - 2*buffer, 50-2*buffer))
                    pygame.display.update()
                    return
                if 1 <= event.key - 48 < 10:
                    pygame.draw.rect(
                        win, background_color, (buffer + position[0]*50, buffer + position[1]*50, 50 - 2*buffer, 50-2*buffer))
                    value = myfont.render(str(event.key-48), True, (0, 0, 0))
                    win.blit(value, (position[0]*50 + 15, position[1]*50))
                    grid[i-1][j-1] = event.key-48
                    pygame.display.update()
                    return
                return


def main():
    """
    Window setup and main game loop.
    """
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    myfont = pygame.font.SysFont('comicsansms', 35)

    for i in range(BOX_SIZE*BOX_SIZE+1):
        line_width = 2
        if (i % BOX_SIZE == 0):
            line_width = 4
        pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50),
                         (50 + 50*i, 500), line_width)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i),
                         (500, 50 + 50*i), line_width)

    for i in range(len(grid[0])):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                value = myfont.render(
                    str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()
