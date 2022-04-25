import pygame


class Hearts(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Hearts, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Images/Heart.png')
        self.screen_rect = self.screen.get_rect()
        self.pos_x = self.screen_rect.left
        self.pos_y = self.screen_rect.top + 20
        self.rect = self.image.get_rect().move(self.pos_x, self.pos_y)

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.image, (self.pos_x, self.pos_y))