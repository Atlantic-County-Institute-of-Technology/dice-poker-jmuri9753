
from die import Dice
from face import face_icons
from multiplayer import player_names,players,player_scores
import random
import time
import inquirer3
import os

dice = Dice()
tries = 1
max_rolls = 3
played_players = 1
single_status = False
multi_status = False



def single_player():
    global index, dice_output, tries, max_rolls,single_status

    dice_output = []

    for i in range(dice.MAX_DICE):
        dices_values = dice.dice[i].roll_dice()
        dice_output.append(dices_values)

    single_status = False

    GAME = True

    if tries == max_rolls:
        GAME = False

    while GAME:
        tries_remaining = max_rolls - tries


        print(f"Roll: {tries}  |  Re-roll's Remaining: {tries_remaining} \n")

        display_dice()

        print(f"Dice #1: {dice_output[0]} | {dice.store[0]}\n"
            f"Dice #2: {dice_output[1]} | {dice.store[1]}\n"
            f"Dice #3: {dice_output[2]} | {dice.store[2]}\n"
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
        single_status = True
        check_end_score()
        
        answer = prompt_menu("Would You Like To Play Again?", ["Yes", "No"])

        match answer:
            case "Yes":
                for i in range(len(dice.store)):
                    dice.store[i] = "Rerolling"
                    dice_output[i] = dice.dice[i].roll_dice()
                tries = 1
                single_player()
            case "No":
                print("[!] Thank You For Playing!")
                exit()

def play_multi():
    global index,dice_output,tries,max_rolls, multi_status, played_players, players, players_play

    dice_output = []
    players_play = len(players)
    
    for i in range(dice.MAX_DICE):
        dices_values = dice.dice[i].roll_dice()
        dice_output.append(dices_values)

    multi_status = False

    GAME = True

    if tries == max_rolls:
        GAME = False

    while GAME:
        tries_remaining = max_rolls - tries

        print(f"{player_names[played_players - 1]}'s Turn!\n")
        print(f"Roll: {tries}  |  Re-roll's Remaining: {tries_remaining} \n")

        display_dice()

        print(f"Dice #1: {dice_output[0]} | {dice.store[0]}\n"
            f"Dice #2: {dice_output[1]} | {dice.store[1]}\n"
            f"Dice #3: {dice_output[2]} | {dice.store[2]}\n"
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
            case "Keep Dice #4":
                index = 3
                change_keep()                
            case "Keep Dice #5":
                index = 4
                change_keep()                
            case "Reroll":
                tries += 1
                reroll_dice()
                # reroll_animation()  
                os.system('cls' if os.name == 'nt' else 'clear') 
                if tries == max_rolls:
                    GAME = False
    

    if tries == max_rolls:

        if played_players == players_play:
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
            multi_status = True
            check_end_score()

            time.sleep(4)

            os.system('cls' if os.name == 'nt' else 'clear') 

            print("STANDINGS \n")
            for i in range(len(players)):
                print(f"{i + 1}. {player_names[i]} - {player_scores[i]}")
            
            winning_score = max(player_scores)

            score_count = player_scores.count(winning_score)

            if score_count == 1:

                winning_player = player_scores.index(winning_score)

                print(f"\n[!] The Winning Player is {player_names[winning_player]} With A Score of {winning_score} \n")
            
            else:
                print("\n[!] There Is No Winner! It's A Tie With Multiple Players! If You Want To Settle The Score... Play Again!\n")
            
            time.sleep(1)

            answer = prompt_menu("Would You Like To Play Again?", ["Yes","No"])

            match answer:
                case "Yes":
                    for i in range(len(players)):
                        player_scores[i] = 0
                    for i in range(len(dice.store)):
                        dice.store[i] = "Rerolling"
                        dice_output[i] = dice.dice[i].roll_dice()
                    tries = 1
                    played_players = 1
                    play_multi()
                case "No":
                    print("[!] Thanks For Playing!")
                    exit()
        else:

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
            multi_status = True
            check_end_score()
            time.sleep(5)

            os.system('cls' if os.name == 'nt' else 'clear') 

            for i in range(len(dice.store)):
                dice.store[i] = "Rerolling"
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
                os.system('cls' if os.name == 'nt' else 'clear') 

                print(f"[-] This Is Player {selection}'s Current Name: {player_names[selection - 1]}")    

                name_change = input(f"[-] What Would You Like To Change Player {selection}'s Name To? ")

                player_names[selection - 1] = name_change

                os.system('cls' if os.name == 'nt' else 'clear') 

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
                os.system('cls' if os.name == 'nt' else 'clear')  
            else:
                print(f"[!] ERROR! PLAYER {selection} DOES NOT EXIST! ONLY PLAYERS 1 - {current_players} EXIST! ")

                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear') 


        except Exception as e:
            print(f"[!] ERROR: {e} PLEASE INPUT AN INTEGER")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear') 


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
            print( """_______  ___   __   __  _______    _______  _______    _______    ___   _  ___   __    _  ______   __  
    |       ||   | |  | |  ||       |  |       ||       |  |   _   |  |   | | ||   | |  |  | ||      | |  | 
    |    ___||   | |  |_|  ||    ___|  |   _   ||    ___|  |  |_|  |  |   |_| ||   | |   |_| ||  _    ||  | 
    |   |___ |   | |       ||   |___   |  | |  ||   |___   |       |  |      _||   | |       || | |   ||  | 
    |    ___||   | |       ||    ___|  |  |_|  ||    ___|  |       |  |     |_ |   | |  _    || |_|   ||__| 
    |   |    |   |  |     | |   |___   |       ||   |      |   _   |  |    _  ||   | | | |   ||       | __  
    |___|    |___|   |___|  |_______|  |_______||___|      |__| |__|  |___| |_||___| |_|  |__||______| |__| \n""")
            player_scores[played_players - 1] += 7
        elif four_kind() == "Four":
            print(""" _______  _______  __   __  ______      _______  _______    _______    ___   _  ___   __    _  ______   __  
    |       ||       ||  | |  ||    _ |    |       ||       |  |   _   |  |   | | ||   | |  |  | ||      | |  | 
    |    ___||   _   ||  | |  ||   | ||    |   _   ||    ___|  |  |_|  |  |   |_| ||   | |   |_| ||  _    ||  | 
    |   |___ |  | |  ||  |_|  ||   |_||_   |  | |  ||   |___   |       |  |      _||   | |       || | |   ||  | 
    |    ___||  |_|  ||       ||    __  |  |  |_|  ||    ___|  |       |  |     |_ |   | |  _    || |_|   ||__| 
    |   |    |       ||       ||   |  | |  |       ||   |      |   _   |  |    _  ||   | | | |   ||       | __  
    |___|    |_______||_______||___|  |_|  |_______||___|      |__| |__|  |___| |_||___| |_|  |__||______| |__| \n""")
            player_scores[played_players - 1] += 6
        elif full_house() == "Full":
            print( """_______  __   __  ___      ___        __   __  _______  __   __  _______  _______  __  
    |       ||  | |  ||   |    |   |      |  | |  ||       ||  | |  ||       ||       ||  | 
    |    ___||  | |  ||   |    |   |      |  |_|  ||   _   ||  | |  ||  _____||    ___||  | 
    |   |___ |  |_|  ||   |    |   |      |       ||  | |  ||  |_|  || |_____ |   |___ |  | 
    |    ___||       ||   |___ |   |___   |       ||  |_|  ||       ||_____  ||    ___||__| 
    |   |    |       ||       ||       |  |   _   ||       ||       | _____| ||   |___  __  
    |___|    |_______||_______||_______|  |__| |__||_______||_______||_______||_______||__| \n""" )
            player_scores[played_players - 1] += 5
        elif straight() == "Straight":
            print( """_______    _______  _______  ______    _______  ___   _______  __   __  _______  __  
    |   _   |  |       ||       ||    _ |  |   _   ||   | |       ||  | |  ||       ||  | 
    |  |_|  |  |  _____||_     _||   | ||  |  |_|  ||   | |    ___||  |_|  ||_     _||  | 
    |       |  | |_____   |   |  |   |_||_ |       ||   | |   | __ |       |  |   |  |  | 
    |       |  |_____  |  |   |  |    __  ||       ||   | |   ||  ||       |  |   |  |__| 
    |   _   |   _____| |  |   |  |   |  | ||   _   ||   | |   |_| ||   _   |  |   |   __  
    |__| |__|  |_______|  |___|  |___|  |_||__| |__||___| |_______||__| |__|  |___|  |__| \n""") 
            player_scores[played_players - 1] += 4
        elif three_kind() == "Three":
            print( """_______  __   __  ______    _______  _______    _______  _______    _______    ___   _  ___   __    _  ______   __  
    |       ||  | |  ||    _ |  |       ||       |  |       ||       |  |   _   |  |   | | ||   | |  |  | ||      | |  | 
    |_     _||  |_|  ||   | ||  |    ___||    ___|  |   _   ||    ___|  |  |_|  |  |   |_| ||   | |   |_| ||  _    ||  | 
    |   |  |       ||   |_||_ |   |___ |   |___   |  | |  ||   |___   |       |  |      _||   | |       || | |   ||  | 
    |   |  |       ||    __  ||    ___||    ___|  |  |_|  ||    ___|  |       |  |     |_ |   | |  _    || |_|   ||__| 
    |   |  |   _   ||   |  | ||   |___ |   |___   |       ||   |      |   _   |  |    _  ||   | | | |   ||       | __  
    |___|  |__| |__||___|  |_||_______||_______|  |_______||___|      |__| |__|  |___| |_||___| |_|  |__||______| |__|\n """ )
            player_scores[played_players - 1] += 3
        elif two_pair() == "Two Pair":
            print( """_______  _     _  _______    _______  _______  ___   ______    __  
    |       || | _ | ||       |  |       ||   _   ||   | |    _ |  |  | 
    |_     _|| || || ||   _   |  |    _  ||  |_|  ||   | |   | ||  |  | 
    |   |  |       ||  | |  |  |   |_| ||       ||   | |   |_||_ |  | 
    |   |  |       ||  |_|  |  |    ___||       ||   | |    __  ||__| 
    |   |  |   _   ||       |  |   |    |   _   ||   | |   |  | | __  
    |___|  |__| |__||_______|  |___|    |__| |__||___| |___|  |_||__| \n""")
            player_scores[played_players - 1] += 2
        elif two_kind() == "Two Kind":
            print( """_______  _     _  _______    _______  _______    _______    ___   _  ___   __    _  ______   __  
    |       || | _ | ||       |  |       ||       |  |   _   |  |   | | ||   | |  |  | ||      | |  | 
    |_     _|| || || ||   _   |  |   _   ||    ___|  |  |_|  |  |   |_| ||   | |   |_| ||  _    ||  |  
    |   |  |       ||  | |  |  |  | |  ||   |___   |       |  |      _||   | |       || | |   ||  | 
    |   |  |       ||  |_|  |  |  |_|  ||    ___|  |       |  |     |_ |   | |  _    || |_|   ||__| 
    |   |  |   _   ||       |  |       ||   |      |   _   |  |    _  ||   | | | |   ||       | __  
    |___|  |__| |__||_______|  |_______||___|      |__| |__|  |___| |_||___| |_|  |__||______| |__| \n""" )
            player_scores[played_players - 1] += 1
        else:
            print("NO COMINATIONS! THAT SUCKS!" )
    else:
        pass

    
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
                print(f"[-] You Now Have {max_rolls} Rolls!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear') 
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