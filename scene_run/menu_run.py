import pygame
from constants import WEIGHT, HEIGHT, FPS, BLACK
from scene_run import scene_manager
from menu import Menu


def run(screen, clock):
    scene_manager.running = True

    menu = Menu()
    menu.append_option('Начать игру!', lambda: scene_manager.change_scene(scene_manager.game))
    menu.append_option('Параметры', lambda: print('hello world!'))
    menu.append_option('Выход', quit)

    while scene_manager.running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # Проверка на закрытие окна
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    menu.switch(-1)
                elif event.key == pygame.K_s:
                    menu.switch(1)
                elif event.key == pygame.K_SPACE:
                    menu.select()
        # Обновление
        # Визуализация, редеринг (сборка)
        screen.fill(BLACK)
        # screen.blit(main_menu_image, (0, 0))

        menu.draw(screen, WEIGHT//2 - 100, HEIGHT//2, 75)
        # Flip, после отрисовки всего переворачиваем экран
        pygame.display.flip()
    if scene_manager.next_scene:
        scene_manager.next_scene(screen, clock)


scene_manager.scene_dict[scene_manager.menu] = run
