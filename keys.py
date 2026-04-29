import pygame
from settings import Settings
from rocket import Rocket

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print("Key pressed: " + str(event.key))
        