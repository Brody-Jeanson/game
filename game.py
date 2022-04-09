import time


def game():

    has_key = False
    has_sword = False
    has_torch = False
    location = 0

    print("You awaken in a cell, wearing nothing but raggedy clothes.")
    while location == 0:
        player_input = input('What would you like to do? > ')
        if player_input == 'search':
            print("You find a key. Wonder what it's for?")
            has_key = True
            time.sleep(1)

        elif player_input == 'leave' and has_key is not True:
            print('You try to leave, but the cell is locked. Try looking around.')
            time.sleep(1)
        elif player_input == 'leave' and has_key is True:
            print('You unlock the cell with the key you found and enter the next room.')
            location = 1
            time.sleep(1)
        else:
            print('Invalid input. Try "search" or "leave"')
            time.sleep(1)

    print('There are 3 rooms in front of you. Which would you like to go into? 1, 2 or 3')

    while location == 1:
        player_input = input('What would you like to do? > ')
        if player_input == '1':
            print(
                'You enter the first room and find a sword on the ground. You pick it up.')
            has_sword = True
            time.sleep(1)
        elif player_input == '1' and has_sword == True:
            print("You enter the first room, but have already found everything inside.")
            time.sleep(1)
        elif player_input == '2' and has_sword == False:
            print('You enter the second room, and see a figure holding a torch. You approach the figure, only for it to be a skeleton! It stabs you, and you succumb to your wounds. You have died.')
            time.sleep(1)
            break
        elif player_input == '2' and has_sword == True:
            print("You enter the second room, and see a figure holding a torch. You approach the figure, only for it to be a skeleton! You parry it's attack, taking it's torch with you.")
            has_torch = True
            time.sleep(1)
        elif player_input == '2' and has_torch == True:
            print("You enter the second room, but have already found everything inside.")
            time.sleep(1)
        elif player_input == '3' and has_torch == False:
            print(
                'You enter the third room, but it is too dark to see and you come back where you came from.')
            time.sleep(1)
        elif player_input == '3' and has_torch == True:
            print('You enter the third room, illuminating the darkness with your torch. You search the seemingly endless hallways for a while, and find the exit! Congratulations, you have won!')
            time.sleep(1)
            break
        else:
            print('Invalid input. Try entering a room using "1", "2", or "3"')
            time.sleep(1)


game()
