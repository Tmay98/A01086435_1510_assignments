"""selection_sort function sorts a list of sortable items"""

# Tommy May
# A01086435

import doctest
from collections.abc import Sequence


def selection_sort(unsorted_list) -> list:
    """Sorts a list of sortable items from lowest to highest

    PARAM: unsorted_list a list
    PRECONDITION: unsorted_list is a list of sortable items
    POSTCONDITION: unsorted_list is sorted
    RETURN: the sorted list

    >>> selection_sort(['a', 'f', 'b', 'l', 'z', 'c'])
    ['a', 'b', 'c', 'f', 'l', 'z']
    >>> selection_sort([1, 5, 25, 3, 15, 2, 54, 32, 7])
    [1, 2, 3, 5, 7, 15, 25, 32, 54]
    """
    # check for empty list
    if not unsorted_list:
        raise TypeError('empty list')

    # check if list contains sequence elements not including strings
    for i in range(len(unsorted_list)):
        if isinstance(unsorted_list[i], Sequence) and not isinstance(unsorted_list[i], str):
            raise TypeError('list elements not sortable')

    sorted_list = []
    length = len(unsorted_list)
    for i in range(length):
        temp = unsorted_list[0]  # creates a temporary variable of the first element in unsorted list
        for j in range(len(unsorted_list)):
            if unsorted_list[j] < temp:  # if the next element in the unsorted list is smaller replace temp with it
                temp = unsorted_list[j]
        sorted_list.append(temp)
        unsorted_list.remove(temp)
    return sorted_list


def main():
    doctest.testmod()
    print(selection_sort(['c', 'a', 'd', 'g', 'b', 'l']))
    print(selection_sort([1, 5, 2, 7, 15, 3]))
    try:
        selection_sort([])
    except TypeError as e:
        print(e)

    try:
        selection_sort([[1, 2, 3], [2, 3, 4]])
    except TypeError as e:
        print(e)

    try:
        selection_sort([(1, 2, 3), (2, 3, 4)])
    except TypeError as e:
        print(e)


if __name__ == '__main__':
    main()
