import pygame

pygame.init()

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Шрифт
ARIAL_50 = pygame.font.SysFont('CLOUD SANS', 50)


class Menu:
    def __init__(self):
        self._option_surface = []  # список поверхностей (пунктов меню)
        self._callbacks = []  # выход обратно в меню(из игры)
        self._current_option_index = 0  # выбранный пункт меню

    def append_option(self, option, callback):  # добавляем опцию(пункт меню)
        self._option_surface.append(ARIAL_50.render(option, True, WHITE))
        self._callbacks.append(callback)

    def switch(self, direction):  # переключение по пунктан меню
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surface) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surface):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                pygame.draw.rect(surf, (100, 0, 0), option_rect)
            surf.blit(option, option_rect)

