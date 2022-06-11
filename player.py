import pygame
from borders import Border
class Player:
    def __init__(self,x,y,width,height, start_x, start_y, vel=5,color=(255,0,0), deaths = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.start_x = x
        self.start_y = y
        self.vel = vel
        self.color = color
        self.deaths = deaths
    def move(self, keys):
        if keys[pygame.K_a]:
            self.x -= self.vel
        if keys[pygame.K_d]:
            self.x += self.vel
        if keys[pygame.K_w]:
            self.y -= self.vel
        if keys[pygame.K_s]:
            self.y += self.vel
    def draw(self,screen):
        pygame.draw.rect(screen, ('black'), (self.x-2, self.y-2, self.width+4, self.height+4))
        return pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    def reset_position(self):
        self.x = self.start_x
        self.y = self.start_y