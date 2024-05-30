# Example file showing a circle moving on screen
import pygame
import numpy as np

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

vel_x = 0
vel_y = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        vel_y = 300
    if keys[pygame.K_s]:
        vel_y = vel_y
    if keys[pygame.K_a]:
        vel_x = -300
    if keys[pygame.K_d]:
        vel_x = 300

    player_pos.x += vel_x * dt
    # player_pos.y -= vel_y * dt
    player_pos.y -= vel_y + 0.5 * (-100) * dt**2

    if np.abs(vel_x) > 0:
        if np.abs(vel_x) > 1:
            vel_x -= np.abs(vel_x)/vel_x * 1
        else:
            vel_x = 0

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
