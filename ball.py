import pygame
from random import uniform, randint

class Ball():
    def __init__(self, game, xvel, yvel, betValue, rainbow):
        self.game = game
        self.width = 15
        self.height = 15
        self.x = self.game.width/2 - self.width/2
        self.y = 0
        self.xvel = xvel
        self.yvel = yvel
        self.color = ((255,255,255))

        self.gravity = 0.05
        self.bumpDamping = 1.5
        self.wallModifier = 2

        self.betValue = betValue

        self.rainbow = rainbow

    def draw(self):
        """Draw the Game Ball"""
        if self.rainbow:
            pygame.draw.rect(self.game.win, ((randint(0,255), randint(0, 255), randint(150, 255))), (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(self.game.win, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        """Move the Game Ball"""
        self.yvel += self.gravity
        self.x += self.xvel
        self.y += self.yvel

        # Max Velocity
        if self.xvel > 25:
            self.xvel = 25
        if self.yvel > 25:
            self.yvel = 25

    def collide(self, objects):
        """Collide Game Ball"""
        # Collide Game Ball with Game edges
        # Right wall bounce
        if (self.x + self.width) >= self.game.width:
            self.x = self.game.width - self.width
            self.xvel = -self.xvel * self.wallModifier
        # Bottom wall
        if (self.y + self.height) >= self.game.height:
            self.y = self.game.height - self.height
            # Multiplier bins
            # Green bins
            if ((self.x >= 0) and (self.x + self.width) < 70) or ((self.x > 1130) and self.x <= 1200):
                self.game.eventManager.bank += self.betValue * self.game.eventManager.greenBinMult
                self.game.gameBalls.remove(self)
            # Dark blue bins
            if ((self.x > 70) and (self.x + self.width) <= 190) or ((self.x > 1010) and self.x <= 1130):
                self.game.eventManager.bank += self.betValue * self.game.eventManager.darkBlueBinMult
                self.game.gameBalls.remove(self)
            # Cyan Bins
            if ((self.x > 190) and (self.x + self.width) <= 310) or ((self.x > 890) and self.x <= 1010):
                self.game.eventManager.bank += self.betValue * self.game.eventManager.cyanBinMult
                self.game.gameBalls.remove(self)
            # Yellow Bins
            if ((self.x > 310) and (self.x + self.width) <= 430) or ((self.x > 770) and self.x <= 890):
                self.game.eventManager.bank += self.betValue * self.game.eventManager.yellowBinMult
                self.game.gameBalls.remove(self)
            # Orange Bins
            if ((self.x > 430) and (self.x + self.width) <= 550) or ((self.x > 650) and self.x <= 770):
                self.game.eventManager.bank += self.betValue * self.game.eventManager.orangeBinMult
                self.game.gameBalls.remove(self)
            # Red bin
            if ((self.x > 550) and (self.x + self.width) <= 650):
                self.game.eventManager.bank += self.betValue * self.game.eventManager.redBinMult
                self.game.gameBalls.remove(self)
        # Left Wall
        if self.x <= 0:
            self.x = 0
            self.xvel = -self.xvel * self.wallModifier
        # Top Wall
        if self.y <= 0:
            self.y = 0
            self.yvel = -self.yvel * self.wallModifier

        # Collide Game Ball with Objects
        for o in objects:
            # If collide
            if ((self.x + self.width) >= o.x) and (self.x <= (o.x + o.width)) and ((self.y + self.height) >= o.y) and (self.y <= (o.y + o.height)):
                # Move ball back to prev position
                self.x -= self.xvel
                self.y -= self.yvel
                # Left side hit
                if ((self.x + self.width) <= o.x) and ((self.y + self.height) >= o.y) and (self.y <= (o.y + o.height)):
                    self.xvel = -self.xvel/self.bumpDamping
                # Right side hit
                elif (self.x >= (o.x + o.width)) and ((self.y + self.height) >= o.y) and (self.y <= (o.y + o.height)):
                    self.xvel = -self.xvel/self.bumpDamping
                # Top or Bottom hit
                else:
                    # If ball is stuck
                    if ((self.yvel < 0.5) and (self.xvel < 0.5)) and (self.y < o.y):
                        self.yvel = uniform(-2, -1)
                        self.xvel = uniform(-1, 1)
                    else:
                        self.yvel = -self.yvel/self.bumpDamping

