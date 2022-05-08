import pygame

# Загрузка изображений для анимации взрыва, используя конверт_альфа для снижения нагрузки
exp1 = pygame.image.load('Images/bull_exp_1.png').convert_alpha()
bull_bng_1 = pygame.transform.scale(exp1, (60, 60))
exp2 = pygame.image.load('Images/bull_exp_2.png').convert_alpha()
bull_bng_2 = pygame.transform.scale(exp2, (60, 60))
exp3 = pygame.image.load('Images/bull_exp_3.png').convert_alpha()
bull_bng_3 = pygame.transform.scale(exp3, (60, 60))
exp4 = pygame.image.load('Images/bull_exp_4.png').convert_alpha()
bull_bng_4 = pygame.transform.scale(exp4, (60, 60))
exp5 = pygame.image.load('Images/bull_exp_5.png').convert_alpha()
bull_bng_5 = pygame.transform.scale(exp5, (60, 60))
exp6 = pygame.image.load('Images/bull_exp_6.png').convert_alpha()
bull_bng_6 = pygame.transform.scale(exp6, (60, 60))
exp7 = pygame.image.load('Images/bull_exp_7.png').convert_alpha()
bull_bng_7 = pygame.transform.scale(exp7, (60, 60))
exp8 = pygame.image.load('Images/bull_exp_8.png').convert_alpha()
bull_bng_8 = pygame.transform.scale(exp8, (60, 60))

# Список взрывов (для анимации)
images_bangs = [bull_bng_1, bull_bng_2, bull_bng_3,
                bull_bng_4, bull_bng_5, bull_bng_6,
                bull_bng_7, bull_bng_8]


class Bang(pygame.sprite.Sprite):
    def __init__(self, screen, pos_x, pos_y):
        """Инициализация взрыва"""
        super(Bang, self).__init__()
        self.screen = screen
        self.type = 'Bang'
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.frame = 0

    def update(self, bangs):
        self.frame += 0.25
        if self.frame >= 8:
            bangs.remove(self)

    def draw(self):
        image_bng = images_bangs[int(self.frame)]
        rect_bng = image_bng.get_rect(center=(self.pos_x, self.pos_y))
        self.screen.blit(image_bng, rect_bng)
