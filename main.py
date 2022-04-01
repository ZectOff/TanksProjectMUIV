import pygame, main_pmoving
from maintank import MainTank
from pygame.sprite import Group


def run():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("Tanks 2000 (ReMake)")
    bg_color = (25,25,25)
    tank = MainTank(screen)
    bullets = Group()
    enemies = Group()


    while True:
        delta_ms = clock.tick(60)
        main_pmoving.events(screen, tank, bullets)
        tank.update_tank(delta_ms)
        bullets.update()
        enemies.update(delta_ms)
        main_pmoving.update(bg_color, screen, tank, bullets, enemies)
        main_pmoving.create_enemies(screen, enemies)

if __name__ == "__main__":
    run()
