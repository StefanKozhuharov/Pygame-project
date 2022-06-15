import pygame

class Enemy3:
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
    def move(self, bound_y1, bound_y2):
        if self.y < bound_y1 or self.y > bound_y2:
            self.right = not self.right
        if self.right:
            self.y +=self.vel
        else:
            self.y -=self.vel