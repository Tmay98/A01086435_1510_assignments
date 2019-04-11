"""database shared headings function shows what keys are shared by all dictionaries inside a dictionary"""

# Tommy May
# A01086435

import doctest


def database_shared_headings(database: dict):
    """ Shows what keys are shared by all dictionaries inside a dictionary

    PARAM: database a dictionary
    PRECONDITION: database must be a dictionary of dictionaries
    POSTCONDITION: creates a list of all shared keys inside the dictionaries
    RETURN: list of all shared keys

    >>> database_shared_headings({'person1' : {'surname': 'sdfb', 'name': 'dfgd', 'notes': 'dsfsd'\
    }, 'person2' : {'surname': 'dsfsd', 'name': 'sdfsd', 'notes': 'sdfs', 'author': 'sdfsd'}})
    ['surname', 'name', 'notes']
    """
    like_keys = list(list(database.values())[0].keys())
    for sub_dict in database.values():
        sub_dict_keys = sub_dict.keys()
        for key in like_keys:
            if key not in sub_dict_keys:
                like_keys.remove(key)
    return like_keys


def main():
    doctest.testmod()
    my_dict = {'tommy': {'name': 'tommy', 'born': 1932, 'died': None, 'notes': 'stuff'},
               'chris': {'name': 'chris', 'born': 1922, 'died': None}
               }
    print(database_shared_headings(my_dict))


if __name__ == '__main__':
    main()
