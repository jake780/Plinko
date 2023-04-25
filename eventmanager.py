import pygame
from random import randint


class EventManager():
    def __init__(self, game):
        self.game = game

        # Bin Colors
        self.sideBinColor = ((69, 245, 66))
        self.centerBinColor = ((219, 22, 22))
        self.binColor1 = ((26, 166, 217))
        self.binColor2 = ((26, 217, 166))
        self.binColor3 = ((217, 214, 26))
        self.binColor4 = ((227, 126, 32))
        self.binColor5 = ((169, 25, 194))

        self.greenBinMult = 5
        self.darkBlueBinMult = 0.25
        self.cyanBinMult = 0.75
        self.yellowBinMult = 0.1
        self.orangeBinMult = 10
        self.redBinMult = 25

        self.bins = []
        self.setBins()

        self.font = pygame.font.Font("freesansbold.ttf", 30)
        self.binFont = pygame.font.Font("freesansbold.ttf", 20)
        self.currentBet = 0.0
        self.bank = 10.0

    def displayText(self):
        """Displays all text elements"""
        # Bank Text
        self.prompt_text = self.font.render(f"Bank: ${float('%.2f' % self.bank):,}", True, ((255,0,0)), self.game.bgColor)
        self.prompt_rect = self.prompt_text.get_rect()
        self.prompt_rect.center = ((900, 60))
        self.game.win.blit(self.prompt_text, self.prompt_rect)

        # Bet Text
        self.prompt_text = self.font.render(f"Bet: ${float('%.2f' % self.currentBet):,}", True, ((255,0,0)), self.game.bgColor)
        self.prompt_rect = self.prompt_text.get_rect()
        self.prompt_rect.center = ((900, 20))
        self.game.win.blit(self.prompt_text, self.prompt_rect)

        # Bin Multiplier Text
        # Green Bins
        self.binText = self.binFont.render(f"x{self.greenBinMult}", True, ((0,0,0)), self.sideBinColor)
        self.binRect = self.binText.get_rect()
        self.binRect.center = ((35, 950))
        self.game.win.blit(self.binText, self.binRect)
        self.binRect.center = ((1165, 950))
        self.game.win.blit(self.binText, self.binRect)

        # Dark Blue Bins
        self.binText = self.binFont.render(f"x{self.darkBlueBinMult}", True, ((0,0,0)), self.binColor1)
        self.binRect = self.binText.get_rect()
        self.binRect.center = ((130, 950))
        self.game.win.blit(self.binText, self.binRect)
        self.binRect.center = ((1070, 950))
        self.game.win.blit(self.binText, self.binRect)

        # Cyan Bins
        self.binText = self.binFont.render(f"x{self.cyanBinMult}", True, ((0,0,0)), self.binColor2)
        self.binRect = self.binText.get_rect()
        self.binRect.center = ((250, 950))
        self.game.win.blit(self.binText, self.binRect)
        self.binRect.center = ((950, 950))
        self.game.win.blit(self.binText, self.binRect)

        # Yellow Bins
        self.binText = self.binFont.render(f"x{self.yellowBinMult}", True, ((0,0,0)), self.binColor3)
        self.binRect = self.binText.get_rect()
        self.binRect.center = ((370, 950))
        self.game.win.blit(self.binText, self.binRect)
        self.binRect.center = ((830, 950))
        self.game.win.blit(self.binText, self.binRect)

        # Orange Bins
        self.binText = self.binFont.render(f"x{self.orangeBinMult}", True, ((0,0,0)), self.binColor4)
        self.binRect = self.binText.get_rect()
        self.binRect.center = ((490, 950))
        self.game.win.blit(self.binText, self.binRect)
        self.binRect.center = ((710, 950))
        self.game.win.blit(self.binText, self.binRect)

        # Red Bin
        self.binText = self.binFont.render(f"x{self.redBinMult}", True, ((0,0,0)), self.centerBinColor)
        self.binRect = self.binText.get_rect()
        self.binRect.center = ((600, 950))
        self.game.win.blit(self.binText, self.binRect)

    def setBins(self):
        """Sets up the scoring bins"""
        # Side bins 
        self.bins.append(Bin(self.game, self.sideBinColor, 0, 900, 70, 100, 20))
        self.bins.append(Bin(self.game, self.sideBinColor, 1130, 900, 70, 100, 20))

        # 2nd bins 
        self.bins.append(Bin(self.game, self.binColor1, 70, 900, 120, 100, 10))
        self.bins.append(Bin(self.game, self.binColor1, 1010, 900, 120, 100, 10))

        # 3rd bins
        self.bins.append(Bin(self.game, self.binColor2, 190, 900, 120, 100, 5))
        self.bins.append(Bin(self.game, self.binColor2, 890, 900, 120, 100, 5))

        # 4th bins 
        self.bins.append(Bin(self.game, self.binColor3, 310, 900, 120, 100, 40))
        self.bins.append(Bin(self.game, self.binColor3, 770, 900, 120, 100, 40))

        # 5th Bins
        self.bins.append(Bin(self.game, self.binColor4, 430, 900, 120, 100, 10))
        self.bins.append(Bin(self.game, self.binColor4, 650, 900, 120, 100, 10))

        # Center Bin
        self.bins.append(Bin(self.game, self.centerBinColor, 550, 900, 100, 100, 0.25))

    def draw(self):
        """Draw game components"""

        # Draw Bins
        for b in self.bins:
            b.draw()

        # Draw Text
        self.displayText()
        
class Bin():
    def __init__(self, game, color, x, y, width, height, mult):
        self.game = game
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.mult = mult

    def draw(self):
        pygame.draw.rect(self.game.win, self.color, (self.x, self.y, self.width, self.height))

