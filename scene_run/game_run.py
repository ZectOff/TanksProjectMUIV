from pygame.sprite import Group
import main_pmoving
from game_stats import Game_stats
from maintank import MainTank
from scene_run import scene_manager



def run(screen, clock):
    scene_manager.running = True

    bg_color = (25, 25, 25)
    all_objects = Group()
    bullets = Group()
    enemies = Group()
    blocks = Group()
    tank = MainTank(screen, all_objects)
    stats = Game_stats()
    main_pmoving.create_enemies(screen, enemies, all_objects)
    main_pmoving.create_blocks(screen, blocks, enemies, tank, all_objects)
    for obj in all_objects:
        print(obj.rect)



    while scene_manager.running:
        delta_ms = clock.tick(60)
        main_pmoving.events(screen, tank, bullets, all_objects)
        main_pmoving.update(bg_color, screen, tank, bullets, enemies, blocks)
        tank.update_tank(delta_ms, blocks)
        main_pmoving.bullets_update(bullets, enemies, stats, delta_ms)
        main_pmoving.update_enemies(enemies, delta_ms, tank, stats, screen, bullets, all_objects, blocks)
        main_pmoving.update_blocks(blocks, bullets, enemies, tank)


scene_manager.scene_dict[scene_manager.game] = run
