import pygame
import mass as ms
import numpy as np

# pygame setup
pygame.init()
display = pygame.display.Info()
screen = pygame.display.set_mode((display.current_w, 0.95*display.current_h))
clock = pygame.time.Clock()
running = True
mouse_is_pressed = False

rate = 100

dt = 0.01
m = 0
pos = [0, 0]
bodies = []


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    mouse = pygame.mouse.get_pressed()

    if mouse[0]:
        if not mouse_is_pressed:
            mouse_is_pressed = True
            pos = pygame.mouse.get_pos()
        if m < 50*rate:
            m += rate
        pygame.draw.circle(screen, "red", pos, m/rate)
    else:
        if mouse_is_pressed:
            mouse_is_pressed = False
            body = ms.Body(m, [0, 0], pos)
            bodies.append(body)
            m = 0

    N = len(bodies)
    for i in range(N):
        pygame.draw.circle(screen, "red", bodies[i].get_pos(), bodies[i].m/rate)
        ms.apply_dynamics(bodies, dt)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(144) / 1000

pygame.quit()
