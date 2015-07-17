"""
Pong Game
"""

import pygame

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(white)

    # ball
    pygame.draw.circle(screen, black, [circle_startx, circle_starty], 10, 0)
    # bar
    pygame.draw.rect(screen, black, [rect_startx, rect_starty, 100, 10])

    circle_startx += circle_dx
    circle_starty += circle_dy

    if circle_startx > 680 or circle_startx < 20:
        circle_dx = circle_dx * -1
    if circle_starty > 480 or circle_starty < 20:
        circle_dy = circle_dy * -1

    clock.tick(20)  # limits frames per second
    pygame.display.flip()  # updates the screen

pygame.quit()
