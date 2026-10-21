import sys

import pygame

from settings import Settings

def run_game():

    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_height,ai_settings.screen_width))

    pygame.display.set_caption("Alien Invasion")

    bg_color = ai_settings.bg_color

    while True :

        for event in pygame.event.get() :

            if event.type == pygame.QUIT : 

                sys.exit()

        screen.fill(bg_color)

        pygame.display.flip()


run_game()