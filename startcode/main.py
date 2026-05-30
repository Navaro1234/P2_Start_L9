import pygame
from snake import *

breedte = 800
hoogte = 600

pygame.init()

venster = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption('Snake')

def game_lus():
    snake = Snake(breedte//2, hoogte//2)

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

    snake.teken(venster)

    pygame.display.update()
    pygame.time.wait(5000)

game_lus()