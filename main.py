import pygame
from random import randint, uniform

from ball import Ball
from obstacle import Obstacle
from eventmanager import EventManager

class Plinko():
    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        self.width = 1200
        self.height = 1000
        self.bgColor = ((0,0,0))
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Plinko")

        self.eventManager = EventManager(self)

        self.gameBalls = []
        self.obstacles = [] 
        self.ballDelay = 20

        self.setObstacles()

        # # Collision Testing
        # self.b = Ball(self, 0, 0)
        # self.gameBalls.append(self.b)

    def setObstacles(self):
        """Creates the Set of Obstacles"""
        xSpacing = 120
        xOffset = 580
        ySpacing = 80
        width = 40
        height = 20

        # First Level design
        for i in range(2, 12):
            for j in range(1, i):
                self.obstacles.append(Obstacle(self, j*xSpacing + xOffset - (i*xSpacing/2), i*ySpacing, width, height))
        for i in range(2, 12):
            for j in range(1, i):
                self.obstacles.append(Obstacle(self, j*xSpacing + 0 - (i*xSpacing/2), i*ySpacing, width, height))
        for i in range(2, 12):
            for j in range(1, i):
                self.obstacles.append(Obstacle(self, j*xSpacing + 1160 - (i*xSpacing/2), i*ySpacing, width, height))
        # Bin seperators
        for i in range(0, 10):
            if i < 5:
                self.obstacles.append(Obstacle(self, 120*i + 60, 900, 20, 100))
            if i >= 5:
                self.obstacles.append(Obstacle(self, 120*i + 40, 900, 20, 100))


    def draw(self):
        """Draw all parts of the game"""

        # Scoreboard
        self.eventManager.draw()

        # Game Background
        # Ball start background
        pygame.draw.rect(self.win, ((255, 0, 0)), (self.width/2 - 10, 0, 20, 20))

        # Draw all game Balls
        for b in self.gameBalls:
            b.draw()

        # Draw all obstacles
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
            self.win.fill(self.bgColor)
            pygame.time.delay(10)
            key = pygame.key.get_pressed()

            # ESC
            if key[27]:
                pygame.quit()
                run = False
                return

            # Up and down arrows to change bet amount
            if key[pygame.K_UP] and self.eventManager.currentBet < self.eventManager.bank:
                self.eventManager.currentBet += 0.25
                pygame.time.delay(20)
            if key[pygame.K_DOWN] and self.eventManager.currentBet > 0:
                self.eventManager.currentBet -= 0.25
                pygame.time.delay(20)

            # ENTER for MAX BET
            if key[pygame.K_RETURN]:
                self.eventManager.currentBet = self.eventManager.bank
            # Right Shift for HALF BET
            if key[pygame.K_RSHIFT]:
                self.eventManager.currentBet = self.eventManager.bank/2
            

            # Space to drop new Game Balls
            if key[32] and delay > self.ballDelay and self.eventManager.currentBet > 0:
                # Check if it is a max bet rainbow ball
                if self.eventManager.currentBet == self.eventManager.bank:
                    rainbow = True
                else:
                    rainbow = False
                self.gameBalls.append(Ball(self, uniform(-4, 4), uniform(-1.5, 1.5), self.eventManager.currentBet, rainbow))
                self.eventManager.bank -= self.eventManager.currentBet
                self.eventManager.currentBet = 0
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