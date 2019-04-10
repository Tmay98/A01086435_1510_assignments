"""database shared headings function"""

# Tommy May
# A01086435


def database_shared_headings(database: dict):
    like_keys = list(list(database.values())[0].keys())
    for sub_dict in database.values():
        sub_dict_keys = sub_dict.keys()
        for key in like_keys:
            if key not in sub_dict_keys:
                like_keys.remove(key)
    return like_keys


def main():
    my_dict = {'tommy': {'name': 'tommy', 'born': 1932, 'died': None, 'notes': 'stuff'},
               'chris': {'name': 'chris', 'born': 1922, 'died': None}
               }
    print(database_shared_headings(my_dict))


if __name__ == '__main__':
    main()
