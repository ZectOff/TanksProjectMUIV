from pygame.sprite import Group
import main_pmoving
from game_stats import Game_stats
from maintank import MainTank
from scene_run import scene_manager


next_scene = None
running = True


def run(screen, clock):
    global next_scene, running
    next_scene = None
    bg_color = (25,25,25)
    tank = MainTank(screen)
    bullets = Group()
    enemies = Group()
    stats = Game_stats()

    while running:
        delta_ms = clock.tick(60)
        main_pmoving.events(screen, tank, bullets)
        tank.update_tank(delta_ms)
        main_pmoving.bullets_update(bullets, enemies, stats)
        main_pmoving.update_enemies(enemies, delta_ms, tank, stats, screen, bullets)
        main_pmoving.update(bg_color, screen, tank, bullets, enemies)
        main_pmoving.create_enemies(screen, enemies)


scene_manager.scene_dict[scene_manager.settings] = run
