import pygame

pygame.init()

RESOLUTION = (80, 60)

display = pygame.display.set_mode(RESOLUTION)

grid = []
for y in range(0, RESOLUTION[1]):
    row = []
    for x in range(0, RESOLUTION[0]):
        row.append(0)
    grid.append(row)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            pygame.quit()
            exit()

    display.fill((0, 0, 0))
    for y in range(0, RESOLUTION[1]):
        for x in range(0, RESOLUTION[0]):
            if grid[y][x] == 1:
                pygame.draw.rect(display, (255, 255, 255), (x, y, 1, 1))

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        grid[pos[1]][pos[0]] = 1

    new_grid = []
    for y in range(0, RESOLUTION[1]):
        row = []
        for x in range(0, RESOLUTION[0]):
            row.append(0)
        new_grid.append(row)

    for y in range(0, RESOLUTION[1]):
        for x in range(0, RESOLUTION[0]):
            try:
                neigbors = {
                    "up": grid[y - 1][x],
                    "down": grid[y + 1][x],
                    "left": grid[y][x - 1],
                    "right": grid[y][x + 1],
                    "down_left": grid[y + 1][x - 1],
                    "down_right": grid[y + 1][x + 1],
                    "up_left": grid[y - 1][x - 1],
                    "up_right": grid[y - 1][x + 1],
                }

                if neigbors["up"]:
                    new_grid[y][x] = 1
            except IndexError:
                if y == 0:
                    new_grid[y][x] = 1
                # new_grid[y][x] = 0

    grid = new_grid

    pygame.display.update()
    pygame.time.Clock().tick(60)
