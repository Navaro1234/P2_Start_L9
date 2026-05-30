import pygame
import time
from snake import Snake

kleur_achtergrond = (0,0,0)

breedte = 800
hoogte = 600
veld_grootte = 20
spel_snelheid = 5

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.x_verandering == 0:
                    snake.x_verandering = -veld_grootte
                    snake.y_verandering = 0
                elif event.key == pygame.K_RIGHT and snake.x_verandering == 0:
                    snake.x_verandering = veld_grootte
                    snake.y_verandering = 0
                elif event.key == pygame.K_UP and snake.y_verandering == 0:
                    snake.x_verandering = 0
                    snake.y_verandering = -veld_grootte
                elif event.key == pygame.K_DOWN and snake.y_verandering == 0:
                    snake.x_verandering = 0
                    snake.y_verandering = -veld_grootte

    snake.beweeg()
    venster.fill(kleur_achtergrond)
    snake.teken(venster)

    pygame.display.update()

    time.sleep(1 / spel_snelheid)

game_lus()