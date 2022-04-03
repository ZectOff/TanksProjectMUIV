import pygame, main_pmoving
from maintank import MainTank
from pygame.sprite import Group
from game_stats import Game_stats


def run():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("Tanks 2000 (ReMake)")
    bg_color = (25,25,25)
    tank = MainTank(screen)
    bullets = Group()
    enemies = Group()
    stats = Game_stats()


    while True:
        delta_ms = clock.tick(60)
        main_pmoving.events(screen, tank, bullets)
        tank.update_tank(delta_ms)
        main_pmoving.bullets_update(bullets, enemies, stats)
        main_pmoving.update_enemies(enemies, delta_ms, tank, stats, screen, bullets)
        main_pmoving.update(bg_color, screen, tank, bullets, enemies)
        main_pmoving.create_enemies(screen, enemies)

if __name__ == "__main__":
    run()