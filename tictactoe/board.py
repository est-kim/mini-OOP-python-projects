from move import Move
from player import Player


class Board:

    EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]

    def print_board(self):
        print("\nPositions:")
        self.print_board_with_positions()

        print("\nBoard:")
        for row in self.game_board:
            print("|", end="")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end="")
                else:
                    print(f" {column} |", end="")
            print()
        print()

    def print_board_with_positions(self):
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")

    def submit_move(self, player, move):
        row = move.get_row()
        col = move.get_col()
        value = self.game_board[row][col]

        if value == Board.EMPTY_CELL:
            self.game_board[row][col] = player.marker
        else:
            print("This position is already taken. Please enter another one.")

    def check_is_game_over(self, player, last_move):
        return ((self.check_row(player, last_move))
                or (self.check_col(player, last_move))
                or (self.check_diagonal(player))
                or (self.check_diagonal_two(player)))

    def check_row(self, player, last_move):
        row_index = last_move.get_row()
        board_row = self.game_board[row_index]

        return board_row.count(player.marker) == 3

    def check_col(self, player, last_move):
        markers_count = 0
        col_index = last_move.get_col()

        for i in range(3):
            if self.game_board[i][col_index] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_diagonal(self, player):
        markers_count = 0
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_diagonal_two(self, player):
        markers_count = 0
        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_is_tie(self):
        empty_counter = 0

        for row in self.game_board:
            empty_counter += row.count(Board.EMPTY_CELL) # check how many cells are 0 in list

        return empty_counter == 0

    def reset_board(self):
        self.game_board = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]


#testing submit_move function and check_is_game_over
# board = Board()
# player = Player()

# move1 = player.get_move()
# move2 = player.get_move()
# move3 = player.get_move()

# board.print_board()

# board.submit_move(player, move1)
# board.submit_move(player, move2)
# board.submit_move(player, move3)

# board.print_board()
# print(board.check_is_game_over(player, move3))
