from pygame.sprite import Group
import main_pmoving
from game_stats import Game_stats
from maintank import MainTank
from scene_run import scene_manager
from bang import Bang
from enemy_bullet import EnemyBullet
from scores import Scores
from hearts import Hearts


def run(screen, clock):
    scene_manager.running = True

    bg_color = (25, 25, 25)
    all_objects = Group()
    bullets = Group()
    enemies = Group()
    blocks = Group()
    bangs = Group()
    tank = MainTank(screen, all_objects)
    stats = Game_stats()
    enemy_bullet = EnemyBullet(screen, all_objects) # Будущая пуля врагов
    main_pmoving.draw_level(screen, blocks, all_objects, enemies, tank)
    sc = Scores(screen, stats)
    hrt = Hearts(screen)


    while scene_manager.running:
        delta_ms = clock.tick(60)
        main_pmoving.events(screen, tank, bullets, all_objects)
        main_pmoving.update(bg_color, screen, tank, bullets, enemies,
                            blocks, bangs, stats, sc, hrt)
        tank.update_tank(delta_ms, blocks)
        main_pmoving.bullets_update(screen, bullets, enemies, stats, delta_ms,
                                    all_objects, bangs, blocks, sc)
        main_pmoving.update_enemies(enemies, delta_ms, tank, stats, screen,
                                    bullets, all_objects, blocks, bangs)
        main_pmoving.update_blocks(screen, all_objects, blocks, bullets, bangs)
        main_pmoving.update_bangs(bangs)



scene_manager.scene_dict[scene_manager.game] = run
