import pygame

pygame.init()
b_Up = pygame.image.load('Images/Bullet_up.png')
UpBull = pygame.transform.scale(b_Up, (30, 30))
b_Right = pygame.image.load('Images/Bullet_right.png')
RightBull = pygame.transform.scale(b_Right, (30, 30))
b_Left = pygame.image.load('Images/Bullet_left.png')
LeftBull = pygame.transform.scale(b_Left, (30, 30))
b_Down = pygame.image.load('Images/Bullet_down.png')
DownBull = pygame.transform.scale(b_Down, (30, 30))

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, screen, all_objects):
        super(EnemyBullet, self).__init__()
        all_objects.add(self)
        self.screen = screen
        self.image = pygame.image.load("Images/Bullet_right.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect().move(200, 300)

    def update_bull(self):
        self.rect.x += 8

    def draw(self):
        self.screen.blit(self.image, self.rect)
