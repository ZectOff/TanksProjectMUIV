import pygame, main_pmoving
from maintank import MainTank


def run():
    pygame.init()
    screen = pygame.display.set_mode((1600, 800))
    pygame.display.set_caption("Tanks 2000 (ReMake)")
    bg_color = (25,25,25)
    tank = MainTank(screen)

    while True:
        main_pmoving.events(tank)
        tank.update_tank()
        screen.fill(bg_color)
        tank.own_tank_draw()
        pygame.display.flip()

if __name__ == "__main__":
    run()