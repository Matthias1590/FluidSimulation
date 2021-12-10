from copy import deepcopy
import pygame

pygame.init()

RESOLUTION = (80, 60)
RESOLUTION_MULTIPLIER = 10

display = pygame.display.set_mode(
    (RESOLUTION[0] * RESOLUTION_MULTIPLIER, RESOLUTION[1] * RESOLUTION_MULTIPLIER)
)

grid = []
for y in range(RESOLUTION[1]):
    row = []
    for x in range(RESOLUTION[0]):
        row.append(0)
    grid.append(row)

frame = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            pygame.quit()
            exit()

    display.fill((0, 0, 0))

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        grid[pos[1] // RESOLUTION_MULTIPLIER][pos[0] // RESOLUTION_MULTIPLIER] = 1
    elif pygame.mouse.get_pressed()[2]:
        pos = pygame.mouse.get_pos()

        grid[pos[1] // RESOLUTION_MULTIPLIER][pos[0] // RESOLUTION_MULTIPLIER] = 0

    for y in range(RESOLUTION[1]):
        for x in range(RESOLUTION[0]):
            if grid[y][x] == 1:
                pygame.draw.rect(
                    display,
                    (255, 255, 255),
                    (
                        x * RESOLUTION_MULTIPLIER,
                        y * RESOLUTION_MULTIPLIER,
                        RESOLUTION_MULTIPLIER,
                        RESOLUTION_MULTIPLIER,
                    ),
                )

    new_grid = deepcopy(grid)
    for y in range(RESOLUTION[1] - 1):
        for x in range(RESOLUTION[0]):
            current = grid[y][x]

            if not current:
                continue

            neighbours = {
                "up": grid[y - 1][x],
                "down": grid[y + 1][x],
                "left": grid[y][x - 1],
                "right": grid[y][x + 1],
                "up_left": grid[y - 1][x - 1],
                "up_right": grid[y - 1][x + 1],
                "down_left": grid[y + 1][x - 1],
                "down_right": grid[y + 1][x + 1],
            }

            if not neighbours["down"]:
                new_grid[y + 1][x] = 1
                new_grid[y][x] = 0
            elif not neighbours["down_left"]:
                new_grid[y + 1][x - 1] = 1
                new_grid[y][x] = 0
            elif not neighbours["down_right"]:
                new_grid[y + 1][x + 1] = 1
                new_grid[y][x] = 0
    grid = deepcopy(new_grid)

    pygame.display.update()
    pygame.time.Clock().tick(60)
    frame += 1
