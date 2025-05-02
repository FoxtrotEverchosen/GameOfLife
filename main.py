import pygame
import numpy as np
from characters import LETTER_GRIDS


def count_neighbors(x, y, array, rows, cols):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            # if there is no offset on both, skip
            if i == 0 and j == 0:
                continue

            current_row = (x+i+rows) % rows
            current_col = (y+j+cols) % cols

            if array[current_row][current_col]:
                neighbors += 1

    return neighbors


# Constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
CELL_SIZE = 10


def main():
    cols = WINDOW_WIDTH // CELL_SIZE
    rows = WINDOW_HEIGHT // CELL_SIZE
    text_start = (rows//6, 5)

    # text to display on zeroth generation
    custom = input("Do you want to display custom text on grid?  (y/n): ")
    text = "~ Game Of Life"

    if custom.lower() == "y":
        text = input(f"What's your text? : ")

        if len(text) > max_chars:
            text = text[:max_chars]

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Game Of Life")
    clock = pygame.time.Clock()

    # Create grid of random values
    grid = np.zeros((rows, cols))

    # Populate grid with text, with arbitrary offset
    c_row, c_col = text_start
    for character in list(text):
        character = character.upper()

        if character in LETTER_GRIDS:
            g = LETTER_GRIDS[character]

            # wrap text
            if c_col + len(g[0]) >= cols-5:
                c_col = 5
                c_row = c_row + len(g) + 3

            # turn on character cells
            for r in range(len(g)):
                for c in range(len(g[0])):
                    try:
                        grid[c_row, c_col] = g[r][c]
                        c_col += 1
                    except IndexError:
                        raise Exception("Provided text was too long, please choose something shorter")

                # after imprinting full row go to the beginning of the next one
                c_row += 1
                c_col -= len(g[0])

            # calculate row, col of next letter
            c_row -= len(g)
            c_col = c_col + len(g[0]) + 2

    # GUI
    running = True
    paused = True
    while running:
        clock.tick(8)  # == 8 FPS

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    grid = np.random.choice([0, 1], size=(rows, cols))
                if event.key == pygame.K_SPACE:
                    paused = not paused
                if event.key == pygame.K_z and paused:
                    grid = np.zeros((rows, cols))

            # # turn clicked cell on/off if game is paused
            if event.type == pygame.MOUSEBUTTONDOWN and paused:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    # converting to int will truncate values after comma
                    col = int(pos[0]/CELL_SIZE)
                    row = int(pos[1]/CELL_SIZE)
                    grid[row, col] = 0 if grid[row, col] else 1

        if not paused:
            new_grid = np.copy(grid)
            for row in range(rows):
                for col in range(cols):
                    neighbors = count_neighbors(row, col, grid, rows, cols)
                    # Game of life rules
                    if grid[row, col] == 1 and (neighbors < 2 or neighbors > 3):
                        new_grid[row, col] = 0
                    elif grid[row, col] == 0 and neighbors == 3:
                        new_grid[row, col] = 1
            grid = new_grid

        # draw rectangles
        screen.fill((0, 0, 0))
        for row in range(rows):
            for col in range(cols):
                if grid[row, col]:
                    rect = pygame.Rect(col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, (255, 255, 255), rect)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
