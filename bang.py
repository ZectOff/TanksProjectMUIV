import pygame


exp1 = pygame.image.load('Images/bull_exp_1.png')
bull_bng_1 = pygame.transform.scale(exp1, (40, 40))
exp2 = pygame.image.load('Images/bull_exp_2.png')
bull_bng_2 = pygame.transform.scale(exp2, (40, 40))
exp3 = pygame.image.load('Images/bull_exp_3.png')
bull_bng_3 = pygame.transform.scale(exp3, (40, 40))

images_bangs = [bull_bng_1, bull_bng_2, bull_bng_3]

class Bang(pygame.sprite.Sprite):
    def __init__(self, screen, pos_x, pos_y):
        super(Bang, self).__init__()
        self.screen = screen
        self.type = 'Bang'
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.frame = 0

    def update(self, bangs):
        self.frame += 0.2
        if self.frame >= 3:
            bangs.remove(self)

    def draw(self):
        image_bng = images_bangs[int(self.frame)]
        rect_bng = image_bng.get_rect(center=(self.pos_x, self.pos_y))
        self.screen.blit(image_bng, rect_bng)
