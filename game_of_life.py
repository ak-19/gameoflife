def game_of_life(board):
    # determine the number of rows and columns in the board
    num_rows = len(board)
    num_cols = len(board[0])

    # create a new board to store the next generation
    new_board = [[0] * num_cols for _ in range(num_rows)]

    # iterate through each cell in the board
    for row in range(num_rows):
        for col in range(num_cols):
            # count the number of live neighbors
            neighbors = count_neighbors(board, row, col)

            # apply the rules of the Game of Life
            if board[row][col] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_board[row][col] = 0
                else:
                    new_board[row][col] = 1
            else:
                if neighbors == 3:
                    new_board[row][col] = 1

    # replace the old board with the new board
    return new_board

def count_neighbors(self, row, col):
    count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r < 0 or c < 0 or r >= len(self.board) or c >= len(self.board[0]):
                continue
            if not (r == row and c == col):
                count += self.board[r][c]
    return count

# define the initial board
board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0]]

# evolve the board for 10 generations
for _ in range(10):
    board = game_of_life(board)

# print the final board
print(board)
