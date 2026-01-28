
from die import Dice
from face import face_icons
import random
import time
import inquirer3
import os

dice = Dice()
tries = 1
max_rolls = 3
players = [True]



def single_player():
    global index
    global dice_output
    global tries
    global max_rolls

    dice_output = []

    for i in range(dice.MAX_DICE):
        dices_values = dice.dice[i].roll_dice()
        dice_output.append(dices_values)


    GAME = True

    if tries == max_rolls:
        GAME = False

    while GAME:
        tries_remaining = max_rolls - tries


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
                reroll_animation()                
                os.system('cls' if os.name == 'nt' else 'clear') 
                if tries == max_rolls:
                    GAME = False
    
    if tries == max_rolls:
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
                single_player()
            case "No":
                print("Thank You For Playing!")
                exit()

def multiplayer():
    print("egg")


def change_keep():
    global index 
    if dice.store[index] == "Keeping":
        dice.store[index] = "Rerolling"
    else:
        dice.store[index] = "Keeping"

def reroll_animation():
    global dice_output
    global face_icons

    rerolls = 0
    reroll = True

    os.system('cls' if os.name == 'nt' else 'clear') 

    while reroll:
        print("Rerolling... ")

        if rerolls == 2:
            for i in range(len(dice_output)):
                rand = random.randint(0,4)
                print(f" {face_icons[dice_output[i] - 1]}")
                time.sleep(0.3)
        else:
            for i in range(len(dice_output)):
                rand = random.randint(0,4)
                if dice.store[i] == "Keeping":
                    print(f" {face_icons[dice_output[i] - 1]}")
                    time.sleep(0.3)

                else:
                    print(f" {face_icons[dice_output[rand] - 1]}")
                    time.sleep(0.3)

        time.sleep(1)
            
        rerolls += 1
        os.system('cls' if os.name == 'nt' else 'clear') 

        if rerolls == 3:
            reroll = False


def check_end_score():
    global dice_output
    global num_scores
    num_scores = [0,0,0,0,0,0]

    for i in range(len(dice_output)):
        if dice_output[i] == 1:
            num_scores[0] += 1
        if dice_output[i] == 2:
            num_scores[1] += 1
        if dice_output[i] == 3:
            num_scores[2] += 1
        if dice_output[i] == 4:
            num_scores[3] += 1
        if dice_output[i] == 5:
            num_scores[4] += 1
        if dice_output[i] == 6:
            num_scores[5] += 1

    if five_kind() == "Five":
        print( """_______  ___   __   __  _______    _______  _______    _______    ___   _  ___   __    _  ______   __  
|       ||   | |  | |  ||       |  |       ||       |  |   _   |  |   | | ||   | |  |  | ||      | |  | 
|    ___||   | |  |_|  ||    ___|  |   _   ||    ___|  |  |_|  |  |   |_| ||   | |   |_| ||  _    ||  | 
|   |___ |   | |       ||   |___   |  | |  ||   |___   |       |  |      _||   | |       || | |   ||  | 
|    ___||   | |       ||    ___|  |  |_|  ||    ___|  |       |  |     |_ |   | |  _    || |_|   ||__| 
|   |    |   |  |     | |   |___   |       ||   |      |   _   |  |    _  ||   | | | |   ||       | __  
|___|    |___|   |___|  |_______|  |_______||___|      |__| |__|  |___| |_||___| |_|  |__||______| |__| \n""")
    elif four_kind() == "Four":
        print(""" _______  _______  __   __  ______      _______  _______    _______    ___   _  ___   __    _  ______   __  
|       ||       ||  | |  ||    _ |    |       ||       |  |   _   |  |   | | ||   | |  |  | ||      | |  | 
|    ___||   _   ||  | |  ||   | ||    |   _   ||    ___|  |  |_|  |  |   |_| ||   | |   |_| ||  _    ||  | 
|   |___ |  | |  ||  |_|  ||   |_||_   |  | |  ||   |___   |       |  |      _||   | |       || | |   ||  | 
|    ___||  |_|  ||       ||    __  |  |  |_|  ||    ___|  |       |  |     |_ |   | |  _    || |_|   ||__| 
|   |    |       ||       ||   |  | |  |       ||   |      |   _   |  |    _  ||   | | | |   ||       | __  
|___|    |_______||_______||___|  |_|  |_______||___|      |__| |__|  |___| |_||___| |_|  |__||______| |__| \n""")
    elif full_house() == "Full":
        print( """_______  __   __  ___      ___        __   __  _______  __   __  _______  _______  __  
|       ||  | |  ||   |    |   |      |  | |  ||       ||  | |  ||       ||       ||  | 
|    ___||  | |  ||   |    |   |      |  |_|  ||   _   ||  | |  ||  _____||    ___||  | 
|   |___ |  |_|  ||   |    |   |      |       ||  | |  ||  |_|  || |_____ |   |___ |  | 
|    ___||       ||   |___ |   |___   |       ||  |_|  ||       ||_____  ||    ___||__| 
|   |    |       ||       ||       |  |   _   ||       ||       | _____| ||   |___  __  
|___|    |_______||_______||_______|  |__| |__||_______||_______||_______||_______||__| \n""" )
    elif straight() == "Straight":
        print( """_______    _______  _______  ______    _______  ___   _______  __   __  _______  __  
|   _   |  |       ||       ||    _ |  |   _   ||   | |       ||  | |  ||       ||  | 
|  |_|  |  |  _____||_     _||   | ||  |  |_|  ||   | |    ___||  |_|  ||_     _||  | 
|       |  | |_____   |   |  |   |_||_ |       ||   | |   | __ |       |  |   |  |  | 
|       |  |_____  |  |   |  |    __  ||       ||   | |   ||  ||       |  |   |  |__| 
|   _   |   _____| |  |   |  |   |  | ||   _   ||   | |   |_| ||   _   |  |   |   __  
|__| |__|  |_______|  |___|  |___|  |_||__| |__||___| |_______||__| |__|  |___|  |__| \n""") 
    elif three_kind() == "Three":
        print( """_______  __   __  ______    _______  _______    _______  _______    _______    ___   _  ___   __    _  ______   __  
|       ||  | |  ||    _ |  |       ||       |  |       ||       |  |   _   |  |   | | ||   | |  |  | ||      | |  | 
|_     _||  |_|  ||   | ||  |    ___||    ___|  |   _   ||    ___|  |  |_|  |  |   |_| ||   | |   |_| ||  _    ||  | 
  |   |  |       ||   |_||_ |   |___ |   |___   |  | |  ||   |___   |       |  |      _||   | |       || | |   ||  | 
  |   |  |       ||    __  ||    ___||    ___|  |  |_|  ||    ___|  |       |  |     |_ |   | |  _    || |_|   ||__| 
  |   |  |   _   ||   |  | ||   |___ |   |___   |       ||   |      |   _   |  |    _  ||   | | | |   ||       | __  
  |___|  |__| |__||___|  |_||_______||_______|  |_______||___|      |__| |__|  |___| |_||___| |_|  |__||______| |__|\n """ )
    elif two_pair() == "Two Pair":
        print( """_______  _     _  _______    _______  _______  ___   ______    __  
|       || | _ | ||       |  |       ||   _   ||   | |    _ |  |  | 
|_     _|| || || ||   _   |  |    _  ||  |_|  ||   | |   | ||  |  | 
  |   |  |       ||  | |  |  |   |_| ||       ||   | |   |_||_ |  | 
  |   |  |       ||  |_|  |  |    ___||       ||   | |    __  ||__| 
  |   |  |   _   ||       |  |   |    |   _   ||   | |   |  | | __  
  |___|  |__| |__||_______|  |___|    |__| |__||___| |___|  |_||__| \n""")
    elif two_kind() == "Two Kind":
        print( """_______  _     _  _______    _______  _______    _______    ___   _  ___   __    _  ______   __  
|       || | _ | ||       |  |       ||       |  |   _   |  |   | | ||   | |  |  | ||      | |  | 
|_     _|| || || ||   _   |  |   _   ||    ___|  |  |_|  |  |   |_| ||   | |   |_| ||  _    ||  |  
  |   |  |       ||  | |  |  |  | |  ||   |___   |       |  |      _||   | |       || | |   ||  | 
  |   |  |       ||  |_|  |  |  |_|  ||    ___|  |       |  |     |_ |   | |  _    || |_|   ||__| 
  |   |  |   _   ||       |  |       ||   |      |   _   |  |    _  ||   | | | |   ||       | __  
  |___|  |__| |__||_______|  |_______||___|      |__| |__|  |___| |_||___| |_|  |__||______| |__| \n""" )
    else:
        print( """ _______  _______  _______    __    _  _______    _______  _______  ___   ______    _______          _______  _______    __   __  __    _  ___      __   __  _______  ___   _  __   __  __  
|       ||       ||       |  |  |  | ||       |  |       ||   _   ||   | |    _ |  |       |        |       ||       |  |  | |  ||  |  | ||   |    |  | |  ||       ||   | | ||  | |  ||  | 
|    ___||   _   ||_     _|  |   |_| ||   _   |  |    _  ||  |_|  ||   | |   | ||  |  _____|        |  _____||   _   |  |  | |  ||   |_| ||   |    |  | |  ||       ||   |_| ||  |_|  ||  | 
|   | __ |  | |  |  |   |    |       ||  | |  |  |   |_| ||       ||   | |   |_||_ | |_____         | |_____ |  | |  |  |  |_|  ||       ||   |    |  |_|  ||       ||      _||       ||  | 
|   ||  ||  |_|  |  |   |    |  _    ||  |_|  |  |    ___||       ||   | |    __  ||_____  | ___    |_____  ||  |_|  |  |       ||  _    ||   |___ |       ||      _||     |_ |_     _||__| 
|   |_| ||       |  |   |    | | |   ||       |  |   |    |   _   ||   | |   |  | | _____| ||   |    _____| ||       |  |       || | |   ||       ||       ||     |_ |    _  |  |   |   __  
|_______||_______|  |___|    |_|  |__||_______|  |___|    |__| |__||___| |___|  |_||_______||___|   |_______||_______|  |_______||_|  |__||_______||_______||_______||___| |_|  |___|  |__| \n""" )

    
def five_kind():
    global dice_output
    global num_scores

    for i in range(len(dice_output)):
        if num_scores[i] == 5:
            return "Five"
        else:
            return None
        
def four_kind():
    global dice_output
    global num_scores

    for i in range(len(dice_output)):
        if num_scores[i] == 4:
            return "Four"
        else:
            return None
        
def full_house():
    global dice_output
    global num_scores

    if 3 in num_scores and 2 in num_scores:
        return "Full"
    else:
        None

def straight():
    global dice_output
    global num_scores

    if num_scores.count(1) == 5:
        return "Straight"
    else:
        None

def three_kind():
    global dice_output
    global num_scores

    for i in range(len(dice_output)):
        if num_scores[i] == 3:
            return "Three"
        else:
            return None

def two_pair():
    global dice_output
    global num_scores

    if num_scores.count(2) == 2:
        return "Two Pair"
    else:
        None

def two_kind():
    global dice_output
    global num_scores

    if num_scores.count(2) == 1:
        return "Two Kind"
    else:
        return None


def reroll_dice():
    for i in range(len(dice.store)):
        if dice.store[i] == "Keeping":
            pass
        else:
            dice_output[i] = dice.dice[i].roll_dice()


def display_dice():
    global dice_output

    print("Dice Rolled: ")

    for i in range(len(dice_output)):
        print(f" {face_icons[dice_output[i] - 1]}")
    # print(f"Dice Rolled:\n {face_icons[dice_output[0] - 1]} {face_icons[dice_output[1] - 1]} {face_icons[dice_output[2] - 1]} {face_icons[dice_output[3] - 1]} {face_icons[dice_output[4] - 1]} ")        


def change_rolls():
    global max_rolls

    while True:
        print(f"Current Rolls: {max_rolls}") 

        answer = prompt_menu("Would You Like to Increase or Decrease Your Amount Of Rolls?", ["Increment", "Decrement", "Done"])

        match answer:
            case "Increment":
                rolls_add()
            case "Decrement":
                rolls_subtract()
            case "Done":
                print(f"You Now Have {max_rolls} Rolls")
                time.sleep(1)
                return max_rolls

def rolls_add():
    global max_rolls

    if max_rolls <= 9:
        max_rolls += 1
    else:
        print("[!] ERROR! THE MAX NUMBER OF ROLLS IS 10! \n")


def rolls_subtract():
    global max_rolls

    if max_rolls > 1:
        max_rolls -= 1
    else:
        print("[!] ERROR! THE MINIMUM NUMBER OF ROLLS IS 1! \n")


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
    print("""╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐  ┌┬┐┬┌─┐┌─┐  ┌─┐┌─┐┬┌─┌─┐┬─┐┬
║║║├┤ │  │  │ ││││├┤    │ │ │   ││││  ├┤   ├─┘│ │├┴┐├┤ ├┬┘│
╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘  ─┴┘┴└─┘└─┘  ┴  └─┘┴ ┴└─┘┴└─o""")

    while True:


    
        answer = prompt_menu("Please Select An Option",["Exit", "Single Player", "Change Rolls", "Multiplayer"] )

        match answer:
            case "Exit":
                print("[!] Thank You For Playing!")
                exit()
            case "Single Player":
                single_player()
            case "Change Rolls":
                change_rolls()
            case "Multiplayer":
                multiplyer()

if __name__ == "__main__":
    main()