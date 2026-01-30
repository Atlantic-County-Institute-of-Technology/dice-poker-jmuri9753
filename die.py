# Creator: Jaydne Murillo
# Project: Dice Poker
# Made: 1.13.26
# Last Edit: 1.13.26

import random
import multiplayer


class Dice:

    def __init__(self):
        self.MAX_DICE = 5
        self.dice = []
        self.store = []
        # self.players_names = []
        # self.players_scores = []

        # for i in range(len(multiplayer.players)):
        #     self.players_scores.append(0)
        #     # self.players_names.append(multiplayer.player_names[i])


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


    # def __str__(self):
    #     return f"This is your number {self.value} and this is the face you landed on {self.faces}"



# if __name__ == '__main__':
#     test = Dice()
#     print(test.players_scores)
    # print(f"This Is what you rolled {test.roll_dice()}, This is number of faces of the dice {test.get_value()}")