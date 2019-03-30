"""Map functions for sud module

get_map: returns the dungeon_map
set_map: sets value of map at given column and row
display_map: displays a 3x3 portion of the map centered on the player
get_user_map: either loads a map if it exists or creates one
get_stored_map: loads an existing map
create_new_map: creates initial map
save_map: saves current map to a file

"""

# Tommy May
# A01086435
# March 10

import character
import json

dungeon_map = [[' / ', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', ' \ '],
               [' | ', ' / ', '---', '---', '---', '|||', ':::', ':::', ':::', ':::', ':::', ' | '],
               [' | ', ' C ', '"""', '"""', '"""', ' L ', ':::', ':::', ':::', ':::', ':::', ' | '],
               [' | ', ' \ ', '---', '---', '---', '|||', ':::', ':::', ':::', ':::', ':::', ' | '],
               [' | ', '~~~', '~~~', '~~~', '~~~', '~~~', '~~~', '~~~', '| |', '~~~', '~~~', ' | '],
               [' | ', '---', '---', ' \ ', '~~~', '~~~', '~~~', '~~~', '| |', '~~~', '~~~', ' | '],
               [' | ', '...', '...', ' | ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' | '],
               [' | ', '...', '...', '   ', '   ', ' | ', ' B ', ' / ', '---', '---', ' \ ', ' | '],
               [' | ', ' S ', '...', ' | ', '   ', ' | ', '---', ' / ', '###', ' K ', '###', ' | '],
               [' | ', '---', '---', ' / ', '   ', ' D ', '###', '###', '###', '###', '###', ' | '],
               [' | ', '   ', '   ', '   ', '   ', ' | ', '---', '---', '---', '---', ' / ', ' | '],
               [' \ ', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', ' / ']]


def reset_map():
    global dungeon_map
    dungeon_map = [[' / ', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', ' \ '],
                   [' | ', ' / ', '---', '---', '---', '|||', ':::', ':::', ':::', ':::', ':::', ' | '],
                   [' | ', ' C ', '"""', '"""', '"""', ' L ', ':::', ':::', ':::', ':::', ':::', ' | '],
                   [' | ', ' \ ', '---', '---', '---', '|||', ':::', ':::', ':::', ':::', ':::', ' | '],
                   [' | ', '~~~', '~~~', '~~~', '~~~', '~~~', '~~~', '~~~', '| |', '~~~', '~~~', ' | '],
                   [' | ', '---', '---', ' \ ', '~~~', '~~~', '~~~', '~~~', '| |', '~~~', '~~~', ' | '],
                   [' | ', '...', '...', ' | ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', ' | '],
                   [' | ', '...', '...', '   ', '   ', ' | ', ' B ', ' / ', '---', '---', ' \ ', ' | '],
                   [' | ', ' S ', '...', ' | ', '   ', ' | ', '---', ' / ', '###', ' K ', '###', ' | '],
                   [' | ', '---', '---', ' / ', '   ', ' D ', '###', '###', '###', '###', '###', ' | '],
                   [' | ', '   ', '   ', '   ', '   ', ' | ', '---', '---', '---', '---', ' / ', ' | '],
                   [' \ ', '---', '---', '---', '---', '---', '---', '---', '---', '---', '---', ' / ']]
def get_map() -> list:
    return dungeon_map


def set_map(column: int, row: int, value: str):
    dungeon_map[column][row] = value


def display_map():
    """displays a 3x3 portion of the map with user in the center

    POSTCONDITION 3x3 map portion is displayed
    """
    player = character.get_character_info()
    for i in range(player['row'] - 1, player['row'] + 2):
        for j in range(player['column'] - 1, player['column'] + 2):
            if player['row'] == i and player['column'] == j:
                print(' P ', end='')
            else:
                print(dungeon_map[i][j], end='')
        print('\n')


def get_user_map():
    """A map is either initialized or loaded if it exists already

    POSTCONDITION map is initialized or loaded as a 12x12 list
    """
    global dungeon_map
    filename = character.get_character_info()['name'] + '_map.json'
    my_map = get_stored_map(filename)
    if my_map:
        pass
    else:
        my_map = create_new_map(filename)
    dungeon_map = my_map


def get_stored_map(filename):
    """Loads map info from a .json file

    PARAM filename a string
    PRECONDITION filename is in format name.json
    POSTCONDITION map info is loaded
    RETURN existing_map a 12x12 list representing a map
    """
    try:
        with open(filename) as f_obj:
            existing_map = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return existing_map


def create_new_map(filename):
    """Creates the initial map

    PARAM filename a string
    PRECONDITION filename is in format name.json
    POSTCONDITION dungeon_map is created
    RETURN dungeon_map 12x12 list representing the map
    """
    with open(filename, 'w') as f_obj:
        json.dump(dungeon_map, f_obj)
        return dungeon_map


def save_map():
    """Saves the current map in a .json file

    PARAM map a list
    PRECONDITION map is a list
    POSTCONDITION the map is saved in a .json file
    """
    filename = character.get_character_info()['name'] + '_map.json'
    with open(filename, 'w') as f_obj:
        json.dump(dungeon_map, f_obj)
