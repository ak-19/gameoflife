import pygame

from colors import Colors
from board import Board

class Game:
    def __init__(self, display):
        self.display = display
        self.run = True
        self.paused = False
        self.clock = pygame.time.Clock()
        self.board = Board(display) 

    def run_loop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type  == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run = False
                elif event.type  == pygame.KEYDOWN and self.paused and event.key == pygame.K_p:                
                    self.paused = False
                # elif event.type  == pygame.KEYDOWN:
                    
            self.board.update()

            self.display.fill(Colors.WHITE)

            self.board.draw()

            pygame.display.update()
            self.clock.tick(10)