from random import randint


class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = randint(1, 6)
        self._value = new_value
        return new_value


class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()


# class DiceGame:

#     def __init__(self, player, computer):
#         self.player = player
#         self.computer = computer

#     def play(self, player, computer):
#         pass

#     def play_round(self, player, computer):
#         pass

#     def check_game_over(self):
#         pass
