"""Simple SUD"""
import random
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


def monster_encounter():
    pass


def monster_fight():
    pass


def print_message(player, dungeon_map, player_input):
    if player_input[0:4] == 'take':
        print('you pick up', player_input[5:])
    elif player_input == 'open door':
        print('you open the door')
    elif player_input == 'unlock door':
        print('you unlock the door')


def user_input(player, dungeon_map):
    error = True
    while error:
        player_input = input()
        if player_input == 'east' or player_input == 'west' or player_input == 'north' or player_input == 'south':
            error = collision_check(player_input, player, dungeon_map)
        elif player_input[0:4] == 'take':
            error = take_item_check(player_input, player, dungeon_map)
        elif player_input == 'unlock door' and dungeon_map[player['xlocation']][player['ylocation'] - 1] == ' L ':
            dungeon_map[player['xlocation']][player['ylocation'] - 1] = '   '
            error = False
        elif player_input == 'open door' and dungeon_map[player['xlocation']][player['ylocation'] + 1] == ' D ':
            dungeon_map[player['xlocation']][player['ylocation'] + 1] = '   '
            error = False
        elif player_input == 'help':
            help_menu()
        elif player_input == 'give bread':
            pass
        elif player_input == 'use sword':
            pass
        else:
            print('i dont understand')
    return player_input


def help_menu():
    print('List of keywords you can type:')
    print('[north, east, south, west] : move in that direction')
    print('[take \'item\'] : takes the item you enter')
    print('[open door] : opens an adjacent door')
    print('[unlock door] : unlocks an adjacent door')
    print('[help] : opens the help menu')


def take_item_check(player_input, player, dungeon_map):
    if player_input == 'take key' and dungeon_map[player['xlocation']][player['ylocation']] == ' K ':
        dungeon_map[player['xlocation']][player['ylocation']] = '   '
        player['inventory'].append('key')
        return False
    elif player_input == 'take sword' and dungeon_map[player['xlocation']][player['ylocation']] == ' S ':
        dungeon_map[player['xlocation']][player['ylocation']] = '   '
        player['inventory'].append('sword')
        return False
    elif player_input == 'take bread' and dungeon_map[player['xlocation']][player['ylocation']] == ' B ':
        dungeon_map[player['xlocation']][player['ylocation']] = '   '
        player['inventory'].append('bread')
        return False
    elif player_input == 'take treasure' and dungeon_map[player['xlocation']][player['ylocation']] == ' C ':
        dungeon_map[player['xlocation']][player['ylocation']] = '   '
        player['inventory'].append('treasure')
        return False
    else:
        print('You cant take that')
        return True


def collision_check(player_input, player, dungeon_map):
    unwalkable_terrain = ('---', ' | ', ' \ ', ' / ', '~~~', '|||', ' D ', ' L ')

    if player_input == 'east' and dungeon_map[player['xlocation']][player['ylocation'] + 1] not in unwalkable_terrain:
        player['ylocation'] += 1
        return False
    elif player_input == 'west' and dungeon_map[player['xlocation']][player['ylocation'] - 1] not in unwalkable_terrain:
        player['ylocation'] -= 1
        return False
    elif player_input == 'north' and dungeon_map[player['xlocation'] - 1][player['ylocation']] not in unwalkable_terrain:
        player['xlocation'] -= 1
        return False
    elif player_input == 'south' and dungeon_map[player['xlocation'] + 1][player['ylocation']] not in unwalkable_terrain:
        player['xlocation'] += 1
        return False
    else:
        print('You cant move in that direction')
        return True


def main():
    new_player = character.create_character()
    new_map = map.create_map()
    print('You come across an abandoned village in your search for a hidden treasure.')
    print('Type north, east, south, or west to move')
    print('Type help to see a list of other keywords you can use')
    map.display_map(new_map, new_player)
    character.print_character(new_player)
    player_input = ''
    while player_input != 'quit':
        player_input = user_input(new_player, new_map)
        print_message(new_player, new_map, player_input)
        map.display_map(new_map, new_player)
        character.print_character(new_player)


if __name__ == '__main__':
    main()
