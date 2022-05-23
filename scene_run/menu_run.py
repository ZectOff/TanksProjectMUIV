import pygame
from constants import FPS
from scene_run import scene_manager
from menu import Button


main_menu_image = pygame.image.load('Images/Game_menu.jpg')
bg_img = pygame.transform.scale(main_menu_image, (1520, 880))


def run_m(screen, clock):
    scene_manager.running = True

    button = Button(450, 85)

    while scene_manager.running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # Проверка на закрытие окна
            if event.type == pygame.QUIT:
                quit()
                scene_manager.running = False

        # Визуализация, редеринг (сборка)
        # screen.fill(BLACK)
        screen.blit(bg_img, (0, 0))
        button.draw(535, 350, ' Начать игру', lambda: scene_manager.change_scene(scene_manager.game))
        # button.draw(680, 460, " Параметры")
        button.draw(535, 460, '     Выход', quit)
        # menu.draw(screen, WEIGHT//2 - 100, HEIGHT//2, 75)
        # Flip, после отрисовки всего переворачиваем экран
        pygame.display.flip()
    if scene_manager.next_scene:
        scene_manager.next_scene(screen, clock)


scene_manager.scene_dict[scene_manager.menu] = run_m
print(f'{scene_manager.scene_dict} menushka')
