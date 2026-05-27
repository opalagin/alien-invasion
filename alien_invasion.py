import sys

import pygame
from pygame.sprite import Group
import game_functions as gf

from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(settings, screen)
    bullets = Group()

    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(settings, screen, ship, bullets)


if __name__ == "__main__":
    run_game()
