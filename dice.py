
from die import Dice

dice = Dice()
dice_output = []

for i in range(dice.MAX_DICE):
    dices_values = str(dice.dice[i].roll_dice())
    dice_output.append(dices_values)

print(dice_output)
