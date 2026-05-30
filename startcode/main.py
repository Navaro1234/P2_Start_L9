import pygame

breedte = 8000
hoogte = 6000

pygame.init()

venster = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption('Snake')

pygame.time.wait(5000)