import pygame


class EventManager():
    def __init__(self, game):
        self.game = game
        self.binColor1 = ((0, 255, 255))
        self.binColor2 = ((0, 184, 200))

    def draw(self):
        # Bins
        # pygame.draw.rect(self.game.win, self.binColor1, (0, 900, 100, 100))
        # pygame.draw.rect(self.game.win, self.binColor1, (1100, 900, 100, 100))

        # pygame.draw.rect(self.game.win, self.binColor2, (100, 900, 100, 100))
        # pygame.draw.rect(self.game.win, self.binColor2, (1000, 900, 100, 100))