# Author: Jayden Murillo
# Created: 1.13.26
# Last Edit: 2.2.26

from die import Dice
from face import face_icons
from multiplayer import player_names,players,player_scores
import random  # Imports packages and variables from other files that can be used
import time
import inquirer3
import os

dice = Dice() 
tries = 1
max_rolls = 3   # Sets a varible for the dice object, the player tries and max rolls, how many players have played and the status of the playing functions, depends on if the game ends or not.
played_players = 1
single_status = False
multi_status = False



def single_player(): # Single player function
    global index, dice_output, tries, max_rolls,single_status # Allows these variables to be used in this function and others.

    dice_output = [] # Placeholder list for 5 dices values

    for i in range(dice.MAX_DICE):
        dices_values = dice.dice[i].roll_dice()
        dice_output.append(dices_values) # Appends 5 dice values into the placeholder list after rolling the 5 dices

    single_status = False # Resets single player status when function is recalled

    GAME = True # Sets game status as true

    if tries == max_rolls:
        GAME = False # Stops game if the number of tries of the players roll is equal to the max rolls they have. Because once the user starts the game a roll takes place.

    while GAME:
        tries_remaining = max_rolls - tries # Variable for the number of tries the player has left


        print(f"Roll: {tries}  |  Re-roll's Remaining: {tries_remaining} \n")

        display_dice() # Displays to the user their tries, tries maining and a visual of the dice

        print(f"Dice #1: {dice_output[0]} | {dice.store[0]}\n"
            f"Dice #2: {dice_output[1]} | {dice.store[1]}\n"
            f"Dice #3: {dice_output[2]} | {dice.store[2]}\n"  # Shows the user the number they rolled and whether they are keeping that dice when rerolling
            f"Dice #4: {dice_output[3]} | {dice.store[3]}\n"
            f"Dice #5: {dice_output[4]} | {dice.store[4]}\n"
            )
    
        
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
            case "Keep Dice #4":       # Sets a global index depending on what dice the user chooses to keep or reroll and then changes that dices keep or reroll status
                index = 3
                change_keep()                
            case "Keep Dice #5":
                index = 4
                change_keep()                
            case "Reroll":
                tries += 1
                reroll_dice()
                reroll_animation()              # Add tries, rerolls the users dice but only the ones with te status of rerolling, and gives the user a visual of the dice rerolling   
                os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code
                if tries == max_rolls:
                    GAME = False # Stops the loop that allows the user to reroll and keep dice after they use their max number of rolls
    
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

        display_dice()  # Displays to the user their final rolled dice and tells them that the game ended

        print(f"Dice #1: {dice_output[0]}\n"
            f"Dice #2: {dice_output[1]}\n"
            f"Dice #3: {dice_output[2]}\n" # Also displays their final dice numbers that they got after rolling all the times they could
            f"Dice #4: {dice_output[3]}\n"
            f"Dice #5: {dice_output[4]}\n"
            )
        
        single_status = True # Switches singke player status to true because the game ended. This is for the-
        check_end_score() # -check end score function that only displays to the user what they got depending on their score for single player depending on the status
        
        answer = prompt_menu("Would You Like To Play Again?", ["Yes", "No"])

        match answer:
            case "Yes":
                for i in range(len(dice.store)):
                    dice.store[i] = "Rerolling" # Gives the user an option to play again and if so, resets the keeping or rerolling of all the dice to all rerolling and rerolls dice, resets the user tries, and then recalls the function for the user to play again.
                    dice_output[i] = dice.dice[i].roll_dice()
                tries = 1
                single_player()
            case "No":
                print("[!] Thank You For Playing!") # If the user doesn't want to, the program ends and thanks the user for playing
                exit()

def play_multi(): # Multiplayer function
    global index,dice_output,tries,max_rolls, multi_status, played_players, players, players_play
    # Allows these variables to be used in this function and others.
    dice_output = [] # Placeholder list for 5 dices values
    players_play = len(players) # This is a variable for the number of people playing
    
    for i in range(dice.MAX_DICE):
        dices_values = dice.dice[i].roll_dice()
        dice_output.append(dices_values) # Appends 5 dice values into the placeholder list after rolling the 5 dices

    multi_status = False # Resets multiplayer status when function is recalled

    GAME = True # Sets game status as true

    if tries == max_rolls:
        GAME = False # Stops game if the number of tries of the players roll is equal to the max rolls they have. Because once the user starts the game a roll takes place.

    while GAME:
        tries_remaining = max_rolls - tries # Variable for the number of tries the player has left

        print(f"{player_names[played_players - 1]}'s Turn!\n") # Displays the players name or the name saved for the player depending on the played_players variable
        print(f"Roll: {tries}  |  Re-roll's Remaining: {tries_remaining} \n")

        display_dice() # Displays to the user their tries, tries maining and a visual of the dice

        print(f"Dice #1: {dice_output[0]} | {dice.store[0]}\n"
            f"Dice #2: {dice_output[1]} | {dice.store[1]}\n"
            f"Dice #3: {dice_output[2]} | {dice.store[2]}\n"  # Shows the user the number they rolled and whether they are keeping that dice when rerolling
            f"Dice #4: {dice_output[3]} | {dice.store[3]}\n"
            f"Dice #5: {dice_output[4]} | {dice.store[4]}\n"
            )
    
        
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
            case "Keep Dice #4": # Sets a global index depending on what dice the user chooses to keep or reroll and then changes that dices keep or reroll status
                index = 3
                change_keep()                
            case "Keep Dice #5":
                index = 4
                change_keep()                
            case "Reroll":
                tries += 1
                reroll_dice()
                reroll_animation()   # Add tries, rerolls the users dice but only the ones with te status of rerolling, and gives the user a visual of the dice rerolling   
                os.system('cls' if os.name == 'nt' else 'clear')  # Clears terminal of previous code
                if tries == max_rolls:
                    GAME = False # Stops the loop that allows the user to reroll and keep dice after they use their max number of rolls
    

    if tries == max_rolls: # If the player uses all their tries then... something happens depending on if all the players played yet or not

        if played_players == players_play: # If all the players played then...
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

            display_dice() # Displays the last players rolled dice when all the players have went and says game over for all the players

            print(f"Dice #1: {dice_output[0]}\n"
                f"Dice #2: {dice_output[1]}\n"
                f"Dice #3: {dice_output[2]}\n" # Also displays the last players dice values after all the players have went because if not, then the final player wouldn't be able to see it
                f"Dice #4: {dice_output[3]}\n"
                f"Dice #5: {dice_output[4]}\n"
                )
            
            multi_status = True
            # Switches multiplayer status to true because the game ended. This is for the-
            check_end_score() # -check end score function that does things for both single player and multiplayer depending on the status

            time.sleep(5) # This delays the next code execution and this is for the final player to be able to have time to see what they got as their score and rolled dice

            os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code

            print("STANDINGS \n") # This is for the final standings of the players, basically just telling all the plays who won
            for i in range(len(players)):
                print(f"{i + 1}. {player_names[i]} - {player_scores[i]}") # Prints out a numbered list that has a players name and score for all the players. Ex: 1. Banana - 5 \n 2. Eggman - 2
            
            winning_score = max(player_scores) # Finds the highest player score from all the player scores

            score_count = player_scores.count(winning_score) # Finds out if in all the player scores, there is multiple of the highest scores

            if score_count == 1: # If there is only one player with the highest score then...

                winning_player = player_scores.index(winning_score) 
                # Finds the winning player's index and then tells the players that the winning player (their name) and what score they got to win.
                print(f"\n[!] The Winning Player is {player_names[winning_player]} With A Score of {winning_score} \n")
            
            else:
                print("\n[!] There Is No Winner! It's A Tie With Multiple Players! If You Want To Settle The Score... Play Again!\n") # if there are multiple players with the highest score then it tells all the players and they're all tied and there is no winner
            
            time.sleep(1) # Delays code execution for effect

            answer = prompt_menu("Would You Like To Play Again?", ["Yes","No"])

            match answer:
                case "Yes":
                    for i in range(len(players)):
                        player_scores[i] = 0
                    for i in range(len(dice.store)):
                        dice.store[i] = "Rerolling" # Gives the user an option to play again and if so, resets the keeping or rerolling of all the dice to all rerolling and rerolls dice, resets the user tries, resets the players that have played already, and then recalls the function for the players  to play again.
                        dice_output[i] = dice.dice[i].roll_dice()
                    tries = 1
                    played_players = 1
                    play_multi()
                case "No":
                    print("[!] Thanks For Playing!") # If the user doesn't want to, the program ends and thanks the user for playing
                    exit()
        else:
            # If all the players have not played yet but a player uses all their tries then this happens..
            print("""
████████╗██╗   ██╗██████╗ ███╗   ██╗     ██████╗ ██╗   ██╗███████╗██████╗ 
╚══██╔══╝██║   ██║██╔══██╗████╗  ██║    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
   ██║   ██║   ██║██████╔╝██╔██╗ ██║    ██║   ██║██║   ██║█████╗  ██████╔╝
   ██║   ██║   ██║██╔══██╗██║╚██╗██║    ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██║  ██║██║ ╚████║    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                                          """)

            display_dice() # Displays to the player their final rolled dice and tells them that their turn ended 

            print(f"Dice #1: {dice_output[0]}\n"
                f"Dice #2: {dice_output[1]}\n"
                f"Dice #3: {dice_output[2]}\n" # Also displays their final dice numbers that they got after rolling all the times they could
                f"Dice #4: {dice_output[3]}\n"
                f"Dice #5: {dice_output[4]}\n"
                )
    
            multi_status = True # Switches multiplayer status to true because the game ended. This is for the-
            check_end_score() # -check end score function that displays what the user got and adds to the players score for  multiplayer depending on the status
            time.sleep(5) # Delays code execution to let the player see what they got and their dice value and visual

            os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code

            for i in range(len(dice.store)):
                dice.store[i] = "Rerolling" # Resets the keeping and rolling, rerolls dice, tries, and then adds to the number of players played and then recalls the function for the next player to play
                dice_output[i] = dice.dice[i].roll_dice()
            tries = 1
            played_players += 1
            play_multi()

def multiplayer():

    while True:
        answer = prompt_menu("Please Select An Option",["Players Playing", "Player Names", "Play", "Return To Main Menu"])

        match answer:
            case "Players Playing":
                players_playing()
            case "Player Names":
                player_naming()
            case "Play":
                play_multi()
            case "Return To Main Menu":
                return

def player_naming():
    global player_naming, player_names

    while True:
        current_players = 0

        for i in range(len(players)):
            current_players += 1

        print(f"Number of Players: {current_players}\nPlayer Names: {player_names} \n")

        try:
            selection = int(input("[-] Please Input Which Player's Name You Would Like To Change (Example: For Player 1 Input 1): "))

            
            if selection in range(1,len(player_names) + 1):
                os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code

                print(f"[-] This Is Player {selection}'s Current Name: {player_names[selection - 1]}")    

                name_change = input(f"[-] What Would You Like To Change Player {selection}'s Name To? ")

                player_names[selection - 1] = name_change

                os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code

                print(f"[-] Player {selection}'s Name Has Been Changed To '{name_change}'. \n")
                time.sleep(1)

                answer = prompt_menu("Would You Like To Change Another Player's Name?", ["Yes", "No"])

                match answer:
                    case "Yes":
                        pass
                    case "No":
                        return
            elif selection == 0:
                print(f"[!] ERROR! PLAYER {selection} DOES NOT EXIST! ONLY PLAYERS 1 - {current_players} EXIST! ")    
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')  # Clears terminal of previous code
            else:
                print(f"[!] ERROR! PLAYER {selection} DOES NOT EXIST! ONLY PLAYERS 1 - {current_players} EXIST! ")

                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code


        except Exception as e:
            print(f"[!] ERROR: {e} PLEASE INPUT AN INTEGER")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code


def players_playing():
    global players,player,player_scores, player_names

    
    while True:
        current_players = 0

        for i in range(len(players)):
            current_players += 1

        print(f"Current Players: {current_players}\nTip: If You Change The Name of Your Players And Then Change Your Number Of Players, The Names Won't Save")

        answer = prompt_menu("Please Select An Option",["2 Players", "3 Players", "4 Players","5 Players", "Custom Players", "Return To Previous Menu"])

        match answer:
            case "2 Players":
                player = 2
                players = []
                player_scores = []
                player_names = []


                for i in range(player):
                    players.append(True)
                    player_scores.append(0)
                    player_names.append("Player " + str(i + 1))

                # for i in range(len(player_names)):
                #     if i >= player:
                #         player_names.pop() // This was to save names after number of players changed but it works but not for custom
                #     elif i == player:
                #         pass      
            case "3 Players":
                player = 3
                players = []
                player_scores = []
                player_names = []

                for i in range(player):
                    players.append(True)
                    player_scores.append(0)
                    player_names.append("Player " + str(i + 1))

            case "4 Players":
                player = 4
                players = []
                player_scores = []
                player_names = []

                for i in range(player):
                    players.append(True)
                    player_scores.append(0)
                    player_names.append("Player " + str(i + 1))

            case "5 Players":
                player = 5
                players = []
                player_scores = []
                player_names = []

                for i in range(player):
                    players.append(True)
                    player_scores.append(0)
                    player_names.append("Player " + str(i + 1))

            case "Custom Players":
                while True:
                    current_players = 0

                    for i in range(len(players)):
                        current_players += 1

                    print(f"Current Players: {current_players}")
                    
                    answer = prompt_menu("Please Select What You Would Like To Do", ["Increment Players", "Decrement Players", "Return To Previous Menu"])

                    match answer:
                        case "Increment Players":
                            custom_players_increase()
                        case "Decrement Players":
                            custom_players_decrease()
                        case "Return To Previous Menu":
                            return
                        
            case "Return To Previous Menu":
                return
                            

def custom_players_increase():
    global players, player, player_scores, player_names

    player = 0

    for i in range(len(players)):
        player += 1

    if player <= 9:
        player_names = []
        players.append(True)
        player_scores.append(0)
        for i in range(len(players)):
            player_names.append("Player " + str(i + 1))

    else:
        print("[!] ERROR! MAXIMUM NUMBER OF PLAYERS IS 10! \n")

def custom_players_decrease():
    global player,players,player_scores, player_names

    if range(len(players)) == 0:
        print("[!] ERROR! YOU NEED TO AT LEAST HAVE 2 PLAYERS \n")

    if player >= 2:
        player -= 1
        players.pop()
        player_scores.pop()
        player_names.pop()

    else:
        print("[!] ERROR! MINIMUM NUMBER OF PLAYERS IS 2! \n")
    

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

    os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code

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
        os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code

        if rerolls == 3:
            reroll = False


def check_end_score():
    global dice_output,num_scores,single_status, multi_status, players,player_scores
    num_scores = [0,0,0,0,0,0]
    if single_status == True:
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
            print("""   
    _______                     ____            __   _           __
   / ____(_)   _____     ____  / __/  ____ _   / /__(_)___  ____/ /
  / /_  / / | / / _ \   / __ \/ /_   / __ `/  / //_/ / __ \/ __  / 
 / __/ / /| |/ /  __/  / /_/ / __/  / /_/ /  / ,< / / / / / /_/ /  
/_/   /_/ |___/\___/   \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/ \n""")
        elif four_kind() == "Four":
            print("""   
    ____                          ____            __   _           __
   / __/___  __  _______   ____  / __/  ____ _   / /__(_)___  ____/ /
  / /_/ __ \/ / / / ___/  / __ \/ /_   / __ `/  / //_/ / __ \/ __  / 
 / __/ /_/ / /_/ / /     / /_/ / __/  / /_/ /  / ,< / / / / / /_/ /  
/_/  \____/\__,_/_/      \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/ \n""")
        elif full_house() == "Full":
            print("""   
    ____      ____   __  __                    
   / __/_  __/ / /  / / / /___  __  __________ 
  / /_/ / / / / /  / /_/ / __ \/ / / / ___/ _ |
 / __/ /_/ / / /  / __  / /_/ / /_/ (__  )  __/
/_/  \__,_/_/_/  /_/ /_/\____/\__,_/____/\___/ \n""" )
        elif straight() == "Straight":
            print("""    
    ___       _____ __             _       __    __ 
   /   |     / ___// /__________ _(_)___ _/ /_  / /_
  / /| |     \__ \/ __/ ___/ __ `/ / __ `/ __ \/ __/
 / ___ |    ___/ / /_/ /  / /_/ / / /_/ / / / / /_  
/_/  |_|   /____/\__/_/   \__,_/_/\__, /_/ /_/\__/  
                                 /____/             \n""") 
        elif three_kind() == "Three":
            print("""  
  ________                            ____            __   _           __
 /_  __/ /_  ________  ___     ____  / __/  ____ _   / /__(_)___  ____/ /
  / / / __ \/ ___/ _ \/ _ \   / __ \/ /_   / __ `/  / //_/ / __ \/ __  / 
 / / / / / / /  /  __/  __/  / /_/ / __/  / /_/ /  / ,< / / / / / /_/ /  
/_/ /_/ /_/_/   \___/\___/   \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/\n """ )
        elif two_pair() == "Two Pair":
            print("""  
  ______                  ____        _     
 /_  __/      ______     / __ \____ _(_)____
  / / | | /| / / __ \   / /_/ / __ `/ / ___/
 / /  | |/ |/ / /_/ /  / ____/ /_/ / / /    
/_/   |__/|__/\____/  /_/    \__,_/_/_/     \n""")
        elif two_kind() == "Two Kind":
            print(""" 
  ______                        ____            __   _           __
 /_  __/      ______     ____  / __/  ____ _   / /__(_)___  ____/ /
  / / | | /| / / __ \   / __ \/ /_   / __ `/  / //_/ / __ \/ __  / 
 / /  | |/ |/ / /_/ /  / /_/ / __/  / /_/ /  / ,< / / / / / /_/ /  
/_/   |__/|__/\____/   \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/ \n""" )
        else:
            print("""   
    __                              ____ 
   / /   ____  ________  _____   _ / __ |
  / /   / __ \/ ___/ _ \/ ___/  (_) / / /
 / /___/ /_/ (__  )  __/ /     _ / /_/ / 
/_____/\____/____/\___/_/     (_)\____/  \n""" )
    else:
        pass
    if multi_status == True:
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
            if five_kind() == "Five":
                print("""   
    _______                     ____            __   _           __
   / ____(_)   _____     ____  / __/  ____ _   / /__(_)___  ____/ /
  / /_  / / | / / _ \   / __ \/ /_   / __ `/  / //_/ / __ \/ __  / 
 / __/ / /| |/ /  __/  / /_/ / __/  / /_/ /  / ,< / / / / / /_/ /  
/_/   /_/ |___/\___/   \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/ \n""")
            player_scores[played_players - 1] += 7
        elif four_kind() == "Four":
            print("""   
    ____                          ____            __   _           __
   / __/___  __  _______   ____  / __/  ____ _   / /__(_)___  ____/ /
  / /_/ __ \/ / / / ___/  / __ \/ /_   / __ `/  / //_/ / __ \/ __  / 
 / __/ /_/ / /_/ / /     / /_/ / __/  / /_/ /  / ,< / / / / / /_/ /  
/_/  \____/\__,_/_/      \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/ \n""")
            player_scores[played_players - 1] += 6
        elif full_house() == "Full":
            print("""   
    ____      ____   __  __                    
   / __/_  __/ / /  / / / /___  __  __________ 
  / /_/ / / / / /  / /_/ / __ \/ / / / ___/ _ |
 / __/ /_/ / / /  / __  / /_/ / /_/ (__  )  __/
/_/  \__,_/_/_/  /_/ /_/\____/\__,_/____/\___/ \n""" )
            player_scores[played_players - 1] += 5
        elif straight() == "Straight":
            print("""    
    ___       _____ __             _       __    __ 
   /   |     / ___// /__________ _(_)___ _/ /_  / /_
  / /| |     \__ \/ __/ ___/ __ `/ / __ `/ __ \/ __/
 / ___ |    ___/ / /_/ /  / /_/ / / /_/ / / / / /_  
/_/  |_|   /____/\__/_/   \__,_/_/\__, /_/ /_/\__/  
                                 /____/             \n""")
            player_scores[played_players - 1] += 4
        elif three_kind() == "Three":
            print("""  
  ________                            ____            __   _           __
 /_  __/ /_  ________  ___     ____  / __/  ____ _   / /__(_)___  ____/ /
  / / / __ \/ ___/ _ \/ _ \   / __ \/ /_   / __ `/  / //_/ / __ \/ __  / 
 / / / / / / /  /  __/  __/  / /_/ / __/  / /_/ /  / ,< / / / / / /_/ /  
/_/ /_/ /_/_/   \___/\___/   \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/\n """ )
            player_scores[played_players - 1] += 3
        elif two_pair() == "Two Pair":
            print("""  
  ______                  ____        _     
 /_  __/      ______     / __ \____ _(_)____
  / / | | /| / / __ \   / /_/ / __ `/ / ___/
 / /  | |/ |/ / /_/ /  / ____/ /_/ / / /    
/_/   |__/|__/\____/  /_/    \__,_/_/_/     \n""")
            player_scores[played_players - 1] += 2
        elif two_kind() == "Two Kind":
            print(""" 
  ______                        ____            __   _           __
 /_  __/      ______     ____  / __/  ____ _   / /__(_)___  ____/ /
  / / | | /| / / __ \   / __ \/ /_   / __ `/  / //_/ / __ \/ __  / 
 / /  | |/ |/ / /_/ /  / /_/ / __/  / /_/ /  / ,< / / / / / /_/ /  
/_/   |__/|__/\____/   \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/ \n""" )
            player_scores[played_players - 1] += 1
        else:
            print("""   
    __                              ____ 
   / /   ____  ________  _____   _ / __ |
  / /   / __ \/ ___/ _ \/ ___/  (_) / / /
 / /___/ /_/ (__  )  __/ /     _ / /_/ / 
/_____/\____/____/\___/_/     (_)\____/  
                  
                  \n""" )
    else:
        pass

    
def five_kind():
    global dice_output
    global num_scores

    
    if num_scores.count(5) == 1:
        return "Five"
    else:
        return None
        
def four_kind():
    global dice_output
    global num_scores

    if num_scores.count(4) == 1:
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

    if num_scores == [0,1,1,1,1,1] or num_scores == [1,1,1,1,1,0]:
        return "Straight"
    else:
        None

def three_kind():
    global dice_output
    global num_scores

    if num_scores.count(3) == 1:
        return "Three"
    else:
        return None

def two_pair():
    global dice_output
    global num_scores

    if num_scores.count(2) == 2:
        return "Two Pair"
    else:
        return None

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
                print(f"[-] You Now Have {max_rolls} Rolls!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code
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
    os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code

    while True:

        print("""╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐  ┌┬┐┬┌─┐┌─┐  ┌─┐┌─┐┬┌─┌─┐┬─┐┬
║║║├┤ │  │  │ ││││├┤    │ │ │   ││││  ├┤   ├─┘│ │├┴┐├┤ ├┬┘│
╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘  ─┴┘┴└─┘└─┘  ┴  └─┘┴ ┴└─┘┴└─o""")
    
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
                multiplayer()

if __name__ == "__main__":
    main()