import sys

import pygame
import game_functions as gf

from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(settings, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(settings, screen, ship)

if __name__ == "__main__":
    run_game()
