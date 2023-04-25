import pygame

class Obstacle():
    def __init__(self, game, x, y, width, height):
        self.game = game
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = ((96, 21, 158))

    def draw(self):
        pygame.draw.rect(self.game.win, self.color, (self.x, self.y, self.width, self.height))
