import pygame

class Border:
    def __init__(self, x, y, width, heigth, color=('black')):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        self.color = color
        self.hitbox = pygame.Rect(x, y, width, heigth)
    def draw(self,screen):
        return pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.heigth))