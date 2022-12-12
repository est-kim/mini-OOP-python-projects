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


# class Player:

#     def __init__(self, die, counter, is_computer):
#         self.die = die
#         self.counter = counter
#         self.is_computer = is_computer

#     def increment_counter(self):
#         self.counter += 1

#     def decrement_counter(self):
#         self.counter -= 1

#     def roll_die(self):
#         pass


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
