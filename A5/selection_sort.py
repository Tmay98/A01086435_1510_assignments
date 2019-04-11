"""selection_sort function sorts a list of sortable items"""

# Tommy May
# A01086435

import doctest


def selection_sort(unsorted_list):
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
    sorted_list = []
    length = len(unsorted_list)
    for i in range(length):
        temp = unsorted_list[0]
        for j in range(len(unsorted_list)):
            if unsorted_list[j] < temp:
                temp = unsorted_list[j]
        sorted_list.append(temp)
        unsorted_list.remove(temp)
    return sorted_list


def main():
    print(selection_sort(['c', 'a', 'd', 'g', 'b', 'l']))


if __name__ == '__main__':
    main()
