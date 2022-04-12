import pygame
from constants import WEIGHT, HEIGHT

pygame.init()
screen = pygame.display.set_mode((WEIGHT, HEIGHT))
btn_swap = pygame.mixer.Sound('Sounds/swap_button.wav')
btn_pressed = pygame.mixer.Sound('Sounds/pressed_button.wav')
btn_font = pygame.font.SysFont('CLOUD SANS', 50)
prsd_btn_font = pygame.font.SysFont('CLOUD SANS', 50, 'bold')
# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Шрифт
ARIAL_50 = pygame.font.SysFont('CLOUD SANS', 50, 1)


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
                pygame.draw.rect(surf, (156, 11, 11), option_rect)
            surf.blit(option, option_rect)


def print_text(message, x, y, font_bold, font_type = 'CLOUD SANS', font_size = 30, font_color = (255, 255, 255)):
    font_type = pygame.font.SysFont(font_type, font_size, font_bold)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))



class Button:
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width
        self.height = height
        self.inactive_clr = (156, 11, 11)
        self.active_clr = (255, 0, 0)

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width: # курсор на кнопке
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, self.active_clr, (x, y, self.width, self.height))
                pygame.mixer.Sound.play(btn_swap)
                pygame.time.delay(300) # задержка звука

                if click[0] == 1:
                    pygame.mixer.Sound.play(btn_pressed)
                    pygame.time.delay(300)
                    if action is not None:
                        action()

        else: # курсор не на кнопке
            pygame.draw.rect(screen, self.inactive_clr, (x, y, self.width, self.height))
        print_text(message, x + 10, y + 10, False)

# доделать изменение жирность при наводки мышки на текст , так же доделать
# функцию кнопки и реализовать меню до конца





















