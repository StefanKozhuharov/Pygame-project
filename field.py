import pygame

class Field:
    def __init__(self, x, y, width, heigth, color=('green')):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        self.color = color
    def draw(self,screen):
        return pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.heigth))