"""A simple SUD adventure

roll_die: takes a number of rolls and sides of a dice and returns the sum
print_message: Prints a message based on player input and location
item_on_ground_message: Prints a message about an item on the ground
scenario_message: Prints a message about the environment
user_input: Takes user input and returns it when a correct input is entered
have_item_check: checks if the user has the item they are trying to use
adjacent_door_check: if user tries to interact with a door, checks if the door is adjacent
help_menu: Prints a help menu with all keywords usable by player
take_item_check: if user inputs to take an item checks if it is on the players tile
collision_check: checks if there is a wall where the player is trying to move

"""

# Tommy May
# A01086435
# 2019 March 05

import random
import json
import character
import map
import monster


def roll_die(number_of_rolls, number_of_sides):
    """ Rolls a die a specified number of times and adds them up

    PARAM number_of_rolls an int
    PARAM number_of_sides an int
    PRECONDITION number_of_rolls must be a positive int
    PRECONDITION number_of_sides must be a positive int
    POSTCONDITION the sum of the rolled die will be added up
    RETURN the sum of the rolled die added together
    """
    if number_of_sides <= 0:
        return 0

    random_total = 0
    # Calculate sum of rolled dice
    for i in range(number_of_rolls):
        random_total += random.randint(1, number_of_sides)
    return random_total


def print_message(player_input):
    """Prints messages based on player input and location on map

    PARAM player a correctly formatted dictionary
    PARAM dungeon_map a list of lists
    PARAM player_input a string
    PRECONDITION player is a correctly formatted dictionary
    PRECONDITION dungeon_map is a list with lists with 12 elements each
    PRECONDITION player_input is a correct input string
    POSTCONDITION A message is printed based on input given
    """
    # contains keywords for movement
    moved_list = ['north', 'east', 'south', 'west']
    # play a message for user taking something
    if player_input[0:4] == 'take':
        # print a message if you take treasure
        if player_input == 'take treasure':
            print('you accomplish your goal and retrieved the treasure')
            print('now you may roam this town killing monsters as you wish')
        # print a message about the item you picked up
        else:
            print('you pick up', player_input[5:])
    # print a message if user uses sword
    elif player_input == 'use sword':
        print('You swing your sword around looking really dumb')
    # print a message and heal user to 10hp if user uses bread
    elif player_input == 'use bread':
        print('You eat the bread and return to full HP')
        character.set_hitpoints(10)
    # print that you open the door if input is open door
    elif player_input == 'open door':
        print('you open the door')
    # print that you unlocked the door if input is unlock door
    elif player_input == 'unlock door':
        print('you unlock the door')
    # play a message about your surroundings if you move
    if player_input in moved_list:
        scenario_message()
    # play a message about what is on the ground if you walk on it
    item_on_ground_message()


def item_on_ground_message():
    """Prints what item is on the ground when moved onto

    PARAM player a correctly formatted dictionary
    PARAM dungeon_map a list of lists
    PRECONDITION player is a correctly formatted dictionary
    PRECONDITION dungeon_map is a list with lists with 12 elements each
    POSTCONDITION prints a message about what item is on the ground is printed
    """
    dungeon_map = map.get_map()
    player = character.get_character_info()
    # prints a message if player is on a key
    if dungeon_map[player['row']][player['column']] == ' K ':
        print('You see a key on a table')
    # prints a message if player is on a sword
    elif dungeon_map[player['row']][player['column']] == ' S ':
        print('There is a sword propped up against the wall, it seems to be in good condition')
    # prints a message if player is on bread
    elif dungeon_map[player['row']][player['column']] == ' B ':
        print('You see some bread left on a bench, it looks edible')
    # prints a message if player is on treasure
    elif dungeon_map[player['row']][player['column']] == ' C ':
        print('You find the treasure you were searching for')


def scenario_message():
    """Prints a message about the environment

    PARAM player a correctly formatted dictionary
    PARAM dungeon_map a list of lists
    PRECONDITION player is a correctly formatted dictionary
    PRECONDITION dungeon_map is a list with lists with 12 elements each
    POSTCONDITION prints a message about the environment the player is on
    """
    dungeon_map = map.get_map()
    player = character.get_character_info()
    if player['row'] == 9 and player['column'] == 4:
        print('You come across a church that is still in good condition')
        print('There is a door that seems to be unlocked')
    elif player['row'] == 7 and player['column'] == 4:
        print('There is a run down shack to your left')
    elif dungeon_map[player['row']][player['column']] == '| |':
        print('You walk over the stone bridge')
    elif dungeon_map[player['row']][player['column'] - 1] == ' L ':
        print('You reach the treasury but it looks like the door is locked')
        print('You will need some sort of key to get through')
    elif dungeon_map[player['row']][player['column']] == '   ':
        print('You are on a dirt path')
    elif dungeon_map[player['row']][player['column']] == '...':
        print('The wooden boards creak underneath your feet')
    elif dungeon_map[player['row']][player['column']] == ':::':
        print('You are on a grassy field')
    elif dungeon_map[player['row']][player['column']] == '###':
        print('You walk over the cold stone floor of the church')
    elif dungeon_map[player['row']][player['column']] == '"""':
        print('You are in the treasury')


def user_input():
    """Takes user input and returns it when a correct input is entered

    PARAM player a correctly formatted dictionary
    PARAM dungeon_map a list of lists
    PRECONDITION player is a correctly formatted dictionary
    PRECONDITION dungeon_map is a list with lists with 12 elements each
    POSTCONDITION prints error messages until a correct input is entered
    RETURN user input once it is a correct input
    """
    error = True
    dungeon_map = map.get_map()
    while error:
        player_input = input()
        if player_input == 'east' or player_input == 'west' or player_input == 'north' or player_input == 'south':
            error = collision_check(player_input)
        elif player_input[0:4] == 'take':
            error = take_item_check(player_input)
        elif player_input[-4:] == 'door':
            error = adjacent_door_check(player_input)
        elif player_input == 'help':
            help_menu()
        elif player_input[0:3] == 'use':
            error = dont_have_item_check(player_input)
        elif player_input == 'quit':
            error = False
        else:
            print('i dont understand')
    return player_input


def dont_have_item_check(player_input):
    """checks if the user has the item they are trying to use

    PARAM player_input a string
    PARAM player a dictionary
    PRECONDITION player_input is a string
    PRECONDITION player is a correctly formatted dictionary
    RETURN True if player doesnt have item, False if they do
    """
    player = character.get_character_info()
    if player_input == 'use sword' and 'sword' in player['inventory']:
        return False
    elif player_input == 'use bread' and 'bread' in player['inventory']:
        return False
    else:
        # no correct input found so returns error = true
        print('You dont have that item')
        return True


def adjacent_door_check(player_input):
    """if user tries to interact with a door, checks if the door is adjacent

    PARAM player a correctly formatted dictionary
    PARAM dungeon_map a list of lists
    PARAM player_input a string
    PRECONDITION player is a correctly formatted dictionary
    PRECONDITION dungeon_map is a list of lists with 12 elements each
    PRECONDITION player_input is a string
    POSTCONDITION Prints nothing or an error message if input is incorrect
    RETURN True if error in input and False if no error
    """
    dungeon_map = map.get_map()
    player = character.get_character_info()
    # if user inputs unlock door, has a key, and there is a locked door then the door opens
    if player_input == 'unlock door' and dungeon_map[player['row']][player['column'] - 1] == ' L ' \
            and 'key' in player['inventory']:
        dungeon_map[player['row']][player['column'] - 1] = '   '
        return False

    # if user inputs open door and there is a door then the door opens
    elif player_input == 'open door' and dungeon_map[player['row']][player['column'] + 1] == ' D ':
        dungeon_map[player['row']][player['column'] + 1] = '   '
        return False

    # if user inputs unlock door but has no key the prints an error message
    elif player_input == 'unlock door' and dungeon_map[player['row']][player['column'] - 1] == ' L ' \
            and 'key' not in player['inventory']:
        print('You do not have a key to open that door')
        return True

    # user input was incorrect so prints an error message
    else:
        print('i dont understand')
        return True


def help_menu():
    """Prints a help menu with all keywords usable by player
    """
    print('List of keywords you can type:')
    print('[north, east, south, west] : move in that direction')
    print('[take \'item\'] : takes the item you enter')
    print('[use \'item\'] : uses the item you enter')
    print('[open door] : opens an adjacent door')
    print('[unlock door] : unlocks an adjacent door')
    print('[help] : opens the help menu')


def take_item_check(player_input):
    """if user inputs to take an item checks if it is on the players tile

    PARAM player a correctly formatted dictionary
    PARAM dungeon_map a list of lists
    PARAM player_input a string
    PRECONDITION player is a correctly formatted dictionary
    PRECONDITION dungeon_map is a list of lists with 12 elements each
    PRECONDITION player_input is a string
    POSTCONDITION Prints nothing or an error message if input is incorrect
    RETURN True if error in input and False if no error
    """
    dungeon_map = map.get_map()
    player = character.get_character_info()
    # if player inputs take key checks if key is on the player and takes it if it is
    if player_input == 'take key' and dungeon_map[player['row']][player['column']] == ' K ':
        dungeon_map[player['row']][player['column']] = '###'
        player['inventory'].append('key')
        return False

    # if player inputs take sword checks if sword is on the player and takes it if it is
    elif player_input == 'take sword' and dungeon_map[player['row']][player['column']] == ' S ':
        dungeon_map[player['row']][player['column']] = '...'
        player['inventory'].append('sword')
        return False

    # if player inputs take bread checks if bread is on the player and takes it if it is
    elif player_input == 'take bread' and dungeon_map[player['row']][player['column']] == ' B ':
        dungeon_map[player['row']][player['column']] = '   '
        player['inventory'].append('bread')
        return False

    # if player inputs take treasure checks if treasure is on the player and takes it if it is
    elif player_input == 'take treasure' and dungeon_map[player['row']][player['column']] == ' C ':
        dungeon_map[player['row']][player['column']] = '"""'
        player['inventory'].append('treasure')
        return False

    # the item the user tried to take is not on the player, prints an error
    else:
        print('You cant take that')
        return True


def collision_check(player_input):
    """Checks if there is a wall where the player is trying to move

    PARAM player a correctly formatted dictionary
    PARAM dungeon_map a list of lists
    PARAM player_input a string
    PRECONDITION player is a correctly formatted dictionary
    PRECONDITION dungeon_map is a list of lists with 12 elements each
    PRECONDITION player_input is the string north, east, south, or west
    POSTCONDITION Prints nothing or an error message if there is a wall
    RETURN True if user cant walk in that direction False otherwise
    """
    # list of all un-walkable terrain
    unwalkable_terrain = ('---', ' | ', ' \ ', ' / ', '~~~', '|||', ' D ', ' L ')
    dungeon_map = map.get_map()
    player = character.get_character_info()

    # Checks user move direction and whether that directions area is in un-walkable terrain
    if player_input == 'east' and dungeon_map[player['row']][player['column'] + 1] not in unwalkable_terrain:
        character.set_row(player['column'] + 1)
        return False
    elif player_input == 'west' and dungeon_map[player['row']][player['column'] - 1] not in unwalkable_terrain:
        character.set_row(player['column'] - 1)
        return False
    elif player_input == 'north' and dungeon_map[player['row'] - 1][player['column']] not in unwalkable_terrain:
        character.set_column(player['row'] - 1)
        return False
    elif player_input == 'south' and dungeon_map[player['row'] + 1][player['column']] not in unwalkable_terrain:
        character.set_column(player['row'] + 1)
        return False
    # User tried to move toward an un-walkable terrain, prints error
    else:
        print('You cant move in that direction')
        return True


def main():
    moved_list = ['north', 'east', 'south', 'west']
    # load or create a character and map
    character.get_user()
    map.get_user_map()

    # prints initial map, character, and message
    print('You are in an abandoned village in your search for a hidden treasure.')
    print('Type north, east, south, or west to move')
    print('Type help to see a list of other keywords you can use')
    map.display_map()
    character.print_character()
    player_input = user_input()

    # game loop continues until user inputs quit
    while player_input != 'quit':
        print_message(player_input)
        map.display_map()

        # If player moves checks for monster encounter
        if player_input in moved_list:
            # Checks for a monster encounter
            if not monster.check_monster_encounter():
                # If not encounter is found increase health
                if character.get_hitpoints() < 10:
                    character.set_hitpoints(character.get_hitpoints() + 1)

        # exits game loop if user dies
        if character.get_hitpoints() <= 0:
            print('You died :(')
            break

        # prints character and asks for next input
        character.print_character()
        player_input = user_input()

    # saves user and map in .json files if user did not die
    if character.get_hitpoints() > 0:
        character.save_user()
        map.save_map()


if __name__ == '__main__':
    main()
