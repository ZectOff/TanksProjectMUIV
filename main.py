import pygame
from constants import WEIGHT, HEIGHT
from scene_run.menu_run import run_m
import scene_run.game_run

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WEIGHT, HEIGHT))
pygame.display.set_caption("Tanks 2000 (ReMake)")

if __name__ == "__main__":
    run_m(screen, clock)
