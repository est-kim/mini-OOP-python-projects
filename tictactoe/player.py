from move import Move
from random import randint


class Player:

    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, is_human=True):
        self._is_human = is_human

        if is_human:
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER

    @property
    def is_human(self):
        return self._is_human

    @property
    def marker(self):
        return self._marker

    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    def get_human_move(self):
        while True:
            user_input = int(input("Please enter your move from 1-9: "))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                print("Please enter a valid integer between 1-9.")
        return move

    def get_computer_move(self):
        random_choice = randint(1, 9)
        move = Move(random_choice)
        print("The computer picked", move.value)
        return move
