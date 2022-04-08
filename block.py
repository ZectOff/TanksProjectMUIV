import pygame

class Block:
    def __init__(self, screen, all_sprites):
        all_sprites.add(self)
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.type = "block"
        self.rect = pygame.Rect(250, 650, 85, 85)
        self.hp = 1

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.screen, "red", self.rect)
        pygame.draw.rect(self.screen, "gray20", self.rect, 2)

    def damage(self, all_sprites):
        self.hp -= 1
        if self.hp <= 0:
            all_sprites.remove(self)

