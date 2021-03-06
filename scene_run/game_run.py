from pygame.sprite import Group
import main_pmoving
from game_stats import GameStats
from maintank import MainTank
from scene_run import scene_manager
from scores import Scores
from base import Base


def run_g(screen, clock):
    scene_manager.running = True

    bg_color = (25, 25, 25)
    lvl_1 = 'level_1_map'
    all_objects = Group()
    tank = MainTank(screen, all_objects)
    base = Base(screen, all_objects)
    bullets = Group()
    enemies = []
    blocks = Group()
    bangs = Group()
    en_bullets = Group()
    stats = GameStats()
    hearts = Group()
    main_pmoving.draw_level(screen, blocks, all_objects, enemies, tank, base, lvl_1)
    sc = Scores(screen, stats)
    main_pmoving.hearts_update(screen, stats, hearts)

    while scene_manager.running:
        delta_ms = clock.tick(60)
        main_pmoving.events(screen, clock, tank, bullets, all_objects, enemies)
        main_pmoving.update(bg_color, screen, tank, bullets, enemies,
                            blocks, bangs, sc, hearts, en_bullets, base)
        tank.update_tank(delta_ms, blocks, base)
        base.update()
        main_pmoving.update_base(screen, clock, all_objects, en_bullets, bangs, bullets,
                                 blocks, enemies, hearts, tank, stats, base)
        main_pmoving.bullets_update(screen, bullets, enemies, stats, delta_ms,
                                    all_objects, bangs, blocks, sc, base)
        main_pmoving.update_enemies(enemies, delta_ms, tank, stats, screen,
                                    bullets, all_objects, blocks, bangs, hearts,
                                    en_bullets, base, clock)
        main_pmoving.en_bullet_update(screen, all_objects, en_bullets, delta_ms,
                                      enemies, blocks, bangs)
        main_pmoving.update_blocks(blocks, bullets)
        main_pmoving.update_bangs(bangs)
    if scene_manager.next_scene:
        scene_manager.running = False
        scene_manager.next_scene(screen, clock)


scene_manager.scene_dict[scene_manager.game] = run_g
