# The Matrix Screensaver 
import pygame, random, sys
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((600, 400)) 
pygame.display.set_caption("Matrix Screensaver")
font = pygame.font.SysFont('Consolas', 20)

columns = 60
drops = [0 for _ in range(columns)]

while True:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for i in range(len(drops)):
        char = chr(random.randint(33, 126))
        text = font.render(char, True, (0, 255, 0))
        window.blit(text, (i * 10, drops[i] * 10))

        drops[i] += 1
        if drops[i] * 10 > 400 or random.random() > 0.95:
            drops[i] = 0

    pygame.display.update()
    pygame.time.delay(30)