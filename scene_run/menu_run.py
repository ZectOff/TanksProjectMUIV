import pygame
from constants import WEIGHT, HEIGHT, FPS, BLACK
from scene_run import scene_manager
from menu import Button

main_menu_image = pygame.image.load('images/Menu.jpg')

aa = pygame.transform.scale(main_menu_image, (1600, 900))

def run(screen, clock):
    scene_manager.running = True

    # menu = Menu()
    # menu.append_option('Начать игру!', lambda: scene_manager.change_scene(scene_manager.game))
    # menu.append_option('Параметры', lambda: print('hello world!'))
    # menu.append_option('Выход', quit)
    button = Button(220, 50)

    while scene_manager.running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # Проверка на закрытие окна
            if event.type == pygame.QUIT:
                running = False

        # Визуализация, редеринг (сборка)
        # screen.fill(BLACK)
        screen.blit(aa, (0, 0))
        button.draw(680, 400, 'Начать игру ', lambda: scene_manager.change_scene(scene_manager.game))
        button.draw(680, 460, " Параметры")
        button.draw(680, 520, '   Выход', quit)
        # menu.draw(screen, WEIGHT//2 - 100, HEIGHT//2, 75)
        # Flip, после отрисовки всего переворачиваем экран
        pygame.display.flip()
    if scene_manager.next_scene:
        scene_manager.next_scene(screen, clock)


scene_manager.scene_dict[scene_manager.menu] = run
