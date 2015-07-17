"""
Pong Game
"""

import pygame
from pygame.locals import K_LEFT, K_RIGHT

pygame.init()

size = [700, 500]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

clock = pygame.time.Clock()

circle_startx, circle_starty = 350, 250
circle_speed = circle_dx, circle_dy = 5, 5
rect_startx, rect_starty = 350, 480
shift = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                rect_startx += shift
            elif event.key == K_LEFT:
                rect_startx += -shift
        elif event.type == pygame.KEYUP:
            if event.key == K_RIGHT:
                rect_move = 0
            elif event.key == K_LEFT:
                rect_move == 0

    screen.fill(white)

    # ball
    pygame.draw.circle(screen, black, [circle_startx, circle_starty], 10, 0)
    # bar
    pygame.draw.rect(screen, black, [rect_startx, rect_starty, 100, 10])

    circle_startx += circle_dx
    circle_starty += circle_dy

    # Collision with boundaries
    if circle_startx > 680 or circle_startx < 20:
        circle_dx = circle_dx * -1
    if circle_starty < 20:
        circle_dy = circle_dy * -1
    if circle_starty > 480:
        circle_startx, circle_starty = 350, 250

    clock.tick(20)  # limits frames per second
    pygame.display.flip()  # updates the screen

pygame.quit()
