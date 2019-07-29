import pygame
import numpy
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
size = 600, 600
max_iterations = 40
factor = 2
factor_w = 300
factor_h = 300
center = 300, 300

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mandelbrot")
screen.fill(black)


def colorize(val, maxiterations):
    r = int((val/maxiterations) * 255)
    if r > 255:
        r = 255
    g = 0
    b = 0
    # print(r, g, b)
    return r, g, b


def mandelbrot(x, y):
    w, h = size[0], size[1]
    # print(factor_w, factor_h)
    zx = factor * (x - factor_w) / w
    zy = factor * (y - factor_h) / h

    z = complex(zx, zy)
    c = complex(0, 0)

    for i in range(1, max_iterations):
        if abs(c) > 4:
            # print(i)
            return colorize(i, max_iterations)
        c = c * c + z


"""
for x in range(0, size[0], 3):
    for y in range(0, size[1], 3):
        # print(x, y)
        color = mandelbrot(x, y)
        # print(color)
        try:
            screen.set_at((x, y), color)
        except TypeError:
            pass
"""
while True:
    # function for Pygame updating the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.button)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            screen.fill(black)
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            factor_w = mouse_pos[0]
            factor_h = mouse_pos[1]
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            screen.fill(black)
            factor -= 0.01
            # mouse_pos = pygame.mouse.get_pos()
            # factor_w += 0.1 * (factor_w - mouse_pos[0]) - factor_w * factor
            # factor_h += 0.1 * (factor_h - mouse_pos[1]) - factor_h * factor
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            screen.fill(black)
            factor += 0.01
            # mouse_pos = pygame.mouse.get_pos()
            # factor_w += 0.1 * (factor_w - mouse_pos[0]) - factor_w * factor
            # factor_h += 0.1 * (factor_h - mouse_pos[1]) - factor_h * factor
    for x in range(0, int(size[0]/1), 3):
        for y in range(0, int(size[1]/1), 3):
            # print(x, y)
            color = mandelbrot(x, y)
            # print(color)
            try:
                screen.set_at((x, y), color)
            except TypeError:
                pass
    pygame.display.update()
