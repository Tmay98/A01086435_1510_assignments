"""selection_sort function"""

# Tommy May
# A01086435


def selection_sort(unsorted_list):
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
