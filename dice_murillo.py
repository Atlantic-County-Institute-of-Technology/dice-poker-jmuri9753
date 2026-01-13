# Creator: Jaydne Murillo
# Project: Dice Poker
# Made: 1.13.26
# Last Edit: 1.13.26

import random

class Die:
    # NUM_OF_FACES = 6
    # DEFAULT_ROLL = 1
    random_value = random.randint(1,6)

    def __init__(self, faces, value):
        self.faces = faces
        self.value = value
        # self.faces = self.NUM_OF_FACES
        # self.value = self.DEFAULT_ROLL

    def roll_dice(self):
        self.value = self.random_value
        return self.value
    
    def get_value(self):
        face_value = random.randint(1,6)
        self.faces = face_value
        return self.faces


    def __str__(self):
        return f"This is your number {self.value} and this is the face you landed on {self.faces}"



if __name__ == '__main__':
    test = Die(5,5)
    print(f"This Is what you rolled {test.roll_dice()}, This is the face you landed on {test.get_value()}")