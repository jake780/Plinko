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
        # for i in range(1, 10):
        #     self.obstacles.append(Obstacle(self, self.width, 5*i, 20, 20))
            # Random Obstacles
            # self.obstacles.append(Obstacle(self, randint(0, 900), randint(0, 900), 50, 50))

        self.obstacles.append(Obstacle(self, 450, 200, 100, 400))
        #self.obstacles.append(Obstacle(self, self.width/2, 50, 20, 20))
        #self.obstacles.append(Obstacle(self, self.width/2, 50, 20, 20))



    def draw(self):
        for b in self.gameBalls:
            b.draw()

        for o in self.obstacles:
            o.draw()

    def move(self):
        for b in self.gameBalls:
            b.move()

    def collide(self):
        for b in self.gameBalls:
            # Collide game balls with obstacles
            b.collide(self.obstacles)

    def run(self):
        # Main Loop
        run = True
        delay = 0

        while run:
            self.win.fill((50,50,50))
            pygame.time.delay(10)
            key = pygame.key.get_pressed()

            if key[27]:
                pygame.quit()
                run = False
                return

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