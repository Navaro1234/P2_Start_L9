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
        self.x_verandering = self.x