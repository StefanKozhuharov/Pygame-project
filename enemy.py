import pygame

class Enemy:
    def __init__(self,x,y,width,height,vel, color=('blue'), right = True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.color = color
        self.right = right
    def draw(self,screen):
        pygame.draw.circle(screen, ('black'), (self.x, self.y), self.width+3, self.height+3)
        return pygame.draw.circle(screen, self.color, (self.x, self.y), self.width, self.height)
    def move(self, bound_x1, bound_x2):
        if self.x < bound_x1 or self.x > bound_x2:
            self.right = not self.right
        if self.right:
            self.x +=self.vel
        else:
            self.x -=self.vel