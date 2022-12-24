import pygame

from colors import Colors

from screen import Screen

from board import Board

class Game:

    def __init__(self, display) -> None:
        self.display = display
        self.run = True
        self.clock = pygame.time.Clock()
        self.fps = 10
        self.board = Board(display)

    def run_game_loop(self): 

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.run = False

            self.board.update()

            self.display.fill(Colors.WHITE)

            self.board.draw()

            pygame.display.update()
            
            self.clock.tick(self.fps)