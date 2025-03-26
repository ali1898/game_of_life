import pygame
import sys

pygame.init()

GREY = (29, 29, 29)
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
FPS = 12

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()

# Simulation Loop
while True:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Updating State
    
    # Drawing
    window.fill(GREY)

    pygame.display.update()