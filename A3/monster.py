"""monster functions for sud"""
import sud


def check_monster_encounter(player):
    if sud.roll_die(1, 10) == 1:
        monster_encounter(player)
    i = 0


def monster_encounter(player):
    print('You encounter a wild monster')
    print('Do you fight it or run away?')
    user_selection = input()
    correct_input = ['run away', 'fight']
    while user_selection not in correct_input:
        user_selection = input('incorrect response, enter either \'fight\' or \'run away\'')
    if user_selection == 'fight':
        monster_fight(player)
    else:
        run_away(player)


def run_away(player):
    if sud.roll_die(1, 10) == 1:
        monster_damage = sud.roll_die(1, 4)
        player['HitPoints'] -= monster_damage
        print('The monster hits you for', monster_damage, 'Hitpoints as you run away')
    else:
        print('You run away safely')


def monster_fight(player):
    monster_hp = 5
    while monster_hp > 0 and player['HitPoints'] > 0:
        player_damage = sud.roll_die(1, 6)
        monster_damage = sud.roll_die(1, 6)
        monster_hp -= player_damage
        print('You hit the monster for', player_damage, 'Damage')
        if monster_hp <= 0:
            print('The monster dies')
        else:
            player['HitPoints'] -= monster_damage
            print('The monster hits you for', monster_damage, 'Damage')

