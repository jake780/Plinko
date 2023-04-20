class dot:
    def __init__(self):
         def draw(self):
        # Top Pipe
        pygame.draw.rect(win, self.color, (self.x, 0, self.width, self.height))
        pygame.draw.rect(win,((0,150,150)), (self.x-10, self.height-20, 100, 20))
        # Bottom Pipe
        pygame.draw.rect(win, self.color, (self.x, self.height+self.gap, self.width, 1000-self.height-self.gap))
        pygame.draw.rect(win,((0,150,150)), (self.x-10, self.height+self.gap, 100, 20))

 def update_score(self):
        global high_score
        self.score_text = self.font.render(f"Score: {b.score}", True, self.fgcolor, self.bgcolor)
        self.score_rect = self.score_text.get_rect()
        self.score_rect.center = ((395,25))

        self.high_text = self.font2.render(f"Highscore: {high_score}", True, self.fgcolor, self.bgcolor)
        self.high_rect = self.high_text.get_rect()
        self.high_rect.center = ((395,60))


          def prompt(self):
        self.font2 = pygame.font.Font("freesansbold.ttf", 30)
        self.prompt_text = self.font2.render(f"Press SPACE to start", True, ((255,0,0)), self.bgcolor)
        self.prompt_rect = self.prompt_text.get_rect()
        self.prompt_rect.center = ((250, 900))
        win.blit(self.prompt_text, self.prompt_rect)

        class ScoreBoard:
    def __init__(self):
        self.fgcolor = ((0,0,0))
        self.bgcolor = ((0,255,255))
        self.font = pygame.font.Font("freesansbold.ttf", 50)
        self.font2 = pygame.font.Font("freesansbold.ttf", 20)
        self.score_text = self.font.render(f"Score: {b.score}", True, self.fgcolor, self.bgcolor)
        self.score_rect = self.score_text.get_rect()
        self.high_score()