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


def print_message(player, dungeon_map, player_input):
    if player_input[0:4] == 'take':
        print('you pick up', player_input[5:])
    elif player_input == 'open door':
        print('you open the door')
    elif player_input == 'unlock door':
        print('you unlock the door')
    scenario_message(player, dungeon_map)
    item_on_ground_message(player, dungeon_map)


def item_on_ground_message(player, dungeon_map):
    if dungeon_map[player['xlocation']][player['ylocation']] == ' K ':
        print('You see a key on a table')
    elif dungeon_map[player['xlocation']][player['ylocation']] == ' S ':
        print('There is a sword propped up against the wall, it seems to be in good condition')
    elif dungeon_map[player['xlocation']][player['ylocation']] == ' B ':
        print('you ses some bread left on a bench, it looks edible')


def scenario_message(player, dungeon_map):
    if 0 not in player['message_seen'] and player['xlocation'] == 9 and player['ylocation'] == 4:
        print('You come across a church that is still in good condition')
        print('There is a door that seems to be unlocked, maybe there is something in there')
        player['message_seen'].append(0)
    if 1 not in player['message_seen'] and player['xlocation'] == 7 and player['ylocation'] == 4:
        print('There is a run down shack to your left')
        player['message_seen'].append(1)
    if 2 not in player['message_seen'] and dungeon_map[player['xlocation'] - 1][player['ylocation']] == '| |':
        print('There is a small bridge leading over the river\nit seems to be the only way to cross')
        player['message_seen'].append(2)
    if 3 not in player['message_seen'] and dungeon_map[player['xlocation']][player['ylocation'] - 1] == ' L ':
        print('You reach the treasury but it looks like the door is locked')
        print('You will need some sort of key to get through')
        player['message_seen'].append(3)
    if 4 not in player['message_seen'] and 'treasure' in player['inventory']:
        print('you accomplish your goal and retrieved the treasure')
        print('now you may roam this town killing monsters as you wish')
        player['message_seen'].append(4)


def user_input(player, dungeon_map):
    error = True
    while error:
        player_input = input()
        if player_input == 'east' or player_input == 'west' or player_input == 'north' or player_input == 'south':
            error = collision_check(player_input, player, dungeon_map)
        elif player_input[0:4] == 'take':
            error = take_item_check(player_input, player, dungeon_map)
        elif player_input[-4:] == 'door':
            error = door_check(player_input, dungeon_map, player)
        elif player_input == 'help':
            help_menu()
        elif player_input[0:3] == 'use':
            error = item_check(player_input, player)
        elif player_input == 'quit':
            error = False
        else:
            print('i dont understand')
    return player_input


def item_check(player_input, player):
    if player_input == 'use sword' and 'sword' in player['inventory']:
        print('You swing your sword around looking really dumb')
        return False
    elif player_input == 'use bread':
        print('You eat the bread and return to full HP')
        player['HitPoints'] = 10
        return False
    else:
        # no correct input found so returns error = true
        return True


def door_check(player_input, dungeon_map, player):
    if player_input == 'unlock door' and dungeon_map[player['xlocation']][player['ylocation'] - 1] == ' L ' \
            and 'key' in player['inventory']:
        dungeon_map[player['xlocation']][player['ylocation'] - 1] = '   '
        return False
    elif player_input == 'open door' and dungeon_map[player['xlocation']][player['ylocation'] + 1] == ' D ':
        dungeon_map[player['xlocation']][player['ylocation'] + 1] = '   '
        return False
    else:
        return True


def help_menu():
    print('List of keywords you can type:')
    print('[north, east, south, west] : move in that direction')
    print('[take \'item\'] : takes the item you enter')
    print('[use \'item\'] : uses the item you enter')
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
    moved_list = ['north', 'east', 'south', 'west']
    new_player = character.create_character()
    new_map = map.create_map()
    print('You come across an abandoned village in your search for a hidden treasure.')
    print('Type north, east, south, or west to move')
    print('Type help to see a list of other keywords you can use')
    map.display_map(new_map, new_player)
    character.print_character(new_player)
    player_input = user_input(new_player, new_map)
    while player_input != 'quit':
        print_message(new_player, new_map, player_input)
        map.display_map(new_map, new_player)
        character.print_character(new_player)

        if player_input in moved_list:
            if new_player['HitPoints'] < 10:
                new_player['HitPoints'] += 1
            monster.check_monster_encounter(new_player)

        if new_player['HitPoints'] <= 0:
            print('You died :(')
            break

        player_input = user_input(new_player, new_map)


if __name__ == '__main__':
    main()
