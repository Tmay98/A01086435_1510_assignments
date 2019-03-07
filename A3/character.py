"""character module"""


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

