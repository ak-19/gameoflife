import pygame

from random import choice

from screen import Screen

from colors import Colors

class Board:
    def __init__(self, display) -> None:
        self.display = display

        self.X = Screen.WIDTH // Screen.CELL_SIDE
        self.Y = Screen.HEIGHT // Screen.CELL_SIDE

        self.board = []

        for _ in range(self.X):
            self.board.append([choice([0,1]) for _ in range(self.Y)])


    def get_live_nb_count(self, xx, yy):
        count = 0
        for x in range(xx - 1, xx + 2):
            for y in range(yy - 1,yy + 2):
                if [x, y] != [xx,yy]:
                    if 0 <= x < self.X and 0 <= y < self.Y and self.board[x][y]:
                        count += 1

        return count

    def update(self):
        new_board = [[0] * self.Y for _ in range(self.X)]

        for x in range(self.X):
            for y in range(self.Y):
                alive_neighbours = self.get_live_nb_count(x, y)

                if self.board[x][y]:
                    if 2 <= alive_neighbours <= 3:
                        new_board[x][y] = 1                    
                else:
                    if alive_neighbours == 3:
                        new_board[x][y] = 1


        self.board = new_board

    def draw(self):
        for x in range(self.X):
            for y in range(self.Y):
                if self.board[x][y]:
                    pygame.draw.rect(self.display, Colors.BLACK, (x * Screen.CELL_SIDE, y * Screen.CELL_SIDE, Screen.CELL_SIDE, Screen.CELL_SIDE))