"""character module"""


import json

character_info = {'name': '', 'class': '', 'HitPoints': 10, 'xlocation': 10, 'ylocation': 1, 'inventory': []}


def create_character(name):
    """ Creates a dictionary with character name and 6 core attributes

    PARAM syllables an int
    PRECONDITION syllables must be a positive int
    POSTCONDITION a correctly formatted character dictionary
    RETURN correctly formatted character dictionary
    """
    global character_info
    # Generate name and class for character_dict
    character_info['name'] = name
    character_info['class'] = class_selection()
    return character_info


def print_character(character):
    """ Prints character Hp and name

    PARAM character a dictionary
    PRECONDITION character must be a dictionary
    POSTCONDITION character is printed

    """
    print('Name:', character['name'], 'Hitpoints:', character['HitPoints'])


def class_selection():
    """ Asks user to select a class from a list of choices

    RETURN a string with the inputted class in lowercase
    """
    class_choice = ''
    class_list = ['barbarian', 'bard', 'cleric', 'druid', 'monk', 'rogue', 'warlock', 'fighter', 'paladin',
                  'ranger', 'bloodhunter', 'wizard', 'sorcerer']

    # Loop through class input until a correct class is entered
    while class_choice.lower() not in class_list:
        class_choice = input('Type in the class you want to select from this list:'
                             '\nbarbarian\nbard\ncleric\ndruid\nmonk\nrogue\nwarlock\nfighter\npaladin\nranger'
                             '\nbloodhunter\nwizard\nsorcerer\n')

        if class_choice.lower() not in class_list:
            print('You did not enter a correct class, try again')

    return class_choice.lower()


def get_user():
    """user enters there characters name and it is either loaded or created

    POSTCONDITION character with entered name is loaded or created
    RETURN player a character info dictionary
    """
    character_name = input('Enter your character\'s name')
    filename = character_name + '.json'
    player = get_stored_user(filename)
    if player:
        pass
    else:
        player = create_new_user(filename, character_name)
    return player


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
        new_player = create_character(character_name)
        return new_player


def save_user(character_dict):
    """saves the current users progress in a .json file

    PARAM character a dictionary
    PRECONDITION character is a dictionary with character info
    POSTCONDITION the character info dictionary is saved in a .json file
    """
    filename = character_dict['name'] + '.json'
    with open(filename, 'w') as f_obj:
        json.dump(character_dict, f_obj)

