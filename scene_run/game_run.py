from pygame.sprite import Group
import main_pmoving
from game_stats import Game_stats
from maintank import MainTank
from scene_run import scene_manager


def run(screen, clock):
    scene_manager.running = True

    bg_color = (25, 25, 25)
    all_objetcs = Group()
    tank = MainTank(screen)
    bullets = Group()
    enemies = Group()
    stats = Game_stats()
    blocks = Group()
    main_pmoving.create_enemies(screen, enemies)
    main_pmoving.create_blocks(screen, blocks)



    while scene_manager.running:
        delta_ms = clock.tick(60)
        main_pmoving.events(screen, tank, bullets, delta_ms)
        main_pmoving.update(bg_color, screen, tank, bullets, enemies, blocks)
        tank.update_tank(delta_ms)
        main_pmoving.bullets_update(bullets, enemies, stats, delta_ms)
        main_pmoving.update_enemies(enemies, delta_ms, tank, stats, screen, bullets)
        main_pmoving.update_blocks(blocks, bullets, enemies, tank)




scene_manager.scene_dict[scene_manager.game] = run
