import numpy as np
import pygame

class line:
    def __init__(self, pos1, pos2) -> None:
        self.pos1 = pos1; self.pos2 = pos2;
    
    def draw(self):
        pygame.draw.line(screen, (0,0,255), self.pos1, self.pos2)

pygame.init()


screen = pygame.display.set_mode([500, 500])
running = True
lines = []



while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    screen.fill((0,0,0))

pygame.quit()




