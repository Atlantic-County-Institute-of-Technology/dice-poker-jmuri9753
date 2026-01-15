
from die import Dice
from face import face_icons
import random
import time
import inquirer3
import os

dice = Dice()
dice_output = []

for i in range(dice.MAX_DICE):
    dices_values = dice.dice[i].roll_dice()
    dice_output.append(dices_values)


def play_dice():
    tries = 1
    tries_remaining = 3 - tries

    print(f"Roll: {tries}  |  Re-roll's Remaining: {tries_remaining} \n")

    display_dice()

    print(f"Dice #1: {dice_output[0]}\n"
          f"Dice #2: {dice_output[1]}\n"
          f"Dice #3: {dice_output[2]}\n"
          f"Dice #4: {dice_output[3]}\n"
          f"Dice #5: {dice_output[4]}\n"
          )

def display_dice():
    global dice_output
    print(f"Dice Rolled:\n {face_icons[dice_output[0] - 1]} {face_icons[dice_output[1] - 1]} {face_icons[dice_output[2] - 1]} {face_icons[dice_output[3] - 1]} {face_icons[dice_output[4] - 1]} ")






def prompt_menu(messages, user_choices): # Function that uses inquirer3 list to make it easy to print out a menu for the user with options.
    # messages and user_choices are parameters that we can give values when we call the function to make a menu as we want it
    menu = [
        inquirer3.List("choice", message = messages, choices = user_choices) # Makes the menu using inquirer3 list and by using the 
        # parameters we can just assign values to them in order to make the menu/inquirer3 list say what we want and give whatever options we want it to.
    ]

    answer = inquirer3.prompt(menu) # This prompts the menu so it prints it out to the user and they can use it to select what they want
    os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code

    return answer['choice'] # This basically returns the inquirere3 list menu so we can just assign values for the parameters to make our menu say what we need and have the options we want to give


def main():
    print("""     ___     __  __      ___   _____     __   __  ___    __  __      ___ __  
|  ||__ |   /  `/  \|\/||__     |/  \   |  \|/  `|__    |__)/  \|__/|__ |__) 
|/\||___|___\__,\__/|  ||___    |\__/   |__/|\__,|___   |   \__/|  \|___|  \ 
                                                                             """)
    
    answer = prompt_menu("Please Select An Option",["Exit", "Play Game"] )

    match answer:
        case "Exit":
            print("[!] Thank Your For Playing!")
            exit()
        case "Play Game":
            play_dice()

if __name__ == "__main__":
    main()