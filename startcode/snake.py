import pygame

kleur_slang = (0, 255, 0)
veld_grootte = 20

class Snake:
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty
        self.lijst_slang = [[startx, starty]]
        self.lengte_slang = 1
        self.x_verandering = 0
        self.y_verandering = 0

    def teken(self, venster):
        for segment in self.lijst_slang:
            pygame.draw.rect(venster, kleur_slang, pygame.Rect(segment[0], segment[1], veld_grootte, veld_grootte))