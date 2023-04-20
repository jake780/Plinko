import pygame
from random import randint, uniform

from ball import Ball
from obstacle import Obstacle

class Plinko():
    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        self.width = 1000
        self.height = 800
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Plinko")

        self.gameBalls = []
        self.obstacles = [] 
        self.ballDelay = 20

        self.setObstacles()

        # # Collision Testing
        # self.b = Ball(self, 0, 0)
        # self.gameBalls.append(self.b)

    def setObstacles(self):
        """Creates the Set of Obstacles"""

    def draw(self):
        """Draw all parts of the game"""
        # Draw all game Balls
        for b in self.gameBalls:
            b.draw()

        # Drawll all obstacles
        for o in self.obstacles:
            o.draw()

    def move(self):
        """Move all game items"""
        for b in self.gameBalls:
            b.move()

    def collide(self):
        """Collide all game items"""
        for b in self.gameBalls:
            b.collide(self.obstacles)

    def run(self):
        # Main Loop
        run = True
        delay = 0

        while run:
            self.win.fill((50,50,50))
            pygame.time.delay(10)
            key = pygame.key.get_pressed()

            # ESC
            if key[27]:
                pygame.quit()
                run = False
                return

            # Space to drop new Game Balls
            if key[32] and delay > self.ballDelay:
                self.gameBalls.append(Ball(self, uniform(-2,2), uniform(-2,2)))
                delay = 0

            # # Collision testing
            # if key[100]:
            #     self.b.xvel += 0.05
            # if key[97]:
            #     self.b.xvel -= 0.05
            # if key[115]:
            #     self.b.yvel += 0.05
            # if key[119]:
            #     self.b.yvel -= 0.05

            self.draw()
            self.move()
            self.collide()

            delay += 1
            pygame.event.pump()
            pygame.display.update()

def main():
    p = Plinko()
    p.run()

if __name__ == "__main__":
    main()