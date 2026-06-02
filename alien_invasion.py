import sys

import pygame
from pygame.sprite import Group
import game_functions as gf

from settings import Settings
from ship import Ship
from game_stats import GameStats


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(settings)
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(settings, screen, ship, aliens)

    while True:
        gf.check_events(settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(settings, bullets, screen, ship, aliens)
            gf.update_aliens(aliens, settings, screen, ship, stats)

        gf.update_screen(settings, screen, ship, aliens, bullets)


if __name__ == "__main__":
    run_game()
