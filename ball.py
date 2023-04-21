import pygame

class Ball():
    def __init__(self, game, xvel, yvel):
        self.game = game
        self.width = 15
        self.height = 15
        self.x = self.game.width/2 - self.width/2
        self.y = 0
        self.xvel = xvel
        self.yvel = yvel
        self.color = ((255,255,255))

        self.gravity = 0.05
        self.bumpDamping = 1.75

    def draw(self):
        """Draw the Game Ball"""
        pygame.draw.rect(self.game.win, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        """Move the Game Ball"""
        self.yvel += self.gravity
        self.x += self.xvel
        self.y += self.yvel

    def collide(self, objects):
        """Collide Game Ball"""
        # Collid Game Ball with Game edges
        if (self.x + self.width) >= self.game.width:
            self.x = self.game.width - self.width
            self.xvel = -self.xvel
        if (self.y + self.height) >= self.game.height:
            self.y = self.game.height - self.height
            self.yvel = -self.yvel
        if self.x <= 0:
            self.x = 0
            self.xvel = -self.xvel
        if self.y <= 0:
            self.y = 0
            self.yvel = -self.yvel

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
                    self.yvel = -self.yvel/self.bumpDamping

