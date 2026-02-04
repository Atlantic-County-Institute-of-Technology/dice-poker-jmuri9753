# Creator: Jayden Murillo
# Project: Dice Poker
# Made: 1.13.26
# Last Edit: 2.4.26

import random


class Dice:

    def __init__(self):
        self.MAX_DICE = 5
        self.dice = []  # Creates a dice object with lists inside it, like a list of dies and a list or keeping or reolling
        self.store = []

        for i in range(self.MAX_DICE):
            self.dice.append(Die())  # Adds the die and the keeping or rolling to the dice objects lists
            self.store.append("Rerolling")


class Die:

    def __init__(self):
        self.faces = 6 # Die object with 6 faces, and a value. This is for each individual dice
        self.value = 1
        

    def roll_dice(self):
        self.value = random.randint(1,self.faces)
        return self.value  # This rolls the dice and changes it value to be a number 1-6.
    
    def get_value(self):
        return self.faces # Returns number of faces but isn't used in dice poker code
