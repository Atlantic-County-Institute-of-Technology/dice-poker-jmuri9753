# Creator: Jayden Murillo
# Project: Dice Poker
# Made: 1.13.26
# Last Edit: 2.1.26

import random


class Dice:

    def __init__(self):
        self.MAX_DICE = 5
        self.dice = []
        self.store = []

        for i in range(self.MAX_DICE):
            self.dice.append(Die())
            self.store.append("Rerolling")


class Die:
    

    def __init__(self):
        self.faces = 6
        self.value = 1
        

    def roll_dice(self):
        self.value = random.randint(1,self.faces)
        return self.value
    
    def get_value(self):
        return self.faces
