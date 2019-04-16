""" Backup function to create a backup of a file """

# Tommy May
# A01086435


def backup(filename):
    """ Creates a backup of the given file

    PARAM: filename a string
    PRECONDITION: filename must be a string of a .txt filename
    POSTCONDITION: the file is copied to a .bak file of the same name
    """
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print('File not found')
    else:
        # takes file name given and creates same file with .bak
        backup_filename = filename[:-4] + '.bak'
        with open(backup_filename, 'w') as f_obj:
            f_obj.write(contents)
        print('generated ' + backup_filename)


def main():
    backup('stuff.txt')


if __name__ == '__main__':
    main()
