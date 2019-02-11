"""dungeonsanddragons module
"""

# Tommy May
# A01086435
# Date

import random
import copy


def roll_die(number_of_rolls, number_of_sides):
    """Rolls a die a specified number of times and adds them up

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
    # calculate sum of rolled dice
    for i in range(number_of_rolls):
        random_total += random.randint(1, number_of_sides)
    return random_total


def choose_inventory(inventory, selection):
    """chooses a certain amount of items randomly from a given list

    PARAM inventory a list
    PARAM selection an int
    PRECONDITION inventory must be a list
    PRECONDITION selection must be a positive int
    POSTCONDITION creates a new list of random items from given inventory
    RETURN list with random items from inventory

    """
    # checking errors in input
    if (not inventory) and (selection == 0):
        return []
    elif selection < 0:
        return None
    elif selection > len(inventory):
        print("you selected too many items")
        return None
    # return a copy of the list
    elif selection == len(inventory):
        return copy.deepcopy(inventory)
    # return a sorted random list of items from inventory
    else:
        sorted_inventory = sorted(random.sample(inventory, selection))
        return sorted_inventory


def create_character(syllables):
    """creates a dictionary with character name and 6 core attributes

    PARAM syllables an int
    PRECONDITION syllables must be a positive int
    POSTCONDITION a correctly formatted character dictionary
    RETURN correctly formatted character dictionary
    """
    # return None if input is not a positive integer
    if (not isinstance(syllables, int)) or (syllables <= 0):
        print('You did not enter a positive integer')
        return None

    character_dict = {'name': '', 'class': '', 'HitPoints': 0, 'strength': '', 'dexterity': '', 'constitution': '', 'intelligence': '',
                      'wisdom': '', 'charisma': '', 'XP': 0, 'items': ''}

    # generate name and class for character_dict
    character_dict['name'] = generate_name(syllables)
    character_dict['class'] = class_selection()

    # calculate hitpoints based on class chosen
    if character_dict['class'] == 'barbarian':
        character_dict['HitPoints'] = roll_die(1, 12)
    elif character_dict['class'] in ('bard', 'cleric', 'druid', 'monk', 'rogue', 'warlock'):
        character_dict['HitPoints'] = roll_die(1, 8)
    elif character_dict['class'] in ('fighter', 'paladin', 'ranger', 'bloodhunter'):
        character_dict['HitPoints'] = roll_die(1, 10)
    elif character_dict['class'] in ('wizard', 'sorcerer'):
        character_dict['HitPoints'] = roll_die(1, 6)

    # roll 3 6-sided dice for each attribute and add it to character_dict
    character_dict['strength'] = roll_die(3, 6)
    character_dict['dexterity'] = roll_die(3, 6)
    character_dict['constitution'] = roll_die(3, 6)
    character_dict['intelligence'] = roll_die(3, 6)
    character_dict['wisdom'] = roll_die(3, 6)
    character_dict['charisma'] = roll_die(3, 6)
    return character_dict


def print_character(character):
    """prints character list to console

    PARAM character a dictionary
    PRECONDITION character must be a dictionary
    POSTCONDITION character is printed to console
    """
    for attribute, value in character.items():
        print(attribute, value)


def generate_name(syllables):
    """ generates a name

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
    """ generate a vowel

    RETURN a string with 1 vowel
    """
    vowels = 'aeiouy'
    random_vowel = random.choice(vowels)
    return random_vowel


def generate_consonant():
    """ generate a consonant

    RETURN a string with 1 consonant
    """
    consonants = 'bcdfghjklmnpqrstvwxz'
    random_consonant = random.choice(consonants)
    return random_consonant


def generate_syllable():
    """ generate a syllable with 1 consonant and 1 vowel

    RETURN a string with a syllable
    """
    random_syllable = generate_consonant() + generate_vowel()
    return random_syllable


def class_selection():
    """ asks user to select a class from a list of choices

    RETURN a string with the inputted class in lowercase
    """
    class_choice = input('Type in the class you want to select from this list:'
                         '\nbarbarian\nbard\ncleric\ndruid\nmonk\nrogue\nwarlock\nfighter\npaladin\nranger'
                         '\nbloodhunter\nwizard\nsorcerer\n')
    return class_choice.lower()


def combat_round(opponent_1, opponent_2):
    """ Plays a round of combat between 2 characters

    PARAM opponent_1 a correctly formatted dictionary
    PARAM opponent_2 a correctly formatted dictionary
    PRECONDITION opponent_1 is a correctly formatted dictionary
    PRECONDITION opponent_2 is a correctly formatted dictionary
    POSTCONDITION a round of combat is played
    """
    attacker = None
    defender = None
    successful_strike = None
    damage = None

    # calculates who the attacker and who the defender is based on die roll
    while attacker is None:
        opponent_1_attack_roll = roll_die(1, 20)
        opponent_2_attack_roll = roll_die(1, 20)
        if opponent_1_attack_roll > opponent_2_attack_roll:
            attacker = opponent_1
            defender = opponent_2
        elif opponent_2_attack_roll > opponent_1_attack_roll:
            attacker = opponent_2
            defender = opponent_1

    if roll_die(1, 20) > defender['dexterity']:
        successful_strike = True

    # if attack is successful calculates damage based on attackers class
    if successful_strike is True:
        if attacker['class'] == 'barbarian':
            damage = roll_die(1, 12)
            defender['HitPoints'] -= damage
        elif attacker['class'] in ('bard', 'cleric', 'druid', 'monk', 'rogue', 'warlock'):
            damage = roll_die(1, 8)
            defender['HitPoints'] -= damage
        elif attacker['class'] in ('fighter', 'paladin', 'ranger', 'bloodhunter'):
            damage = roll_die(1, 10)
            defender['HitPoints'] -= damage
        elif attacker['class'] in ('wizard', 'sorcerer'):
            damage = roll_die(1, 6)
            defender['HitPoints'] -= damage

        # prints defenders hp and whether he died or not
        if defender['HitPoints'] < 1:
            print(attacker['name'], 'hit', defender['name'], 'for', damage, 'damage\n', defender['name'], 'died')
        else:
            print(attacker['name'], 'hit', defender['name'], 'for', damage, 'damage\n', defender['name'], 'has',
                  defender['HitPoints'], 'hitpoints left')

    # attack was unsuccessful prints did not hit
    else:
        print(attacker['name'], 'did not hit', defender['name'])


def main():
    new_guy = create_character(3)
    print_character(new_guy)
    new_guy['items'] = choose_inventory(['a', 'b', 'c', 'd', 'e'], 3)
    print_character(new_guy)
    new_guy_2 = create_character(6)
    print_character(new_guy_2)
    combat_round(new_guy, new_guy_2)


if __name__ == '__main__':
    main()
