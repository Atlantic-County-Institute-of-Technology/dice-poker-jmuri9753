# Author: Jayden Murillo
# Created: 1.13.26
# Last Edit: 2.4.26

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


def multiplayer(): # A menu with options for the user if in the main menu they pick multiplayer

    while True:
        answer = prompt_menu("Please Select An Option",["Players Playing", "Player Names", "Play", "Return To Main Menu"])

        match answer:
            case "Players Playing":
                players_playing()
            case "Player Names": # Gives the user options to change the number of players playing, the player names, play, and if they want to go back to the main menu
                player_naming()
            case "Play":
                play_multi()
            case "Return To Main Menu":
                return


def player_naming(): # Lets players change their player names
    global player_naming, player_names # Allows these variables to be used in this function and others.

    while True:
        current_players = 0 # Sets a placeholder variable for the # of players

        for i in range(len(players)):
            current_players += 1 # Adds to the variable depend on how many players there are

        print(f"Number of Players: {current_players}\nPlayer Names: {player_names} \n") # Displays number of players and all their names

        try: # Executes code, checks for errors
            selection = int(input("[-] Please Input Which Player's Name You Would Like To Change (Example: For Player 1 Input 1): ")) # Allows the user to input the number of the player in the ones displayed that they want to change their name

            
            if selection in range(1,len(player_names) + 1): # If they're input is in the the range of the number of players, then...
                os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code

                print(f"[-] This Is Player {selection}'s Current Name: {player_names[selection - 1]}")    
                # Displays to the user the name of the player they selected
                name_change = input(f"[-] What Would You Like To Change Player {selection}'s Name To? ")
                # Prompts the user to input what they'd like to change that players name to
                player_names[selection - 1] = name_change
                # Changes that selected played name to the name the user wants
                os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code

                print(f"[-] Player {selection}'s Name Has Been Changed To '{name_change}'. \n")
                time.sleep(1) # Delays code execution for effect
                # Tells the user that that players name has been changed
                answer = prompt_menu("Would You Like To Change Another Player's Name?", ["Yes", "No"])

                match answer:
                    case "Yes":
                        pass
                    case "No":  # If the user wants to change another name, nothing happens because this function is in a while loop so it keep looping until the loop breaks. If they dont want to then the loop breaks
                        return
                    
            elif selection == 0:
                print(f"[!] ERROR! PLAYER {selection} DOES NOT EXIST! ONLY PLAYERS 1 - {current_players} EXIST! ")     # If the user inputs 0 for the player's name they want to change, a error prints to them
                time.sleep(1.5) # Delays code execution for effect
                os.system('cls' if os.name == 'nt' else 'clear')  # Clears terminal of previous code
            else:
                print(f"[!] ERROR! PLAYER {selection} DOES NOT EXIST! ONLY PLAYERS 1 - {current_players} EXIST! ")
                # If the user inputs any number greater than the number of players then a error appears to the user
                time.sleep(1.5) # Delays code execution for effect
                os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code

        # If any of the code in the try: function breaks then it tells the user their error and lets them try again because the code is looped until broken.
        except Exception as e:
            print(f"[!] ERROR: {e} PLEASE INPUT AN INTEGER")
            time.sleep(2) # Delays code execution for effect
            os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code


def players_playing(): # Lets user change the number of player playing in multiplayer
    global players,player,player_scores, player_names, current_players # Allows these variables to be used in this function and others.

    
    while True:
        current_players = 0 # Placeholder variable for the number of players

        for i in range(len(players)):
            current_players += 1 # Adds to the varible so that it equals the number of players

        print(f"Current Players: {current_players}\nTip: If You Change The Name of Your Players And Then Change Your Number Of Players, The Names Won't Save")
        # Gives the user the number of current players, and a tip of what happens if thye change the number of players after they named them
        answer = prompt_menu("Please Select An Option",["2 Players", "3 Players", "4 Players","5 Players", "Custom Players", "Return To Main Menu"])

        match answer:
            case "2 Players":
                player = 2
                players = []
                player_scores = [] # Makes players, player_scores, and player names placeholder lists and sets a varible of players they want (player) depending on their choice in the menu
                player_names = []


                for i in range(player):
                    players.append(True)
                    player_scores.append(0) # For the number of players the user wants, the placeholder lists get added True, 0, or "Player I+1"  depending on the purpose of the list. For example if they player wants 2 players then player = [True, True] 2 Trues for the number of players they wanted.
                    player_names.append("Player " + str(i + 1))

                # for i in range(len(player_names)):
                #     if i >= player:
                #         player_names.pop() // This was to save names after number of players changed but it works but not for custom. So I just commented it out and didnt use it in my game
                #     elif i == player:
                #         pass      
            case "3 Players":
                player = 3
                players = []
                player_scores = [] # Makes players, player_scores, and player names placeholder lists and sets a varible of players they want (player) depending on their choice in the menu
                player_names = []

                for i in range(player):
                    players.append(True)
                    player_scores.append(0) # For the number of players the user wants, the placeholder lists get added True, 0, or "Player I+1"  depending on the purpose of the list. For example if they player wants 2 players then player = [True, True] 2 Trues for the number of players they wanted.
                    player_names.append("Player " + str(i + 1))

            case "4 Players":
                player = 4
                players = []
                player_scores = [] # Makes players, player_scores, and player names placeholder lists and sets a varible of players they want (player) depending on their choice in the menu
                player_names = []

                for i in range(player):
                    players.append(True)
                    player_scores.append(0) # For the number of players the user wants, the placeholder lists get added True, 0, or "Player I+1"  depending on the purpose of the list. For example if they player wants 2 players then player = [True, True] 2 Trues for the number of players they wanted.
                    player_names.append("Player " + str(i + 1))

            case "5 Players":
                player = 5
                players = []
                player_scores = [] # Makes players, player_scores, and player names placeholder lists and sets a varible of players they want (player) depending on their choice in the menu
                player_names = []

                for i in range(player):
                    players.append(True)
                    player_scores.append(0) # For the number of players the user wants, the placeholder lists get added True, 0, or "Player I+1"  depending on the purpose of the list. For example if they player wants 2 players then player = [True, True] 2 Trues for the number of players they wanted.
                    player_names.append("Player " + str(i + 1))

            case "Custom Players":
                while True:
                    current_players = 0 # Placeholder variable for the number of players

                    for i in range(len(players)):
                        current_players += 1 # Adds to the placeholder variable so that it equals the number of players

                    print(f"Current Players: {current_players}") # Displays number of players to the user
                    
                    answer = prompt_menu("Please Select What You Would Like To Do", ["Increment Players", "Decrement Players", "Return To Previous Menu"])

                    match answer:
                        case "Increment Players":
                            custom_players_increase()
                        case "Decrement Players": # Calls functions depending on what the user chooses in this custom players option. Functions if the user wants to increase or decrease players. Also it gaves the user an option to return to the previous menu when they're done.
                            custom_players_decrease()
                        case "Return To Previous Menu":
                            return
                        
            case "Return To Main Menu":
                return # Takes the user back to the main menu
                            

def custom_players_increase(): # Lets users increase their players
    global players, player, player_scores, player_names # Allows these variables to be used in this function and others.

    player = 0 # Placeholder variable for the number of players

    for i in range(len(players)):
        player += 1 # Adds to the varible so that ti equals the number of players

    if player <= 9:
        player_names = []
        players.append(True) # As long as the number of players is less than or equal to 10, it adds player names (by setting the player names list as a placeholder/empty and then depending on the number of players, a player name is added), adds player scores, and players to their lists. So it just increases the number of players as long as the current players is equal to or less than 9.
        player_scores.append(0)
        for i in range(len(players)):
            player_names.append("Player " + str(i + 1))

    else: # If the user tries to increment the number of players more than 10, than it prevents that and prints our a error to the user because the limit is 10 players.
        print("[!] ERROR! MAXIMUM NUMBER OF PLAYERS IS 10! \n")


def custom_players_decrease(): # Lets players decrease their players
    global player,players,player_scores, player_names, current_players # Allows these variables to be used in this function and others.

    player = current_players # Makes player variable the current number of players the user has

    if player > 2:
        player -= 1
        players.pop() # As long as the the player has a number of players is greater than 2 that the user wants, then it decreases the players, player_scores, and player names lists by 1. It gets rid of the last thing in the list in order to decrease the number of players.
        player_scores.pop()
        player_names.pop()

    else: # Prints out an error to the user if they try to decrease the number of players less than 2, because for multiplayer, at least 2 players are needed
        print("[!] ERROR! MINIMUM NUMBER OF PLAYERS IS 2! \n")
    

def change_keep(): # Changes the dices being kept or rerolling, letting the user change their keep or rerolling status
    global index  # Allows these variables to be used in this function and others.
    if dice.store[index] == "Keeping":
        dice.store[index] = "Rerolling" # This function depends on the index variable that is set for each individual dice and their indexes. So, depending on the index, if the user already decided to keep that specific dices value, then it reverts it back to rerolling and if it's on rerolling then it goes to keeping that vlaue for the user so that it stays even if the user rerolls.
    else:
        dice.store[index] = "Keeping"

def reroll_animation(): # Visual rerolling animation of the dices
    global dice_output, face_icons # Allows these variables to be used in this function and others.

    rerolls = 0
    reroll = True # Rerolls serves as the number of times the animation happens and reroll makes the function loop

    os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code

    while reroll:
        print("Rerolling... ") # Displays to the user that their dice is rerolling

        if rerolls == 2:
            for i in range(len(dice_output)):
                print(f" {face_icons[dice_output[i] - 1]}") # On the last reroll animation, the dices that were rolled showed to the user are the actual players dice values
                time.sleep(0.3) # Delays code execution for effect
        else:
            for i in range(len(dice_output)):
                rand = random.randint(0,4) # Sets a random variable between 0 and 4 for the dices indexes in order to make it seem like the dices are rerolling randomly
                if dice.store[i] == "Keeping": 
                    print(f" {face_icons[dice_output[i] - 1]}") # When a dices value is being kept, that displayed dice does not change since it's not being rerolled
                    time.sleep(0.3) # Delays code execution for effect

                else:
                    print(f" {face_icons[dice_output[rand] - 1]}") # Displays to the user a random dice visual to show to the user the dices being rerolled randomly
                    time.sleep(0.3) # Delays code execution for effect

        time.sleep(1) # Delays code execution for effect
            
        rerolls += 1 # When it cycles through all the dices and after showing to the user a reroll visual it adds to the number of rerolls that the animation does for effect
        os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code

        if rerolls == 3:
            reroll = False # When the functions show to the user the dice being rerolled 3 times, it breaks the loop and ends the function.


def check_end_score(): # This is to score the user based on yahtee combinations and tell them what they got
    global dice_output,num_scores,single_status, multi_status, players,player_scores # Allows these variables to be used in this function and others.
    num_scores = [0,0,0,0,0,0] # This list is for each dice value, for example, in the first index, if the user got 2 1's then that first index would each 2
    if single_status == True:
        for i in range(len(dice_output)):
            if dice_output[i] == 1:
                num_scores[0] += 1
            if dice_output[i] == 2:
                num_scores[1] += 1
            if dice_output[i] == 3:
                num_scores[2] += 1
            if dice_output[i] == 4:
                num_scores[3] += 1 # This code happens if the program is in single player mode and after they used all their rerolls. This checks each of the users final values that they got for each dice and adds 1 to their assigned index in num_scores in order to determine how much of each value they got after they finished rerolling. The total of num scores should equal 5 for the 5 dices the user had.
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
/_/   /_/ |___/\___/   \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/ \n""") # Displays to the player what they got depending on if the function, that checks for this certain combination (five of a kind), returns something. If not, then the function returns nothing and does not display to the user that they got this because they didnt.
        elif four_kind() == "Four":
            print("""   
    ____                          ____            __   _           __
   / __/___  __  _______   ____  / __/  ____ _   / /__(_)___  ____/ /
  / /_/ __ \/ / / / ___/  / __ \/ /_   / __ `/  / //_/ / __ \/ __  / 
 / __/ /_/ / /_/ / /     / /_/ / __/  / /_/ /  / ,< / / / / / /_/ /  
/_/  \____/\__,_/_/      \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/ \n""") # Displays to the player what they got depending on if the function, that checks for this certain combination (four of a kind), returns something. If not, then the function returns nothing and does not display to the user that they got this because they didnt.
        elif full_house() == "Full":
            print("""   
    ____      ____   __  __                    
   / __/_  __/ / /  / / / /___  __  __________ 
  / /_/ / / / / /  / /_/ / __ \/ / / / ___/ _ |
 / __/ /_/ / / /  / __  / /_/ / /_/ (__  )  __/
/_/  \__,_/_/_/  /_/ /_/\____/\__,_/____/\___/ \n""" ) # Displays to the player what they got depending on if the function, that checks for this certain combination (full house), returns something. If not, then the function returns nothing and does not display to the user that they got this because they didnt.
        elif straight() == "Straight":
            print("""    
    ___       _____ __             _       __    __ 
   /   |     / ___// /__________ _(_)___ _/ /_  / /_
  / /| |     \__ \/ __/ ___/ __ `/ / __ `/ __ \/ __/
 / ___ |    ___/ / /_/ /  / /_/ / / /_/ / / / / /_  
/_/  |_|   /____/\__/_/   \__,_/_/\__, /_/ /_/\__/  
                                 /____/             \n""")  # Displays to the player what they got depending on if the function, that checks for this certain combination (A straight), returns something. If not, then the function returns nothing and does not display to the user that they got this because they didnt.
        elif three_kind() == "Three":
            print("""  
  ________                            ____            __   _           __
 /_  __/ /_  ________  ___     ____  / __/  ____ _   / /__(_)___  ____/ /
  / / / __ \/ ___/ _ \/ _ \   / __ \/ /_   / __ `/  / //_/ / __ \/ __  / 
 / / / / / / /  /  __/  __/  / /_/ / __/  / /_/ /  / ,< / / / / / /_/ /  
/_/ /_/ /_/_/   \___/\___/   \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/\n """ ) # Displays to the player what they got depending on if the function, that checks for this certain combination (three of a kind), returns something. If not, then the function returns nothing and does not display to the user that they got this because they didnt.
        elif two_pair() == "Two Pair":
            print("""  
  ______                  ____        _     
 /_  __/      ______     / __ \____ _(_)____
  / / | | /| / / __ \   / /_/ / __ `/ / ___/
 / /  | |/ |/ / /_/ /  / ____/ /_/ / / /    
/_/   |__/|__/\____/  /_/    \__,_/_/_/     \n""") # Displays to the player what they got depending on if the function, that checks for this certain combination (two pair), returns something. If not, then the function returns nothing and does not display to the user that they got this because they didnt.
        elif two_kind() == "Two Kind":
            print(""" 
  ______                        ____            __   _           __
 /_  __/      ______     ____  / __/  ____ _   / /__(_)___  ____/ /
  / / | | /| / / __ \   / __ \/ /_   / __ `/  / //_/ / __ \/ __  / 
 / /  | |/ |/ / /_/ /  / /_/ / __/  / /_/ /  / ,< / / / / / /_/ /  
/_/   |__/|__/\____/   \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/ \n""" ) # Displays to the player what they got depending on if the function, that checks for this certain combination (two of a kind), returns something. If not, then the function returns nothing and does not display to the user that they got this because they didnt.
        else:
            print("""   
    __                              ____ 
   / /   ____  ________  _____   _ / __ |
  / /   / __ \/ ___/ _ \/ ___/  (_) / / /
 / /___/ /_/ (__  )  __/ /     _ / /_/ / 
/_____/\____/____/\___/_/     (_)\____/  \n""" ) # Displays to the player that they're a "loser" because they didn't get any combination
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
            if dice_output[i] == 4: # This code happens if the program is in multiplayer mode and a player used all their rerolls. This checks each of the users final values that they got for each dice and adds 1 to their assigned index in num_scores in order to determine how much of each value they got after they finished rerolling. The total of num scores should equal 5 for the 5 dices the user had.
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
/_/   /_/ |___/\___/   \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/ \n""")  # Displays to the player what they got depending on if the function, that checks for this certain combination (five of a kind), returns something. If not, then the function returns nothing and does not display to the user that they got this because they didnt. Then adds points to that players score, according to their index in player_scores, depending on what they got in the end.
            player_scores[played_players - 1] += 7
        elif four_kind() == "Four":
            print("""   
    ____                          ____            __   _           __
   / __/___  __  _______   ____  / __/  ____ _   / /__(_)___  ____/ /
  / /_/ __ \/ / / / ___/  / __ \/ /_   / __ `/  / //_/ / __ \/ __  / 
 / __/ /_/ / /_/ / /     / /_/ / __/  / /_/ /  / ,< / / / / / /_/ /  
/_/  \____/\__,_/_/      \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/ \n""") # Displays to the player what they got depending on if the function, that checks for this certain combination (four of a kind), returns something. If not, then the function returns nothing and does not display to the user that they got this because they didnt. Then adds points to that players score, according to their index in player_scores, depending on what they got in the end.
            player_scores[played_players - 1] += 6
        elif full_house() == "Full":
            print("""   
    ____      ____   __  __                    
   / __/_  __/ / /  / / / /___  __  __________ 
  / /_/ / / / / /  / /_/ / __ \/ / / / ___/ _ |
 / __/ /_/ / / /  / __  / /_/ / /_/ (__  )  __/
/_/  \__,_/_/_/  /_/ /_/\____/\__,_/____/\___/ \n""" ) # Displays to the player what they got depending on if the function, that checks for this certain combination (full house), returns something. If not, then the function returns nothing and does not display to the user that they got this because they didnt. Then adds points to that players score, according to their index in player_scores, depending on what they got in the end.
            player_scores[played_players - 1] += 5
        elif straight() == "Straight":
            print("""    
    ___       _____ __             _       __    __ 
   /   |     / ___// /__________ _(_)___ _/ /_  / /_
  / /| |     \__ \/ __/ ___/ __ `/ / __ `/ __ \/ __/
 / ___ |    ___/ / /_/ /  / /_/ / / /_/ / / / / /_  
/_/  |_|   /____/\__/_/   \__,_/_/\__, /_/ /_/\__/  
                                 /____/             \n""") # Displays to the player what they got depending on if the function, that checks for this certain combination (A straight), returns something. If not, then the function returns nothing and does not display to the user that they got this because they didnt. Then adds points to that players score, according to their index in player_scores, depending on what they got in the end.
            player_scores[played_players - 1] += 4
        elif three_kind() == "Three":
            print("""  
  ________                            ____            __   _           __
 /_  __/ /_  ________  ___     ____  / __/  ____ _   / /__(_)___  ____/ /
  / / / __ \/ ___/ _ \/ _ \   / __ \/ /_   / __ `/  / //_/ / __ \/ __  / 
 / / / / / / /  /  __/  __/  / /_/ / __/  / /_/ /  / ,< / / / / / /_/ /  
/_/ /_/ /_/_/   \___/\___/   \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/\n """ ) # Displays to the player what they got depending on if the function, that checks for this certain combination (Three of a kind), returns something. If not, then the function returns nothing and does not display to the user that they got this because they didnt. Then adds points to that players score, according to their index in player_scores, depending on what they got in the end.
            player_scores[played_players - 1] += 3
        elif two_pair() == "Two Pair":
            print("""  
  ______                  ____        _     
 /_  __/      ______     / __ \____ _(_)____
  / / | | /| / / __ \   / /_/ / __ `/ / ___/
 / /  | |/ |/ / /_/ /  / ____/ /_/ / / /    
/_/   |__/|__/\____/  /_/    \__,_/_/_/     \n""") # Displays to the player what they got depending on if the function, that checks for this certain combination (two pair), returns something. If not, then the function returns nothing and does not display to the user that they got this because they didnt. Then adds points to that players score, according to their index in player_scores, depending on what they got in the end.
            player_scores[played_players - 1] += 2
        elif two_kind() == "Two Kind":
            print(""" 
  ______                        ____            __   _           __
 /_  __/      ______     ____  / __/  ____ _   / /__(_)___  ____/ /
  / / | | /| / / __ \   / __ \/ /_   / __ `/  / //_/ / __ \/ __  / 
 / /  | |/ |/ / /_/ /  / /_/ / __/  / /_/ /  / ,< / / / / / /_/ /  
/_/   |__/|__/\____/   \____/_/     \__,_/  /_/|_/_/_/ /_/\__,_/ \n""" ) # Displays to the player what they got depending on if the function, that checks for this certain combination (two of a kind), returns something. If not, then the function returns nothing and does not display to the user that they got this because they didnt. Then adds points to that players score, according to their index in player_scores, depending on what they got in the end.
            player_scores[played_players - 1] += 1
        else:
            print("""   
    __                              ____ 
   / /   ____  ________  _____   _ / __ |
  / /   / __ \/ ___/ _ \/ ___/  (_) / / /
 / /___/ /_/ (__  )  __/ /     _ / /_/ / 
/_____/\____/____/\___/_/     (_)\____/  
                  
                  \n""" )  # Displays to the player that they're a "loser" because they didn't get any combination and does not add any score because they didnt get any combination.
    else:
        pass # If neither of the status's are true then nothing happens.

    
# The count() function checks for a value in a list and returns how many times of that value is in a list
def five_kind(): # Checks for five of a kind
    global dice_output, num_scores # Allows these variables to be used in this function and others.

    if num_scores.count(5) == 1:
        return "Five" # If there is 5 of one kind of value then this function returns something, meaning that the user got a five of a kind combination, if not, nothing happens.
    else:
        return None
        

def four_kind(): # Checks for four of a kind
    global dice_output, num_scores # Allows these variables to be used in this function and others.

    if num_scores.count(4) == 1: 
        return "Four" # If there is 4 of one kind of value then this function returns something, meaning that the user got a four of a kind combination, if not, nothing happens.
    else:
        return None
        

def full_house(): # Checks for full house
    global dice_output, num_scores # Allows these variables to be used in this function and others.

    if 3 in num_scores and 2 in num_scores:
        return "Full" # If there is 3 of one kind of value and 2 of another value then this function returns something, meaning that the user got a full house combination, if not, nothing happens.
    else:
        None


def straight(): # Checks for a straight
    global dice_output, num_scores # Allows these variables to be used in this function and others.

    if num_scores == [0,1,1,1,1,1] or num_scores == [1,1,1,1,1,0]:
        return "Straight" # If there is 5 of 5 kinds of values (only if 1 or 6 is missing from these values) then this function returns something, meaning that the user got a straight, if not, nothing happens.
    else:
        None


def three_kind(): # Checks for three of a kind
    global dice_output, num_scores # Allows these variables to be used in this function and others.

    if num_scores.count(3) == 1:
        return "Three" # If there is 3 of one kind of value then this function returns something, meaning that the user got a three of a kind combination, if not, nothing happens.
    else:
        return None


def two_pair(): # Checks for a two pair
    global dice_output, num_scores # Allows these variables to be used in this function and others.

    if num_scores.count(2) == 2:
        return "Two Pair" # If there is 2 pairs of something (2 of one kind of value equalling 2), meaning that the user got a two pair combination, if not, nothing happens.
    else:
        return None


def two_kind(): # Checks for two of a kind
    global dice_output, num_scores # Allows these variables to be used in this function and others.

    if num_scores.count(2) == 1:
        return "Two Kind" # If there is 2 of one kind of value then this function returns something, meaning that the user got a two of a kind combination, if not, nothing happens.
    else:
        return None


def reroll_dice(): # Rerolls dice
    for i in range(len(dice.store)):
        if dice.store[i] == "Keeping":
            pass # If the dices are being kept then thhey are not rerolled but if they're "rerolling" then they get rerolled.
        else:
            dice_output[i] = dice.dice[i].roll_dice()


def display_dice(): # Displays to the user a visual of their dice
    global dice_output # Allows these variables to be used in this function and others.

    print("Dice Rolled: ")
    # Displays to the user a visual of the dices and their values they rolled as they choose whether to reroll or not or keep a specific dice.
    for i in range(len(dice_output)):
        print(f" {face_icons[dice_output[i] - 1]}")


def change_rolls(): # Allows the user to change the number of rolls they want
    global max_rolls # Allows these variables to be used in this function and others.

    while True:
        print(f"Current Rolls: {max_rolls}") # Displays to the user their current maximum number of rolls/the number of rolls they have available

        answer = prompt_menu("Would You Like to Increase or Decrease Your Amount Of Rolls?", ["Increment", "Decrement", "Done"])

        match answer:
            case "Increment":
                rolls_add()
            case "Decrement": # Calls functions depending on the users choice to increase or decrease rolls
                rolls_subtract()
            case "Done":
                print(f"[-] You Now Have {max_rolls} Rolls!") # Just tell the users how many rolls they have after changing their rolls
                time.sleep(1) # Delays code execution for effect
                os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code
                return max_rolls # Changes number of rolls


def rolls_add(): # Adds/increases to the total number of user rolls
    global max_rolls # Allows these variables to be used in this function and others.

    if max_rolls <= 9:
        max_rolls += 1 # As long as the maximum rolls is less than or equal to 9 then the user can increase the number of rolls
    else:
        print("[!] ERROR! THE MAX NUMBER OF ROLLS IS 10! \n") # If the user tries to increase the more than 10, than my program screams at them because the max is 10 rolls.


def rolls_subtract(): # Subtracts/decreases to the total number of user rolls
    global max_rolls # Allows these variables to be used in this function and others.

    if max_rolls > 1:
        max_rolls -= 1 # As long as the user's max rolls is grater than 1, then the user can decrease rolls
    else:
        print("[!] ERROR! THE MINIMUM NUMBER OF ROLLS IS 1! \n") # Screams as the user if they try to decrease rolls less than 1 because the minimum is 1 roll


def prompt_menu(messages, user_choices): # Function that uses inquirer3 list to make it easy to print out a menu for the user with options.
    # messages and user_choices are parameters that we can give values when we call the function to make a menu as we want it
    menu = [
        inquirer3.List("choice", message = messages, choices = user_choices) # Makes the menu using inquirer3 list and by using the 
        # parameters we can just assign values to them in order to make the menu/inquirer3 list say what we want and give whatever options we want it to.
    ]

    answer = inquirer3.prompt(menu) # This prompts the menu so it prints it out to the user and they can use it to select what they want
    os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal to get rid of past executed code

    return answer['choice'] # This basically returns the inquirere3 list menu so we can just assign values for the parameters to make our menu say what we need and have the options we want to give


def main(): # Program main menu
    os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal of previous code

    while True:

        print("""
╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐  ┌┬┐┬┌─┐┌─┐  ┌─┐┌─┐┬┌─┌─┐┬─┐┬
║║║├┤ │  │  │ ││││├┤    │ │ │   ││││  ├┤   ├─┘│ │├┴┐├┤ ├┬┘│
╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘  ─┴┘┴└─┘└─┘  ┴  └─┘┴ ┴└─┘┴└─o""") # Welcomes the user
    
        answer = prompt_menu("Please Select An Option",["Exit", "Single Player", "Change Rolls", "Multiplayer"] )

        match answer:
            case "Exit":
                print("[!] Thank You For Playing!")
                exit()
            case "Single Player":
                single_player() # Allows the user to exit the program, play single player, change the number of rolls they have, and play multiplayer depend on what they choose and calls functions that does that.
            case "Change Rolls":
                change_rolls()
            case "Multiplayer":
                multiplayer()

if __name__ == "__main__":
    main() # If this file is the main one being run, then it calls the main menu/ the program.