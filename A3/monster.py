"""monster functions for sud"""
import sud
import character


def check_monster_encounter():
    if sud.roll_die(1, 10) == 1:
        monster_encounter()


def monster_encounter():
    print('You encounter a wild monster')
    print('Do you fight it or run away?')
    user_selection = input()
    correct_input = ['run away', 'fight']
    while user_selection not in correct_input:
        user_selection = input('incorrect response, enter either \'fight\' or \'run away\'')
    if user_selection == 'fight':
        monster_fight()
    else:
        run_away()


def run_away():
    if sud.roll_die(1, 10) == 1:
        monster_damage = sud.roll_die(1, 4)
        character.set_hitpoints(character.get_hitpoints() - monster_damage)
        print('The monster hits you for', monster_damage, 'Hitpoints as you run away')
    else:
        print('You run away safely')


def monster_fight():
    monster_hp = 5
    while monster_hp > 0 and character.get_hitpoints() > 0:
        player_damage = sud.roll_die(1, 6)
        monster_damage = sud.roll_die(1, 6)
        monster_hp -= player_damage
        print('You hit the monster for', player_damage, 'Damage')
        if monster_hp <= 0:
            print('The monster dies')
        else:
            character.set_hitpoints(character.get_hitpoints() - monster_damage)
            print('The monster hits you for', monster_damage, 'Damage')

