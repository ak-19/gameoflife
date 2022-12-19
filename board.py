import pygame
from random import choice
from colors import Colors
from screen import Screen

class Board:
    def __init__(self, display):
        self.display = display        
        self.board = []        
        for r in range(Screen.WIDTH // Screen.BOX):
            self.board.append([choice([0,1]) for _ in range(Screen.HEIGHT // Screen.BOX)])

    def update(self):
        num_rows = len(self.board)
        num_cols = len(self.board[0])
        new_board = [[0] * num_cols for _ in range(num_rows)]
        for row in range(num_rows):
            for col in range(num_cols):
                neighbors = self.count_neighbors(row, col)
                if self.board[row][col] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_board[row][col] = 0
                    else:
                        new_board[row][col] = 1
                else:
                    if neighbors == 3:
                        new_board[row][col] = 1
        self.board = new_board        

    def count_neighbors(self, row, col):
        count = 0
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r < 0 or c < 0 or r >= len(self.board) or c >= len(self.board[0]):
                    continue
                if [r, c] != [row, col]:
                    count += self.board[r][c]
        return count

    def draw(self):
        rows = len(self.board)
        cols = len(self.board[0])
        for r in range(rows):
            for c in range(cols):
                if self.board[r][c]:
                    pygame.draw.rect(self.display, Colors.BLACK, (r*Screen.BOX, c*Screen.BOX, Screen.BOX, Screen.BOX))