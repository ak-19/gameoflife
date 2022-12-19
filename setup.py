import pygame

from screen import Screen

class Setup:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Game of life')
        self.display = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))

    def get_display(self):
        return self.display

    def quit(self):
        pygame.quit()