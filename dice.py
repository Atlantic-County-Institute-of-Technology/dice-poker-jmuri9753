
from die import Dice
from face import face_icons
import random
import time
import inquirer3
import os

dice = Dice()
dice_output = []


def play_dice():
    tries = 1
    global index

    for i in range(dice.MAX_DICE):
        dices_values = dice.dice[i].roll_dice()
        dice_output.append(dices_values)

    GAME = True

    while GAME:
        tries_remaining = 3 - tries

        print(f"Roll: {tries}  |  Re-roll's Remaining: {tries_remaining} \n")

        display_dice()

        print(f"Dice #1: {dice_output[0]}\n"
            f"Dice #2: {dice_output[1]}\n"
            f"Dice #3: {dice_output[2]}\n"
            f"Dice #4: {dice_output[3]}\n"
            f"Dice #5: {dice_output[4]}\n"
            )
        
        print(f"This Shows The Dices Your Keeping Or Rerolling: {dice.store}")

        
        answer = prompt_menu("Please Select An Option", ["Keep Dice #1","Keep Dice #2","Keep Dice #3","Keep Dice #4","Keep Dice #5", "Reroll"])

        match answer:
            case "Keep Dice #1":
                index = 0
                change_keep()                
            case "Keep Dice #2":
                index = 1
                change_keep()                
            case "Keep Dice #3":
                index = 2
                change_keep()                
            case "Keep Dice #4":
                index = 3
                change_keep()                
            case "Keep Dice #5":
                index = 4
                change_keep()                
            case "Reroll":
                tries += 1
                reroll_dice()
                print("Rerolling...")
                os.system('cls' if os.name == 'nt' else 'clear') 
                if tries == 3:
                    GAME = False
    
    if tries == 3:
        print("""  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   """)

        display_dice()

        print(f"Dice #1: {dice_output[0]}\n"
            f"Dice #2: {dice_output[1]}\n"
            f"Dice #3: {dice_output[2]}\n"
            f"Dice #4: {dice_output[3]}\n"
            f"Dice #5: {dice_output[4]}\n"
            )
        
        check_end_score()
        
        answer = prompt_menu("Would You Like To Play Again?", ["Yes", "No"])

        match answer:
            case "Yes":
                for i in range(len(dice.store)):
                    dice.store[i] = "Rerolling"
                    dice_output[i] = dice.dice[i].roll_dice()
                play_dice()
            case "No":
                print("Thank You For Playing!")
                exit()



def change_keep():
    global index 
    if dice.store[index] == "Keeping":
        dice.store[index] = "Rerolling"
    else:
        dice.store[index] = "Keeping"

def check_end_score():
    pass


def reroll_dice():
    for i in range(len(dice.store)):
        if dice.store[i] == "Keeping":
            pass
        else:
            dice_output[i] = dice.dice[i].roll_dice()





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