# Example file showing a circle moving on screen
import pygame
import numpy as np

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = []

vel_x = []
vel_y = []
radius = []

circles = 0
mouse_is_pressed = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    mouse = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    if mouse[0]:
        if not mouse_is_pressed:
            circles += 1
            mouse_is_pressed = True
            player_pos.append(pygame.mouse.get_pos())
            radius.append(0)
        radius[-1] += 2
    else:
        if mouse_is_pressed:
            mouse_is_pressed = False

    for i in range(circles):
        pygame.draw.circle(screen, "red", player_pos[i], radius[i])

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
