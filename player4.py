import pygame

class Player:
    def __init__(self,x,y,width,height,vel=5,color=(255,0,0), deaths = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.color = color
        self.deaths = deaths
    def move(self, keys):
        if keys[pygame.K_a] and self.x > 0 + self.width:
            self.x -= self.vel
        if keys[pygame.K_d] and self.x < 800:
            self.x += self.vel
        if keys[pygame.K_w] and self.y > 0 + self.height:
            self.y -= self.vel
        if keys[pygame.K_s] and self.y < 600:
            self.y += self.vel
    def draw(self,screen):
        pygame.draw.rect(screen, ('black'), (self.x-3, self.y-3, self.width+6, self.height+6))
        return pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    def reset_position(self):
        self.x = 66
        self.y = 477