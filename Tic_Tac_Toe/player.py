import math
import random

class Player:
    def __init__(self,letter):
        #letter is x or o
        self.letter = letter

        #we want all player to get their next move given a game
        def get_move(self,game):
            pass

class RandomComputerPlayer(Player):
        def __init__(self,letter):
            super().__init__(letter)
        
        def get_move(self,game):
            square = random.choice(game.available_moves())
            return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        vaild_square = False
        val = None 
        while not vaild_square:
            square = input(self.letter + '\'s tuen. Input move(0-9):')
            #we are going to check that this is a correct value by trying to cast
            #in to an integer, and if its's not, then we say its invalid
            #if that spot is not available on the board, we also say its invalid

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                vaild_square = True # if these are successful, then yay!

            except ValueError:
                print('Invalid square. Try again. ')

        return val



