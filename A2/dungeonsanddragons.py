"""dungeons and dragons module
"""

# Tommy May
# A01086435
# Date

import random
import copy
import doctest


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


def choose_inventory(inventory, selection):
    """ Chooses a certain amount of items randomly from a given list

    PARAM inventory a list
    PARAM selection an int
    PRECONDITION inventory must be a list
    PRECONDITION selection must be a positive int
    POSTCONDITION creates a new list of random items from given inventory
    RETURN list with random items from inventory

    """
    # Checking errors in input
    if (not inventory) and (selection == 0):
        return []
    elif selection < 0:
        return None
    elif selection > len(inventory):
        print("you selected too many items")
        return None
    # Return a copy of the list
    elif selection == len(inventory):
        return copy.deepcopy(inventory)
    # Return a sorted random list of items from inventory
    else:
        sorted_inventory = sorted(random.sample(inventory, selection))
        return sorted_inventory


def create_character(syllables):
    """ Creates a dictionary with character name and 6 core attributes

    PARAM syllables an int
    PRECONDITION syllables must be a positive int
    POSTCONDITION a correctly formatted character dictionary
    RETURN correctly formatted character dictionary
    """
    # Return None if input is not a positive integer
    if (not isinstance(syllables, int)) or (syllables <= 0):
        print('You did not enter a positive integer')
        return None

    # Creates initial character dictionary
    character_dict = {'name': '', 'class': '', 'HitPoints': 0, 'strength': '', 'dexterity': '', 'constitution': '', 'intelligence': '',
                      'wisdom': '', 'charisma': '', 'XP': 0, 'items': ''}

    # Generate name and class for character_dict
    character_dict['name'] = generate_name(syllables)
    character_dict['class'] = class_selection()

    # Calculate HitPoints based on class chosen
    character_dict['HitPoints'] = calculate_hit_die(character_dict['class'])


    # Roll 3 6-sided dice for each attribute and add it to character_dict
    character_dict['strength'] = roll_die(3, 6)
    character_dict['dexterity'] = roll_die(3, 6)
    character_dict['constitution'] = roll_die(3, 6)
    character_dict['intelligence'] = roll_die(3, 6)
    character_dict['wisdom'] = roll_die(3, 6)
    character_dict['charisma'] = roll_die(3, 6)
    return character_dict


def print_character(character):
    """ Prints character dictionary to console

    PARAM character a dictionary
    PRECONDITION character must be a dictionary
    POSTCONDITION character is printed to console

    >>> print_character({'name': 'tommy', 'class': 'druid', 'HitPoints': 5, 'strength': 9, 'dexterity': 13,\
                         'constitution': 14, 'intelligence': 9, 'wisdom': 9, 'charisma': 7, 'XP': 0,\
                         'items': ['sword', 'axe', 'bow', 'blowgun', 'staff']})
    name tommy
    class druid
    HitPoints 5
    strength 9
    dexterity 13
    constitution 14
    intelligence 9
    wisdom 9
    charisma 7
    XP 0
    items ['sword', 'axe', 'bow', 'blowgun', 'staff']
    """
    for attribute, value in character.items():
        print(attribute, value)


def generate_name(syllables):
    """ Generates a name

    PARAM syllables an int
    PRECONDITION syllables is a positive integer
    POSTCONDITION a name is created with the entered amount of syllables
    RETURN the name created
    """
    name = ''
    for i in range(syllables):
        name = name + generate_syllable()
    return name


def generate_vowel():
    """ Generate a vowel

    RETURN a string with 1 vowel
    """
    vowels = 'aeiouy'
    random_vowel = random.choice(vowels)
    return random_vowel


def generate_consonant():
    """ Generate a consonant

    RETURN a string with 1 consonant
    """
    consonants = 'bcdfghjklmnpqrstvwxz'
    random_consonant = random.choice(consonants)
    return random_consonant


def generate_syllable():
    """ Generate a syllable with 1 consonant and 1 vowel

    RETURN a string with a syllable
    """
    random_syllable = generate_consonant() + generate_vowel()
    return random_syllable


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


def combat_round(opponent_1, opponent_2):
    """ Plays a round of combat between 2 characters

    PARAM opponent_1 a correctly formatted dictionary
    PARAM opponent_2 a correctly formatted dictionary
    PRECONDITION opponent_1 is a correctly formatted dictionary
    PRECONDITION opponent_2 is a correctly formatted dictionary
    POSTCONDITION a round of combat is played with players hp lowered by amount lost in battle
    """
    attacker_1 = None
    attacker_2 = None

    # Calculates who the attacker and who the defender is based on die roll until they aren't equal
    while attacker_1 is None:
        opponent_1_attack_roll = roll_die(1, 20)
        opponent_2_attack_roll = roll_die(1, 20)
        if opponent_1_attack_roll > opponent_2_attack_roll:
            attacker_1 = opponent_1
            attacker_2 = opponent_2
        elif opponent_2_attack_roll > opponent_1_attack_roll:
            attacker_1 = opponent_2
            attacker_2 = opponent_1

    # First attacker attacks second attacker
    attack_player(attacker_1, attacker_2)
    # If attacker 2 is not dead then attacker 2 attacks attacker 1
    if attacker_2['HitPoints'] >= 1:
        attack_player(attacker_2, attacker_1)


def attack_player(attacker, defender):
    """ Attacker rolls dice to see how much he hits the defender for

    PARAM attacker a correctly formatted dictionary
    PARAM defender a correctly formatted dictionary
    PRECONDITION attacker is a correctly formatted dictionary
    PRECONDITION defender is a correctly formatted dictionary
    POSTCONDITION attacker attacks defender and lowers defenders health by amount hit and prints a message
    """
    # Rolls die to check if attacker hits the defender
    if roll_die(1, 20) > defender['dexterity']:
        successful_strike = True
    else:
        successful_strike = False

    # If attack is successful calculates damage based on attackers class
    if successful_strike is True:
        damage = calculate_hit_die(attacker['class'])
        defender['HitPoints'] -= damage

        # Prints defenders hp and whether he died or not
        if defender['HitPoints'] < 1:
            print(attacker['name'], 'hit', defender['name'], 'for', damage, 'damage\n', defender['name'], 'died')
        else:
            print(attacker['name'], 'hit', defender['name'], 'for', damage, 'damage\n', defender['name'], 'has',
                  defender['HitPoints'], 'HitPoints left')

    # Attack was unsuccessful prints did not hit
    else:
        print(attacker['name'], 'did not hit', defender['name'])


def calculate_hit_die(character_class):
    """Rolls a hit die based on character class for damage or hp

    PARAM character_class a correctly formatted dictionary
    PRECONDITION character_class is a correctly formatted dictionary
    POSTCONDITION a die is rolled based on class
    RETURN the integer value of the rolled hit die
    """
    if character_class == 'barbarian':
        return roll_die(1, 12)
    elif character_class in ('bard', 'cleric', 'druid', 'monk', 'rogue', 'warlock'):
        return roll_die(1, 8)
    elif character_class in ('fighter', 'paladin', 'ranger', 'bloodhunter'):
        return roll_die(1, 10)
    elif character_class in ('wizard', 'sorcerer'):
        return roll_die(1, 6)


def main():
    doctest.testmod()
    new_guy = create_character(3)
    print_character(new_guy)
    new_guy['items'] = choose_inventory(['a', 'b', 'c', 'd', 'e'], 3)
    print_character(new_guy)
    new_guy_2 = create_character(6)
    print_character(new_guy_2)
    combat_round(new_guy, new_guy_2)
    print_character(new_guy_2)
    print_character(new_guy)


if __name__ == '__main__':
    main()
