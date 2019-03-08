"""character module"""
import json

character_info = {'name': '', 'HitPoints': 10, 'row': 1, 'column': 10, 'inventory': []}


def get_character_info():
    """returns character_info dictionary"""
    return character_info


def get_hitpoints():
    return character_info['HitPoints']


def set_hitpoints(hp):
    character_info['HitPoints'] = hp


def set_row(row):
    character_info['row'] = row


def set_column(column):
    character_info['column'] = column


def print_character():
    """ Prints character Hp and name

    PARAM character a dictionary
    PRECONDITION character must be a dictionary
    POSTCONDITION character is printed

    """
    print('Name:', character_info['name'], 'Hitpoints:', character_info['HitPoints'])


def get_user():
    """user enters there characters name and it is either loaded or created

    POSTCONDITION character with entered name is loaded or created
    RETURN player a character info dictionary
    """
    global character_info
    character_name = input('Enter your character\'s name')
    filename = character_name + '.json'
    player = get_stored_user(filename)
    if player:
        pass
    else:
        player = create_new_user(filename, character_name)
    character_info = player


def get_stored_user(filename):
    """loads a characters info from a .json file

    PARAM filename a string
    PRECONDITION filename is in format name.json
    POSTCONDITION character info is loaded
    RETURN existing_player a character info dictionary
    """
    try:
        with open(filename) as f_obj:
            existing_player = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return existing_player


def create_new_user(filename, character_name):
    """Creates a new user given a character name

    PARAM filename a string
    PARAM character_name a string
    PRECONDITION filename is in format name.json
    PRECONDITION character_name is a string
    POSTCONDITION character info dictionary is created
    RETURN character info dictionary
    """
    with open(filename, 'w') as f_obj:
        character_info['name'] = character_name
        json.dump(character_info, f_obj)
        return character_info


def save_user():
    """saves the current users progress in a .json file

    PARAM character a dictionary
    PRECONDITION character is a dictionary with character info
    POSTCONDITION the character info dictionary is saved in a .json file
    """
    filename = character_info['name'] + '.json'
    with open(filename, 'w') as f_obj:
        json.dump(character_info, f_obj)

