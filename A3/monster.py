"""monster functions for sud"""
import sud
import character


def check_monster_encounter():
    """rolls a dice with a 1/10 chance of encountering a monster

    POSTCONDITION either plays a monster encounter or not depending on roll
    RETURN true if monster encountered false if not
    """
    # rolls a die for 1/10 chance of monster encounter
    if sud.roll_die(1, 10) == 1:
        monster_encounter()
        return True
    return False


def monster_encounter():
    """Asks user if they want to fight or run away from the monster

    POSTCONDITION monster_fight or run_away are executed depending on input
    """
    print('You encounter a wild monster')
    print('Do you fight it or run away?')
    user_selection = input()
    correct_input = ['run away', 'fight']

    # keeps asking for input if input is incorrect
    while user_selection not in correct_input:
        user_selection = input('incorrect response, enter either \'fight\' or \'run away\'')

    # if input is fight then monster_fight initiates
    if user_selection == 'fight':
        monster_fight()

    # if input is run away then run_away initiates
    else:
        run_away()


def run_away():
    """runs away with a 1/10 chance of taking 1 - 4 damage from the monster

    POSTCONDITION player runs away with a chance at taking 1 - 4 damage
    """
    # rolls die for 1/10 chance of monster hitting player
    if sud.roll_die(1, 10) == 1:
        # monster rolls 1d4 for damage and lowers player hp by that amount
        monster_damage = sud.roll_die(1, 4)
        character.set_hitpoints(character.get_hitpoints() - monster_damage)
        print('The monster hits you for', monster_damage, 'Hitpoints as you run away')

    # if die is > 1 then user runs away safely
    else:
        print('You run away safely')


def monster_fight():
    """Plays a monster fight to the death

    POSTCONDITION either the player or the monster dies
    """
    monster_hp = 5
    # keeps fighting while both monster and player are alive
    while monster_hp > 0 and character.get_hitpoints() > 0:
        # calculates monster and player damage
        player_damage = sud.roll_die(1, 6)
        monster_damage = sud.roll_die(1, 6)
        # player attacks monster
        monster_hp -= player_damage
        print('You hit the monster for', player_damage, 'Damage')
        # if monster dies prints a message
        if monster_hp <= 0:
            print('The monster dies')
        # if monster didnt die it attacks the player
        else:
            character.set_hitpoints(character.get_hitpoints() - monster_damage)
            print('The monster hits you for', monster_damage, 'Damage')

